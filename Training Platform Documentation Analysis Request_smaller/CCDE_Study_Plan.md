# CCDE Certification Study Plan

*Updated on: 2025-05-05*

## Overview

This comprehensive study plan is organized by focus areas aligned with the CCDE certification requirements. Each focus area is broken down into weekly study objectives with specific topics and technologies, incorporating specialized guides for key technology domains.

| Focus Area             | Weeks | Resource Count | Est. Study Time |
| ---------------------- | ----- | -------------- | --------------- |
| AI Infrastructure      | 3     | 12             | 15 hours        |
| On-Prem Services & ACI | 4     | 15             | 20 hours        |
| Cloud Services         | 2     | 8              | 10 hours        |
| Container Technologies | 2     | 6              | 10 hours        |
| Large Scale Networks   | 2     | 5              | 10 hours        |
| Workforce Mobility     | 1     | 4              | 5 hours         |

## Specialized Study Guides

This master plan is supplemented by specialized study guides that provide in-depth coverage of key technology areas:

1. **[AI_STUDY_MATERIAL.MD](../AI_STUDY_MATERIAL.MD)** - Comprehensive AI infrastructure study plan
2. **[ACI_STUDY_MATERIAL.MD](../ACI_STUDY_MATERIAL.MD)** - ACI architecture and features
3. **[CISCO_ACI_MIGRATION_STUDY.MD](../CISCO_ACI_MIGRATION_STUDY.MD)** - ACI migration strategies
4. **[CONTAINER_NETWORKING_STUDY.MD](../CONTAINER_NETWORKING_STUDY.MD)** - Container and eBPF technologies
5. **[AI_SOURCES_INVENTORY.MD](../AI_SOURCES_INVENTORY.MD)** - Complete inventory of AI-related materials

## Detailed Study Plan

### AI Infrastructure

AI Infrastructure - CCDE certification core focus area

#### Week 1: Foundations

**Topics:**
- AI/Machine Learning fundamentals 
- AI infrastructure impact on network design
- Network fabric design for AI workloads

**Technologies:**
- AI Infrastructure Technology List
- Lossless fabrics
- RDMA and RoCE/RoCEv2
- Data processing unit (DPU) architectures

**Resources:**
- [CCDE_v3.1_Practical_AI_Infrastructure_Technology_List_12132024.pdf](../CCDE_v3.1_Practical_AI_Infrastructure_Technology_List_12132024.pdf)
- [The Evolution of AI in Networking](../Cisco_Sales_ACI_AI/The%20Evolution%20of%20AI%20in%20Networking%20-%203_21_24%20%2360PartnerSuccess.PDF)
- [Guidelines-for-secure-AI-system-development.pdf](../Guidelines-for-secure-AI-system-development.pdf)

**Activities:**
- Review official Cisco documentation on AI infrastructure
- Study AI networking fundamentals and requirements
- Analyze use cases for AI/ML in enterprise networks

#### Week 2: Design & Architecture

**Topics:**
- AI network design use cases (ML, LLMs, pattern recognition)
- Storage networking for AI
- Compute and GPU connectivity considerations

**Technologies:**
- GPU networking optimization
- NVMe/NVMe-oF
- AI clusters and network fabric design

**Resources:**
- [Networking for AI Workloads](../Cisco_Sales_ACI_AI/Networking%20for%20AI%20Workloads%20-%207_16_24%20%2360PartnerSuccess.PDF)
- [Navigating AI in Data Centers: CVD and MLOps Strategies](../Cisco_Sales_ACI_AI/EMEA%20DC%20PVT%20May%202024_Navigating%20AI%20in%20Data%20Centers_%20CVD%20and%20MLOps%20Strategies-PDF.PDF)

**Activities:**
- Design a reference architecture for AI infrastructure 
- Develop network scaling strategies for AI workloads
- Study QoS design for AI applications

#### Week 3: Security & Automation

**Topics:**
- AI security considerations
- Automation and orchestration for AI infrastructure
- Infrastructure as Code frameworks

**Technologies:**
- HyperShield
- AI-native security
- CI/CD for AI environments

**Resources:**
- [Cisco Hypershield: A New Era of AI-Native Security](../ACI_Cisco/Cisco_Hypershield_a_New_Era_of_AI_Native_Security_for_Data_Centers_and_Cloud%20(1).PDF)
- [AI Powered Security with Cisco Hypershield](../ACI_Cisco/PIW_-_AI_powered_Security_with_Cisco_Hypershield.pdf)

**Activities:**
- Practice securing AI infrastructure designs
- Develop automation workflows for AI environments
- Design scalable monitoring solutions for AI workloads

---

### On-Prem Services & ACI

