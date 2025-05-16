# Technical Primer: Policy-Based Redirect (PBR) in ACI

## Introduction

Policy-Based Redirect (PBR) is a powerful feature in Cisco Application Centric Infrastructure (ACI) that enables service insertion and traffic steering through network services like firewalls and load balancers. This technical primer explores PBR concepts, implementation details, packet flow mechanics, and advanced deployment scenarios, structured according to Bloom's Taxonomy to facilitate comprehensive learning.

## 1. Remember: Fundamental Concepts and Terminology

### 1.1 Policy-Based Redirect Fundamentals
- PBR stands for Policy-Based Redirect, not Policy-Based Routing
- Enables service insertion in ACI fabrics, particularly for firewalls
- Implemented as part of contracts between EPGs (Endpoint Groups)
- Redirects traffic to service devices instead of sending directly to destination
- Maintains the source and destination IP addresses during redirection

### 1.2 Service Graph Components
- Service Graph: Logical representation of service insertion
- Shadow EPG (Service EPG): Automatically deployed EPG for service device connectivity
- Connector: Leg of the service device connecting to the fabric
- Consumer Connector: Connection between consumer and service device
- Provider Connector: Connection between service device and provider

### 1.3 Service Device Configuration
- One-arm mode: Single interface for both consumer and provider traffic
- Two-arm mode: Separate interfaces for consumer and provider traffic
- Virtual MAC: MAC address used for redirection
- Service IP: IP address assigned to the service device
- L4-L7 Device: Physical or virtual appliance providing network services

### 1.4 Policy Application in ACI
- Ingress policy: Applied at the leaf where traffic enters the fabric
- Egress policy: Applied at the leaf where traffic exits the fabric
- SPDP bit: Policy Done bit in VXLAN header indicating policy application status
- S-Class: Source EPG class identifier
- D-Class: Destination EPG class identifier

### 1.5 PBR Deployment Scenarios
- East-West traffic: Between EPGs within the ACI fabric
- North-South traffic: Between EPGs and external networks
- Multi-Pod: PBR across multiple ACI pods
- Multi-Site: PBR across multiple ACI sites
- Any-to-Any: PBR between any endpoints regardless of location

## 2. Understand: Explaining Concepts and Relationships

### 2.1 PBR vs. Traditional Service Insertion
- Traditional approach requires default gateway on firewall or VRF stitching
- PBR maintains the original destination IP while redirecting traffic
- PBR simplifies routing by keeping services in-line with traffic flow
- One-arm deployment is possible with PBR, simplifying firewall configuration
- PBR preserves the contract model while adding service insertion

### 2.2 Policy Application Process
- Ingress leaf attempts to apply policy based on source and destination EPG
- Source EPG (S-Class) is always known based on ingress interface/VLAN
- Destination EPG (D-Class) may be known if endpoint is in local table
- If D-Class is unknown, SPDP bit is set to 0 (policy not applied)
- Egress leaf applies policy if SPDP bit indicates policy was not applied at ingress

### 2.3 PBR Packet Flow
- Original packet arrives at ingress leaf with destination MAC of next hop
- Policy lookup determines redirection is required
- Ingress leaf rewrites destination MAC to service device virtual MAC
- Packet is encapsulated in VXLAN with VNID of service bridge domain
- Packet is sent to spine proxy for forwarding to service device
- Service device processes packet and returns it to fabric
- Return packet is classified in service EPG and permitted to destination

### 2.4 Service Graph Deployment
- Contract with redirect policy is configured between consumer and provider EPGs
- Service graph template is attached to the contract
- ACI automatically creates shadow EPGs for service device connectivity
- VLAN is allocated for service device connection
- Virtual MAC is configured on service device or discovered via IP SLA

### 2.5 Multi-Pod and Multi-Site Considerations
- Symmetric PBR ensures traffic returns through the same service device
- Pod ID-aware redirection controls service device selection based on pod
- Anycast service nodes allow active-active service device deployment
- Multi-site PBR requires special configuration for cross-site traffic
- Any-to-Any PBR enables service insertion regardless of endpoint location

