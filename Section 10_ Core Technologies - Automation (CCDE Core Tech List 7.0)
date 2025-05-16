


---

## Section 10: Core Technologies - Automation (CCDE Core Tech List 7.0)

This section contains assessment items related to the learning objectives defined in `ccde_lo_core_automation.md`.

### Topic 7.1: Automation concepts and benefits

**Learning Objective 7.1.7 (Understand):** Explain the importance of idempotency in automation scripts and tools.

*   **Question 7.1.7.1 (Short Answer - Understand):**
    What does it mean for an automation script or tool to be idempotent? Why is idempotency a desirable characteristic in network automation?

    **Answer Outline:**
    *   **Idempotency Definition:** An operation is idempotent if applying it multiple times has the same effect as applying it once. In network automation, an idempotent script or tool, when run multiple times with the same desired state input, will ensure the system reaches that state without causing errors or unintended changes on subsequent runs if the system is already in the desired state.
    *   **Importance in Network Automation:**
        1.  **Safety and Predictability:** Allows automation to be run repeatedly without adverse effects. If a script fails midway, it can often be rerun safely once the issue is fixed.
        2.  **Configuration Management:** Ensures that the network converges to the desired state. If a device is already correctly configured, an idempotent tool will not try to re-apply the configuration or report an error.
        3.  **Simplifies Automation Logic:** Reduces the need for complex pre-check logic in scripts to determine if an operation needs to be performed.
        4.  **Reliability:** Helps in achieving consistent configurations across multiple devices, even if the automation is interrupted and restarted.

    **Bloom\"s Level:** Understand
    **Rationale:** Requires explaining the concept of idempotency and its importance in the context of network automation.

---

### Topic 7.2: Data models and formats (JSON, YAML, XML, YANG)

**Learning Objective 7.2.6 (Understand):** Discuss the benefits of using standardized data models like YANG for network automation (e.g., interoperability, consistency, validation).

*   **Question 7.2.6.1 (Conceptual Explanation - Understand):**
    Discuss three key benefits of using a standardized data modeling language like YANG in network automation, particularly in multi-vendor environments.

    **Answer Outline:**
    1.  **Interoperability:** YANG provides a common, vendor-neutral way to define the structure and syntax of configuration and operational data. This allows automation tools to interact with devices from different vendors using a consistent data model, rather than relying on vendor-specific CLIs or proprietary APIs. Protocols like NETCONF and RESTCONF leverage YANG for this.
    2.  **Consistency:** Standardized models ensure that configuration data is structured consistently across different devices and platforms. This simplifies the development of automation scripts and tools, as they can expect data in a predictable format.
    3.  **Validation:** YANG models define data types, constraints, and relationships. This allows for automatic validation of configuration data before it is applied to a device, reducing the risk of errors and misconfigurations. Automation tools can validate input against the YANG model.

    **Bloom\"s Level:** Understand
    **Rationale:** Requires discussing the advantages of standardized data models in automation.

---

### Topic 7.3: APIs and protocols (NETCONF, RESTCONF, gRPC, SNMP)

**Learning Objective 7.3.12 (Compare):** Compare the scalability and performance characteristics of NETCONF, RESTCONF, and gRPC for different automation use cases.

