## Learning Objectives for Network Design (Domain 3.0)

### CCDE Blueprint Topic ID: 3.2
### CCDE Blueprint Topic Name: AI network design use cases (such as machine learning, large language models, and pattern recognition)

**Specific Sub-topics Covered:** 
*   Network Design for Distributed Large Language Model (LLM) Training
*   Network Design for Machine Learning (ML) Clusters (General)
*   Network Design for Pattern Recognition Systems (High-throughput, low-latency inference)

**Overall Goal for this Topic:** The candidate should be able to design, justify, and evaluate robust, scalable, and high-performance network infrastructure to support various AI/ML workloads (including LLM training, general ML, and pattern recognition inference), considering diverse technical, operational, and business constraints.

---

### Learning Objectives by Bloom's Taxonomy Level:

**Level 1: Remember**
*   **Objective 1.1 (LLM Focus):** List the primary network characteristics critical for LLM training (e.g., high bandwidth, low latency, lossless transport, non-blocking fabric).
*   **Objective 1.2 (LLM Focus):** Identify common distributed training parallelism techniques used for LLMs (e.g., data parallelism, model parallelism, pipeline parallelism, tensor parallelism).
*   **Objective 1.3 (General ML):** Recall key network requirements for generic machine learning clusters (e.g., storage connectivity, inter-GPU communication).
*   **Objective 1.4 (Pattern Recognition):** State the typical network demands for high-throughput pattern recognition inference systems (e.g., low-latency response, high concurrent connections).

**Level 2: Understand**
*   **Objective 2.1 (LLM Focus):** Explain how different parallelism techniques (data, model, pipeline, tensor) for LLM training impact network traffic patterns, communication intensity (e.g., all-reduce, all-to-all), and overall network requirements.
*   **Objective 2.2 (LLM Focus):** Describe the role and benefits of RDMA-capable interconnects (e.g., RoCEv2, InfiniBand) in optimizing LLM training network performance and reducing CPU overhead.
*   **Objective 2.3 (General ML):** Discuss the differences in network needs between AI training workloads and AI inference workloads.
*   **Objective 2.4 (Pattern Recognition):** Explain how network design choices can affect the real-time performance and scalability of pattern recognition applications.

**Level 3: Apply**
*   **Objective 3.1 (LLM Focus):** Given a specific LLM model size, dataset characteristics, and GPU cluster size, apply appropriate formulas or heuristics to estimate the required aggregate network bandwidth and per-GPU bandwidth for training.
*   **Objective 3.2 (LLM Focus):** Choose a suitable network topology (e.g., Clos, Fat-Tree, Dragonfly, Torus) for an LLM training cluster based on its scale, budget, and performance requirements.
*   **Objective 3.3 (General ML):** Select appropriate QoS mechanisms to prioritize different types of traffic (e.g., inter-GPU, storage, management) within an AI/ML cluster.
*   **Objective 3.4 (Pattern Recognition):** Develop a basic network diagram for deploying a pattern recognition inference service, considering load balancing and edge deployment scenarios.

**Level 4: Analyze**
*   **Objective 4.1 (LLM Focus):** Analyze the trade-offs (e.g., cost, complexity, performance, scalability) between different interconnect technologies (e.g., high-speed Ethernet with RoCEv2 vs. InfiniBand) for a large-scale LLM training fabric.
*   **Objective 4.2 (General ML):** Differentiate the network design considerations for building an on-premises AI training cluster versus utilizing cloud-based AI training services.
*   **Objective 4.3 (Pattern Recognition):** Investigate the impact of network jitter and packet loss on the accuracy and responsiveness of a real-time pattern recognition system.
*   **Objective 4.4 (LLM/General ML):** Break down the components of end-to-end latency in a distributed AI training job and identify potential network bottlenecks.

**Level 5: Evaluate**
*   **Objective 5.1 (LLM Focus):** Evaluate a proposed network design for an LLM training cluster against criteria such as non-blocking performance, fault tolerance, scalability (up and out), cost-effectiveness, and ease of management/automation.
*   **Objective 5.2 (LLM Focus):** Justify the selection of specific congestion control mechanisms (e.g., ECN, DCQCN) and lossless Ethernet features (e.g., PFC) for an LLM training network to prevent performance degradation.
*   **Objective 5.3 (General ML):** Critique an existing data center network design for its suitability to host a new, demanding AI/ML workload, identifying areas for improvement.
*   **Objective 5.4 (Pattern Recognition):** Assess the security implications of deploying pattern recognition systems at the network edge versus a centralized data center, and recommend appropriate security controls.

**Level 6: Create**
*   **Objective 6.1 (LLM Focus):** Design a high-level network architecture for a multi-rack, multi-tenant LLM training cluster, including topology, interconnect speeds, oversubscription ratios, key protocol choices, and a strategy for traffic isolation.
*   **Objective 6.2 (General ML):** Develop a phased migration strategy for upgrading an existing enterprise data center network to support a significant new AI/ML research initiative, minimizing disruption to existing services.
*   **Objective 6.3 (Pattern Recognition):** Formulate a network design proposal for a city-wide deployment of smart cameras using pattern recognition for traffic management, addressing connectivity, bandwidth, and security challenges.

---

**Notes & Considerations for this Topic (CCDE Blueprint 3.2 - AI Network Design Use Cases):**
*   **Key Technologies:** High-speed Ethernet (100G, 200G, 400G+), InfiniBand, RoCEv2, PFC, ECN, DCQCN, Spine-Leaf/Clos topologies, Fat-Tree, Dragonfly, Torus, SDN for fabric management (e.g., ACI in context of AI), network telemetry for AI workloads, QoS for mixed traffic, security for AI data and models.
*   **Interdependencies:** Strong links to Business Strategy (1.4 - AI/ML business needs), Control/Data/Management Plane (2.0 - especially automation and visibility for AI fabrics), Service Design (4.0 - supporting AI applications, cloud integration for AI), and Security Design (5.0 - securing AI infrastructure and data).
*   **CCDE Exam Focus:** Expect scenarios requiring justification of design choices for specific AI workloads (training vs. inference, LLM vs. other ML). Questions will likely involve analyzing requirements, comparing solutions, evaluating trade-offs (performance, cost, scalability, resilience), and creating high-level designs. Understanding the *why* behind technology choices is critical, not just the *what*.
*   **Emerging Area:** AI networking is rapidly evolving. Candidates should understand current best practices and be able to apply design principles to new or evolving AI application requirements.

