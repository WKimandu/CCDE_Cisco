## Learning Objectives for Core Technologies (CCDE v3.1)

### Core Technology List Section: 2.0 Layer 2 Control Plane

**Overall Goal for this Section:** The candidate should be able to design, analyze, and evaluate robust, scalable, and resilient Layer 2 control plane solutions for enterprise and data center networks, considering loop prevention, fault isolation, multicast switching, and integration with various physical media and Layer 2 technologies.

---

### CCDE Core Technology Topic: 2.1 Physical media considerations

**Overall Goal for this Topic:** The candidate should be able to analyze how physical media characteristics and failure detection mechanisms impact Layer 2 control plane behavior and overall network convergence.

#### Learning Objectives by Bloom\'s Taxonomy Level:

**Level 1: Remember**
*   **Objective 2.1.1:** Identify common Layer 1 down detection mechanisms (e.g., loss of light, loss of signal).
*   **Objective 2.1.2:** Recall factors that influence interface convergence times (e.g., debounce timers, protocol timers).

**Level 2: Understand**
*   **Objective 2.1.3:** Explain how physical layer issues (e.g., unidirectional links, flapping interfaces) can impact Layer 2 control plane stability.
*   **Objective 2.1.4:** Describe the interaction between physical layer down detection and higher-layer Layer 2 protocols (e.g., Spanning Tree).

**Level 3: Apply**
*   **Objective 2.1.5:** Choose appropriate interface settings (e.g., keepalive timers, debounce timers) to balance rapid fault detection with stability.

**Level 4: Analyze**
*   **Objective 2.1.6:** Analyze the convergence characteristics of a Layer 2 network given specific physical media types and interface configurations.
*   **Objective 2.1.7:** Differentiate the impact of physical media failures (e.g., fiber cut vs. copper cable issue) on Layer 2 control plane reconvergence.

**Level 5: Evaluate**
*   **Objective 2.1.8:** Evaluate the design of a Layer 2 network for its resilience to various physical media failures and its ability to quickly detect and recover from them.
*   **Objective 2.1.9:** Justify the use of specific physical layer monitoring and diagnostic tools in a Layer 2 environment.

**Level 6: Create**
*   **Objective 2.1.10:** Design a Layer 2 access network that incorporates robust physical media considerations to minimize downtime and ensure rapid fault detection.

---

### CCDE Core Technology Topic: 2.2 Loop detection protocols and loop-free topology mechanisms

**Overall Goal for this Topic:** The candidate should be able to design, analyze, and evaluate Layer 2 loop prevention and detection mechanisms, including various Spanning Tree protocols and alternative loop-free technologies, to ensure a stable and efficient Layer 2 domain.

#### Learning Objectives by Bloom\'s Taxonomy Level:

**Level 1: Remember**
*   **Objective 2.2.1:** List common Spanning Tree Protocol (STP) versions (e.g., CST, PVST+, RPVST+, MSTP).
*   **Objective 2.2.2:** Identify key STP concepts (e.g., Root Bridge, Designated Port, Root Port, BPDU, Port States).
*   **Objective 2.2.3:** Recall alternative Layer 2 multipathing or loop-free technologies (e.g., TRILL, SPB, switch clustering/stacking, fabric path).

**Level 2: Understand**
*   **Objective 2.2.4:** Explain the process of STP root bridge election and path cost calculation.
*   **Objective 2.2.5:** Describe the benefits of Rapid PVST+ and MSTP over legacy STP versions in terms of convergence and scalability.
*   **Objective 2.2.6:** Discuss common STP tuning techniques (e.g., portfast, BPDU guard, root guard, loop guard, UDLD).
*   **Objective 2.2.7:** Explain how switch clustering or stacking technologies provide a loop-free active-active forwarding path.

**Level 3: Apply**
*   **Objective 2.2.8:** Choose an appropriate STP version for a given campus LAN design based on vendor capabilities and network requirements.
*   **Objective 2.2.9:** Configure MSTP instances and regions to align with VLAN topology and load balancing goals.
*   **Objective 2.2.10:** Implement STP tuning features to optimize convergence and protect against common Layer 2 issues.

