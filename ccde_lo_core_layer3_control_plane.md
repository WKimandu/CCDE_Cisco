## Learning Objectives for Core Technologies (CCDE v3.1)

### Core Technology List Section: 3.0 Layer 3 Control Plane

**Overall Goal for this Section:** The candidate should be able to design, analyze, evaluate, and troubleshoot complex Layer 3 control plane solutions for diverse network environments, leveraging various unicast and multicast routing protocols, convergence mechanisms, addressing schemes, and traffic engineering techniques to meet specific business and technical requirements for scalability, resilience, security, and performance.

---

### CCDE Core Technology Topic: 3.1 Network hierarchy and topologies

**Overall Goal for this Topic:** The candidate should be able to design and justify hierarchical network topologies that promote scalability, modularity, fault isolation, and efficient routing, understanding the purpose of different layers in various network environments and the principles of topology hiding.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.1.1:** List common network topology types (e.g., star, ring, mesh, bus, tree, hierarchical/multi-tier).
*   **Objective 3.1.2:** Identify the typical layers in enterprise network design (e.g., access, distribution/aggregation, core) and data center design (e.g., access/leaf, aggregation/spine).
*   **Objective 3.1.3:** Define network topology hiding.

**Level 2: Understand**
*   **Objective 3.1.4:** Explain the benefits of a hierarchical network design (e.g., scalability, predictability, ease of management, fault isolation).
*   **Objective 3.1.5:** Describe the purpose and function of each layer in a typical three-tier enterprise hierarchical model.
*   **Objective 3.1.6:** Discuss how network topology hiding can improve routing protocol scalability and stability.

**Level 3: Apply**
*   **Objective 3.1.7:** Choose an appropriate network topology for a given scenario (e.g., campus LAN, small data center, WAN branch connectivity).
*   **Objective 3.1.8:** Develop a basic hierarchical design for a campus network, outlining the roles of core, distribution, and access layers.

**Level 4: Analyze**
*   **Objective 3.1.9:** Analyze the traffic flow patterns and failure domain implications of different network topologies (e.g., spine-leaf vs. traditional three-tier DC).
*   **Objective 3.1.10:** Compare the scalability and resilience characteristics of a flat Layer 2 network versus a hierarchical Layer 3 routed network.
*   **Objective 3.1.11:** Differentiate the design considerations for network hierarchy in enterprise campus, WAN, and data center environments.

**Level 5: Evaluate**
*   **Objective 3.1.12:** Evaluate a proposed network topology for its suitability to meet specific business requirements related to growth, resilience, and application performance.
*   **Objective 3.1.13:** Justify the selection of a specific hierarchical model (e.g., two-tier collapsed core vs. three-tier) for an enterprise network based on size, budget, and complexity.

**Level 6: Create**
*   **Objective 3.1.14:** Design a scalable and resilient hierarchical network topology for a large, multi-building university campus, incorporating principles of modularity and fault isolation.
*   **Objective 3.1.15:** Develop a network topology hiding strategy for a large OSPF or IS-IS domain to improve routing stability and reduce convergence times.

---

### CCDE Core Technology Topic: 3.2 Unicast routing protocols (OSPF, EIGRP, ISIS, BGP, and RIP)

**Overall Goal for this Topic:** The candidate should be able to design, analyze, evaluate, and troubleshoot solutions using OSPF, EIGRP, IS-IS, and BGP (and understand RIP for migration/legacy contexts) for various network scenarios, focusing on scalability, convergence, policy enforcement, security, and optimal path selection.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.2.1:** List the key characteristics of OSPF, EIGRP, IS-IS, BGP, and RIP (e.g., link-state vs. distance-vector, interior vs. exterior).
*   **Objective 3.2.2:** Identify common message types or packet types for each protocol (e.g., OSPF LSA types, EIGRP packets, BGP messages).
*   **Objective 3.2.3:** Recall default administrative distances for these routing protocols.
*   **Objective 3.2.4:** Define key terms like neighbor relationship, flooding domain, routing policy, redistribution, aggregation.

