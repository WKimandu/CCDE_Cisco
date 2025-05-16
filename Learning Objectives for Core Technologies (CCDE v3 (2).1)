## Learning Objectives for Core Technologies (CCDE v3.1)

### Core Technology List Section: 5.0 Security

**Overall Goal for this Section:** The candidate should be able to design, analyze, and evaluate comprehensive network security solutions across various domains, incorporating principles of defense-in-depth, threat modeling, and risk management. This includes designing secure network infrastructure, implementing access control, protecting against common network attacks, securing network services, and ensuring data confidentiality, integrity, and availability.

---

### CCDE Core Technology Topic: 5.1 Infrastructure security

**Overall Goal for this Topic:** The candidate should be able to design secure network infrastructure by implementing control plane protection, management plane security, and data plane security mechanisms to protect network devices and ensure the integrity of network operations.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 5.1.1:** List common control plane, management plane, and data plane security mechanisms (e.g., CoPP, CPPr, MPF, ACLs, uRPF, routing protocol authentication, secure management access - SSH/HTTPS/SNMPv3).
*   **Objective 5.1.2:** Define terms like Control Plane Policing (CoPP), Control Plane Protection (CPPr), Management Plane Protection (MPP).

**Level 2: Understand**
*   **Objective 5.1.3:** Explain the importance of securing the control plane, management plane, and data plane of network devices.
*   **Objective 5.1.4:** Describe how CoPP/CPPr protect the router CPU from DoS attacks targeting the control plane.
*   **Objective 5.1.5:** Discuss best practices for securing management access to network devices (e.g., strong passwords, AAA, role-based access control, disabling unused services, secure protocols).
*   **Objective 5.1.6:** Explain how Unicast Reverse Path Forwarding (uRPF) helps mitigate spoofing attacks.
*   **Objective 5.1.7:** Describe the purpose and methods of routing protocol authentication (e.g., MD5, SHA for OSPF, EIGRP, BGP).

**Level 3: Apply**
*   **Objective 5.1.8:** Choose appropriate control plane protection mechanisms for a given router or switch based on its role and potential threats.
*   **Objective 5.1.9:** Develop a basic CoPP policy to rate-limit specific types of control plane traffic.
*   **Objective 5.1.10:** Implement secure management access configurations on a network device (e.g., SSH, AAA, SNMPv3).
*   **Objective 5.1.11:** Configure routing protocol authentication between neighbors.

**Level 4: Analyze**
*   **Objective 5.1.12:** Analyze the effectiveness of different CoPP/CPPr policies in mitigating various control plane attacks.
*   **Objective 5.1.13:** Compare the security benefits of different management access methods (e.g., console vs. VTY vs. SNMP).
*   **Objective 5.1.14:** Differentiate the strict mode versus loose mode operation of uRPF and their implications.

**Level 5: Evaluate**
*   **Objective 5.1.15:** Evaluate a proposed infrastructure security design for its completeness in protecting control, management, and data planes.
*   **Objective 5.1.16:** Justify the selection of specific routing protocol authentication mechanisms based on security strength and operational impact.

**Level 6: Create**
*   **Objective 5.1.17:** Design a comprehensive infrastructure security plan for a large enterprise network, specifying control plane, management plane, and data plane protection measures for all critical network devices.

---

### CCDE Core Technology Topic: 5.2 Access control

**Overall Goal for this Topic:** The candidate should be able to design and evaluate robust access control solutions using various techniques like ACLs, firewalls, and identity-based networking to enforce security policies and protect network resources.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 5.2.1:** List different types of Access Control Lists (ACLs) (e.g., standard, extended, named, numbered, reflexive, dynamic, time-based).
*   **Objective 5.2.2:** Define firewall and list common firewall types (e.g., stateless, stateful, next-generation firewall - NGFW, web application firewall - WAF).
*   **Objective 5.2.3:** Recall identity-based networking concepts (e.g., 802.1X, RADIUS, TACACS+, NAC).

**Level 2: Understand**
*   **Objective 5.2.4:** Explain how ACLs are processed and the importance of ACL entry order.
*   **Objective 5.2.5:** Describe the difference between stateless and stateful firewalls.
*   **Objective 5.2.6:** Discuss the additional capabilities of NGFWs compared to traditional firewalls (e.g., application visibility, IPS, threat intelligence integration).
*   **Objective 5.2.7:** Explain the role of 802.1X Port-Based Network Access Control in authenticating users and devices.
*   **Objective 5.2.8:** Describe how Network Admission Control (NAC) solutions can enforce security posture compliance before granting network access.

**Level 3: Apply**
*   **Objective 5.2.9:** Design an ACL to permit or deny specific traffic flows based on source/destination IP, protocol, and port numbers.
*   **Objective 5.2.10:** Choose an appropriate firewall type and placement for a given network security requirement (e.g., perimeter firewall, internal segmentation firewall).
*   **Objective 5.2.11:** Develop a basic 802.1X deployment plan for securing wired or wireless access.