## 3. Apply: Implementing PBR in ACI

### 3.1 Configuring Basic PBR
```
# APIC GUI Configuration Steps

## Step 1: Create L4-L7 Device
- Navigate to Tenants > [Tenant] > Services > L4-L7 > Devices
- Create new device with appropriate interfaces
- Configure virtual MAC for service redirection

## Step 2: Create Service Graph Template
- Navigate to Tenants > [Tenant] > Services > L4-L7 > Service Graph Templates
- Create new template with firewall node
- Configure consumer and provider connectors

## Step 3: Create Redirect Policy
- Navigate to Tenants > [Tenant] > Networking > Protocol Policies > L4-L7 Policy-Based Redirect
- Create new policy with service IP and virtual MAC
- Configure IP SLA monitoring if needed

## Step 4: Create Device Selection Policy
- Navigate to Tenants > [Tenant] > Services > L4-L7 > Device Selection Policies
- Create new policy linking service graph, logical device, and redirect policy

## Step 5: Apply to Contract
- Navigate to Tenants > [Tenant] > Contracts
- Create or edit contract between consumer and provider EPGs
- Apply service graph to contract
```

### 3.2 Configuring One-Arm Mode
```
# One-Arm Configuration Example

## L4-L7 Device Configuration
- Single interface for both consumer and provider traffic
- Same bridge domain for consumer and provider connectors
- Single virtual MAC for redirection

## Firewall Configuration
- Single interface with default route pointing back to fabric
- Static routes or dynamic routing for specific subnets if needed
- Security policies for both directions on single interface

## Redirect Policy Configuration
- Single destination IP (service IP)
- Single virtual MAC
- Health monitoring via IP SLA
```

### 3.3 Configuring Two-Arm Mode
```
# Two-Arm Configuration Example

## L4-L7 Device Configuration
- Separate interfaces for consumer and provider traffic
- Different bridge domains for consumer and provider connectors
- Separate virtual MACs for each direction

## Firewall Configuration
- Two interfaces with appropriate routing
- Security policies applied to appropriate interfaces
- Routing between interfaces (internal routing)

## Redirect Policy Configuration
- Separate redirect policies for consumer and provider directions
- Different destination IPs and virtual MACs
- Health monitoring for both interfaces
```

### 3.4 Implementing Multi-Pod PBR
```
# Multi-Pod PBR Configuration

## Redirect Policy Configuration
- Enable "Symmetric PBR" option
- Do NOT enable "Pod ID Aware Redirection" for east-west traffic
- Configure IP SLA monitoring for each service device

## L4-L7 Device Configuration
- Configure devices in each pod
- Use separate concrete devices for each pod
- Configure appropriate interfaces and VLANs

## Service Graph Configuration
- Single service graph template for all pods
- Device selection policy maps to concrete devices in each pod
- Apply to contracts spanning pods
```

### 3.5 Troubleshooting PBR
```
# PBR Troubleshooting Commands

## Verify PBR Configuration
- show service redir detail
- show service redir info
- show service redir stats

## Verify Policy Application
- show zoning-rule scope vrf
- show zoning-rule filter <filter-id>

## Verify Endpoint Information
- show endpoint ip <ip-address>
- show endpoint mac <mac-address>

## Verify VXLAN Encapsulation
- show platform internal hal l2 port gpd

## Capture Packets with ELAM
- debug platform internal hal init asic <asic-num>
- debug platform internal hal start-elam asic <asic-num>
- debug platform internal hal show-elam asic <asic-num>
```

## 4. Analyze: Breaking Down Complex PBR Scenarios

### 4.1 PBR Packet Flow Analysis
- **Ingress Leaf Processing**:
  - Packet arrives with original source and destination
  - Source EPG determined from ingress interface/VLAN
  - Destination EPG determined from endpoint table
  - Policy lookup identifies redirect action
  - Destination MAC rewritten to service device virtual MAC
  - VXLAN encapsulation with service bridge domain VNID
  - Packet sent to spine proxy

