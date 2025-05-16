# Technical Primer: CI/CD Pipelines for Network Infrastructure with NDI

## Introduction

Continuous Integration/Continuous Deployment (CI/CD) pipelines have revolutionized software development practices, and now these methodologies are being applied to network infrastructure management. This technical primer explores how CI/CD pipelines can be integrated with Nexus Dashboard Insights (NDI) to create safer, more efficient network change processes, structured according to Bloom's Taxonomy to facilitate comprehensive learning.

## 1. Remember: Fundamental Concepts and Terminology

### 1.1 CI/CD Pipeline Fundamentals
- CI/CD stands for Continuous Integration/Continuous Deployment
- Operational model imported from software development industry
- Consists of automated, heterogeneous tasks to accomplish specific goals
- Provides consistency, efficiency, and reduced deployment time

### 1.2 Nexus Dashboard Architecture
- Underlay platform that hosts multiple applications
- Supports day-zero, day-one, and day-two operations
- Applications include Nexus Dashboard Orchestrator, Fabric Controller, and Insights
- Runs as a Kubernetes-based cluster

### 1.3 Nexus Dashboard Insights (NDI)
- Day-two operations tool for network management
- Provides visibility, monitoring, analytics, correlation, advisories, and tools
- Focuses on assurance, compliance, and troubleshooting
- Supports pre-change validation and post-change verification

### 1.4 Network Infrastructure as Code
- Represents network configurations as code files
- Enables version control and change tracking
- Supports automated testing and validation
- Facilitates consistent deployment across environments

### 1.5 Change Management Terminology
- Pre-change validation: Testing changes before implementation
- Post-change verification: Confirming changes were successful
- Anomalies: Detected issues or deviations from expected behavior
- Snapshots: Point-in-time captures of network state

## 2. Understand: Explaining Concepts and Relationships

### 2.1 CI/CD Pipeline Benefits for Network Infrastructure
- Increases efficiency by automating repetitive tasks
- Ensures consistency through standardized processes
- Reduces human error through automation
- Decreases overall deployment time
- Improves change success rates through validation

### 2.2 Network Change Risk Factors
- 65% of network incidents are caused by change activities
- Lack of testing before implementation leads to outages
- Manual processes introduce inconsistency and errors
- Complex dependencies between network components
- Limited visibility into potential impact of changes

### 2.3 NDI Snapshot Functionality
- Periodically captures fabric state as data models
- Contains running configuration and operational status
- Includes statistics about endpoints, external routes, and deployed networks
- Records active anomalies at the time of capture
- Enables comparison between different points in time

### 2.4 Pre-Change Validation Process
- Creates a deep copy of the current network snapshot
- Applies proposed configuration changes to the copy
- Uses machine learning algorithms to simulate the resulting state
- Predicts potential anomalies or issues before actual implementation
- Provides go/no-go recommendation based on analysis

### 2.5 Post-Change Verification Process
- Compares snapshots before and after change implementation
- Identifies new anomalies or issues introduced by the change
- Verifies that expected configuration changes were applied correctly
- Detects unexpected side effects or consequences
- Provides confirmation of successful change or identifies remediation needs

## 3. Apply: Implementing CI/CD Pipelines with NDI

### 3.1 Setting Up the CI/CD Environment
```bash
# Install required tools
pip install ansible
pip install ansible-galaxy

# Install Ansible collection for NDI
ansible-galaxy collection install cisco.ndi

# Configure GitHub Actions workflow directory
mkdir -p .github/workflows
```

### 3.2 Creating a Basic CI/CD Workflow
```yaml
# .github/workflows/network-change.yml
name: Network Change Pipeline

on:
  push:
    branches: [ main ]
    paths:
      - 'network-configs/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ansible
          ansible-galaxy collection install cisco.ndi
      - name: Lint Ansible playbooks
        run: ansible-lint network-configs/*.yml
      - name: Generate configuration file
        run: ansible-playbook network-configs/generate-config.yml --check
      - name: Pre-change validation with NDI
        run: ansible-playbook network-configs/ndi-validate.yml
```