**Level 2: Understand**
*   **Objective 3.2.5:** Explain the neighbor discovery and adjacency formation process for OSPF, EIGRP, IS-IS, and BGP.
*   **Objective 3.2.6:** Describe how each protocol builds and maintains its routing table or topology database (e.g., OSPF LSDB, EIGRP topology table, BGP RIB).
*   **Objective 3.2.7:** Discuss the loop prevention mechanisms inherent in each protocol (e.g., split horizon for DV, SPF algorithm for LS, AS_PATH for BGP).
*   **Objective 3.2.8:** Explain the concept of routing policy and how it is applied in BGP (e.g., route maps, prefix lists, AS path filters).
*   **Objective 3.2.9:** Compare the scalability characteristics of different IGPs (OSPF, EIGRP, IS-IS) in various network sizes and topologies.
*   **Objective 3.2.10:** Describe common methods for securing routing protocols (e.g., authentication, TTL security, prefix filtering).
*   **Objective 3.2.11:** Explain the purpose and methods of route redistribution between different routing protocols and the potential issues (e.g., routing loops, suboptimal routing).
*   **Objective 3.2.12:** Discuss the benefits and techniques of route aggregation/summarization in IGPs and BGP.

**Level 3: Apply**
*   **Objective 3.2.13:** Choose an appropriate IGP (OSPF, EIGRP, IS-IS) for a given enterprise network scenario based on requirements for scalability, convergence, and vendor interoperability.
*   **Objective 3.2.14:** Design a basic single-area OSPF or EIGRP network, including addressing and router ID planning.
*   **Objective 3.2.15:** Implement BGP peering (iBGP and eBGP) between autonomous systems.
*   **Objective 3.2.16:** Apply BGP path attributes (e.g., LOCAL_PREF, AS_PATH prepend, MED, weight) to influence BGP path selection.
*   **Objective 3.2.17:** Configure route redistribution between two different routing protocols, implementing mechanisms to prevent loops (e.g., route tagging, administrative distance manipulation).
*   **Objective 3.2.18:** Develop a route aggregation strategy for an IGP or BGP to reduce routing table size.
*   **Objective 3.2.19:** Implement routing protocol authentication to secure neighbor adjacencies.

**Level 4: Analyze**
*   **Objective 3.2.20:** Analyze the impact of different OSPF area types (e.g., stub, NSSA, totally stubby) on LSA flooding and routing table size.
*   **Objective 3.2.21:** Compare and contrast the design considerations for BGP route reflectors versus BGP confederations for iBGP scalability.
*   **Objective 3.2.22:** Differentiate the convergence behavior of OSPF, EIGRP, and IS-IS in response to various network failures.
*   **Objective 3.2.23:** Investigate suboptimal routing scenarios that can occur due to improper redistribution or summarization, and propose solutions.
*   **Objective 3.2.24:** Analyze the security implications of different BGP peering policies and filtering techniques.

**Level 5: Evaluate**
*   **Objective 3.2.25:** Evaluate a proposed multi-area OSPF or multi-level IS-IS design for its scalability, resilience, and adherence to hierarchical design principles.
*   **Objective 3.2.26:** Justify the selection of BGP over an IGP for a specific WAN connectivity scenario (e.g., connecting to multiple ISPs, complex policy requirements).
*   **Objective 3.2.27:** Critique a BGP route policy implementation for its effectiveness in achieving desired traffic engineering goals and preventing unwanted route propagation.
*   **Objective 3.2.28:** Assess the suitability of different IGP tuning parameters (e.g., timers, LSA retransmission intervals) for optimizing convergence in a specific network environment.
*   **Objective 3.2.29:** Recommend a secure routing protocol design for a critical infrastructure network, justifying the choice of protocols and security mechanisms.

**Level 6: Create**
*   **Objective 3.2.30:** Design a highly scalable and resilient BGP architecture for a global enterprise network with multiple data centers and internet peering points, including route reflector placement and policy design.
*   **Objective 3.2.31:** Develop a comprehensive IGP design (OSPF or IS-IS) for a large service provider access and aggregation network, incorporating summarization, filtering, and fast convergence mechanisms.
*   **Objective 3.2.32:** Formulate a detailed route redistribution and filtering plan for a network merger scenario involving multiple disparate routing domains.
*   **Objective 3.2.33:** Design a secure BGP peering strategy for an ISP, including prefix filtering, RPKI validation, and DDoS mitigation considerations.