*   **Question 7.3.12.1 (Comparative Analysis - Analyze):**
    Compare NETCONF, RESTCONF, and gRPC in terms of their typical performance characteristics and scalability for two different network automation use cases: 
    a) Bulk configuration changes on many devices.
    b) High-frequency streaming of operational state telemetry.

    **Answer Outline:**
    **a) Bulk Configuration Changes:**
    *   **NETCONF:** Well-suited for bulk configuration. It uses XML over SSH, provides robust transaction capabilities (commit, rollback, candidate datastore). Performance can be good for large, structured configuration changes. Its session-oriented nature can be efficient for multiple operations on the same device.
    *   **RESTCONF:** Uses HTTP(S) and typically JSON or XML. While capable, it might be less efficient for very large bulk changes compared to NETCONF due to HTTP overhead per request if not carefully managed (e.g., using PATCH for partial updates). However, its stateless nature can be simpler for some tools.
    *   **gRPC:** Can be very performant due to HTTP/2 and Protocol Buffers, but its primary strength isn\"t traditionally bulk configuration in the same way as NETCONF. However, if services are defined via gRPC for configuration, it can be efficient.
    *   **Scalability:** NETCONF and gRPC can scale well. RESTCONF scalability depends on the HTTP server implementation on the device.

    **b) High-Frequency Streaming Telemetry:**
    *   **NETCONF:** Supports notifications (event subscriptions) which can be used for telemetry, but it may not be as optimized for very high-frequency, low-latency streaming as gRPC.
    *   **RESTCONF:** Not inherently designed for streaming telemetry. Typically uses a request-response model. Server-Sent Events (SSE) could be an option but less common than gRPC for this.
    *   **gRPC:** Excels at high-frequency streaming telemetry. Its use of HTTP/2 allows for bi-directional streaming, and Protocol Buffers provide efficient data serialization. It is the preferred choice for modern model-driven telemetry (MDT).
    *   **Scalability:** gRPC is designed for high-performance, scalable streaming.

    **Bloom\"s Level:** Analyze
    **Rationale:** Requires comparing three different APIs/protocols across two distinct use cases based on performance and scalability.

---

### Topic 7.4: Automation tools and frameworks

**Learning Objective 7.4.10 (Compare):** Compare the capabilities of open-source automation tools (e.g., Ansible, Python libraries) versus vendor-specific controllers or commercial orchestration platforms.

*   **Question 7.4.10.1 (Comparative Analysis - Analyze):**
    Compare open-source network automation tools like Ansible or Python with custom scripts, against vendor-specific controllers (e.g., Cisco DNA Center, Juniper Contrail) or commercial orchestrators (e.g., Cisco NSO) in terms of the following aspects:
    a) Flexibility and Customization
    b) Ease of Use and Learning Curve for common tasks
    c) Multi-vendor Support
    d) End-to-End Service Orchestration capabilities

    **Answer Outline:**
    **a) Flexibility and Customization:**
    *   **Open-source (Ansible/Python):** Highly flexible and customizable. Python allows for virtually any logic. Ansible allows custom module development. Ideal for bespoke requirements.
    *   **Vendor Controllers/Commercial Orchestrators:** Less flexible for deep customization beyond their intended scope. They provide a structured environment and defined service models. Customization is often through their defined extension points or APIs.

    **b) Ease of Use and Learning Curve:**
    *   **Open-source:** Ansible has a relatively moderate learning curve for common tasks due to its declarative nature and large module library. Python requires programming skills, so the learning curve can be steeper for non-programmers.
    *   **Vendor Controllers/Commercial Orchestrators:** Often designed with GUIs and abstracted workflows for common tasks within their domain (e.g., fabric provisioning in DNA Center), which can make them easier to use for those specific tasks. However, understanding their architecture and advanced features can have a steep learning curve.

    **c) Multi-vendor Support:**
    *   **Open-source:** Ansible and Python libraries (like NAPALM, Netmiko) generally have good multi-vendor support, driven by community contributions and the tools\" design.
    *   **Vendor Controllers:** Primarily focused on the vendor\"s own hardware, with limited or more complex multi-vendor support (often via APIs or integration packs).
    *   **Commercial Orchestrators (e.g., NSO):** Specifically designed for multi-vendor service orchestration, often a key strength, using Network Element Drivers (NEDs).

    **d) End-to-End Service Orchestration:**
    *   **Open-source:** Possible to build service orchestration with Ansible/Python, but requires significant development effort to manage state, transactions, and complex workflows across multiple domains/devices.
    *   **Vendor Controllers:** Provide orchestration within their specific domain (e.g., SD-WAN service via vManage).
    *   **Commercial Orchestrators (e.g., NSO):** Excel at end-to-end, multi-domain, multi-vendor service orchestration. They provide features like service modeling, transaction management, and automated rollback.

    **Bloom\"s Level:** Analyze
    **Rationale:** Requires comparing different categories of automation tools across several key characteristics.

---

*(This completes the initial set of assessment items for the Automation section. More can be added to cover all learning objectives comprehensively.)*