### 3.3 Implementing Pre-Change Validation with Ansible
```yaml
# network-configs/ndi-validate.yml
---
- name: Validate network changes with NDI
  hosts: localhost
  gather_facts: no
  vars:
    ndi_host: "nexus-dashboard.example.com"
    ndi_username: "admin"
    ndi_password: "password"
    config_file: "generated-config.json"
  
  tasks:
    - name: Perform pre-change validation
      cisco.ndi.prechange_validation:
        host: "{{ ndi_host }}"
        username: "{{ ndi_username }}"
        password: "{{ ndi_password }}"
        fabric_id: "fabric1"
        config_file: "{{ config_file }}"
      register: validation_result
    
    - name: Fail if validation detects new anomalies
      fail:
        msg: "Pre-change validation detected new anomalies: {{ validation_result.new_anomalies }}"
      when: validation_result.new_anomalies | length > 0
```

### 3.4 Implementing Post-Change Verification with Ansible
```yaml
# network-configs/ndi-verify.yml
---
- name: Verify network changes with NDI
  hosts: localhost
  gather_facts: no
  vars:
    ndi_host: "nexus-dashboard.example.com"
    ndi_username: "admin"
    ndi_password: "password"
    baseline_snapshot_id: "{{ lookup('file', 'baseline_snapshot_id.txt') }}"
  
  tasks:
    - name: Collect current snapshot
      cisco.ndi.collect_snapshot:
        host: "{{ ndi_host }}"
        username: "{{ ndi_username }}"
        password: "{{ ndi_password }}"
        fabric_id: "fabric1"
      register: current_snapshot
    
    - name: Perform delta analysis
      cisco.ndi.delta_analysis:
        host: "{{ ndi_host }}"
        username: "{{ ndi_username }}"
        password: "{{ ndi_password }}"
        fabric_id: "fabric1"
        snapshot1_id: "{{ baseline_snapshot_id }}"
        snapshot2_id: "{{ current_snapshot.id }}"
      register: delta_result
    
    - name: Fail if new anomalies detected
      fail:
        msg: "Post-change verification detected new anomalies: {{ delta_result.new_anomalies }}"
      when: delta_result.new_anomalies | length > 0
```

### 3.5 Implementing the Complete CI/CD Pipeline
```yaml
# .github/workflows/complete-pipeline.yml
name: Complete Network Change Pipeline

on:
  push:
    branches: [ main ]
    paths:
      - 'network-configs/**'

jobs:
  validate_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ansible
          ansible-galaxy collection install cisco.ndi
      
      - name: Lint Ansible playbooks
        run: ansible-lint network-configs/*.yml
      
      - name: Generate configuration file (dry run)
        run: ansible-playbook network-configs/generate-config.yml --check
      
      - name: Pre-change validation with NDI
        run: ansible-playbook network-configs/ndi-validate.yml
      
      - name: Take baseline snapshot
        run: ansible-playbook network-configs/take-snapshot.yml
      
      - name: Deploy configuration changes
        run: ansible-playbook network-configs/deploy-config.yml
      
      - name: Post-change verification
        run: ansible-playbook network-configs/ndi-verify.yml
      
      - name: Send notification
        uses: cisco-webex/action-message@v1
        with:
          roomId: ${{ secrets.WEBEX_ROOM_ID }}
          token: ${{ secrets.WEBEX_TOKEN }}
          message: "Network change successfully deployed and verified"
```

## 4. Analyze: Breaking Down Complex Systems

### 4.1 CI/CD Pipeline Component Analysis
- **Version Control System (GitHub/GitLab)**:
  - Stores network configuration as code
  - Tracks changes and maintains history
  - Triggers pipeline execution on changes
  - Facilitates collaboration and review

- **CI/CD Engine (GitHub Actions)**:
  - Orchestrates workflow execution
  - Manages environment setup
  - Handles job sequencing and dependencies
  - Provides execution logs and status reporting

- **Configuration Management (Ansible)**:
  - Generates configuration files from templates
  - Supports dry-run capability for testing
  - Implements idempotent operations
  - Provides abstraction for different platforms

- **Validation Tool (NDI)**:
  - Performs pre-change validation
  - Collects and analyzes snapshots
  - Detects potential issues before implementation
  - Verifies changes after implementation

### 4.2 Pre-Change Validation Workflow Analysis
1. **Configuration Generation**:
   - Templates are rendered with specific variables
   - Configuration is generated but not applied
   - Output is captured for validation

2. **Snapshot Duplication**:
   - Baseline snapshot is taken or retrieved
   - Deep copy is created for simulation
   - Metadata is preserved for comparison

