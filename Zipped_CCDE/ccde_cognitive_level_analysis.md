# CCDE Cognitive Level Analysis by Subject Area

**Date:** May 12, 2025

This document analyzes the cognitive levels (based on Bloom's Taxonomy) required for each main subject area of the CCDE v3.1 certification, as derived from the `CCDE_v3.1_Unified_Exam_Topics_12132024.pdf` and general understanding of a design expert role.

**Bloom's Taxonomy Levels (for reference):**

*   **Remember:** Recall facts and basic concepts.
*   **Understand:** Explain ideas or concepts.
*   **Apply:** Use information in new situations.
*   **Analyze:** Draw connections among ideas; differentiate, organize, relate, compare, contrast.
*   **Evaluate:** Justify a stand or decision; appraise, argue, defend, judge, select, support, value, critique.
*   **Create:** Produce new or original work; design, assemble, construct, conjecture, develop, formulate, author, investigate.

## Analysis of CCDE v3.1 Unified Exam Topics Domains:

### 1.0 Business Strategy Design (15%)

**Overall Cognitive Expectation:** High. Requires understanding business needs and translating them into network design implications, justifying choices based on business metrics.

*   **1.1 Impact on network design, implementation, and optimization using various customer project management methodologies (for instance Waterfall and Agile)**
    *   **Understand:** Explain Waterfall and Agile methodologies.
    *   **Analyze:** Compare and contrast the impact of Waterfall vs. Agile on network design phases.
    *   **Apply:** Describe how network design deliverables might change based on the project methodology.
    *   **Evaluate:** Justify the choice of a design approach given a specific project management methodology and business context.
*   **1.2 Solutions based on business continuity and operational sustainability (for instance RPO, ROI, CAPEX/OPEX cost analysis, and risk/reward)**
    *   **Understand:** Define RPO, ROI, CAPEX, OPEX, and risk/reward analysis.
    *   **Apply:** Calculate or estimate ROI/TCO for a given network solution.
    *   **Analyze:** Analyze how different design choices impact RPO/RTO and overall business continuity.
    *   **Evaluate:** Justify a network design solution based on its alignment with business continuity goals and cost-effectiveness (CAPEX/OPEX, ROI).
    *   **Create:** Design a network solution that meets specific RPO/RTO targets and business sustainability requirements.
*   **1.3 Environmental sustainability**
    *   **Understand:** Explain how network design can impact environmental sustainability.
    *   **Apply:** Identify design choices that promote environmental sustainability (e.g., power-efficient hardware, virtualization).
    *   **Evaluate:** Assess the environmental impact of different network design options.
*   **1.4 AI/Machine Learning (Business needs, data sovereignty, security, assurance, integrity, impacts, auto scalability, cost/ROI, governance)**
    *   **Understand:** Explain the business implications and requirements of AI/ML workloads (as listed).
    *   **Analyze:** Analyze how AI/ML business needs (e.g., data sovereignty, security) translate into specific network design requirements.
    *   **Apply:** Propose network design considerations to support AI/ML initiatives considering factors like auto-scalability and governance.
    *   **Evaluate:** Justify network design choices for AI/ML based on cost/ROI and business objectives.

### 2.0 Control, Data, Management Plane, and Operational Design (25%)

**Overall Cognitive Expectation:** Very high. Requires deep understanding of network planes, traffic flow, and modern operational paradigms like automation and SDN.

*   **2.1 End-to-end IP traffic flow in a feature-rich environment**
    *   **Understand:** Explain the path of IP traffic through various network features (e.g., QoS, PBR, firewalls).
    *   **Analyze:** Trace and troubleshoot complex IP traffic flows in a multi-feature network.
    *   **Apply:** Design traffic paths to meet specific service requirements.
*   **2.2 Data, control, and management plane technologies**
    *   **Understand:** Define and differentiate the data, control, and management planes. List key technologies for each.
    *   **Analyze:** Compare different control plane technologies (e.g., distributed vs. centralized) for a given scenario.
    *   **Apply:** Select appropriate technologies for each plane based on design requirements.
*   **2.3 Centralized, decentralized, or hybrid control plane**
    *   **Understand:** Explain the characteristics, pros, and cons of centralized, decentralized, and hybrid control planes.
    *   **Analyze:** Compare these models in terms of scalability, resilience, complexity, and agility.
    *   **Evaluate:** Justify the selection of a control plane model for a specific enterprise network design.
    *   **Create:** Design a network architecture based on a chosen control plane model.
*   **2.4 Automation/orchestration design, integration, and on-going support for networks (such as interfacing with APIs, model-driven management, controller-based technologies, and evolution to CI/CD framework)**
    *   **Understand:** Explain key concepts in network automation/orchestration (APIs, model-driven management, CI/CD).
    *   **Apply:** Describe how automation tools and platforms can be integrated into network operations.
    *   **Analyze:** Analyze the requirements for evolving a network towards a CI/CD framework.
    *   **Create:** Design an automation strategy for a given network, including tool selection and integration points.
    *   **Evaluate:** Assess the benefits and challenges of different automation approaches.
*   **2.5 Software-defined architecture and controller-based solution design (SD-WAN, overlay, underlay, and fabric)**
    *   **Understand:** Explain the principles of SDA and controller-based solutions (SD-WAN, fabrics).
    *   **Apply:** Design an underlay and overlay network for an SD-WAN or DC fabric solution.
    *   **Analyze:** Compare different SD-WAN or fabric architectures.
    *   **Evaluate:** Justify the choice of a specific software-defined solution based on requirements.
    *   **Create:** Develop a high-level design for an SD-WAN or fabric deployment.
*   **2.6 Visibility, observability, and assurance**
    *   **Understand:** Define visibility, observability, and assurance in a network context.
    *   **Apply:** Select appropriate tools and techniques to achieve desired levels of network visibility and assurance.
    *   **Analyze:** Analyze the data required for effective network observability.
    *   **Create:** Design a network monitoring and assurance strategy.
*   **2.7 User and application experience**
    *   **Understand:** Explain factors affecting user and application experience.
    *   **Apply:** Design network services (e.g., QoS, traffic shaping) to optimize application experience.
    *   **Analyze:** Correlate network performance metrics with user/application experience.
    *   **Evaluate:** Assess the impact of network design choices on user and application experience.

### 3.0 Network Design (30%)

**Overall Cognitive Expectation:** Highest. This is the core of CCDE, demanding comprehensive design skills across various constraints and technologies.

*   **3.1 Resilient, scalable, and secure modular networks, covering traditional and software-defined architectures, considering: (Technical constraints and requirements, Operational constraints and requirements, Application behavior and needs, Business requirements, Implementation plans, Migration and transformation, Automation goals and requirements)**
    *   **Understand:** Explain principles of resilient, scalable, secure, and modular network design.
    *   **Apply:** Develop network designs that meet a complex set of technical, operational, application, and business requirements.
    *   **Analyze:** Analyze trade-offs between different design choices concerning resilience, scalability, security, cost, and complexity.
    *   **Evaluate:** Justify design decisions against all stated constraints and requirements. Critique existing designs.
    *   **Create:** Produce comprehensive high-level network designs, including migration plans and considerations for automation.
*   **3.2 AI network design use cases (such as machine learning, large language models, and pattern recognition)**
    *   **Understand:** Describe the specific network requirements for different AI use cases (ML, LLM, pattern recognition).
    *   **Apply:** Design network segments or architectures optimized for AI workloads.
    *   **Analyze:** Compare network design approaches for different AI training and inference scenarios.
    *   **Evaluate:** Justify design choices for AI networks based on performance, scalability, and cost.
    *   **Create:** Develop a high-level network design to support a specific AI application or cluster.

### 4.0 Service Design (15%)

**Overall Cognitive Expectation:** High. Focuses on designing the network to support various services and applications, including cloud integration.

*   **4.1 Resilient, scalable, and secure modular network design based on constraints (such as technical, operational, application, and business constraints) to support applications on the IP network (such as voice, video, backups, data center replication, IoT, and storage)**
    *   **Understand:** Explain the network requirements of various applications (voice, video, IoT, etc.).
    *   **Apply:** Design network services (QoS, security policies, path selection) to support specific application requirements.
    *   **Analyze:** Analyze the impact of different applications on network design.
    *   **Evaluate:** Justify network design choices to ensure optimal performance and reliability for critical applications.
    *   **Create:** Design a network capable of supporting a diverse mix of applications with varying requirements.
*   **4.2 Cloud/hybrid solutions based on business-critical operations (Regulatory compliance, Data governance, Service placement, SaaS, PaaS, IaaS, Cloud connectivity, Security, AI/ML)**
    *   **Understand:** Explain different cloud service models (SaaS, PaaS, IaaS) and connectivity options.
    *   **Apply:** Design secure and resilient connectivity to public/private/hybrid cloud environments.
    *   **Analyze:** Analyze the implications of data governance and regulatory compliance on cloud service design and placement.
    *   **Evaluate:** Justify cloud strategy (e.g., hybrid vs. multi-cloud) and connectivity choices based on business and technical requirements, including for AI/ML workloads.
    *   **Create:** Develop a high-level design for a hybrid cloud network architecture, including security and service placement.

### 5.0 Security Design (15%)

**Overall Cognitive Expectation:** Very high. Requires designing security into the network fabric from the ground up, not as an afterthought.

*   **5.1 Network security design and integration (Segmentation, Network access control, Visibility, observability, and assurance, Policy enforcement, CIA triad, Regulatory compliance, Impacts of AI on corporate security policy)**
    *   **Understand:** Explain core security principles (CIA triad, defense-in-depth) and technologies (segmentation, NAC).
    *   **Apply:** Design secure network segments and implement access control policies.
    *   **Analyze:** Analyze security risks in a given network design and propose mitigation strategies. Analyze the impact of AI on security policies.
    *   **Evaluate:** Justify security design choices based on risk assessment, compliance requirements, and business impact. Critique existing security postures.
    *   **Create:** Develop a comprehensive security design for an enterprise network, incorporating multiple layers of defense and addressing regulatory and AI-related security concerns.

**General Conclusion on Cognitive Levels for CCDE:**

The CCDE certification inherently tests higher-order cognitive skills. While **Remember** and **Understand** are foundational for all topics, the exam questions and scenarios will heavily emphasize:

*   **Apply:** Using knowledge in practical design scenarios.
*   **Analyze:** Breaking down complex problems, comparing solutions, identifying interdependencies.
*   **Evaluate:** Making judgments about the value of ideas or solutions, justifying design choices, critiquing designs.
*   **Create:** Generating new designs, strategies, and solutions to meet complex requirements.

This analysis will inform the development of the comprehensive Bloom's Taxonomy framework and subject-specific learning objectives for the CCDE knowledge base.