**Level 4: Analyze**
*   **Objective 2.2.11:** Analyze the convergence behavior of different STP versions in response to various network failures (e.g., link failure, root bridge failure).
*   **Objective 2.2.12:** Compare and contrast the scalability, complexity, and fault tolerance of MSTP versus a large RPVST+ deployment.
*   **Objective 2.2.13:** Differentiate the loop prevention mechanisms used in traditional STP environments versus modern data center fabrics (e.g., VXLAN BGP EVPN).

**Level 5: Evaluate**
*   **Objective 2.2.14:** Evaluate a proposed STP design for a large campus network, assessing its root bridge placement, instance design (for MSTP), and use of protection features.
*   **Objective 2.2.15:** Justify the selection of a specific Layer 2 multipathing technology (e.g., switch stacking, MLAG, or a fabric technology) over traditional STP for a data center access layer.

**Level 6: Create**
*   **Objective 2.2.16:** Design a highly resilient and scalable Layer 2 STP architecture for a multi-building campus network, specifying STP versions, root bridge strategy, and protective features.
*   **Objective 2.2.17:** Develop a migration plan from a legacy PVST+ environment to MSTP to improve scalability and reduce BPDU overhead.

---

### CCDE Core Technology Topic: 2.3 Loop detection and mitigation (distinct from STP, e.g., for non-STP environments or as a backup)

**Overall Goal for this Topic:** The candidate should be able to design and evaluate mechanisms for detecting and mitigating Layer 2 loops in environments where STP might not be fully effective or as a secondary protection layer.

#### Learning Objectives by Bloom\'s Taxonomy Level:

**Level 1: Remember**
*   **Objective 2.3.1:** Identify mechanisms for loop detection beyond STP (e.g., keepalives, proprietary loop detection protocols).

**Level 2: Understand**
*   **Objective 2.3.2:** Explain how misconfigurations (e.g., accidental bridging, unmanaged switches) can lead to Layer 2 loops even with STP present.
*   **Objective 2.3.3:** Describe the symptoms of a Layer 2 loop (e.g., broadcast storm, MAC address flapping, high CPU on switches).

**Level 3: Apply**
*   **Objective 2.3.4:** Choose appropriate loop detection or mitigation features (e.g., storm control, MAC move limits) to minimize the impact of potential loops.

**Level 4: Analyze**
*   **Objective 2.3.5:** Analyze the effectiveness of different loop mitigation techniques in various network scenarios.
*   **Objective 2.3.6:** Differentiate between proactive loop prevention (like STP) and reactive loop detection/mitigation.

**Level 5: Evaluate**
*   **Objective 2.3.7:** Evaluate the design of a Layer 2 network for its robustness against accidental loops, considering both STP and non-STP mitigation techniques.

**Level 6: Create**
*   **Objective 2.3.8:** Design a layered defense strategy against Layer 2 loops for a critical network segment, incorporating STP best practices and supplementary loop detection/mitigation features.

---

### CCDE Core Technology Topic: 2.4 Multicast switching

**Overall Goal for this Topic:** The candidate should be able to design and analyze Layer 2 multicast switching solutions to efficiently deliver multicast traffic within a switched domain, considering IGMP/MLD snooping and querier functions.

#### Learning Objectives by Bloom\'s Taxonomy Level:

**Level 1: Remember**
*   **Objective 2.4.1:** Define IGMP (Internet Group Management Protocol) and MLD (Multicast Listener Discovery).
*   **Objective 2.4.2:** List common IGMP versions (v1, v2, v3) and MLD versions (v1, v2).
*   **Objective 2.4.3:** Identify the purpose of IGMP/MLD snooping and IGMP/MLD querier.

**Level 2: Understand**
*   **Objective 2.4.4:** Explain how IGMP/MLD snooping optimizes multicast traffic delivery in a Layer 2 network.
*   **Objective 2.4.5:** Describe the role of an IGMP/MLD querier in a snooping environment.
*   **Objective 2.4.6:** Discuss potential issues with IGMP/MLD snooping if not configured correctly (e.g., multicast flooding, querier election problems).

**Level 3: Apply**
*   **Objective 2.4.7:** Configure IGMP snooping on Layer 2 switches to support a multicast video streaming application.
*   **Objective 2.4.8:** Choose appropriate IGMP/MLD versions based on application requirements and device capabilities.

**Level 4: Analyze**
*   **Objective 2.4.9:** Analyze multicast traffic flow in a Layer 2 network with and without IGMP/MLD snooping enabled.
*   **Objective 2.4.10:** Differentiate the behavior of IGMPv2, IGMPv3, and MLDv2 in terms of source-specific multicast (SSM) support at Layer 2.

