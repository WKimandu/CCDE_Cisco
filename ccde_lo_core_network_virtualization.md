## Learning Objectives for Core Technologies (CCDE v3.1)

### Core Technology List Section: 4.0 Network Virtualization

**Overall Goal for this Section:** The candidate should be able to design, analyze, and evaluate various network virtualization solutions across different network domains (campus, WAN, data center), leveraging device, path, and network-level virtualization techniques to achieve multi-tenancy, service isolation, resource optimization, and operational flexibility while meeting specific business and technical requirements.

---

### CCDE Core Technology Topic: 4.1 Device virtualization

**Overall Goal for this Topic:** The candidate should be able to design and justify the use of device virtualization technologies to consolidate physical infrastructure, improve resource utilization, and provide logical separation of network functions within a single physical device.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 4.1.1:** List common device virtualization technologies (e.g., virtual routing and forwarding - VRF, virtual device contexts - VDC, switch virtualization/stacking - VSS/vPC/StackWise, virtual firewalls, virtual load balancers).
*   **Objective 4.1.2:** Define multi-tenancy in the context of network devices.

**Level 2: Understand**
*   **Objective 4.1.3:** Explain how device virtualization technologies enable logical separation of control planes and data planes within a physical device.
*   **Objective 4.1.4:** Describe the benefits of device virtualization (e.g., hardware consolidation, operational isolation, simplified management for logical instances).
*   **Objective 4.1.5:** Discuss resource allocation considerations (e.g., CPU, memory, interface assignment) when implementing device virtualization.

**Level 3: Apply**
*   **Objective 4.1.6:** Choose an appropriate device virtualization technology for a given scenario (e.g., creating separate routing instances for different departments on a core router using VRFs).
*   **Objective 4.1.7:** Develop a basic design for implementing VDCs on a data center switch to separate different tenant environments.

**Level 4: Analyze**
*   **Objective 4.1.8:** Analyze the scalability and fault isolation characteristics of different device virtualization solutions.
*   **Objective 4.1.9:** Compare the operational impact of managing multiple virtual devices versus multiple physical devices.
*   **Objective 4.1.10:** Differentiate the use cases for VRF-lite versus full MPLS VRFs in the context of device-level virtualization.

**Level 5: Evaluate**
*   **Objective 4.1.11:** Evaluate a proposed device virtualization design for its ability to meet security, performance, and administrative requirements for a multi-tenant environment.
*   **Objective 4.1.12:** Justify the selection of a specific switch virtualization technology (e.g., stacking vs. chassis-based virtualization like VSS/vPC) based on factors like scale, resilience, and management complexity.

**Level 6: Create**
*   **Objective 4.1.13:** Design a device virtualization strategy for a large enterprise network that utilizes VRFs for departmental separation, VDCs for data center segmentation, and virtualized network services (firewalls, load balancers).

---

### CCDE Core Technology Topic: 4.2 Path virtualization

**Overall Goal for this Topic:** The candidate should be able to design and evaluate path virtualization solutions that create logical overlay paths over a physical underlay network, enabling flexible traffic engineering, service differentiation, and simplified provisioning of end-to-end connectivity.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 4.2.1:** List common path virtualization technologies (e.g., MPLS TE tunnels, GRE tunnels, IPsec tunnels, Segment Routing paths).
*   **Objective 4.2.2:** Define overlay network and underlay network.

**Level 2: Understand**
*   **Objective 4.2.3:** Explain how path virtualization decouples service paths from the physical network topology.
*   **Objective 4.2.4:** Describe the benefits of path virtualization (e.g., traffic engineering, VPN creation, service insertion).
*   **Objective 4.2.5:** Discuss the control plane and data plane mechanisms involved in establishing and maintaining virtual paths (e.g., RSVP-TE signaling for MPLS TE, SR SIDs for Segment Routing).

