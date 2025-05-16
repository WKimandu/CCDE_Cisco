# Technical Primer: Infrastructure as Code for ACI with Ansible and Terraform

## Introduction

This technical primer explores the implementation of Infrastructure as Code (IaC) principles for Cisco Application Centric Infrastructure (ACI) using both Ansible and Terraform. It covers fundamental concepts, implementation approaches, and advanced techniques for network automation, structured according to Bloom's Taxonomy to facilitate comprehensive learning from basic recall to advanced solution creation.

## 1. Remember: Fundamental Concepts and Terminology

### 1.1 Infrastructure as Code Basics
- Infrastructure as Code (IaC) is the management and provisioning of computing resources through code and data structures instead of CLI commands
- IaC allows network operators to move beyond traditional CLI-based configuration to programmatic approaches
- Key components include source control management, CI/CD pipelines, and execution software
- ACI's REST API enables the use of IaC tools like Ansible and Terraform

### 1.2 Key Components in Network Automation Ecosystem
- **Source Control Management (SCM)**: Git, GitHub, GitLab, BitBucket
- **CI/CD Pipelines**: Jenkins, Drone, CircleCI
- **Execution Software**: Ansible, Terraform, Python, Go
- **Target Infrastructure**: ACI fabric, Multi-site deployments

### 1.3 Ansible Fundamentals for ACI
- Ansible is an agentless automation platform
- Requires Python environment on the control node
- Uses YAML for configuration files and playbooks
- Connects to ACI via REST API
- Doesn't require programming knowledge, just understanding of data structures

### 1.4 Terraform Fundamentals for ACI
- Terraform is an open-source IaC tool by HashiCorp
- Uses HashiCorp Configuration Language (HCL)
- Declarative approach to infrastructure definition
- Maintains state of managed infrastructure
- Provides plan, apply, and destroy workflow

## 2. Understand: Explaining Concepts and Relationships

### 2.1 Infrastructure as Code Principles for ACI
- **Declarative vs. Imperative**: Defining what the infrastructure should look like rather than how to create it
- **Idempotency**: Running the same code multiple times produces the same result
- **Version Control**: Tracking changes to infrastructure over time
- **Collaboration**: Enabling team-based infrastructure management
- **Automation**: Reducing manual intervention and human error

### 2.2 CI/CD Pipeline for ACI Infrastructure
- **Code Submission**: Engineers submit infrastructure code to SCM
- **Automated Testing**: CI/CD tool detects changes and runs tests
- **Execution**: Runners trigger Ansible or Terraform to apply changes
- **Validation**: Verification that changes were applied correctly
- **Feedback Loop**: Results reported back to engineers

### 2.3 Ansible Architecture for ACI Automation
- **Control Node**: Where Ansible is installed and playbooks are executed
- **Collections**: Cisco.ACI collection contains modules for ACI configuration
- **Inventory**: Defines ACI controllers and their connection parameters
- **Variables**: Store configuration data separately from playbooks
- **Roles**: Reusable units of organization for playbooks

### 2.4 Terraform Architecture for ACI Automation
- **Terraform Core**: Processes configuration files and manages state
- **Providers**: Cisco ACI provider interfaces with ACI API
- **Resources**: Represent ACI objects like tenants, VRFs, and EPGs
- **State Management**: Tracks current state of infrastructure
- **Plan and Apply Workflow**: Preview changes before applying them

## 3. Apply: Implementing IaC with Ansible and Terraform

### 3.1 Setting Up Ansible for ACI
```bash
# Create Python virtual environment
python -m venv ansible_env
source ansible_env/bin/activate

# Install Ansible (lightweight core version)
pip install ansible-core

# Install required collections
ansible-galaxy collection install cisco.aci
```

### 3.2 Creating an Ansible Directory Structure
```
ansible-aci/
├── ansible.cfg
├── inventory.yml
├── group_vars/
│   └── apic.yml
├── host_vars/
│   └── apic1.yml
├── roles/
│   ├── tenant/
│   ├── vrf/
│   └── bd/
└── playbooks/
    └── deploy_tenant.yml
```

