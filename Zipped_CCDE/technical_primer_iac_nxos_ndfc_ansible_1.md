# Technical Primer: Infrastructure as Code for NXOS and NDFC with Ansible

## Introduction

This technical primer explores the implementation of Infrastructure as Code (IaC) principles for Cisco NXOS devices and Nexus Dashboard Fabric Controller (NDFC) using Ansible. It covers fundamental concepts, implementation approaches, and advanced techniques for network automation, structured according to Bloom's Taxonomy to facilitate comprehensive learning from basic recall to advanced solution creation.

## 1. Remember: Fundamental Concepts and Terminology

### 1.1 Infrastructure as Code Basics
- Infrastructure as Code (IaC) is the practice of managing infrastructure through code rather than manual processes
- IaC treats infrastructure configuration as software code that can be versioned, tested, and deployed
- Key components include version control systems, automation tools, and CI/CD pipelines
- The code becomes the source of truth, not the network devices themselves

### 1.2 Key Components in Network Automation Ecosystem
- **SCM (Software Code Management)**: GitHub, GitLab for version control
- **CI/CD Pipelines**: Jenkins, GitLab CI, GitHub Actions for automated testing and deployment
- **Automation Tools**: Ansible, Terraform, Puppet, Chef for infrastructure provisioning
- **Testing Frameworks**: For validating infrastructure changes before deployment

### 1.3 Ansible Fundamentals
- Ansible is an open-source automation platform maintained by Red Hat
- Uses YAML for configuration files and playbooks
- Agentless architecture that connects to network devices via SSH, NETCONF, or REST APIs
- Modular design with collections of modules for different device types and functions

### 1.4 Ansible Components for Cisco Networking
- **Control Host**: The system where Ansible is installed (Linux, macOS, or Windows with WSL)
- **Collections**: Cisco.NXOS for direct switch management, Cisco.DCNM for NDFC management
- **Modules**: Pre-built code for specific network configuration tasks
- **Playbooks**: YAML files that define the desired state and tasks to achieve it

## 2. Understand: Explaining Concepts and Relationships

### 2.1 Infrastructure as Code Principles
- **Idempotency**: Running the same code multiple times produces the same result
- **Consistency**: Ensures uniform configuration across environments
- **Versioning**: Tracks changes to infrastructure over time
- **Testing**: Validates changes before deployment
- **Automation**: Reduces manual intervention and human error

### 2.2 CI/CD Pipeline for Network Infrastructure
- **Continuous Integration (CI)**: Automatically tests code changes in a staging environment
- **Continuous Delivery**: Prepares changes for deployment but requires manual approval
- **Continuous Deployment**: Automatically deploys changes to production after successful testing
- Pipeline detects changes in the repository and triggers automated workflows

### 2.3 Ansible Architecture for Network Automation
- **Control Host to Device**: Direct connection from Ansible control host to network devices
- **Control Host to Controller**: Connection to a controller (NDFC) that manages devices
- **Connection Methods**: Network CLI (SSH), NETCONF, or REST API (NX-API)
- **Inventory**: Defines target devices and their connection parameters
- **Variables**: Store configuration data separately from playbooks

### 2.4 Ansible Collections and Modules
- Collections are distributions of Ansible content (modules, roles, plugins)
- Cisco.NXOS collection contains 77+ modules for Nexus switch configuration
- Modules are maintained by Red Hat with Cisco support
- Fully Qualified Collection Name (FQCN) format: `cisco.nxos.nxos_vlans`

## 3. Apply: Implementing IaC with Ansible

### 3.1 Setting Up the Ansible Environment
```bash
# Create Python virtual environment
python -m venv ansible_env
source ansible_env/bin/activate

# Install Ansible (lightweight core version)
pip install ansible-core

# Install required collections
ansible-galaxy collection install cisco.nxos cisco.dcnm
```