**Level 3: Apply**
*   **Objective 4.2.6:** Choose an appropriate path virtualization technology for a given requirement (e.g., creating a secure tunnel between two sites using IPsec, engineering traffic over an MPLS core using TE tunnels).
*   **Objective 4.2.7:** Develop a basic design for a GRE tunnel to connect two non-adjacent IP networks.

**Level 4: Analyze**
*   **Objective 4.2.8:** Analyze the scalability and management complexity of different path virtualization solutions (e.g., full mesh of GRE tunnels vs. MPLS L3VPN).
*   **Objective 4.2.9:** Compare the traffic engineering capabilities and granularity of MPLS TE versus Segment Routing TE.
*   **Objective 4.2.10:** Differentiate the fault recovery mechanisms for different path virtualization technologies.

**Level 5: Evaluate**
*   **Objective 4.2.11:** Evaluate a proposed path virtualization design for its ability to meet specific SLA requirements (e.g., bandwidth guarantees, low latency) for critical applications.
*   **Objective 4.2.12:** Justify the selection of Segment Routing over traditional MPLS TE for a new service provider backbone based on operational simplicity and SDN integration benefits.

**Level 6: Create**
*   **Objective 4.2.13:** Design a path virtualization strategy for a service provider network to offer differentiated transport services (e.g., premium low-latency paths, best-effort paths) using MPLS TE or Segment Routing.

---

### CCDE Core Technology Topic: 4.3 Network virtualization (L2, L3)

**Overall Goal for this Topic:** The candidate should be able to design, analyze, and evaluate comprehensive Layer 2 and Layer 3 network virtualization solutions (e.g., L2VPNs, L3VPNs, EVPN) to provide end-to-end virtualized services across various underlay technologies, supporting multi-tenancy, service separation, and flexible connectivity.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 4.3.1:** List common Layer 2 VPN (L2VPN) technologies (e.g., VPLS, EoMPLS/VPWS, EVPN L2) and Layer 3 VPN (L3VPN) technologies (e.g., MPLS L3VPN, DMVPN, GETVPN, EVPN L3).
*   **Objective 4.3.2:** Define key terms like PE (Provider Edge), CE (Customer Edge), VRF (Virtual Routing and Forwarding), RD (Route Distinguisher), RT (Route Target).
*   **Objective 4.3.3:** Recall common overlay encapsulation methods (e.g., MPLS, VXLAN, GRE).

**Level 2: Understand**
*   **Objective 4.3.4:** Explain the fundamental differences between L2VPNs and L3VPNs in terms of service model and routing interaction between PE and CE.
*   **Objective 4.3.5:** Describe the role of RDs and RTs in MPLS L3VPNs for maintaining VPN uniqueness and controlling route propagation.
*   **Objective 4.3.6:** Discuss how EVPN provides a unified control plane for both L2 and L3 VPN services over various data planes (MPLS, VXLAN).
*   **Objective 4.3.7:** Explain the concept of data plane and control plane separation in network virtualization solutions.
*   **Objective 4.3.8:** Compare different DCI (Data Center Interconnect) solutions that leverage network virtualization (e.g., VPLS, EVPN-VXLAN, OTV - though OTV is more legacy).

**Level 3: Apply**
*   **Objective 4.3.9:** Choose an appropriate L2VPN or L3VPN technology for a given enterprise or service provider requirement (e.g., extending a VLAN between two sites using VPLS, providing isolated IP routing for multiple customers using MPLS L3VPN).
*   **Objective 4.3.10:** Develop a basic design for an MPLS L3VPN service, including PE-CE routing protocol selection and VRF configuration.
*   **Objective 4.3.11:** Implement a simple DMVPN network for hub-spoke and spoke-spoke connectivity.

