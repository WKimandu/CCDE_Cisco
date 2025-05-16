# Technical Primer: Nexus Dashboard Insights REST API

## Introduction

Nexus Dashboard Insights (NDI) is a powerful application that runs on the Nexus Dashboard Cluster, providing day-2 operational tools for network management. This technical primer explores the NDI REST API capabilities, authentication methods, use cases, and implementation strategies, structured according to Bloom's Taxonomy to facilitate comprehensive learning.

## 1. Remember: Fundamental Concepts and Terminology

### 1.1 Nexus Dashboard Architecture
- Nexus Dashboard is a Kubernetes-based cluster composed of multiple nodes
- Provides a platform for running various network management applications
- Kubernetes implementation is transparent to the end user

### 1.2 Nexus Dashboard Applications
- Nexus Dashboard Orchestrator (NDO): Extends fabrics into multi-site architecture
- Nexus Dashboard Fabric Controller (NDFC): Manages NXOS fabrics without ACI
- Nexus Dashboard Insights (NDI): Day-2 operations tool for network assurance

### 1.3 NDI Core Functionality Categories
- **Assurance**: Resource utilization, pre-change validation, troubleshooting
- **Troubleshooting**: Both proactive and reactive approaches
- **Proactive Advisories**: Vulnerability notifications, field notices, end-of-life notices

### 1.4 REST API Fundamentals
- Accessible over HTTPS transport (secure, encrypted communication)
- Supports standard HTTP methods: GET, POST, DELETE
- Uses JSON payloads for data transmission
- All applications expose APIs through the Nexus Dashboard API Gateway

## 2. Understand: Explaining Concepts and Relationships

### 2.1 NDI's Role in Network Operations
- Focuses on maintaining operational stability after initial configuration
- Ensures service continuity for business-critical applications
- Prevents configuration changes from causing network failures
- Monitors resource utilization and operational status

### 2.2 Troubleshooting Approaches
- **Proactive Troubleshooting**: Analyzes signals from the fabric, correlates data, and notifies operators before problems affect applications
- **Reactive Troubleshooting**: Identifies and resolves problems that have already occurred
- Key metrics: Mean Time to Detect (MTTD) and Mean Time to Resolve (MTTR)

### 2.3 API Authentication Methods
- **Username/Password Authentication**:
  - Requires username, password, and login domain
  - Returns a token used in subsequent API calls via cookies
  - Supports role-based access control
  
- **API Keys Authentication**:
  - Created from NDI Web UI or via APIs
  - Multiple API keys can be created for a single user
  - Each key can be used for different scripts/applications
  - Individual keys can be revoked without affecting others

### 2.4 API Documentation Sources
- DevNet portal: Starting guides for developers, authentication information, use cases, examples
- Nexus Dashboard Insights Help Center: Swagger page with API reference and testing capabilities

## 3. Apply: Implementing API Interactions

### 3.1 API Access Methods
- **Ansible**: Dedicated modules available for NDI interaction
- **Postman**: Collections available for download from DevNet
- **Python**: Using requests library for HTTP REST API calls

### 3.2 Authentication Implementation
- Username/Password Authentication Process:
  ```python
  import requests
  import json
  
  # Disable SSL warnings for self-signed certificates
  requests.packages.urllib3.disable_warnings()
  
  # Authentication endpoint
  url = "https://nexus-dashboard/api/v1/auth/login"
  
  # Authentication payload
  payload = {
      "username": "admin",
      "password": "password",
      "domain": "local"
  }
  
  # Make the authentication request
  response = requests.post(url, json=payload, verify=False)
  
  # Extract the token from the response
  token = response.cookies.get('AuthToken')
  
  # Use the token in subsequent requests
  cookies = {"AuthToken": token}
  ```

- API Key Authentication Process:
  ```python
  import requests
  
  # Disable SSL warnings for self-signed certificates
  requests.packages.urllib3.disable_warnings()
  
  # API endpoint
  url = "https://nexus-dashboard/api/v1/endpoint"
  
  # Headers with API key
  headers = {
      "X-API-KEY": "your-api-key-here"
  }
  
  # Make the request
  response = requests.get(url, headers=headers, verify=False)
  ```

### 3.3 Common API Use Cases
- Pre-change validation for ACI fabrics
- Setting and monitoring compliance requirements
- Retrieving and analyzing anomalies
- Accessing inventory information
- Retrieving health scores and operational data

## 4. Analyze: Breaking Down Complex Systems

### 4.1 API Gateway Architecture
- Nexus Dashboard serves as the API Gateway for all applications
- Routes API calls to appropriate applications based on URI
- Maintains authentication and session state across applications
- Provides a unified entry point for diverse application functionalities

### 4.2 Pre-Change Validation Process
- Configuration is submitted to NDI before being applied to the fabric
- NDI calculates the projected operational state after configuration changes
- System identifies potential faults or communication breakages
- Results allow for informed decision-making before applying changes

### 4.3 Compliance Requirements Framework
- Baselines are established for fabric configurations
- NDI periodically checks configurations against established patterns
- Deviations trigger anomalies and notifications
- Dynamic compliance requirements can be managed through API automation

