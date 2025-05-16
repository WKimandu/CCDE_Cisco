## Learning Objectives for Network Design (Domain 3.0) & Large-Scale Networks Elective

### CCDE Blueprint Topic Focus: Design of Large-Scale Networks (incorporating elements from Domain 3.0 and the Large-Scale Networks Elective Technology List)

**Specific Sub-topics Covered (examples, not exhaustive):**
*   Large-scale IGP design (OSPF, IS-IS) and BGP for internet and private backbones.
*   MPLS architecture (LDP, RSVP-TE, Segment Routing - SR-MPLS, SRv6).
*   Traffic Engineering (TE) in large networks (RSVP-TE, SR-TE, Flex-Algo).
*   Quality of Service (QoS) strategies in carrier and large enterprise networks.
*   Network virtualization at scale (L2VPN, L3VPN, EVPN).
*   Convergence and resilience in large networks (Fast Reroute, BFD, loop prevention).
*   Security considerations for large-scale infrastructure (control plane, data plane, DDoS mitigation).
*   Automation and orchestration in large network environments.
*   Inter-domain routing and peering strategies.

**Overall Goal for this Topic:** The candidate should be able to design, justify, and evaluate highly resilient, scalable, secure, and manageable network architectures for large-scale environments (e.g., service provider cores, global enterprise backbones), leveraging appropriate routing protocols, virtualization technologies, traffic engineering techniques, and operational best practices to meet complex business and service requirements.

---

### Learning Objectives by Bloom's Taxonomy Level:

**Level 1: Remember**
*   **Objective 1.1:** List common routing protocols used in large-scale networks (e.g., BGP, OSPF, IS-IS, MPLS LDP, RSVP).
*   **Objective 1.2:** Identify key components of MPLS architecture (e.g., LSR, LER, LSP, FEC).
*   **Objective 1.3:** Define Segment Routing (SR) and its core concepts (e.g., SID, SRGB, Adjacency SID, Prefix SID).
*   **Objective 1.4:** Recall common QoS models (e.g., IntServ, DiffServ) and their basic mechanisms (e.g., classification, marking, queuing, shaping).
*   **Objective 1.5:** List different types of VPNs used in large networks (e.g., L3 MPLS VPN, L2 MPLS VPN/VPLS, EVPN).

**Level 2: Understand**
*   **Objective 2.1:** Explain the scalability challenges of IGPs (OSPF, IS-IS) in very large networks and how techniques like area design or multi-level IS-IS address them.
*   **Objective 2.2:** Describe the differences between LDP, RSVP-TE, and Segment Routing for MPLS label distribution and path establishment.
*   **Objective 2.3:** Explain how Traffic Engineering can be used to optimize resource utilization and meet SLAs in large networks.
*   **Objective 2.4:** Discuss the role of BGP in providing inter-domain routing and policy enforcement in service provider networks.
*   **Objective 2.5:** Compare and contrast different EVPN service types (e.g., VLAN-based, VLAN-bundle, Port-based) and their use cases.
*   **Objective 2.6:** Explain the importance of fast convergence in large-scale networks and how mechanisms like BFD or MPLS FRR contribute to it.

**Level 3: Apply**
*   **Objective 3.1:** Given a set of requirements for a large enterprise WAN, choose an appropriate IGP design (e.g., multi-area OSPF, multi-level IS-IS) and BGP peering strategy.
*   **Objective 3.2:** Select suitable MPLS technologies (e.g., LDP for basic transport, RSVP-TE for explicit paths, SR for simplicity and TE) for a service provider core network.
*   **Objective 3.3:** Develop a basic QoS policy for a large network, including classification, marking, and queuing strategies for different traffic types.
*   **Objective 3.4:** Apply BGP path attributes (e.g., LOCAL_PREF, AS_PATH, MED) to influence routing decisions in a multi-homed environment.
*   **Objective 3.5:** Choose appropriate EVPN route types to implement a specific L2 or L3 VPN service over an MPLS or VXLAN underlay.