**Level 4: Analyze**
*   **Objective 4.3.12:** Analyze the scalability and control plane complexity of different L3VPN solutions (e.g., MPLS L3VPN vs. large-scale DMVPN).
*   **Objective 4.3.13:** Compare the benefits and drawbacks of using EVPN-VXLAN versus traditional VPLS for data center L2 extension.
*   **Objective 4.3.14:** Differentiate the inter-AS L3VPN options (Option A, B, C) and their implications for scalability and operational complexity.
*   **Objective 4.3.15:** Investigate the security considerations for different network virtualization technologies, including isolation between VPNs and protection of the underlay.

**Level 5: Evaluate**
*   **Objective 4.3.16:** Evaluate a proposed network virtualization design (e.g., EVPN for a multi-tenant DC, MPLS L3VPN for a global enterprise WAN) for its ability to meet technical requirements (scalability, resilience, performance) and business objectives (agility, cost-effectiveness).
*   **Objective 4.3.17:** Justify the selection of EVPN as a unified control plane for delivering both L2 and L3 services in a modern network environment.
*   **Objective 4.3.18:** Assess the suitability of different DCI technologies for interconnecting data centers based on factors like L2/L3 extension needs, distance, and underlying transport.

**Level 6: Create**
*   **Objective 4.3.19:** Design a comprehensive MPLS L3VPN architecture for a service provider to offer IP VPN services to enterprise customers, including PE design, CE connectivity options, and inter-AS connectivity.
*   **Objective 4.3.20:** Develop an EVPN-VXLAN fabric design for a multi-tenant data center, specifying VTEP placement, underlay routing, BGP EVPN control plane, and L2/L3 service delivery.
*   **Objective 4.3.21:** Create a secure and scalable DMVPN solution for an enterprise with hundreds of remote branches requiring dynamic spoke-to-spoke communication.

---

### CCDE Core Technology Topic: 4.4 Data path virtualization

**Overall Goal for this Topic:** The candidate should be able to design and evaluate solutions that leverage data path virtualization technologies (e.g., VXLAN, NVGRE, Geneve) to create logical L2/L3 networks over an IP fabric, enabling network agility, scalability, and decoupling from physical infrastructure constraints.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 4.4.1:** List common data path virtualization/overlay encapsulation technologies (e.g., VXLAN, NVGRE, Geneve, MPLS over GRE/UDP).
*   **Objective 4.4.2:** Define key terms like VTEP (VXLAN Tunnel Endpoint), VNI/VNID (VXLAN Network Identifier), NVE (Network Virtualization Edge).

**Level 2: Understand**
*   **Objective 4.4.3:** Explain how overlay encapsulations like VXLAN allow L2 segments to be extended over an L3 IP network.
*   **Objective 4.4.4:** Describe the format of a VXLAN header and its key fields.
*   **Objective 4.4.5:** Discuss the benefits of data path virtualization in data centers (e.g., overcoming VLAN scale limitations, enabling VM mobility, network automation).
*   **Objective 4.4.6:** Explain the difference between data plane learning (flood and learn) and control plane learning (e.g., BGP EVPN) for MAC address discovery in VXLAN environments.

**Level 3: Apply**
*   **Objective 4.4.7:** Choose an appropriate data path virtualization technology for a given data center or cloud environment.
*   **Objective 4.4.8:** Develop a basic VXLAN design using a flood-and-learn data plane for a small data center pod.

**Level 4: Analyze**
*   **Objective 4.4.9:** Analyze the impact of different underlay network designs (e.g., L3 Clos fabric) on the performance and scalability of VXLAN overlays.
*   **Objective 4.4.10:** Compare the scalability and operational characteristics of VXLAN with flood-and-learn versus VXLAN with a BGP EVPN control plane.
*   **Objective 4.4.11:** Differentiate the capabilities and use cases of VXLAN, NVGRE, and Geneve.

**Level 5: Evaluate**
*   **Objective 4.4.12:** Evaluate a proposed VXLAN fabric design for its suitability to support a large-scale, multi-tenant cloud data center, considering control plane choice, underlay design, and gateway functions.
*   **Objective 4.4.13:** Justify the use of a BGP EVPN control plane for a VXLAN deployment over simpler flood-and-learn or static VTEP configurations.