### 3.2 Creating an Ansible Inventory
```yaml
# inventory.yml
all:
  children:
    spine:
      hosts:
        spine1:
          ansible_host: 192.168.1.1
        spine2:
          ansible_host: 192.168.1.2
    leaf:
      hosts:
        leaf1:
          ansible_host: 192.168.1.3
        leaf2:
          ansible_host: 192.168.1.4
  vars:
    ansible_connection: network_cli
    ansible_network_os: nxos
    ansible_user: admin
    ansible_password: "{{ vault_password }}"
```

### 3.3 Writing a Basic Ansible Playbook for NXOS
```yaml
# nxos_config.yml
---
- name: Configure NXOS devices
  hosts: all
  gather_facts: no
  
  tasks:
    - name: Configure hostname
      cisco.nxos.nxos_config:
        lines:
          - hostname {{ inventory_hostname }}
    
    - name: Enable features
      cisco.nxos.nxos_feature:
        feature: "{{ item }}"
        state: enabled
      loop:
        - lacp
        - vpc
        - interface-vlan
```

### 3.4 Implementing Variable Separation
```yaml
# group_vars/all.yml
ntp_servers:
  - 10.1.1.1
  - 10.1.1.2

# group_vars/spine.yml
bgp_as: 65001

# host_vars/leaf1.yml
vlans:
  - id: 100
    name: Production
  - id: 200
    name: Development
```

## 4. Analyze: Breaking Down Complex Automation Scenarios

### 4.1 Ansible Playbook Structure Analysis
- **Play**: Defines a set of tasks to be executed against specific hosts
- **Tasks**: Individual actions to be performed on hosts
- **Handlers**: Tasks that only run when notified by other tasks
- **Roles**: Reusable units of organization for playbooks
- **Variables**: Data that can be used across plays and tasks

### 4.2 Data Model Design Patterns
- **Hierarchical Variable Structure**: Group_vars and host_vars for different levels of specificity
- **Template-Based Configuration**: Using Jinja2 templates for complex configurations
- **Structured Data Models**: YAML or JSON structures representing network intent
- **Source of Truth Separation**: Keeping configuration data separate from automation logic

### 4.3 Connection Methods Comparison
- **Network CLI (SSH)**:
  - Advantages: Widely supported, familiar to network engineers
  - Considerations: Serial execution, potential for parsing errors
  
- **NETCONF**:
  - Advantages: Structured data, transaction support
  - Considerations: Not all features may be supported
  
- **REST API (NX-API)**:
  - Advantages: Parallel execution, structured data
  - Considerations: Requires API access, different authentication

### 4.4 Error Handling and Idempotency
- Handling connection failures and timeouts
- Dealing with configuration conflicts
- Ensuring idempotent operations
- Implementing rollback mechanisms
- Validation before and after configuration changes

## 5. Evaluate: Assessing Different Approaches

### 5.1 Direct Device Management vs. Controller-Based Approach
- **Direct to NXOS Devices**:
  - Advantages: No additional controller required, direct control
  - Disadvantages: Scales poorly, requires managing individual devices
  
- **NDFC Controller-Based**:
  - Advantages: Centralized management, fabric-level operations
  - Disadvantages: Additional component, potential single point of failure

### 5.2 Playbook Organization Strategies
- **Monolithic Playbooks**:
  - Simple to understand but difficult to maintain
  - Limited reusability and flexibility
  
- **Role-Based Organization**:
  - Better modularity and reusability
  - More complex structure but easier maintenance
  
- **Collection-Based Approach**:
  - Highest level of modularity and distribution
  - Requires more initial setup but best for large-scale automation

### 5.3 CI/CD Implementation Options
- **Basic Git Workflow**:
  - Simple pull request and review process
  - Manual execution of playbooks
  
- **Semi-Automated Pipeline**:
  - Automated testing in staging environment
  - Manual approval for production deployment
  
- **Fully Automated Pipeline**:
  - Complete automation from commit to production
  - Requires high confidence in testing and validation

### 5.4 Testing Strategy Assessment
- **Syntax Checking**: Basic validation of YAML and playbook structure
- **Linting**: Enforcing style and best practices
- **Simulation Testing**: Using network simulation tools
- **Staging Environment Testing**: Testing on replica of production
- **Production Validation**: Verifying successful deployment