**Level 4: Analyze**
*   **Objective 4.1:** Analyze the trade-offs (e.g., scalability, complexity, convergence, feature set) between different IGP summarization and filtering techniques in a large, hierarchical network.
*   **Objective 4.2:** Compare the benefits and drawbacks of using RSVP-TE versus Segment Routing with TE (SR-TE, Flex-Algo) for traffic engineering in a service provider network.
*   **Objective 4.3:** Differentiate the control plane and data plane operations of L3 MPLS VPNs versus EVPN L3VPNs.
*   **Objective 4.4:** Investigate the impact of different BGP confederation or route reflector design choices on scalability and policy enforcement in a global network.
*   **Objective 4.5:** Analyze the security vulnerabilities inherent in large-scale routing infrastructures and identify appropriate mitigation techniques (e.g., RPKI, BGP FlowSpec, CoPP).

**Level 5: Evaluate**
*   **Objective 5.1:** Evaluate a proposed BGP design for a global service provider network against criteria such as scalability, stability, policy flexibility, and ease of management.
*   **Objective 5.2:** Justify the selection of a specific MPLS Traffic Engineering approach (e.g., SR-TE with ODN/AS vs. traditional RSVP-TE) for a network requiring guaranteed bandwidth and low latency for critical services.
*   **Objective 5.3:** Critique an existing large-scale network's QoS implementation for its effectiveness in meeting diverse application performance requirements and recommend improvements.
*   **Objective 5.4:** Assess the suitability of an EVPN-VXLAN fabric versus an MPLS-based solution for providing L2/L3 services in a large, distributed enterprise network, considering factors like DCI and multi-tenancy.
*   **Objective 5.5:** Recommend a strategy for DDoS mitigation in a service provider network, evaluating different options like BGP FlowSpec, scrubbing centers, and uRPF.

**Level 6: Create**
*   **Objective 6.1:** Design a highly scalable and resilient multi-area OSPF or multi-level IS-IS architecture for a national service provider network, including summarization, filtering, and BGP redistribution strategies.
*   **Objective 6.2:** Develop a comprehensive MPLS/Segment Routing architecture for a large enterprise backbone, incorporating traffic engineering for critical applications, L3VPN services for different business units, and fast reroute mechanisms.
*   **Objective 6.3:** Formulate a detailed QoS design for a converged service provider network supporting voice, video, mission-critical data, and best-effort internet traffic, specifying PHBs, queuing mechanisms, and bandwidth allocation.
*   **Objective 6.4:** Design a secure and scalable BGP peering architecture for a content delivery network (CDN) to optimize content delivery and manage transit costs.
*   **Objective 6.5:** Devise an automation strategy for provisioning and managing VPN services (L2/L3) across a large-scale MPLS/SR network, including considerations for service assurance and lifecycle management.

---

**Notes & Considerations for this Topic (Large-Scale Networks):**
*   **Key Technologies:** BGP (iBGP, eBGP, RRs, Confederations, Path Attributes, Policies, RPKI), OSPF (Multi-Area, Stub Areas, LSAs), IS-IS (Multi-Level, LSP flooding), MPLS (LDP, RSVP-TE, L3VPN, L2VPN/VPLS, TE FRR), Segment Routing (SR-MPLS, SRv6, TI-LFA, SR-TE, Flex-Algo), EVPN (VXLAN, MPLS data plane, various service types), QoS (DiffServ, PHB, Queuing, Shaping, Policing), Multicast VPN (mVPN), Carrier Ethernet, Optical Transport (DWDM, OTN interaction), BFD, Network Automation tools (Ansible, NSO, Crosswork), DDoS mitigation techniques (FlowSpec, RTBH).
*   **Interdependencies:** Deeply intertwined with all core CCDE domains. Business Strategy (1.0) drives the need for scale and services. Control/Data/Management Plane (2.0) is fundamental. Service Design (4.0) defines what the large network must deliver. Security Design (5.0) is critical at this scale.
*   **CCDE Exam Focus:** Expect complex scenarios involving service provider or very large enterprise environments. Questions will focus on choosing the right technologies and design patterns for scalability, resilience, manageability, and service delivery. Justification of design choices against specific constraints (technical, business, operational) is paramount. Understanding how different technologies interact at scale is crucial.
*   **Scalability Limits:** Be aware of the scalability limits of different protocols and design techniques and how to overcome them.
*   **Migration & Evolution:** Scenarios might involve migrating from older large-scale technologies to newer ones (e.g., classic MPLS to SR, or integrating acquisitions).