---

### CCDE Core Technology Topic: 3.3 Fast convergence techniques and mechanisms

**Overall Goal for this Topic:** The candidate should be able to design and evaluate solutions that minimize network downtime by incorporating various fast convergence techniques and mechanisms within Layer 3 routing protocols.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.3.1:** List common fast convergence mechanisms (e.g., BFD, IGP LFA/rLFA/TI-LFA, EIGRP Feasible Successors, BGP PIC Edge/Core, BGP Add-Path).
*   **Objective 3.3.2:** Identify routing protocols that support specific fast convergence features.
*   **Objective 3.3.3:** Recall typical convergence timers for IGPs and BGP.

**Level 2: Understand**
*   **Objective 3.3.4:** Explain how Bidirectional Forwarding Detection (BFD) enables rapid failure detection for routing protocols.
*   **Objective 3.3.5:** Describe the concept of Loop-Free Alternates (LFA) and its variations (rLFA, TI-LFA) in IGPs like OSPF and IS-IS.
*   **Objective 3.3.6:** Explain how EIGRP Feasible Successors provide pre-computed backup paths.
*   **Objective 3.3.7:** Discuss the role of BGP Prefix Independent Convergence (PIC) Edge and Core in speeding up BGP convergence.
*   **Objective 3.3.8:** Explain how BGP Add-Path can improve convergence and path diversity.
*   **Objective 3.3.9:** Describe how IGP timer tuning (e.g., hello/dead intervals, SPF timers) can impact convergence, and the associated risks.

**Level 3: Apply**
*   **Objective 3.3.10:** Choose appropriate fast convergence mechanisms for a given network scenario based on protocol capabilities and design goals.
*   **Objective 3.3.11:** Implement BFD for OSPF or BGP neighbors to reduce failure detection times.
*   **Objective 3.3.12:** Configure IGP LFA or EIGRP Feasible Successor functionality.

**Level 4: Analyze**
*   **Objective 3.3.13:** Analyze the convergence timeline of a network with and without specific fast convergence mechanisms implemented.
*   **Objective 3.3.14:** Compare the effectiveness and complexity of different LFA techniques (LFA, rLFA, TI-LFA).
*   **Objective 3.3.15:** Differentiate the scenarios where BGP PIC Edge is more beneficial than BGP PIC Core, and vice-versa.

**Level 5: Evaluate**
*   **Objective 3.3.16:** Evaluate a proposed network design for its ability to meet stringent convergence requirements (e.g., sub-second failover).
*   **Objective 3.3.17:** Justify the selection of specific fast convergence features (e.g., BFD with aggressive timers vs. LFA) considering the trade-offs between speed, stability, and processing overhead.
*   **Objective 3.3.18:** Assess the impact of aggressive IGP timer tuning on network stability and CPU utilization.

**Level 6: Create**
*   **Objective 3.3.19:** Design a multi-layered fast convergence strategy for a critical service provider network, incorporating BFD, IGP LFA/TI-LFA, and BGP PIC.
*   **Objective 3.3.20:** Develop a testing and validation plan to verify the effectiveness of implemented fast convergence mechanisms.

---

### CCDE Core Technology Topic: 3.4 Factors affecting convergence

**Overall Goal for this Topic:** The candidate should be able to analyze and mitigate factors that can negatively impact Layer 3 network convergence, including recursion, microloops, micro-bursts, and physical failures.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.4.1:** Define routing recursion, microloops, and micro-bursts.
*   **Objective 3.4.2:** List common types of physical failures that affect convergence (e.g., link down, node down, intermittent errors).

**Level 2: Understand**
*   **Objective 3.4.3:** Explain how routing recursion (e.g., BGP next-hop recursion) can impact convergence times.
*   **Objective 3.4.4:** Describe the conditions under which transient microloops can occur during routing protocol reconvergence.
*   **Objective 3.4.5:** Discuss how micro-bursts of traffic can exacerbate congestion and impact control plane processing during convergence events.
*   **Objective 3.4.6:** Explain how the nature of a physical failure (e.g., hard down vs. flapping link) influences convergence behavior.