## 6. Create: Designing Advanced Automation Solutions

### 6.1 Enterprise Network Automation Framework
- Design modular playbook structure for different network functions
- Implement role-based access control for automation tasks
- Create standardized templates for common configurations
- Develop custom modules for organization-specific requirements
- Implement comprehensive logging and auditing

### 6.2 VXLAN EVPN Fabric Automation
- Design data models for fabric, overlay, and tenant configurations
- Create validation workflows for fabric consistency
- Implement automated fabric deployment and expansion
- Develop tenant onboarding automation
- Create migration tools for transitioning from legacy networks

### 6.3 Multi-Domain Orchestration
- Design workflows that span multiple network domains
- Implement integration with service management systems
- Create abstraction layers for consistent automation across platforms
- Develop cross-domain validation and testing
- Implement change windows and scheduling

### 6.4 Network as Code Operating Model
- Design team workflows and collaboration processes
- Create documentation and knowledge sharing systems
- Implement training and skill development programs
- Develop metrics and KPIs for automation effectiveness
- Create continuous improvement processes

## Practical Exercises

1. **Basic Ansible Environment Setup (Apply)**
   - Set up a Python virtual environment
   - Install Ansible and required collections
   - Create a basic inventory and test connectivity

2. **NXOS Configuration Automation (Apply/Analyze)**
   - Create playbooks for common NXOS configurations
   - Implement variable separation for different device roles
   - Test playbooks in a lab environment

3. **CI/CD Pipeline Implementation (Analyze/Create)**
   - Set up a GitLab repository for network automation
   - Configure GitLab CI for testing playbooks
   - Implement staging and production deployment workflows

4. **VXLAN EVPN Fabric Automation (Create)**
   - Design data models for VXLAN EVPN fabric
   - Create playbooks for fabric deployment
   - Implement tenant onboarding automation

## Assessment Questions

### Remember Level
1. What is Infrastructure as Code and why is it important for network management?
2. Name three key components of the network automation ecosystem.
3. What are Ansible collections and how do they relate to modules?

### Understand Level
1. Explain the difference between Continuous Integration, Continuous Delivery, and Continuous Deployment.
2. Describe how Ansible connects to and manages Cisco NXOS devices.
3. Explain the concept of idempotency and why it's important in network automation.

### Apply Level
1. Write an Ansible playbook that configures VLANs on NXOS switches.
2. Implement variable separation using group_vars and host_vars for a network with spine and leaf switches.
3. Create an Ansible inventory that organizes devices by role and includes connection parameters.

### Analyze Level
1. Compare and contrast the different connection methods available for Ansible to manage NXOS devices.
2. Analyze the structure of an Ansible role and explain how it promotes code reusability.
3. Break down the components of a CI/CD pipeline for network automation and explain their functions.

### Evaluate Level
1. Evaluate the suitability of direct device management versus controller-based management for different network sizes.
2. Assess different strategies for organizing Ansible playbooks and roles for a large enterprise network.
3. Critique a given network automation implementation for scalability, maintainability, and security.

### Create Level
1. Design a comprehensive network automation framework for a multi-site enterprise network.
2. Develop a strategy for migrating from manual network management to Infrastructure as Code.
3. Create a VXLAN EVPN fabric automation solution that includes validation and testing.

## References and Resources

1. Ansible Documentation: [https://docs.ansible.com/](https://docs.ansible.com/)
2. Cisco NXOS Collection: [https://galaxy.ansible.com/cisco/nxos](https://galaxy.ansible.com/cisco/nxos)
3. Cisco DCNM/NDFC Collection: [https://galaxy.ansible.com/cisco/dcnm](https://galaxy.ansible.com/cisco/dcnm)
4. GitLab CI Documentation: [https://docs.gitlab.com/ee/ci/](https://docs.gitlab.com/ee/ci/)
5. VXLAN EVPN Design and Deployment Guides