**Level 4: Analyze**
*   **Objective 5.2.12:** Analyze the effectiveness of different ACL designs in terms of security enforcement and manageability.
*   **Objective 5.2.13:** Compare the security benefits and performance impact of different firewall deployment models (e.g., transparent vs. routed mode).
*   **Objective 5.2.14:** Differentiate the roles and capabilities of RADIUS versus TACACS+ for network access control and device administration.

**Level 5: Evaluate**
*   **Objective 5.2.15:** Evaluate a proposed access control strategy for its ability to meet the principle of least privilege and provide defense-in-depth.
*   **Objective 5.2.16:** Justify the selection of a specific NGFW solution based on its features, performance, and integration capabilities for a given enterprise.
*   **Objective 5.2.17:** Assess the complexity and benefits of implementing a comprehensive NAC solution.

**Level 6: Create**
*   **Objective 5.2.18:** Design a multi-layered access control architecture for an enterprise network, incorporating perimeter firewalls, internal segmentation firewalls, ACLs on routers/switches, and an identity-based access solution (802.1X/NAC).

---

### CCDE Core Technology Topic: 5.3 Network attacks and mitigation techniques

**Overall Goal for this Topic:** The candidate should be able to analyze common network attack vectors and design effective mitigation strategies to protect against threats like DoS/DDoS, spoofing, reconnaissance, and man-in-the-middle attacks.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 5.3.1:** List common network attack types (e.g., Denial of Service - DoS, Distributed DoS - DDoS, IP spoofing, MAC spoofing, ARP poisoning, reconnaissance attacks - port scanning/ping sweeps, man-in-the-middle - MitM).
*   **Objective 5.3.2:** Identify common mitigation techniques for these attacks (e.g., ACLs, firewalls, IPS/IDS, uRPF, DAI, DHCP snooping, CoPP, BGP FlowSpec, traffic scrubbing centers).

**Level 2: Understand**
*   **Objective 5.3.3:** Explain the mechanisms behind common DoS/DDoS attack vectors (e.g., SYN flood, UDP flood, ICMP flood, amplification attacks).
*   **Objective 5.3.4:** Describe how IP spoofing can be used to bypass security controls or launch reflection attacks.
*   **Objective 5.3.5:** Discuss how ARP poisoning or MAC spoofing can lead to MitM attacks or session hijacking.
*   **Objective 5.3.6:** Explain the purpose of Dynamic ARP Inspection (DAI) and DHCP Snooping in mitigating ARP-related attacks.

**Level 3: Apply**
*   **Objective 5.3.7:** Choose appropriate mitigation techniques for specific network attack scenarios.
*   **Objective 5.3.8:** Develop a basic configuration for DAI and DHCP snooping on an access layer switch.
*   **Objective 5.3.9:** Implement ACLs or firewall rules to block known malicious IP addresses or attack patterns.

**Level 4: Analyze**
*   **Objective 5.3.10:** Analyze the effectiveness of different DDoS mitigation strategies (e.g., on-premise vs. cloud-based scrubbing).
*   **Objective 5.3.11:** Compare the capabilities of Intrusion Detection Systems (IDS) versus Intrusion Prevention Systems (IPS).
*   **Objective 5.3.12:** Differentiate the methods for detecting and mitigating reconnaissance attacks versus active exploitation attacks.

**Level 5: Evaluate**
*   **Objective 5.3.13:** Evaluate a proposed network security design for its ability to detect, prevent, and respond to common network attacks.
*   **Objective 5.3.14:** Justify the investment in a dedicated DDoS mitigation service for an organization with critical online presence.

**Level 6: Create**
*   **Objective 5.3.15:** Design a layered defense strategy against common network attacks for an enterprise, incorporating perimeter security, internal segmentation, endpoint protection, and threat intelligence.
*   **Objective 5.3.16:** Develop an incident response plan for handling a major DDoS attack, including detection, mitigation, and post-incident analysis steps.

---

### CCDE Core Technology Topic: 5.4 Network services security

**Overall Goal for this Topic:** The candidate should be able to design secure implementations of common network services like DNS, DHCP, NTP, and SNMP to prevent abuse and ensure their integrity and availability.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 5.4.1:** List common network services (e.g., DNS, DHCP, NTP, SNMP, SYSLOG, RADIUS, TACACS+).
*   **Objective 5.4.2:** Identify common security threats to these services (e.g., DNS spoofing/cache poisoning, DHCP starvation/rogue servers, NTP manipulation, SNMP unauthorized access).

**Level 2: Understand**
*   **Objective 5.4.3:** Explain how DNSSEC helps protect against DNS spoofing and cache poisoning.
*   **Objective 5.4.4:** Describe how DHCP snooping and DAI help secure DHCP services.
*   **Objective 5.4.5:** Discuss the importance of secure NTP synchronization and the risks of NTP manipulation.
*   **Objective 5.4.6:** Explain the security benefits of SNMPv3 over SNMPv1/v2c (e.g., authentication, encryption).