**Level 3: Apply**
*   **Objective 3.4.7:** Identify potential points of routing recursion in a given network design.
*   **Objective 3.4.8:** Choose IGP design principles (e.g., summarization, area design) that can help mitigate the impact of widespread physical failures.

**Level 4: Analyze**
*   **Objective 3.4.9:** Analyze a BGP design for potential next-hop recursion issues and their impact on convergence.
*   **Objective 3.4.10:** Investigate how different IGP convergence mechanisms (e.g., SPF throttling, LSA pacing) attempt to balance speed with stability in the presence of flapping links.
*   **Objective 3.4.11:** Differentiate the impact of control plane load versus data plane load (micro-bursts) on overall network convergence.

**Level 5: Evaluate**
*   **Objective 3.4.12:** Evaluate a network design for its susceptibility to prolonged convergence due to factors like recursion, potential for microloops, or inadequate handling of physical failures.
*   **Objective 3.4.13:** Justify design choices (e.g., iBGP full mesh vs. route reflectors, IGP summarization strategy) based on their impact on minimizing factors that negatively affect convergence.

**Level 6: Create**
*   **Objective 3.4.14:** Design a BGP architecture that minimizes next-hop recursion issues and optimizes convergence for a large-scale network.
*   **Objective 3.4.15:** Develop operational procedures for handling flapping links or other intermittent physical failures to maintain network stability and acceptable convergence.

---

### CCDE Core Technology Topic: 3.5 Route aggregation

**Overall Goal for this Topic:** The candidate should be able to design and evaluate effective route aggregation (summarization) strategies for IGPs and BGP to improve scalability, stability, and routing policy enforcement, while avoiding suboptimal routing and black holes.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.5.1:** Define route aggregation/summarization.
*   **Objective 3.5.2:** List the benefits of route aggregation (e.g., smaller routing tables, reduced control plane overhead, improved stability, topology hiding).
*   **Objective 3.5.3:** Identify where route aggregation is typically performed (e.g., ABRs in OSPF, ASBRs, BGP border routers).

**Level 2: Understand**
*   **Objective 3.5.4:** Explain how route aggregation can improve routing protocol scalability and convergence times.
*   **Objective 3.5.5:** Describe the potential risks of route aggregation, such as suboptimal routing or black-holing traffic if not implemented correctly.
*   **Objective 3.5.6:** Discuss the concept of leaking more specific routes from an aggregate and when it might be necessary.
*   **Objective 3.5.7:** Explain how aggregation interacts with routing policy and filtering.

**Level 3: Apply**
*   **Objective 3.5.8:** Develop an IP addressing plan that facilitates efficient route aggregation.
*   **Objective 3.5.9:** Configure route aggregation in OSPF (area range) or BGP (aggregate-address).
*   **Objective 3.5.10:** Choose appropriate aggregation points in a hierarchical network design.

**Level 4: Analyze**
*   **Objective 3.5.11:** Analyze the impact of different aggregation strategies on routing table size, convergence, and traffic path selection.
*   **Objective 3.5.12:** Compare the mechanisms and implications of route aggregation in OSPF versus BGP.
*   **Objective 3.5.13:** Investigate scenarios where aggressive route aggregation can lead to suboptimal routing and how to mitigate this (e.g., by leaking specific routes, using conditional advertisement).

**Level 5: Evaluate**
*   **Objective 3.5.14:** Evaluate a proposed route aggregation plan for its effectiveness in achieving scalability goals while minimizing risks of suboptimal routing or reachability issues.
*   **Objective 3.5.15:** Justify the decision to aggregate or not aggregate routes at specific points in a network based on technical and business requirements.

**Level 6: Create**
*   **Objective 3.5.16:** Design a comprehensive route aggregation strategy for a multi-area OSPF network that balances routing table size with path optimality.
*   **Objective 3.5.17:** Develop a BGP aggregation policy for an ISP that provides optimal summarization to upstream providers while allowing for specific customer route advertisements.

---

### CCDE Core Technology Topic: 3.6 Fault isolation and resiliency (at Layer 3)