3. **Change Simulation**:
   - Generated configuration is applied to snapshot copy
   - Machine learning algorithms predict resulting state
   - Potential anomalies are identified

4. **Decision Point**:
   - Results are evaluated against criteria
   - Go/no-go decision is made
   - Feedback is provided to initiator

### 4.3 Post-Change Verification Workflow Analysis
1. **Baseline Capture**:
   - Snapshot is taken before changes
   - Snapshot ID is stored for reference
   - Current state is documented

2. **Change Implementation**:
   - Configuration is applied to production
   - Implementation is logged and tracked
   - Completion is confirmed

3. **Post-Change Snapshot**:
   - New snapshot is taken after changes
   - Timing considerations for state convergence
   - Snapshot ID is captured for comparison

4. **Delta Analysis**:
   - Baseline and current snapshots are compared
   - Differences are identified and categorized
   - New anomalies are flagged for review

### 4.4 Failure Mode Analysis
- **Pre-Validation Failures**:
   - Configuration syntax errors
   - Simulation prediction errors
   - Connectivity issues with NDI
   - Timeout during validation process

- **Deployment Failures**:
   - Network device access issues
   - Configuration rejection by devices
   - Partial application of changes
   - Timeout during deployment

- **Verification Failures**:
   - New anomalies detected
   - Expected changes not applied
   - Unexpected side effects
   - Snapshot collection failures

### 4.5 Integration Point Analysis
- **VCS to CI/CD Engine**:
   - Webhook configuration
   - Authentication and authorization
   - Event filtering and triggering
   - Repository structure and organization

- **CI/CD Engine to Ansible**:
   - Environment setup
   - Variable passing
   - Secret management
   - Error handling and reporting

- **Ansible to NDI**:
   - API authentication
   - Module functionality
   - Response parsing
   - Error handling and retry logic

## 5. Evaluate: Assessing Different Approaches

### 5.1 CI/CD Engine Comparison
- **GitHub Actions**:
  - Advantages: Tight integration with GitHub, simple setup, free tier available
  - Disadvantages: Limited execution environments, potential vendor lock-in
  
- **Jenkins**:
  - Advantages: Highly customizable, extensive plugin ecosystem, self-hosted option
  - Disadvantages: More complex setup, requires maintenance, resource intensive
  
- **GitLab CI**:
  - Advantages: Integrated with GitLab, container-native, built-in registry
  - Disadvantages: Less flexible than Jenkins, potential performance issues

### 5.2 Configuration Management Tool Evaluation
- **Ansible**:
  - Advantages: Agentless, YAML-based, extensive module library, NDI collection available
  - Disadvantages: Limited state management, potential performance issues at scale
  
- **Terraform**:
  - Advantages: Strong state management, declarative approach, provider ecosystem
  - Disadvantages: Steeper learning curve, limited NDI integration
  
- **Custom Scripts**:
  - Advantages: Maximum flexibility, tailored to specific needs
  - Disadvantages: Maintenance overhead, lack of standardization, potential fragility

### 5.3 Validation Strategy Assessment
- **Pre-Change Only**:
  - Advantages: Faster pipeline execution, prevents most issues
  - Disadvantages: Misses implementation issues, limited verification
  
- **Post-Change Only**:
  - Advantages: Confirms actual state, identifies real issues
  - Disadvantages: Reactive approach, issues already in production
  
- **Combined Approach**:
  - Advantages: Comprehensive validation, highest success rate
  - Disadvantages: Longer pipeline execution, more complex implementation

### 5.4 Rollback Strategy Evaluation
- **Automatic Rollback**:
  - Advantages: Immediate remediation, minimal downtime
  - Disadvantages: Potential for cascading issues, complex implementation
  
- **Manual Approval for Rollback**:
  - Advantages: Human oversight, controlled process
  - Disadvantages: Slower response, requires human availability
  
- **No Rollback (Fix Forward)**:
  - Advantages: Simpler implementation, avoids rollback complications
  - Disadvantages: Longer resolution time, extended impact duration

### 5.5 Notification Strategy Assessment
- **Event-Based Notifications**:
  - Advantages: Immediate awareness, targeted information
  - Disadvantages: Potential notification fatigue, context limitations
  