- **Spine Processing**:
  - Receives VXLAN packet from ingress leaf
  - Looks up destination MAC in COOP database
  - Identifies leaf where service device is connected
  - Forwards packet to appropriate leaf

- **Service Device Leaf Processing**:
  - Receives VXLAN packet from spine
  - Decapsulates VXLAN header
  - Forwards layer 2 packet to service device
  - Classifies return traffic from service device
  - Applies permit policy for service EPG to destination

- **Return Path Processing**:
  - Similar flow in reverse direction
  - May involve different service device for asymmetric flows
  - Requires symmetric PBR for stateful services

### 4.2 Service Graph Deployment Analysis
- **Shadow EPG Creation**:
  - Automatically generated during service graph deployment
  - Contains service device endpoints
  - Has implicit contracts with consumer and provider EPGs
  - Uses dynamically allocated VLANs
  - Not directly configurable by users

- **VLAN Allocation**:
  - Dynamic allocation from VLAN pool
  - One VLAN per connector
  - Same VLAN for both connectors in one-arm mode
  - Different VLANs for each connector in two-arm mode
  - VLAN information passed to service device via device package or manual configuration

- **Contract Transformation**:
  - Original contract between consumer and provider
  - Transformed into two contracts:
    1. Consumer EPG to Service EPG
    2. Service EPG to Provider EPG
  - Filter information preserved in both contracts
  - Redirect action applied to appropriate contract

- **Service Device Discovery**:
  - MAC address learned in shadow EPG
  - IP address monitored via IP SLA
  - Health status tracked for each service device
  - Failure detection triggers redirection to backup device

### 4.3 Multi-Pod PBR Analysis
- **Traffic Flow Considerations**:
  - Inter-pod traffic traverses IPN (Inter-Pod Network)
  - Service devices may exist in one or both pods
  - Symmetric flow requires consistent service device selection
  - State information must be maintained for stateful services

- **Symmetric PBR Mechanism**:
  - Uses hash-based selection of service device
  - Hash calculated from 5-tuple (source IP, destination IP, protocol, source port, destination port)
  - Same hash value for both directions of flow
  - Ensures traffic returns through same service device
  - Critical for stateful services like firewalls

- **Pod ID-Aware Redirection Limitations**:
  - Only appropriate for north-south traffic
  - Can cause asymmetric flows for east-west traffic
  - Based on endpoint location rather than flow characteristics
  - May override symmetric hash-based selection

- **Anycast Service Nodes**:
  - Same virtual IP and MAC in multiple pods
  - Requires service device state synchronization
  - Allows active-active deployment across pods
  - Simplifies configuration but requires compatible service devices

### 4.4 Multi-Site PBR Analysis
- **Cross-Site Considerations**:
  - Sites connected via Inter-Site Network (ISN)
  - Different BGP ASNs per site
  - Limited bandwidth and higher latency between sites
  - Potential for asymmetric routing

- **Service Placement Options**:
  - Local service insertion (within each site)
  - Centralized service insertion (at one site)
  - Distributed service insertion (active-active across sites)
  - Each option has different traffic flow implications

- **State Synchronization Requirements**:
  - Stateful services require state synchronization
  - Synchronization may occur via dedicated links
  - Latency impacts synchronization effectiveness
  - Failure scenarios must be carefully considered

- **Configuration Propagation**:
  - Service graph configuration via Multi-Site Orchestrator (MSO)
  - Local vs. stretched service graph templates
  - Site-specific concrete device mapping
  - Consistent policy application across sites

### 4.5 Failure Mode Analysis
- **Service Device Failure**:
  - Detection via IP SLA monitoring
  - Traffic redirection to backup device
  - Session state loss for stateful services
  - Recovery when primary device returns

- **Leaf Node Failure**:
  - Service device becomes unreachable
  - Traffic redirected to service devices on other leaves
  - Potential for asymmetric flows during convergence
  - Recovery when leaf returns

- **Spine Node Failure**:
  - Alternative paths through other spines
  - Minimal impact due to spine redundancy
  - Potential for temporary packet loss during convergence
  - No specific PBR recovery actions needed

