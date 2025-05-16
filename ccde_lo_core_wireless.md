## Learning Objectives for Core Technologies (CCDE v3.1)

### Core Technology List Section: 6.0 Wireless

**Overall Goal for this Section:** The candidate should be able to design, analyze, and evaluate secure, scalable, and high-performing wireless LAN (WLAN) solutions for various enterprise environments, considering RF design principles, controller architectures, client roaming, security mechanisms, QoS, and integration with the wired network.

---

### CCDE Core Technology Topic: 6.1 Wireless LAN (WLAN) design principles

**Overall Goal for this Topic:** The candidate should be able to apply fundamental WLAN design principles related to RF planning, capacity, coverage, and interference mitigation to create effective wireless network solutions.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 6.1.1:** List key RF concepts relevant to WLAN design (e.g., frequency bands - 2.4GHz/5GHz/6GHz, channels, bandwidth, RSSI, SNR, interference, attenuation, reflection, refraction, diffraction).
*   **Objective 6.1.2:** Identify common WLAN standards (e.g., 802.11a/b/g/n/ac/ax - Wi-Fi 4/5/6/6E).
*   **Objective 6.1.3:** Recall different types of wireless antennas (e.g., omnidirectional, directional, patch, Yagi) and their basic characteristics.

**Level 2: Understand**
*   **Objective 6.1.4:** Explain the differences between the 2.4 GHz, 5 GHz, and 6 GHz frequency bands in terms of channel availability, interference potential, and propagation characteristics.
*   **Objective 6.1.5:** Describe the importance of conducting a wireless site survey (predictive, passive, active).
*   **Objective 6.1.6:** Discuss factors that influence WLAN capacity and coverage (e.g., number of users, application types, AP density, building materials, RF interference sources).
*   **Objective 6.1.7:** Explain common sources of RF interference (e.g., microwave ovens, Bluetooth devices, cordless phones, co-channel/adjacent-channel interference) and their impact on WLAN performance.

**Level 3: Apply**
*   **Objective 6.1.8:** Choose appropriate Wi-Fi standards and frequency bands for a given wireless deployment scenario based on client device capabilities and performance requirements.
*   **Objective 6.1.9:** Develop a basic channel plan for a small office WLAN to minimize co-channel and adjacent-channel interference.
*   **Objective 6.1.10:** Select suitable antenna types and orientations for specific coverage requirements (e.g., covering a hallway vs. a large open office).

**Level 4: Analyze**
*   **Objective 6.1.11:** Analyze the results of a wireless site survey to identify areas of poor coverage, high interference, or insufficient capacity.
*   **Objective 6.1.12:** Compare the design considerations for deploying WLANs in different environments (e.g., office, warehouse, healthcare, outdoor).
*   **Objective 6.1.13:** Differentiate the impact of various building materials on RF signal propagation and attenuation.

**Level 5: Evaluate**
*   **Objective 6.1.14:** Evaluate a proposed WLAN RF design for its ability to meet specified coverage, capacity, and performance SLAs.
*   **Objective 6.1.15:** Justify the selection of specific RF parameters (e.g., transmit power levels, channel widths) to optimize WLAN performance and minimize interference in a dense deployment.

**Level 6: Create**
*   **Objective 6.1.16:** Design a comprehensive RF plan for a multi-floor office building, including AP placement, channel assignments, power settings, and antenna selection to provide seamless coverage and capacity for a mix of client devices and applications.

---

### CCDE Core Technology Topic: 6.2 Wireless LAN (WLAN) controller architectures

**Overall Goal for this Topic:** The candidate should be able to design and evaluate different WLAN controller architectures (e.g., autonomous, centralized, cloud-managed, embedded) based on scalability, resilience, feature requirements, and operational considerations.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 6.2.1:** List common WLAN deployment architectures (e.g., autonomous APs, controller-based - centralized/split-MAC, cloud-managed APs, embedded WLC on switches/routers).
*   **Objective 6.2.2:** Define terms like Lightweight Access Point (LAP), Wireless LAN Controller (WLC), CAPWAP/LWAPP.

**Level 2: Understand**
*   **Objective 6.2.3:** Explain the difference between autonomous APs and controller-based APs in terms of management and control plane functions.
*   **Objective 6.2.4:** Describe the split-MAC architecture used in centralized controller-based WLANs.
*   **Objective 6.2.5:** Discuss the benefits and drawbacks of cloud-managed WLAN solutions.
*   **Objective 6.2.6:** Explain how WLC redundancy and high availability (HA) are achieved (e.g., N+1, SSO).

**Level 3: Apply**
*   **Objective 6.2.7:** Choose an appropriate WLAN controller architecture for a given enterprise size and deployment model (e.g., small branch, large campus, distributed retail).
*   **Objective 6.2.8:** Develop a basic design for WLC placement and AP connectivity in a centralized controller architecture.