On-Prem Services - CCDE certification core focus area

#### Week 1: ACI Fundamentals

**Topics:**
- ACI architecture and design principles
- ACI fabric components and topology
- Policy model and application profiles

**Technologies:**
- ACI 6.x
- VXLAN fabrics
- MP-BGP EVPN

**Resources:**
- [ACI 6.1.2f Features BDM](../ACI_Cisco/aci-6-1-2f-features-bdm.pptx)
- [ACI Release BDM Deck](../ACI_Cisco/aci-release-bdm-deck%20(1).pptx)
- [10 Years of ACI and Still More to Come](../ACI_Cisco/EMEA_DC_PVT_May_2024_10_years_of_ACI_and_still_more_to_come%20(2).pdf)

**Activities:**
- Study ACI fabric design options and limitations
- Analyze ACI policy model implementation scenarios
- Practice network policy design with ACI

#### Week 2: ACI Advanced Features

**Topics:**
- ESG migration and implementation
- External connectivity best practices
- Multi-site ACI design

**Technologies:**
- Endpoint Security Groups
- L3Out connectivity
- Multi-Pod and Multi-Site

**Resources:**
- [Migration Strategies for ACI ESGs](../ACI_Cisco/EMEA_DC_PVT_Nov_2023_Migration_Strategies_for_ACI_ESGs%20(1).pdf)
- [ACI External Connectivity Best Practices](../ACI_Cisco/EMEAR_Data_Center_PVT_May_2022_Cisco_ACI_External_Connectivity_Best_Practices%20(2).pdf)
- [Multi-Site Design](../ACI_Cisco/PIW_Design_and_Deploy_Everything_Multi_Site_The_Series_Part_2_Sites_and_How_to_Interconnect_Them_1_of_2_%20(1).pdf)

**Activities:**
- Design migration strategy from traditional networking to ACI
- Create multi-site ACI topology designs
- Practice ESG policy implementation

#### Week 3: Integration & Automation

**Topics:**
- Infrastructure as Code for ACI
- API integration and programmability
- Nexus Dashboard and operational tools

**Technologies:**
- Terraform
- Python with Cobra SDK
- Nexus Dashboard Insights

**Resources:**
- [Nexus as Code & CI/CD pipelines](../Cisco_Sales_ACI_AI/EMEA%20DC%20PVT%20Jun%202023_Nexus%20as%20Code%20%26%20CI_CD%20pipelines...%20-%20PDF.PDF)
- [BRKDCN-2673_Netxus_as_Code.pdf](../BRKDCN-2673_Netxus_as_Code.pdf)
- [NDI Best Practices in Deployment](../ACI_Cisco/NDI_Best_Practices_in_Deployment_Testing_and_Troubleshooting.pdf)

**Activities:**
- Develop Terraform templates for ACI deployment
- Configure Nexus Dashboard monitoring solutions
- Practice API-based configuration and automation

#### Week 4: Advanced Design & Troubleshooting

**Topics:**
- Policy-Based Routing in ACI
- Resilient and scalable modular network design
- Testing and troubleshooting methodologies

**Technologies:**
- PBR service insertion
- Contract and filter design
- ACI troubleshooting tools

**Resources:**
- [ACI Best Practices: PBR Part 1](../ACI_Cisco/PIW_ACI_Best_Practices_Series_PBR_Part_1%20(1).pdf)
- [ACI Best Practices: PBR Part 2](../ACI_Cisco/PIW_ACI_Best_Practices_Series_PBR_Part_2%20(1).pdf)
- [ACI Best Practices in Scoping, Deployment, Testing and Troubleshooting](../ACI_Cisco/ACI_Best_Practices_in_Scoping_Deployment_Testing_and_Troubleshooting.pdf)

**Activities:**
- Design service insertion workflows with ACI
- Develop troubleshooting methodologies
- Create reference designs for common enterprise scenarios

---

### Cloud Services

Cloud Services - CCDE certification core focus area

#### Week 1: Hybrid Cloud Architecture

**Topics:**
- Cloud/hybrid solution design
- Multi-cloud connectivity
- Securing hybrid deployments

**Technologies:**
- Cloud on-ramp solutions
- Cloud connectivity options
- Extended fabric designs

**Resources:**
- [Security Architecture Summit Cisco Multicloud Defense](../ACI_Cisco/Security_Architecture_Summit_Cisco_Multicloud_Defense.pdf)
- [CCDE v3.1 Practical On-Prem and Cloud Services Technology List](../CCDE_v3.1_Practical_On-Prem_and_Cloud_Services_Technology_List_12132024.pdf)