**Level 5: Evaluate**
*   **Objective 2.4.11:** Evaluate a proposed Layer 2 multicast design for its efficiency, scalability, and resilience, considering snooping and querier placement.
*   **Objective 2.4.12:** Justify the need for IGMP snooping in a large VLAN with significant multicast traffic.

**Level 6: Create**
*   **Objective 2.4.13:** Design a Layer 2 multicast distribution solution for a campus network supporting IPTV and financial market data feeds, specifying snooping configurations and querier strategy.

---

### CCDE Core Technology Topic: 2.5 Fault isolation and resiliency

**Overall Goal for this Topic:** The candidate should be able to design Layer 2 networks that incorporate robust fault isolation and resiliency mechanisms, considering fate sharing, redundancy, virtualization, and segmentation techniques.

#### Learning Objectives by Bloom\'s Taxonomy Level:

**Level 1: Remember**
*   **Objective 2.5.1:** Define fate sharing in the context of network design.
*   **Objective 2.5.2:** List common Layer 2 redundancy mechanisms (e.g., link aggregation, redundant switches, STP).
*   **Objective 2.5.3:** Identify Layer 2 virtualization technologies (e.g., VLANs, VSS/vPC/stacking).
*   **Objective 2.5.4:** Recall Layer 2 segmentation methods (e.g., VLANs, PVLANs).

**Level 2: Understand**
*   **Objective 2.5.5:** Explain how minimizing fate sharing can improve network resilience.
*   **Objective 2.5.6:** Describe how VLANs and PVLANs contribute to fault isolation and security segmentation at Layer 2.
*   **Objective 2.5.7:** Discuss how switch virtualization/stacking technologies enhance Layer 2 resiliency and simplify management.

**Level 3: Apply**
*   **Objective 2.5.8:** Choose appropriate Layer 2 redundancy techniques for critical access layer switches.
*   **Objective 2.5.9:** Implement VLANs to segment different user groups or traffic types for fault isolation.

**Level 4: Analyze**
*   **Objective 2.5.10:** Analyze a Layer 2 design to identify potential single points of failure and areas of shared fate.
*   **Objective 2.5.11:** Compare the resiliency characteristics of different link aggregation designs (e.g., active/standby vs. active/active LACP).
*   **Objective 2.5.12:** Differentiate the fault isolation capabilities provided by standard VLANs versus Private VLANs (PVLANs).

**Level 5: Evaluate**
*   **Objective 2.5.13:** Evaluate a proposed Layer 2 design for its overall fault tolerance and ability to isolate failures to minimize impact.
*   **Objective 2.5.14:** Justify the use of switch virtualization (e.g., VSS, vPC) in a data center core or aggregation layer based on resiliency and operational benefits.

**Level 6: Create**
*   **Objective 2.5.15:** Design a Layer 2 architecture for a mission-critical application environment that maximizes fault isolation and provides multiple layers of redundancy.
*   **Objective 2.5.16:** Develop a Layer 2 segmentation strategy for a multi-tenant data center environment using VLANs and PVLANs to ensure traffic isolation and security.

---

**Notes & Considerations for Section 2.0 Layer 2 Control Plane:**
*   **Interdependencies:** Layer 2 control plane design is fundamental to network stability. It directly impacts Layer 3 routing, application performance, and overall network resilience. Choices here affect security (e.g., VLAN segmentation) and multicast delivery.
*   **CCDE Exam Focus:** Expect scenarios testing deep understanding of STP (especially MSTP and RPVST+), loop prevention in various contexts, and designing resilient Layer 2 domains. Questions will likely involve analyzing existing L2 designs, troubleshooting L2 issues based on symptoms, and creating robust L2 architectures that scale and converge quickly. Justification of STP choices, root bridge placement, and protection mechanisms is critical.
*   **Modern L2:** While STP is core, be aware of how modern fabric technologies (e.g., VXLAN BGP EVPN, TRILL, SPB - though TRILL/SPB are less prominent now) aim to overcome STP limitations. The focus in CCDE core is still largely on traditional Ethernet L2 with STP.
*   **Fault Domains:** A key design principle is to limit the size and impact of Layer 2 fault domains.