**Overall Goal for this Topic:** The candidate should be able to design Layer 3 networks that maximize fault isolation and resiliency through techniques like minimizing fate sharing, implementing redundancy, and leveraging appropriate routing protocol behaviors.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.6.1:** Define Layer 3 fault isolation and resiliency.
*   **Objective 3.6.2:** List common Layer 3 redundancy techniques (e.g., redundant routers, multiple paths, ECMP, fast reroute mechanisms).

**Level 2: Understand**
*   **Objective 3.6.3:** Explain how Layer 3 routing protocols contribute to resiliency by dynamically rerouting around failures.
*   **Objective 3.6.4:** Describe how hierarchical network design and modularity aid in Layer 3 fault isolation.
*   **Objective 3.6.5:** Discuss the concept of fate sharing at Layer 3 and how to design to minimize it (e.g., diverse paths, geographically separate PoPs).

**Level 3: Apply**
*   **Objective 3.6.6:** Choose appropriate routing protocol features (e.g., ECMP, LFA) to enhance Layer 3 resiliency.
*   **Objective 3.6.7:** Design redundant Layer 3 connectivity for critical network segments or devices.

**Level 4: Analyze**
*   **Objective 3.6.8:** Analyze a Layer 3 design to identify potential single points of failure and areas of shared fate that could impact multiple services.
*   **Objective 3.6.9:** Compare the resiliency characteristics of different IGP designs (e.g., single area vs. multi-area OSPF) in response to various failure scenarios.
*   **Objective 3.6.10:** Differentiate the fault isolation capabilities of different BGP peering strategies (e.g., dual-homing to one ISP vs. multi-homing to multiple ISPs).

**Level 5: Evaluate**
*   **Objective 3.6.11:** Evaluate a proposed Layer 3 routing design for its overall fault tolerance, ability to isolate failures, and speed of recovery.
*   **Objective 3.6.12:** Justify design choices that prioritize fault isolation (e.g., dedicated routers for specific services, separate routing domains) even if they increase complexity or cost.

**Level 6: Create**
*   **Objective 3.6.13:** Design a highly resilient Layer 3 architecture for a financial trading network that minimizes downtime and isolates faults to the smallest possible domain.
*   **Objective 3.6.14:** Develop a Layer 3 disaster recovery strategy for an enterprise network, including diverse pathing, redundant data centers, and routing policy for failover.

---

### CCDE Core Technology Topic: 3.7 Metric-based traffic flow and modification

**Overall Goal for this Topic:** The candidate should be able to design solutions that influence Layer 3 traffic flow by manipulating routing protocol metrics and understand the implications of using third-party next hops.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.7.1:** List common routing protocol metrics (e.g., OSPF cost, EIGRP composite metric components, IS-IS metric, BGP MED/Local Pref).
*   **Objective 3.7.2:** Define third-party next hop (also known as next-hop self in some contexts, or next-hop reachability).

**Level 2: Understand**
*   **Objective 3.7.3:** Explain how different routing protocols calculate their default metrics.
*   **Objective 3.7.4:** Describe how modifying metrics can influence path selection within an IGP or for BGP.
*   **Objective 3.7.5:** Discuss the scenarios where a third-party next hop might be used or encountered (e.g., BGP route reflectors, inter-AS MPLS VPNs Option C).
*   **Objective 3.7.6:** Explain the potential issues with third-party next hops if next-hop reachability is not ensured.

**Level 3: Apply**
*   **Objective 3.7.7:** Modify OSPF interface costs or EIGRP interface delays/bandwidth to influence path selection for specific traffic flows.
*   **Objective 3.7.8:** Use BGP attributes like MED or Local Preference to engineer traffic flow for multi-homed connections.

**Level 4: Analyze**
*   **Objective 3.7.9:** Analyze the impact of metric manipulation on overall network traffic patterns and potential for suboptimal routing or routing loops.
*   **Objective 3.7.10:** Compare the effectiveness and complexity of using IGP metrics versus BGP attributes for traffic engineering.
*   **Objective 3.7.11:** Investigate routing issues caused by incorrect third-party next-hop advertisements or lack of next-hop reachability.