### 4.4 Security Considerations in API Usage
- Credential storage risks with username/password authentication
- Benefits of API key segmentation for different scripts/applications
- Revocation strategies for compromised credentials
- Role-based access control implementation through API authentication

## 5. Evaluate: Assessing Different Approaches

### 5.1 Authentication Method Comparison
- **Username/Password Authentication**:
  - Advantages: Familiar approach, works with all systems
  - Disadvantages: Security risks with credential storage, less granular control
  
- **API Keys Authentication**:
  - Advantages: Better security, granular control, selective revocation
  - Disadvantages: Additional management overhead, requires initial setup

### 5.2 API Integration Tool Selection
- **Ansible**:
  - Best for: Organizations already using Ansible for network automation
  - Considerations: Requires learning Ansible syntax, module limitations
  
- **Postman**:
  - Best for: Development, testing, and API exploration
  - Considerations: Not ideal for production automation
  
- **Python**:
  - Best for: Custom integrations, complex workflows, production automation
  - Considerations: Requires programming knowledge, more development time

### 5.3 Use Case Prioritization
- **Pre-change Validation**:
  - Critical for preventing service disruptions
  - High value in CI/CD pipelines
  
- **Compliance Monitoring**:
  - Important for security and governance
  - Valuable for regulated industries
  
- **Anomaly Detection**:
  - Essential for proactive operations
  - Reduces MTTD and MTTR

### 5.4 Integration Strategy Assessment
- Direct API calls vs. using provided modules
- Synchronous vs. asynchronous processing
- Polling vs. event-driven approaches
- Error handling and retry strategies

## 6. Create: Designing Solutions and Implementations

### 6.1 CI/CD Pipeline Integration Design
- Integrate NDI pre-change validation into deployment workflows
- Implement automated testing of configuration changes
- Design approval gates based on validation results
- Create reporting mechanisms for validation outcomes

### 6.2 Custom Compliance Framework
- Design dynamic compliance rule generation based on organizational policies
- Develop automated remediation workflows for compliance violations
- Create compliance dashboards and reporting systems
- Implement compliance trend analysis for continuous improvement

### 6.3 Comprehensive Monitoring Solution
- Design multi-fabric health monitoring system using NDI APIs
- Develop custom alerting mechanisms based on anomaly detection
- Create historical analysis tools for performance trends
- Implement predictive analytics for proactive issue prevention

### 6.4 Cross-Platform Integration Architecture
- Design workflows that integrate NDI with other systems (ITSM, monitoring, etc.)
- Develop abstraction layers for consistent interaction across platforms
- Create unified dashboards combining data from multiple sources
- Implement event correlation across different network management systems

## Practical Exercises

1. **Basic API Authentication (Apply)**
   - Implement both authentication methods (username/password and API key)
   - Compare the implementation complexity and security implications

2. **Pre-Change Validation Workflow (Apply/Analyze)**
   - Create a script that submits configuration changes for validation
   - Parse and interpret validation results
   - Implement decision logic based on validation outcomes

3. **Compliance Monitoring System (Analyze/Create)**
   - Design and implement a system for dynamic compliance rule management
   - Create automated reporting for compliance status
   - Develop remediation workflows for compliance violations

4. **Cross-Platform Integration (Create)**
   - Design and implement an integration between NDI and an ITSM system
   - Create workflows that span multiple platforms
   - Develop unified reporting across integrated systems

## Assessment Questions

### Remember Level
1. What are the three main categories of functionality provided by Nexus Dashboard Insights?
2. Which transport protocol is used for NDI REST API communication?
3. Name two authentication methods supported by the NDI REST API.

### Understand Level
1. Explain the difference between proactive and reactive troubleshooting in NDI.
2. Describe how the Nexus Dashboard API Gateway routes requests to different applications.
3. Explain the purpose of pre-change validation in network operations.

### Apply Level
1. Write a Python code snippet that authenticates to the NDI API using an API key.
2. Implement a function that retrieves anomalies from NDI and filters them by severity.
3. Create an Ansible playbook that performs pre-change validation for an ACI configuration.

### Analyze Level
1. Compare and contrast the security implications of username/password authentication versus API key authentication.
2. Analyze the workflow of pre-change validation and identify potential bottlenecks or failure points.
3. Break down the compliance requirements framework and explain how it interacts with fabric configurations.

### Evaluate Level
1. Evaluate the suitability of different API integration tools (Ansible, Postman, Python) for various organizational contexts.
2. Assess the relative importance of different NDI use cases for a financial services organization with strict compliance requirements.
3. Critique a given API integration design for scalability, security, and maintainability.

### Create Level
1. Design a comprehensive CI/CD pipeline that incorporates NDI pre-change validation.
2. Develop a cross-platform integration architecture that combines NDI data with other monitoring systems.
3. Create a custom compliance framework that automatically generates and enforces rules based on organizational policies.

## References and Resources

1. Cisco DevNet Portal: [https://developer.cisco.com/](https://developer.cisco.com/)
2. Nexus Dashboard Insights Documentation
3. Cisco Ansible Collection for NDI
4. Python Requests Library Documentation
5. REST API Design Best Practices