- **Pod or Site Failure**:
  - Service devices in failed pod/site unreachable
  - Traffic redirected to devices in operational pods/sites
  - Significant state loss for stateful services
  - Recovery procedures depend on deployment model

## 5. Evaluate: Assessing Different PBR Approaches

### 5.1 Service Insertion Model Comparison
- **PBR-Based Service Insertion**:
  - Advantages: Flexible placement, one-arm support, maintains original addressing
  - Disadvantages: Complexity, potential asymmetry, troubleshooting challenges
  - Best for: East-west traffic, distributed services, ACI-native deployments

- **VRF Stitching**:
  - Advantages: Simpler routing, traditional design, familiar to network teams
  - Disadvantages: Requires two-arm mode, more VRFs, complex routing
  - Best for: North-south traffic, traditional firewall deployments

- **Service Chain**:
  - Advantages: Multiple services in sequence, comprehensive service insertion
  - Disadvantages: Increased complexity, potential performance impact
  - Best for: Complex security requirements, multiple service types

### 5.2 Deployment Mode Assessment
- **One-Arm Mode**:
  - Advantages: Simpler firewall configuration, fewer interfaces, easier routing
  - Disadvantages: Potential hairpinning, single interface bottleneck
  - Best for: Smaller deployments, simpler service requirements

- **Two-Arm Mode**:
  - Advantages: Clearer traffic separation, traditional firewall deployment
  - Disadvantages: More complex configuration, additional interfaces required
  - Best for: High-security environments, traditional firewall teams

- **Mixed Mode**:
  - Advantages: Flexibility to choose per service, optimization opportunities
  - Disadvantages: Inconsistent configuration, more complex management
  - Best for: Diverse service requirements, transitional deployments

### 5.3 Multi-Pod Strategy Evaluation
- **Pod-Local Services**:
  - Advantages: Lower inter-pod bandwidth, better performance, simpler failure domains
  - Disadvantages: More service devices, potential configuration duplication
  - Best for: Distributed applications, latency-sensitive services

- **Centralized Services**:
  - Advantages: Fewer service devices, centralized management, consistent policy
  - Disadvantages: Higher inter-pod bandwidth, potential latency impact
  - Best for: Centralized applications, limited service device licenses

- **Hybrid Approach**:
  - Advantages: Optimized for specific traffic patterns, balanced resource usage
  - Disadvantages: More complex configuration, potential asymmetry
  - Best for: Mixed application requirements, phased migrations

### 5.4 Multi-Site Strategy Assessment
- **Site-Local Services**:
  - Advantages: Lower inter-site bandwidth, better performance, independent operation
  - Disadvantages: More service devices, potential policy inconsistency
  - Best for: Geographically distributed applications, disaster recovery scenarios

- **Stretched Services**:
  - Advantages: Consistent policy, fewer service devices, simplified management
  - Disadvantages: Higher inter-site bandwidth, synchronization challenges
  - Best for: Active-active data centers, centralized security requirements

- **Service Tiering**:
  - Advantages: Optimized resource usage, appropriate service placement
  - Disadvantages: More complex design, potential policy inconsistency
  - Best for: Mixed criticality applications, cost-optimized deployments

### 5.5 Monitoring and Troubleshooting Approach Evaluation
- **Proactive Monitoring**:
  - Advantages: Early detection of issues, trend analysis, capacity planning
  - Disadvantages: Additional tools required, potential alert fatigue
  - Best for: Critical services, high-availability requirements

- **Reactive Troubleshooting**:
  - Advantages: Focused on actual issues, detailed analysis
  - Disadvantages: After-the-fact detection, potential service impact
  - Best for: Less critical services, limited monitoring resources

- **Hybrid Approach**:
  - Advantages: Balanced resource usage, prioritized monitoring
  - Disadvantages: More complex implementation, tool integration challenges
  - Best for: Mixed service criticality, optimized operations

## 6. Create: Designing Solutions and Implementations