**Level 5: Evaluate**
*   **Objective 3.7.12:** Evaluate a proposed traffic engineering solution that relies on metric manipulation for its stability, predictability, and scalability.
*   **Objective 3.7.13:** Justify the use of specific metric tuning techniques to achieve desired traffic distribution or path preference in a complex network.

**Level 6: Create**
*   **Objective 3.7.14:** Design a traffic engineering policy using IGP metric manipulation to balance load across multiple paths in an enterprise backbone.
*   **Objective 3.7.15:** Develop a BGP policy using MED and Local Preference to manage inbound and outbound traffic flow for a multi-homed AS with diverse peering arrangements.

---

### CCDE Core Technology Topic: 3.8 Generic routing and addressing concepts

**Overall Goal for this Topic:** The candidate should be able to design and evaluate solutions incorporating policy-based routing (PBR), Network Address Translation (NAT), subnetting, and understand RIB-FIB relationships for effective traffic management and addressing.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.8.1:** Define Policy-Based Routing (PBR), Network Address Translation (NAT), and subnetting.
*   **Objective 3.8.2:** List different types of NAT (e.g., Static NAT, Dynamic NAT, PAT/NAPT, Dynamic PAT).
*   **Objective 3.8.3:** Recall the purpose of the Routing Information Base (RIB) and Forwarding Information Base (FIB).

**Level 2: Understand**
*   **Objective 3.8.4:** Explain how PBR overrides normal destination-based routing decisions.
*   **Objective 3.8.5:** Describe common use cases for PBR (e.g., directing traffic to specific WAN links, sending traffic through security devices).
*   **Objective 3.8.6:** Discuss the benefits and drawbacks of using NAT.
*   **Objective 3.8.7:** Explain the relationship between the RIB (control plane) and the FIB (data plane) and how they are populated.
*   **Objective 3.8.8:** Describe how subnetting is used for efficient IP address allocation and network segmentation.

**Level 3: Apply**
*   **Objective 3.8.9:** Design a PBR policy to route specific application traffic via a preferred path.
*   **Objective 3.8.10:** Choose an appropriate NAT type for a given scenario (e.g., providing internet access for internal users, publishing an internal server).
*   **Objective 3.8.11:** Develop an IP subnetting plan for a small to medium-sized enterprise network.

**Level 4: Analyze**
*   **Objective 3.8.12:** Analyze the impact of PBR on network troubleshooting and complexity.
*   **Objective 3.8.13:** Compare the performance and scalability implications of implementing NAT on different network devices (e.g., routers vs. firewalls).
*   **Objective 3.8.14:** Investigate issues related to NAT traversal for certain applications and protocols (e.g., FTP, SIP, IPsec).
*   **Objective 3.8.15:** Differentiate the information contained in the RIB versus the FIB for a given set of routes and policies.

**Level 5: Evaluate**
*   **Objective 3.8.16:** Evaluate the suitability of using PBR versus dynamic routing protocol manipulation for a specific traffic engineering requirement.
*   **Objective 3.8.17:** Justify a NAT design strategy (e.g., centralized vs. distributed NAT) for a large enterprise with multiple internet egress points.
*   **Objective 3.8.18:** Assess an IP addressing and subnetting scheme for its efficiency, scalability, and support for route summarization.

**Level 6: Create**
*   **Objective 3.8.19:** Design a comprehensive PBR solution to support differentiated services for various applications across a WAN.
*   **Objective 3.8.20:** Develop a scalable and resilient NAT architecture for an ISP providing services to many customers.
*   **Objective 3.8.21:** Create a hierarchical IP addressing and subnetting plan for a global enterprise that facilitates route aggregation and policy enforcement.

---

### CCDE Core Technology Topic: 3.9 Multicast routing concepts