**Level 4: Analyze**
*   **Objective 6.2.9:** Analyze the scalability limitations of different WLAN controller architectures.
*   **Objective 6.2.10:** Compare the traffic flow patterns (e.g., centralized data forwarding vs. local switching/FlexConnect) in different controller-based WLAN designs.
*   **Objective 6.2.11:** Differentiate the management and operational complexities of on-premises WLCs versus cloud-managed WLANs.

**Level 5: Evaluate**
*   **Objective 6.2.12:** Evaluate a proposed WLAN controller architecture for its ability to meet requirements for scalability, resilience, security, and ease of management.
*   **Objective 6.2.13:** Justify the selection of a specific WLC redundancy model (e.g., N+1 vs. HA pair) based on cost and availability requirements.

**Level 6: Create**
*   **Objective 6.2.14:** Design a scalable and resilient WLAN controller architecture for a global enterprise with multiple regional offices and a central headquarters, incorporating appropriate redundancy and centralized management.

---

### CCDE Core Technology Topic: 6.3 Wireless LAN (WLAN) client roaming

**Overall Goal for this Topic:** The candidate should be able to design WLAN solutions that support seamless and efficient client roaming between access points, considering factors like RF overlap, security, and application requirements (e.g., voice over Wi-Fi).

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 6.3.1:** Define WLAN client roaming.
*   **Objective 6.3.2:** List factors that influence roaming decisions by wireless clients.
*   **Objective 6.3.3:** Recall WLAN standards that facilitate faster roaming (e.g., 802.11k, 802.11r, 802.11v).

**Level 2: Understand**
*   **Objective 6.3.4:** Explain the process of Layer 2 and Layer 3 roaming in a WLAN environment.
*   **Objective 6.3.5:** Describe how RF cell overlap and signal strength influence roaming behavior.
*   **Objective 6.3.6:** Discuss the impact of roaming on real-time applications like voice and video over Wi-Fi.
*   **Objective 6.3.7:** Explain how 802.11k (Neighbor Reports), 802.11r (Fast BSS Transition), and 802.11v (BSS Transition Management) help optimize client roaming.

**Level 3: Apply**
*   **Objective 6.3.8:** Design AP placement to ensure adequate RF overlap for smooth roaming in a specific area.
*   **Objective 6.3.9:** Choose appropriate WLAN security methods (e.g., WPA2/3-Enterprise with 802.1X) that support fast roaming capabilities.

**Level 4: Analyze**
*   **Objective 6.3.10:** Analyze roaming issues in a WLAN deployment based on client behavior and RF measurements.
*   **Objective 6.3.11:** Compare the effectiveness of different fast roaming mechanisms (e.g., OKC, 802.11r) in reducing roaming latency.

**Level 5: Evaluate**
*   **Objective 6.3.12:** Evaluate a WLAN design for its ability to support seamless roaming for voice-over-Wi-Fi clients.
*   **Objective 6.3.13:** Justify the implementation of 802.11k/r/v based on the types of client devices and applications in use.

**Level 6: Create**
*   **Objective 6.3.14:** Design a WLAN infrastructure that optimizes client roaming for a large hospital environment with critical mobile applications, specifying RF design, security settings, and fast roaming features.

---

### CCDE Core Technology Topic: 6.4 Wireless LAN (WLAN) security

**Overall Goal for this Topic:** The candidate should be able to design secure WLAN solutions by implementing robust authentication, encryption, intrusion detection/prevention, and guest access mechanisms.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 6.4.1:** List common WLAN security mechanisms (e.g., WEP - legacy/insecure, WPA, WPA2, WPA3, 802.1X/EAP, PSK, MAC filtering, SSID hiding - weak).
*   **Objective 6.4.2:** Identify common wireless threats (e.g., rogue APs, evil twins, eavesdropping, DoS attacks, deauthentication attacks).
*   **Objective 6.4.3:** Define Wireless Intrusion Prevention System (WIPS) / Wireless Intrusion Detection System (WIDS).

**Level 2: Understand**
*   **Objective 6.4.4:** Explain the vulnerabilities of older WLAN security protocols like WEP and WPA (TKIP).
*   **Objective 6.4.5:** Describe the differences between WPA2-Personal (PSK) and WPA2-Enterprise (802.1X).
*   **Objective 6.4.6:** Discuss the security enhancements introduced in WPA3 (e.g., SAE, enhanced open, 192-bit security suite).
*   **Objective 6.4.7:** Explain how 802.1X/EAP provides strong authentication for wireless clients using a RADIUS server.
*   **Objective 6.4.8:** Describe common methods for providing secure guest wireless access (e.g., captive portal, PSK, sponsored guest).
*   **Objective 6.4.9:** Explain how WIPS/WIDS can detect and mitigate wireless threats.