**Level 3: Apply**
*   **Objective 5.4.7:** Choose appropriate security mechanisms for protecting DNS, DHCP, NTP, and SNMP services.
*   **Objective 5.4.8:** Develop a basic secure configuration for an NTP client/server.
*   **Objective 5.4.9:** Implement SNMPv3 with authentication and privacy on a network device.

**Level 4: Analyze**
*   **Objective 5.4.10:** Analyze the security implications of different DNS deployment models (e.g., internal vs. external DNS, split DNS).
*   **Objective 5.4.11:** Compare the security features and vulnerabilities of different AAA protocols (RADIUS vs. TACACS+).

**Level 5: Evaluate**
*   **Objective 5.4.12:** Evaluate a proposed design for securing critical network services within an enterprise.
*   **Objective 5.4.13:** Justify the implementation of DNSSEC for an organization with a significant online presence.

**Level 6: Create**
*   **Objective 5.4.14:** Design a secure architecture for providing DNS, DHCP, and NTP services in a large enterprise, including redundancy and protection against common attacks.

---

### CCDE Core Technology Topic: 5.5 Data confidentiality and integrity

**Overall Goal for this Topic:** The candidate should be able to design solutions that ensure data confidentiality and integrity in transit and at rest, using encryption technologies, VPNs, and secure protocols.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 5.5.1:** Define data confidentiality, data integrity, and data availability (CIA triad).
*   **Objective 5.5.2:** List common encryption technologies and protocols (e.g., IPsec, SSL/TLS, MACsec, WPA2/3, AES, SHA).
*   **Objective 5.5.3:** Identify different types of VPNs (e.g., site-to-site IPsec, remote access IPsec/SSL VPN, DMVPN, GETVPN, MACsec for L2 encryption).

**Level 2: Understand**
*   **Objective 5.5.4:** Explain the difference between symmetric and asymmetric encryption.
*   **Objective 5.5.5:** Describe the basic operation of IPsec (e.g., IKE phases, AH, ESP).
*   **Objective 5.5.6:** Discuss how SSL/TLS provides secure communication for web applications.
*   **Objective 5.5.7:** Explain how MACsec provides Layer 2 hop-by-hop encryption.
*   **Objective 5.5.8:** Describe the role of digital certificates and Public Key Infrastructure (PKI) in establishing trust and enabling encryption.

**Level 3: Apply**
*   **Objective 5.5.9:** Choose an appropriate VPN technology for a given scenario (e.g., connecting two branch offices securely over the internet using site-to-site IPsec).
*   **Objective 5.5.10:** Develop a basic IPsec policy for a site-to-site VPN tunnel.
*   **Objective 5.5.11:** Select appropriate encryption algorithms and key lengths based on security requirements and performance considerations.

**Level 4: Analyze**
*   **Objective 5.5.12:** Analyze the security and performance trade-offs of different VPN solutions (e.g., IPsec vs. SSL VPN for remote access).
*   **Objective 5.5.13:** Compare the use cases and benefits of MACsec versus IPsec for data protection.
*   **Objective 5.5.14:** Differentiate the security provided by tunnel mode versus transport mode IPsec.

**Level 5: Evaluate**
*   **Objective 5.5.15:** Evaluate a proposed data encryption strategy for its effectiveness in protecting sensitive information in transit across different network segments.
*   **Objective 5.5.16:** Justify the selection of a specific cryptographic suite (algorithms for encryption, hashing, key exchange) for an IPsec VPN based on current security best practices.

**Level 6: Create**
*   **Objective 5.5.17:** Design a comprehensive VPN architecture for a global enterprise, incorporating site-to-site VPNs, remote access VPNs, and potentially DMVPN or GETVPN for scalable and secure connectivity.
*   **Objective 5.5.18:** Develop a data-in-transit security policy for an organization, specifying required encryption standards for different types of data and communication channels.

---

**Notes & Considerations for Section 5.0 Security:**
*   **Interdependencies:** Security is pervasive and intersects with all other network domains. Infrastructure security (CoPP, MPF) is vital for control/management plane stability. Access control (ACLs, firewalls) is fundamental to segmentation and policy. VPNs are a key part of network virtualization and WAN design. Securing network services (DNS, DHCP) is critical for overall network function.
*   **CCDE Exam Focus:** Expect security to be woven into almost every scenario. Questions will require designing secure solutions, not just isolated security features. This includes secure routing, secure VPNs, infrastructure hardening, access control strategies, and DDoS mitigation. Justifying security choices based on risk, compliance, and business impact is key. Defense-in-depth is a core principle.
*   **Threat Landscape:** A general awareness of common network threats and attack vectors is important for designing effective countermeasures.
*   **Compliance:** Scenarios may involve specific compliance requirements (e.g., PCI DSS, HIPAA) that dictate certain security controls.