**Level 6: Create**
*   **Objective 4.4.14:** Design a scalable and resilient VXLAN BGP EVPN fabric for a data center, including underlay routing, VTEP configuration, distributed L2/L3 gateway design, and DCI considerations.

---

### CCDE Core Technology Topic: 4.5 VRF and EVN

**Overall Goal for this Topic:** The candidate should be able to design and evaluate solutions using Virtual Routing and Forwarding (VRF) instances and Easy Virtual Network (EVN) to provide Layer 3 traffic isolation and network segmentation on routers and switches.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 4.5.1:** Define VRF (Virtual Routing and Forwarding) and EVN (Easy Virtual Network).
*   **Objective 4.5.2:** List common use cases for VRFs (e.g., multi-tenancy, separating guest/corporate traffic, MPLS L3VPN PE routers).

**Level 2: Understand**
*   **Objective 4.5.3:** Explain how VRFs provide separate routing tables, forwarding tables, and interfaces within a single router.
*   **Objective 4.5.4:** Describe the concept of VRF-lite (intra-device VRFs without MPLS).
*   **Objective 4.5.5:** Explain how EVN simplifies the configuration and management of VRF-lite by using VNET tags and trunk interfaces.
*   **Objective 4.5.6:** Discuss how routes are leaked or shared between VRFs when inter-VRF communication is required.

**Level 3: Apply**
*   **Objective 4.5.7:** Configure VRF-lite on a router to segment traffic for different user groups.
*   **Objective 4.5.8:** Implement basic route leaking between two VRFs using static routes or BGP.
*   **Objective 4.5.9:** Design a simple EVN solution for a campus network to provide logical network separation.

**Level 4: Analyze**
*   **Objective 4.5.10:** Analyze the scalability limitations of VRF-lite deployments compared to MPLS L3VPNs.
*   **Objective 4.5.11:** Compare the operational complexity of managing multiple VRFs using traditional VRF-lite versus using EVN.
*   **Objective 4.5.12:** Differentiate the methods for providing shared services (e.g., internet access, DNS, DHCP) to multiple VRFs.

**Level 5: Evaluate**
*   **Objective 4.5.13:** Evaluate a proposed VRF design for its effectiveness in achieving traffic isolation, security, and manageability requirements.
*   **Objective 4.5.14:** Justify the use of EVN over traditional VRF-lite for a campus network requiring simplified multi-VRF management.

**Level 6: Create**
*   **Objective 4.5.15:** Design a comprehensive VRF-lite architecture for a large enterprise campus network to provide secure segmentation for various departments and guest access, including strategies for shared services and inter-VRF routing.
*   **Objective 4.5.16:** Develop an EVN deployment plan for an organization looking to simplify its existing VRF-lite implementation.

---

**Notes & Considerations for Section 4.0 Network Virtualization:**
*   **Interdependencies:** Network virtualization technologies are heavily reliant on robust Layer 2 and Layer 3 underlay designs. They are fundamental to modern data center architectures, cloud connectivity, and service provider offerings. Security design is critical for ensuring isolation between virtual networks.
*   **CCDE Exam Focus:** Expect scenarios involving multi-tenancy, data center fabrics, DCI, and complex VPN requirements. Questions will test the ability to choose the right virtualization technology (device, path, L2/L3 network, data path) for the job, and to design scalable, resilient, and manageable solutions. Understanding the control plane and data plane interactions is key. EVPN, VXLAN, and MPLS L3VPNs are particularly important.
*   **Overlay vs. Underlay:** Clearly distinguishing between the overlay (virtualized service) and the underlay (physical transport) is crucial in design and troubleshooting.
*   **Control Planes:** The choice of control plane (e.g., BGP EVPN for VXLAN, MP-BGP for MPLS VPNs) is a major design decision with significant implications.