**Activities:**
- Design hybrid cloud connectivity architectures
- Develop cloud migration strategies
- Implement security controls for hybrid environments

#### Week 2: Cloud Native Networking

**Topics:**
- Cloud-native networking models
- SaaS, PaaS, and IaaS integration
- Cloud-based network services

**Technologies:**
- Cloud network virtualization
- Virtual network appliances
- Cloud connectivity services

**Resources:**
- [Data Center Use Cases](../ACI_Cisco/PIW_Data_Center_Use_Cases%20(1)%20(1).pdf)
- [PSOCRT-1010.pdf](../PSOCRT-1010.pdf)

**Activities:**
- Design cloud network segmentation strategies
- Develop connectivity patterns for cloud resources
- Create hybrid governance and compliance frameworks

---

### Container Technologies

Container Technologies - CCDE certification supporting focus area

#### Week 1: Container Networking Fundamentals

**Topics:**
- Container networking models
- eBPF technology fundamentals
- Integration with data center infrastructure

**Technologies:**
- Kubernetes CNI
- eBPF
- Isovalent Cilium

**Resources:**
- [Introduction to eBPF](../ACI_Cisco/Introduction%20to%20eBPF.pptx)
- [Isovalent eBPF Based Networking](../ACI_Cisco/EMEA_DC_PVT_May_2024_Isovalent_eBPF_based_networking_security_and_observability%20(1).pdf)

**Activities:**
- Study container network models and traffic flows
- Compare CNI implementation options
- Analyze eBPF use cases for networking

#### Week 2: Container Security & Integration

**Topics:**
- Container network security
- Service mesh implementation
- Integration with traditional infrastructure

**Technologies:**
- Network policies
- Service mesh architectures
- API gateways

**Resources:**
- [HyperShield: AI-Native Security](../ACI_Cisco/Cisco_Hypershield_a_New_Era_of_AI_Native_Security_for_Data_Centers_and_Cloud%20(1).PDF)
- [Zero Trust Architecture](../ACI_Cisco/zero-trust-architecture%20(1).pdf)

**Activities:**
- Design container security policies
- Develop integration patterns with existing infrastructure
- Create multi-cluster networking designs

---

### Large Scale Networks

Large Scale Networks - CCDE certification core focus area

#### Week 1: SDN Architecture

**Topics:**
- Software-defined architecture principles
- Controller-based solution design
- Overlay/underlay models

**Technologies:**
- SD-WAN
- VXLAN/EVPN
- Segment routing

**Activities:**
- Study SDN controller architectures and protocols
- Design scalable overlay networks
- Analyze migration strategies to SD-WAN

#### Week 2: Network Design & Security

**Topics:**
- User and application experience
- Network security design and integration
- Network virtualization

**Technologies:**
- Network segmentation
- End-to-end security
- Traffic engineering

**Activities:**
- Design secure segment routing deployments
- Develop QoS for application experience
- Create scalable network virtualization designs

---

### Workforce Mobility

Workforce Mobility - CCDE certification core focus area

#### Week 1: Mobility Solutions

**Topics:**
- Enterprise mobility architecture
- Wireless network design
- Remote access solutions

**Technologies:**
- 802.11 standards (up to Wi-Fi 7)
- SD-Access
- ZTNA/SASE

**Resources:**
- [Zero Trust Architecture](../ACI_Cisco/zero-trust-architecture%20(1).pdf)
- [ISE: The Core of Cisco's Zero Trust Architecture](../ACI_Cisco/EMEA_PVT_Security_Jun_2024_ISE_The_Core_of_Ciscos_Zero_Trust_Architecture.pdf)

**Activities:**
- Design enterprise mobility solutions
- Create wireless network designs for high-density environments
- Develop secure remote access architectures

---

## Study Method

1. **Begin with Focus Area Foundations**:
   - Start with the CCDE v3.1 Technology Lists for your focus areas
   - Review the specialized study guide (MD files) for each area

2. **Progressive Learning Approach**:
   - Week 1: Study fundamental concepts and architectures
   - Week 2: Focus on design principles and implementation techniques
   - Week 3+: Work through advanced topics and integration challenges

3. **Practical Application**:
   - For each technology area, create design scenarios
   - Practice mapping requirements to technology selections
   - Develop justifications for design decisions

4. **Comprehensive Review**:
   - After completing each focus area, review key concepts
   - Create mind maps of technology relationships
   - Practice explaining design decisions verbally

## Additional Resources

- [9780137601042_Sample.pdf](../9780137601042_Sample.pdf) - CCDE Study Guide sample
- Official Cisco CCDE documentation and white papers
- Cisco Learning Network (CCDE study group)
- CCDE Practice Exams
- Hands-on labs with relevant technologies