**Overall Goal for this Topic:** The candidate should be able to design, analyze, and evaluate IP multicast routing solutions using various PIM modes, RP selection strategies, and inter-domain multicast mechanisms to efficiently deliver multicast traffic for applications like video streaming and financial data distribution.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 3.9.1:** Define IP multicast and its benefits.
*   **Objective 3.9.2:** List common PIM (Protocol Independent Multicast) modes (e.g., PIM Dense Mode, PIM Sparse Mode, PIM Sparse-Dense Mode, PIM Source-Specific Multicast - SSM).
*   **Objective 3.9.3:** Identify key multicast concepts like Rendezvous Point (RP), Designated Router (DR) in PIM, IGMP/MLD (as client protocols).
*   **Objective 3.9.4:** Recall inter-domain multicast solutions like MSDP (Multicast Source Discovery Protocol).
*   **Objective 3.9.5:** Define Anycast RP and Prioritycast RP (if applicable to specific vendor implementations or concepts).

**Level 2: Understand**
*   **Objective 3.9.6:** Explain the difference between dense mode and sparse mode PIM operation.
*   **Objective 3.9.7:** Describe the role of the RP in PIM Sparse Mode for source registration and group discovery.
*   **Objective 3.9.8:** Discuss common RP selection mechanisms (e.g., Static RP, Auto-RP, BSR - Bootstrap Router).
*   **Objective 3.9.9:** Explain how PIM-SSM simplifies multicast routing by eliminating the need for RPs for SSM groups.
*   **Objective 3.9.10:** Describe how MSDP enables inter-domain multicast source discovery between different PIM domains.
*   **Objective 3.9.11:** Explain the general concepts of intra-domain versus inter-domain multicast routing.

**Level 3: Apply**
*   **Objective 3.9.12:** Choose an appropriate PIM mode (Sparse, Dense, SSM) for a given multicast application scenario.
*   **Objective 3.9.13:** Design a basic PIM Sparse Mode network with static RP configuration.
*   **Objective 3.9.14:** Implement an RP redundancy solution using Anycast RP with MSDP.

**Level 4: Analyze**
*   **Objective 3.9.15:** Analyze multicast traffic flow and tree building process (shared tree, source tree) in PIM Sparse Mode.
*   **Objective 3.9.16:** Compare the scalability and complexity of different RP discovery and redundancy mechanisms (Auto-RP vs. BSR vs. Static with Anycast MSDP).
*   **Objective 3.9.17:** Differentiate the design considerations for enterprise multicast versus service provider multicast (e.g., IPTV delivery).
*   **Objective 3.9.18:** Investigate common issues in multicast deployments (e.g., RPF failures, RP reachability, snooping problems).

**Level 5: Evaluate**
*   **Objective 3.9.19:** Evaluate a proposed multicast routing design for its efficiency, scalability, resilience, and suitability for specific multicast applications.
*   **Objective 3.9.20:** Justify the selection of PIM-SSM over PIM-SM for a network primarily supporting one-to-many applications with known sources.
*   **Objective 3.9.21:** Assess the security implications of a multicast design and recommend appropriate security measures (e.g., multicast boundary filtering, source authentication).

**Level 6: Create**
*   **Objective 3.9.22:** Design a scalable and resilient PIM Sparse Mode multicast architecture for a large enterprise network supporting video conferencing and IPTV, including RP strategy and inter-VLAN multicast routing.
*   **Objective 3.9.23:** Develop an inter-domain multicast solution using MSDP to connect multiple PIM domains for a global organization.
*   **Objective 3.9.24:** Create a multicast network design for a financial institution distributing real-time market data, focusing on low latency and high availability.

---

**Notes & Considerations for Section 3.0 Layer 3 Control Plane:**
*   **Interdependencies:** This is a cornerstone section. Layer 3 control plane choices heavily influence network scalability, resilience, security, service delivery (VPNs, multicast), and traffic engineering capabilities. It interacts with Layer 2 (for next-hop resolution) and transport technologies.
*   **CCDE Exam Focus:** Expect deep and complex scenarios. Questions will require not just knowing how protocols work, but *why* one design choice is better than another in a given context. Scalability, convergence, policy, and security are always key themes. Be prepared to justify choices related to IGP selection, BGP design (RR, confederations, policies), redistribution, summarization, and fast convergence mechanisms. Multicast design is also a common topic.
*   **Design Principles:** Emphasize hierarchical design, modularity, summarization, and minimizing control plane load.
*   **Trade-offs:** Many design choices involve trade-offs (e.g., convergence speed vs. stability, summarization vs. path optimality). Understanding and articulating these is crucial.

