# ACI Multi-Site Design: Architecture and Implementation

## Learning Objectives

By the end of this module, you will be able to:
- Describe the key components and architecture of Cisco ACI Multi-Site (Remember/Understand)
- Analyze connectivity requirements for Multi-Site deployments with disaster recovery (Apply/Analyze)
- Design an ACI Multi-Site solution that meets business continuity requirements (Evaluate/Create)

## Prerequisites

- Understanding of basic ACI fabric architecture
- Knowledge of BGP routing concepts
- Completion of "ACI Single-Site Design Fundamentals" module

## Module Information

- **Difficulty Level**: Intermediate
- **Estimated Completion Time**: 45 minutes
- **CCDE Domain**: ACI & Data Center

## Introduction

Cisco ACI Multi-Site is a critical architecture for organizations requiring multiple data centers with synchronized policy. This module explores how Multi-Site Orchestrator (MSO) enables centralized policy management across geographically distributed ACI fabrics while supporting disaster recovery and business continuity requirements. Understanding Multi-Site design is essential for CCDE candidates as it represents a common enterprise requirement for modern data center architecture.

## Key Concepts

### Multi-Site Architecture Components

The ACI Multi-Site architecture consists of several key components:

1. **Multi-Site Orchestrator (MSO)**: Centralized policy controller that manages multiple ACI fabrics
2. **Site Controllers (APICs)**: Local APIC clusters managing individual ACI fabrics
3. **Spine Proxy**: Feature on spine switches that handles inter-site communications
4. **Inter-Site Network (ISN)**: IP network connecting the sites
5. **Stretched VLANs**: Layer 2 extensions between sites (when required)