### 3.3 Writing a Basic Ansible Playbook for ACI
```yaml
# deploy_tenant.yml
---
- name: Configure ACI Tenant
  hosts: apic
  gather_facts: no
  
  tasks:
    - name: Create Tenant
      cisco.aci.aci_tenant:
        host: "{{ inventory_hostname }}"
        username: "{{ apic_username }}"
        password: "{{ apic_password }}"
        tenant: "{{ tenant_name }}"
        description: "Tenant created by Ansible"
        state: present
      delegate_to: localhost
```

### 3.4 Setting Up Terraform for ACI
```bash
# Install Terraform
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform

# Create directory structure
mkdir -p terraform-aci/{modules,environments}
```

### 3.5 Writing a Basic Terraform Configuration for ACI
```hcl
# main.tf
terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci"
      version = "~> 2.0"
    }
  }
}

provider "aci" {
  username = var.apic_username
  password = var.apic_password
  url      = var.apic_url
  insecure = true
}

resource "aci_tenant" "tenant" {
  name        = var.tenant_name
  description = "Tenant created by Terraform"
}
```

## 4. Analyze: Breaking Down Complex Automation Scenarios

### 4.1 Ansible Playbook Structure Analysis for ACI
- **Inventory**: Defines APIC controllers and their connection parameters
- **Variables**: Different levels (group_vars, host_vars) for configuration data
- **Roles**: Modular organization for tenant, VRF, BD, EPG configurations
- **Tasks**: Individual actions to configure ACI objects
- **Templates**: Jinja2 templates for complex configurations

### 4.2 Terraform Configuration Structure Analysis for ACI
- **Provider Configuration**: Authentication and connection to APIC
- **Variables**: Input parameters for configuration
- **Resources**: ACI objects to be created or managed
- **Modules**: Reusable components for tenant, VRF, BD, EPG configurations
- **Outputs**: Information to be displayed after applying configuration

### 4.3 Data Model Design Patterns for ACI
- **Hierarchical Structure**: Reflecting ACI's object hierarchy
- **Tenant-Based Organization**: Grouping configurations by tenant
- **Application Profile Modeling**: Structuring around application requirements
- **Contract-Based Relationships**: Modeling communication policies
- **Abstraction Layers**: Creating simplified interfaces for complex configurations

### 4.4 Error Handling and Validation
- **Ansible**:
  - Using `register` to capture task results
  - Implementing conditional execution with `when`
  - Using `failed_when` and `changed_when` for custom failure conditions
  - Implementing handlers for dependent actions
  
- **Terraform**:
  - Using `depends_on` for resource dependencies
  - Implementing `lifecycle` blocks for resource management
  - Using `count` and `for_each` for conditional resource creation
  - Validating with `terraform plan` before applying

## 5. Evaluate: Assessing Different Approaches

### 5.1 Ansible vs. Terraform for ACI Management
- **Ansible**:
  - Advantages: Procedural capabilities, broader IT automation, no state management needed
  - Disadvantages: Less visibility into changes, more complex for large deployments
  
- **Terraform**:
  - Advantages: State management, plan before apply, easier to understand changes
  - Disadvantages: Steeper learning curve, more complex setup, state management overhead

### 5.2 Organization Strategies for ACI Automation
- **Monolithic Approach**:
  - Single playbook or configuration file for all ACI objects
  - Simple to understand but difficult to maintain
  
- **Modular Approach**:
  - Separate files or modules for different ACI object types
  - Better organization but requires more initial setup
  
- **Tenant-Based Approach**:
  - Organizing automation by tenant
  - Good for multi-tenant environments but may duplicate code
  
- **Application-Based Approach**:
  - Organizing around application requirements
  - Aligns with business needs but may cross tenant boundaries

### 5.3 CI/CD Implementation Options for ACI
- **Basic Git Workflow**:
  - Simple pull request and review process
  - Manual execution of automation
  
- **Semi-Automated Pipeline**:
  - Automated testing in staging environment
  - Manual approval for production deployment
  
- **Fully Automated Pipeline**:
  - Complete automation from commit to production
  - Requires high confidence in testing and validation