- **Summary Notifications**:
  - Advantages: Consolidated information, reduced noise
  - Disadvantages: Delayed awareness, potential information loss
  
- **Tiered Notification Approach**:
  - Advantages: Balanced information flow, priority-based alerting
  - Disadvantages: More complex implementation, rule maintenance

## 6. Create: Designing Solutions and Implementations

### 6.1 Enterprise-Grade CI/CD Pipeline Architecture
- Design a scalable pipeline architecture for multi-fabric environments
- Implement role-based access control for pipeline operations
- Create approval gates for high-risk changes
- Develop comprehensive logging and audit trail mechanisms
- Design pipeline metrics and performance monitoring

### 6.2 Advanced Validation Framework
- Create a multi-stage validation process with increasing scrutiny
- Develop custom validation rules based on organizational policies
- Implement historical trend analysis for change risk assessment
- Design validation result visualization and reporting
- Create validation exception handling and override mechanisms

### 6.3 Comprehensive Rollback System
- Design automated rollback triggers based on verification results
- Develop snapshot-based configuration restoration
- Create transaction boundaries for atomic changes
- Implement rollback verification and confirmation
- Design rollback notification and documentation

### 6.4 Change Management Integration
- Design integration with ITSM systems (ServiceNow, Jira)
- Develop change request to pipeline mapping
- Create automated change documentation generation
- Implement change calendar awareness and scheduling
- Design change success metrics and reporting

### 6.5 Self-Service Network Change Portal
- Create a user-friendly interface for initiating network changes
- Develop templates for common change types
- Implement change simulation and preview functionality
- Design approval workflows and notifications
- Create change status tracking and history

## Practical Exercises

1. **Basic CI/CD Pipeline Setup (Apply)**
   - Set up a GitHub repository for network configurations
   - Create a GitHub Actions workflow for validation
   - Implement Ansible playbooks for NDI integration

2. **Pre-Change Validation Implementation (Apply/Analyze)**
   - Create an Ansible playbook for NDI pre-change validation
   - Implement configuration generation in dry-run mode
   - Develop decision logic based on validation results

3. **Complete Pipeline Development (Analyze/Create)**
   - Design and implement a full CI/CD pipeline with pre and post validation
   - Create notification mechanisms for pipeline events
   - Implement error handling and retry logic

4. **Enterprise Integration Design (Create)**
   - Design integration with change management systems
   - Develop approval workflows for different change types
   - Create comprehensive reporting and metrics

## Assessment Questions

### Remember Level
1. What does CI/CD stand for in the context of network infrastructure?
2. What are the three main categories of functionality provided by Nexus Dashboard Insights?
3. What is the purpose of pre-change validation in a network CI/CD pipeline?

### Understand Level
1. Explain the relationship between pre-change validation and post-change verification in a network CI/CD pipeline.
2. Describe how NDI uses snapshots to perform delta analysis.
3. Explain why 65% of network incidents being caused by change activities is significant for CI/CD implementation.

### Apply Level
1. Write an Ansible playbook that performs pre-change validation using the NDI collection.
2. Implement a GitHub Actions workflow that triggers on network configuration changes.
3. Create a notification system that alerts appropriate teams based on pipeline results.

### Analyze Level
1. Analyze the potential failure points in a network CI/CD pipeline and propose mitigation strategies.
2. Break down the pre-change validation process and identify opportunities for optimization.
3. Compare the workflow differences between software CI/CD pipelines and network infrastructure CI/CD pipelines.

### Evaluate Level
1. Evaluate different CI/CD engines for network infrastructure automation and recommend the most appropriate for a given scenario.
2. Assess the trade-offs between automatic rollbacks and fix-forward approaches for failed changes.
3. Critique a given pipeline design for scalability, reliability, and security.

### Create Level
1. Design a comprehensive CI/CD pipeline for a multi-fabric environment with appropriate validation stages.
2. Develop an integration strategy between network CI/CD pipelines and IT service management systems.
3. Create a self-service portal design that allows non-technical users to initiate pre-approved network changes.

## References and Resources

1. Cisco Nexus Dashboard Insights Documentation
2. Cisco Ansible Collection for NDI
3. GitHub Actions Documentation: [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
4. Ansible Documentation: [https://docs.ansible.com/](https://docs.ansible.com/)
5. Network Automation Best Practices
6. CI/CD for Infrastructure as Code: Patterns and Practices