![Multi-Site Architecture Diagram](https://example.com/mso-architecture.png)

#### Knowledge Check
What is the primary role of the Multi-Site Orchestrator (MSO) in an ACI Multi-Site deployment?
- A. Direct control of leaf and spine switches
- B. Local policy enforcement within a single fabric
- C. Centralized policy management across multiple ACI fabrics
- D. BGP route reflection between sites

### Multi-Site Communication Models

ACI Multi-Site supports several inter-site communication models:

1. **Stretched EPG Model**: Extends an EPG across multiple sites
   - Requires Layer 2 stretch between sites
   - Provides seamless workload mobility
   - Higher complexity and potential failure domain expansion

2. **Disjoint EPG Model**: Separate EPGs at each site with contractual relationships
   - More resilient failure domain boundaries
   - Requires explicit contract configuration
   - Simpler Layer 3 connectivity between sites

3. **Shared Services Model**: Centralized services accessed by multiple sites
   - Optimizes resource utilization
   - Reduces duplication of service infrastructure
   - May introduce single points of failure

#### Knowledge Check
In a disaster recovery scenario with limited inter-site bandwidth, which Multi-Site communication model would typically be most appropriate?
- A. Stretched EPG with full Layer 2 extension
- B. Disjoint EPG with Layer 3 connectivity
- C. Full mesh of stretched VLANs
- D. Direct VXLAN tunneling without MSO

### Disaster Recovery Design Considerations

When designing ACI Multi-Site for disaster recovery, consider these factors:

1. **Recovery Point Objective (RPO)**: How much data loss is acceptable
   - Influences synchronization requirements
   - Impacts bandwidth requirements between sites

2. **Recovery Time Objective (RTO)**: How quickly services must be restored
   - Affects automation requirements
   - Determines whether active/active or active/standby is appropriate

3. **Traffic Patterns**: Application communication flows
   - Intra-application communication requirements
   - External client access patterns
   - Service dependency mapping

4. **Stretched vs. Non-Stretched**: Layer 2 extension requirements
   - Application requirements for Layer 2 adjacency
   - Implementation options (OTV, VXLAN, etc.)
   - Failure domain considerations

#### Knowledge Check
If an application requires synchronous database replication between sites with an RPO near zero, which design aspect becomes most critical?
- A. Inter-site latency and bandwidth
- B. Number of spine switches
- C. APIC cluster size
- D. L4-L7 service graph implementation

## Practical Application

### Scenario
Financial Services Company XYZ needs to design an ACI Multi-Site solution connecting their primary data center in New York with a disaster recovery site in Chicago. They require:
- RPO of less than 15 minutes for critical applications
- RTO of 1 hour for all services
- Active/standby configuration with automated failover
- Support for both Layer 2 and Layer 3 applications

### Requirements
- Primary data center: 50 leaf switches, 6 spine switches
- DR site: 20 leaf switches, 4 spine switches
- 10 Gbps inter-site connectivity (dual links)
- Round-trip latency of 15ms between sites
- Critical database applications requiring Layer 2 adjacency
- Web and application tiers that can operate with Layer 3 connectivity

### Design Exercise
1. **Determine MSO Placement**:
   - Analyze the pros and cons of hosting MSO in each site
   - Consider a third site for MSO placement
   - Document your recommendation with justification

2. **Design Inter-Site Connectivity**:
   - Calculate bandwidth requirements based on replication needs
   - Determine routing protocol configuration
   - Plan for QoS to prioritize critical replication traffic

3. **Application Placement Strategy**:
   - Identify which applications require stretched EPGs
   - Design disjoint EPGs for applications that can use Layer 3
   - Create a mapping of applications to communication models

## Design Considerations

When implementing ACI Multi-Site for disaster recovery, consider these critical design factors:

1. **MSO Resilience**: The MSO is critical for policy updates but not for data plane operations. Consider deploying MSO in a third site or cloud location to ensure availability during a site failure.

2. **Bandwidth Engineering**: Carefully calculate replication traffic and ensure adequate inter-site bandwidth. Consider compression and deduplication technologies to optimize WAN utilization.

3. **Failure Domain Isolation**: Minimize Layer 2 stretching to reduce failure domain propagation. Use disjoint EPGs where possible to maintain isolation.

4. **Testing Strategy**: Develop a comprehensive testing plan for disaster scenarios. Regular testing is essential to validate recovery procedures.

5. **Automation**: Implement automation for failover procedures to meet RTO requirements. Scripts should validate both application and infrastructure readiness.

## Common Pitfalls

- **Over-stretching Layer 2**: Extending too many VLANs between sites increases risk and complexity
- **Underestimating Bandwidth**: Failing to account for peak replication loads
- **Neglecting External Connectivity**: Forgetting to design for consistent external access during failover
- **Manual Recovery Procedures**: Relying on manual steps that extend RTO
- **Incomplete Application Mapping**: Missing application dependencies that break during failover

## Key Takeaways

- ACI Multi-Site provides policy consistency across multiple data centers while supporting disaster recovery
- The communication model (stretched EPG, disjoint EPG, shared services) should be selected based on application requirements
- RPO and RTO requirements drive key design decisions including bandwidth, automation, and Layer 2 extension requirements
- Carefully manage failure domains to prevent cascading failures across sites

## Further Learning

- "ACI Multi-Site Troubleshooting" module
- "VXLAN EVPN Multi-Site Implementation" module
- Cisco Live session: BRKDCN-3615 - ACI Multi-Site Design and Deployment
- Cisco White Paper: "Cisco ACI Multi-Site Architecture"

## Summary

ACI Multi-Site architecture enables organizations to implement robust disaster recovery solutions while maintaining consistent policy across multiple data centers. By understanding the components, communication models, and design considerations presented in this module, you can design effective Multi-Site solutions that balance business continuity requirements with technical constraints. These concepts are fundamental to the CCDE exam and represent real-world challenges faced by network designers.

## Assessment

### Multiple Choice Questions

1. In an ACI Multi-Site design, which component is responsible for centralized policy management?
   - A. Local APIC cluster
   - B. Multi-Site Orchestrator
   - C. Spine Proxy
   - D. Inter-Site Network

2. When designing ACI Multi-Site with minimal inter-site latency impact, which approach is most appropriate?
   - A. Always use stretched EPGs for all applications
   - B. Implement full Layer 2 extension between sites
   - C. Use disjoint EPGs with Layer 3 communication where possible
   - D. Duplicate all services at both sites regardless of cost

### Scenario-Based Question

A retail company is implementing ACI Multi-Site between their primary and backup data centers. They have a mix of applications including a legacy inventory system that requires Layer 2 adjacency, modern web applications that can use Layer 3, and a PCI-compliant payment processing system that requires strict isolation.

#### Question
Which design approach best addresses these requirements while minimizing risk?
1. Design separate tenants for each application type with appropriate communication models
2. Use stretched EPGs for all applications to simplify management
3. Implement a dedicated ISN network for each application type
4. Deploy all applications using only Layer 3 communication

### Design Challenge

Design an ACI Multi-Site solution for a healthcare organization with three data centers (Primary, DR, and Edge). Consider data sovereignty requirements, latency-sensitive medical applications, and periodic batch processing requirements. Document your architecture including communication models, MSO placement, bandwidth requirements, and failure handling procedures. 