### 6.1 Enterprise-Scale PBR Architecture
- Design a comprehensive PBR architecture for large enterprise deployments
- Create service insertion zones based on security requirements
- Develop redundancy models for critical services
- Implement monitoring and alerting for service health
- Design troubleshooting procedures and runbooks

### 6.2 Multi-Tier Service Insertion Model
- Create a service insertion architecture with multiple security tiers
- Design traffic flow patterns between tiers
- Develop policy models for different security zones
- Implement service chaining for complex requirements
- Create migration strategies from traditional models

### 6.3 Cross-Domain Service Insertion
- Design service insertion across multiple ACI domains
- Create consistent policy models across domains
- Develop inter-domain traffic flow patterns
- Implement monitoring for cross-domain services
- Design failure recovery procedures

### 6.4 Cloud-Integrated Service Insertion
- Create a hybrid service insertion model spanning on-premises and cloud
- Design consistent policy application across environments
- Develop traffic steering mechanisms for cloud workloads
- Implement monitoring and visibility across domains
- Create migration strategies for workload mobility

### 6.5 Automated PBR Deployment Framework
- Design templates for common PBR deployment scenarios
- Create validation procedures for PBR configurations
- Develop automated testing for service insertion
- Implement CI/CD pipelines for PBR deployment
- Design monitoring and rollback procedures

## Practical Exercises

1. **Basic PBR Configuration (Apply)**
   - Configure a simple one-arm firewall insertion using PBR
   - Verify traffic flow through the firewall
   - Test failover to a backup firewall
   - Troubleshoot common configuration issues

2. **Multi-Pod PBR Implementation (Apply/Analyze)**
   - Configure PBR across multiple ACI pods
   - Analyze traffic flow patterns and service device selection
   - Implement symmetric PBR for stateful services
   - Test failure scenarios and recovery

3. **Complex Service Chain Design (Analyze/Create)**
   - Design a service chain with multiple service types
   - Analyze traffic flow through the service chain
   - Implement the design in a lab environment
   - Test and validate the implementation

4. **Enterprise PBR Architecture (Create)**
   - Design a comprehensive PBR architecture for an enterprise
   - Create deployment templates and procedures
   - Develop monitoring and troubleshooting strategies
   - Document design decisions and rationales

## Assessment Questions

### Remember Level
1. What does PBR stand for in the context of Cisco ACI?
2. What is a shadow EPG in the context of service insertion?
3. What is the difference between one-arm and two-arm service device deployment?

### Understand Level
1. Explain how PBR differs from traditional service insertion methods.
2. Describe the packet flow when traffic is redirected through a service device using PBR.
3. Explain the purpose of symmetric PBR in multi-pod deployments.

### Apply Level
1. Configure a basic PBR policy for inserting a firewall between two EPGs.
2. Implement health monitoring for service devices in a PBR configuration.
3. Troubleshoot a PBR configuration where traffic is not being redirected properly.

### Analyze Level
1. Analyze the packet flow in a multi-pod PBR deployment and identify potential asymmetry issues.
2. Break down the service graph deployment process and explain how shadow EPGs are created and used.
3. Compare the traffic flow patterns in one-arm versus two-arm deployments and identify the implications for firewall configuration.

### Evaluate Level
1. Evaluate different service insertion models for a multi-site ACI deployment and recommend the most appropriate approach.
2. Assess the trade-offs between centralized and distributed service insertion in a multi-pod environment.
3. Critique a given PBR design for redundancy, scalability, and manageability.

### Create Level
1. Design a comprehensive PBR architecture for a multi-pod, multi-site ACI deployment with appropriate redundancy and failover mechanisms.
2. Develop a service insertion strategy for migrating from a traditional firewall deployment to PBR-based insertion.
3. Create a troubleshooting guide for common PBR issues, including diagnostic procedures and resolution steps.

## References and Resources

1. Cisco ACI Policy-Based Redirect Documentation
2. Cisco ACI Service Insertion White Paper
3. Cisco ACI Multi-Pod Design Guide
4. Cisco ACI Multi-Site Design Guide
5. Cisco ACI Troubleshooting Guide
6. Cisco Live Presentations on ACI Service Insertion