### 5.4 Testing Strategy Assessment
- **Syntax Checking**: Validating YAML, HCL, and JSON syntax
- **Linting**: Enforcing style and best practices
- **Simulation Testing**: Using ACI simulator or mocks
- **Staging Environment Testing**: Testing on non-production APIC
- **Production Validation**: Verifying successful deployment

## 6. Create: Designing Advanced Automation Solutions

### 6.1 Enterprise ACI Automation Framework
- Design modular playbook or configuration structure
- Implement role-based access control for automation
- Create standardized templates for common configurations
- Develop custom modules for organization-specific requirements
- Implement comprehensive logging and auditing

### 6.2 Multi-Site ACI Automation
- Design data models for multi-site deployments
- Create validation workflows for site consistency
- Implement automated site onboarding
- Develop tenant migration automation
- Create disaster recovery automation

### 6.3 Application-Centric Deployment Automation
- Design application-focused automation interfaces
- Implement integration with CI/CD pipelines for applications
- Create abstraction layers for application teams
- Develop self-service portals for application deployment
- Implement automated testing of application connectivity

### 6.4 ACI as Code Operating Model
- Design team workflows and collaboration processes
- Create documentation and knowledge sharing systems
- Implement training and skill development programs
- Develop metrics and KPIs for automation effectiveness
- Create continuous improvement processes

## Practical Exercises

1. **Basic ACI Automation Setup (Apply)**
   - Set up Ansible and Terraform environments
   - Configure authentication for ACI APIC
   - Create a simple tenant with both tools

2. **Tenant and Application Profile Automation (Apply/Analyze)**
   - Create automation for complete tenant configuration
   - Implement application profiles, EPGs, and contracts
   - Compare approaches between Ansible and Terraform

3. **CI/CD Pipeline Implementation (Analyze/Create)**
   - Set up a GitLab repository for ACI automation
   - Configure GitLab CI for testing configurations
   - Implement staging and production deployment workflows

4. **Multi-Site Automation (Create)**
   - Design data models for multi-site deployments
   - Create automation for site-specific and shared configurations
   - Implement validation and consistency checking

## Assessment Questions

### Remember Level
1. What is Infrastructure as Code and why is it important for ACI management?
2. Name three key components of the network automation ecosystem for ACI.
3. What are the main differences between Ansible and Terraform for ACI automation?

### Understand Level
1. Explain how a CI/CD pipeline works for ACI infrastructure automation.
2. Describe the relationship between ACI's object model and IaC data structures.
3. Explain the concept of idempotency and why it's important in ACI automation.

### Apply Level
1. Write an Ansible playbook that creates a tenant, VRF, and bridge domain in ACI.
2. Implement a Terraform configuration that creates an application profile with EPGs.
3. Create a directory structure for organizing ACI automation code.

### Analyze Level
1. Compare and contrast the approaches to variable management in Ansible and Terraform for ACI.
2. Analyze the structure of an ACI tenant configuration and break it down into modular components.
3. Examine the dependencies between ACI objects and explain how to handle them in automation.

### Evaluate Level
1. Evaluate the suitability of Ansible versus Terraform for different ACI automation scenarios.
2. Assess different strategies for organizing automation code for a large ACI deployment.
3. Critique a given ACI automation implementation for scalability, maintainability, and security.

### Create Level
1. Design a comprehensive ACI automation framework for a multi-site enterprise deployment.
2. Develop a strategy for migrating from manual ACI management to Infrastructure as Code.
3. Create an application-centric automation solution that abstracts ACI complexity from application teams.

## References and Resources

1. Ansible Documentation: [https://docs.ansible.com/](https://docs.ansible.com/)
2. Cisco ACI Collection: [https://galaxy.ansible.com/cisco/aci](https://galaxy.ansible.com/cisco/aci)
3. Terraform Documentation: [https://www.terraform.io/docs](https://www.terraform.io/docs)
4. Cisco ACI Terraform Provider: [https://registry.terraform.io/providers/CiscoDevNet/aci](https://registry.terraform.io/providers/CiscoDevNet/aci)
5. Cisco ACI Programmability Guide