**Level 3: Apply**
*   **Objective 6.4.10:** Choose appropriate WLAN security protocols and authentication methods for different use cases (e.g., corporate access, guest access, IoT devices).
*   **Objective 6.4.11:** Develop a basic security policy for a corporate WLAN, specifying encryption standards and authentication requirements.
*   **Objective 6.4.12:** Implement rogue AP detection and containment strategies.

**Level 4: Analyze**
*   **Objective 6.4.13:** Analyze the security implications of different EAP types used with 802.1X (e.g., EAP-TLS, PEAP, EAP-FAST).
*   **Objective 6.4.14:** Compare the effectiveness of different guest access solutions in terms of security, usability, and manageability.
*   **Objective 6.4.15:** Differentiate the capabilities of overlay WIPS versus integrated WIPS solutions.

**Level 5: Evaluate**
*   **Objective 6.4.16:** Evaluate a proposed WLAN security design for its ability to protect against common wireless threats and meet compliance requirements.
*   **Objective 6.4.17:** Justify the migration from WPA2 to WPA3 for an enterprise network based on improved security benefits.

**Level 6: Create**
*   **Objective 6.4.18:** Design a comprehensive, multi-layered WLAN security architecture for an enterprise, including strong authentication (802.1X), robust encryption (WPA3), WIPS, secure guest access, and BYOD policies.

---

### CCDE Core Technology Topic: 6.5 Wireless LAN (WLAN) Quality of Service (QoS)

**Overall Goal for this Topic:** The candidate should be able to design WLAN QoS solutions to prioritize critical applications (e.g., voice, video) and ensure a good user experience by leveraging Wi-Fi Multimedia (WMM) and integrating with wired network QoS.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 6.5.1:** Define Wi-Fi Multimedia (WMM) / 802.11e.
*   **Objective 6.5.2:** List the four WMM Access Categories (ACs): Voice (VO), Video (VI), Best Effort (BE), Background (BK).
*   **Objective 6.5.3:** Recall common QoS marking schemes (e.g., DSCP, CoS).

**Level 2: Understand**
*   **Objective 6.5.4:** Explain how WMM prioritizes traffic using EDCA (Enhanced Distributed Channel Access).
*   **Objective 6.5.5:** Describe the importance of mapping wired QoS markings (DSCP/CoS) to WMM Access Categories at the AP/WLC.
*   **Objective 6.5.6:** Discuss how RF conditions (e.g., interference, low SNR) can impact the effectiveness of WLAN QoS.
*   **Objective 6.5.7:** Explain the concept of call admission control (CAC) in voice over Wi-Fi deployments.

**Level 3: Apply**
*   **Objective 6.5.8:** Configure WMM settings on an AP/WLC to prioritize voice and video traffic.
*   **Objective 6.5.9:** Develop a mapping scheme between wired DSCP values and WMM ACs for an enterprise network.

**Level 4: Analyze**
*   **Objective 6.5.10:** Analyze the impact of WLAN QoS policies on application performance, particularly for real-time traffic.
*   **Objective 6.5.11:** Compare different strategies for implementing end-to-end QoS for wireless clients, including wired network integration.

**Level 5: Evaluate**
*   **Objective 6.5.12:** Evaluate a proposed WLAN QoS design for its ability to meet the performance requirements of critical applications like voice and video.
*   **Objective 6.5.13:** Justify the use of specific WMM parameters (e.g., CWmin, CWmax, AIFS, TXOP) to optimize performance for different traffic types.

**Level 6: Create**
*   **Objective 6.5.14:** Design an end-to-end QoS architecture for an enterprise network that seamlessly integrates WLAN QoS (WMM) with wired network QoS policies to support high-quality voice and video services for wireless users.

---

**Notes & Considerations for Section 6.0 Wireless:**
*   **Interdependencies:** WLAN design is heavily dependent on the wired network infrastructure for backhaul, power (PoE), security services (RADIUS, DHCP, DNS), and QoS integration. Controller placement and connectivity are critical.
*   **CCDE Exam Focus:** Expect scenarios involving designing WLANs for various environments (campus, branch, high-density, specialized like healthcare or warehousing). Key aspects include RF planning, controller architecture selection, security (WPA3/802.1X), guest access, roaming for real-time apps, and QoS. Justification of design choices based on requirements (capacity, coverage, security, cost, specific applications) is crucial.
*   **Site Surveys:** Understanding the importance and types of site surveys is fundamental, even if not performing them directly in the exam.
*   **Emerging Trends:** Awareness of newer Wi-Fi standards (Wi-Fi 6/6E, Wi-Fi 7) and their implications for design (e.g., OFDMA, MU-MIMO, 6GHz band).
*   **Integration:** Focus on how the WLAN integrates with the overall network architecture, not just as an isolated island.

