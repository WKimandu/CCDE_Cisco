## Learning Objectives for Core Technologies (CCDE v3.1)

### Core Technology List Section: 7.0 Automation

**Overall Goal for this Section:** The candidate should be able to design, analyze, and evaluate network automation strategies and solutions that leverage appropriate tools, APIs, data models, and programmability concepts to improve operational efficiency, consistency, agility, and scalability in complex network environments, while considering security and manageability.

---

### CCDE Core Technology Topic: 7.1 Automation concepts and benefits

**Overall Goal for this Topic:** The candidate should be able to articulate the core concepts and benefits of network automation and identify suitable use cases for automation in network design, deployment, and operations.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 7.1.1:** Define network automation and programmability.
*   **Objective 7.1.2:** List common benefits of network automation (e.g., reduced manual effort, faster provisioning, improved consistency, fewer errors, enhanced scalability, operational cost savings).
*   **Objective 7.1.3:** Identify typical use cases for network automation (e.g., device provisioning, configuration management, compliance checking, network monitoring, automated troubleshooting, service orchestration).

**Level 2: Understand**
*   **Objective 7.1.4:** Explain the difference between imperative and declarative approaches to automation.
*   **Objective 7.1.5:** Describe the concept of Infrastructure as Code (IaC) as it applies to networking.
*   **Objective 7.1.6:** Discuss the role of automation in enabling NetDevOps practices.
*   **Objective 7.1.7:** Explain the importance of idempotency in automation scripts and tools.

**Level 3: Apply**
*   **Objective 7.1.8:** Choose suitable network tasks or processes that would benefit most from automation in a given scenario.
*   **Objective 7.1.9:** Develop a high-level workflow for automating a common network operational task (e.g., VLAN provisioning).

**Level 4: Analyze**
*   **Objective 7.1.10:** Analyze the potential challenges and risks associated with implementing network automation (e.g., initial investment, skill gap, security concerns, complexity of legacy systems).
*   **Objective 7.1.11:** Compare the benefits of automating greenfield deployments versus brownfield (existing) network environments.

**Level 5: Evaluate**
*   **Objective 7.1.12:** Evaluate the readiness of an organization to adopt network automation based on its current processes, skills, and infrastructure.
*   **Objective 7.1.13:** Justify the business case for investing in network automation for a specific enterprise or service provider.

**Level 6: Create**
*   **Objective 7.1.14:** Design a strategic roadmap for introducing and scaling network automation within an organization, identifying priority areas and key milestones.

---

### CCDE Core Technology Topic: 7.2 Data models and formats (JSON, YAML, XML, YANG)

**Overall Goal for this Topic:** The candidate should be able to understand and utilize common data serialization formats (JSON, YAML, XML) and data modeling languages (YANG) in the context of network automation and programmability.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 7.2.1:** Identify common data serialization formats: JSON (JavaScript Object Notation), YAML (YAML Ain\"t Markup Language), XML (Extensible Markup Language).
*   **Objective 7.2.2:** Define YANG (Yet Another Next Generation) as a data modeling language for network configuration and state.
*   **Objective 7.2.3:** List key characteristics of JSON, YAML, and XML (e.g., human-readable, machine-parsable).

**Level 2: Understand**
*   **Objective 7.2.4:** Explain the basic syntax and structure of JSON, YAML, and XML documents.
*   **Objective 7.2.5:** Describe the purpose of YANG models in defining the structure, syntax, and semantics of network device configuration and operational data.
*   **Objective 7.2.6:** Discuss the benefits of using standardized data models like YANG for network automation (e.g., interoperability, consistency, validation).
*   **Objective 7.2.7:** Explain the difference between configuration data models and state data models in YANG.

**Level 3: Apply**
*   **Objective 7.2.8:** Choose an appropriate data format (JSON, YAML, XML) for representing network configuration data for an automation script.
*   **Objective 7.2.9:** Interpret a simple YANG model to understand the structure of a network device configuration element.

**Level 4: Analyze**
*   **Objective 7.2.10:** Compare the readability, verbosity, and ease of use of JSON, YAML, and XML for network automation tasks.
*   **Objective 7.2.11:** Analyze how YANG models facilitate model-driven programmability and interaction with network devices via protocols like NETCONF and RESTCONF.

**Level 5: Evaluate**
*   **Objective 7.2.12:** Evaluate the suitability of using vendor-specific YANG models versus standard (e.g., IETF, OpenConfig) YANG models for a multi-vendor network environment.

**Level 6: Create**
*   **Objective 7.2.13:** Design a data structure in JSON or YAML to represent a desired network service configuration (e.g., a new VLAN with specific interface assignments) that can be consumed by an automation tool.

---

### CCDE Core Technology Topic: 7.3 APIs and protocols (NETCONF, RESTCONF, gRPC, SNMP)

**Overall Goal for this Topic:** The candidate should be able to design solutions that leverage appropriate APIs and protocols (NETCONF, RESTCONF, gRPC, SNMP) for programmatic interaction with network devices and controllers to enable automation.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 7.3.1:** List common network management and automation protocols/APIs: NETCONF (Network Configuration Protocol), RESTCONF (RESTful Configuration Protocol), gRPC (gRPC Remote Procedure Calls), SNMP (Simple Network Management Protocol).
*   **Objective 7.3.2:** Define API (Application Programming Interface) in the context of network devices.
*   **Objective 7.3.3:** Recall the basic operations supported by NETCONF (e.g., get-config, edit-config, copy-config, delete-config, lock, unlock).

**Level 2: Understand**
*   **Objective 7.3.4:** Explain the key differences between NETCONF and SNMP for network configuration and management.
*   **Objective 7.3.5:** Describe how RESTCONF provides a RESTful HTTP-based interface to data defined in YANG models.
*   **Objective 7.3.6:** Discuss the benefits of gRPC for network telemetry and high-performance RPCs (e.g., streaming, bi-directional communication, efficiency with Protocol Buffers).
*   **Objective 7.3.7:** Explain the role of YANG models in conjunction with NETCONF and RESTCONF.
*   **Objective 7.3.8:** Compare the transport mechanisms used by NETCONF (SSH), RESTCONF (HTTPS), and gRPC (HTTP/2).

**Level 3: Apply**
*   **Objective 7.3.9:** Choose an appropriate API/protocol (NETCONF, RESTCONF, gRPC, SNMP) for a specific automation task (e.g., configuring a device, retrieving operational state, streaming telemetry).
*   **Objective 7.3.10:** Develop a high-level design for using RESTCONF to retrieve and modify configuration on a network device.

**Level 4: Analyze**
*   **Objective 7.3.11:** Analyze the security considerations for using different network APIs (e.g., authentication, authorization, transport encryption).
*   **Objective 7.3.12:** Compare the scalability and performance characteristics of NETCONF, RESTCONF, and gRPC for different automation use cases.
*   **Objective 7.3.13:** Differentiate the capabilities of traditional SNMP (v1, v2c, v3) for monitoring versus modern streaming telemetry approaches using gRPC or NETCONF notifications.

**Level 5: Evaluate**
*   **Objective 7.3.14:** Evaluate a proposed network automation architecture for its choice of APIs and protocols based on factors like vendor support, scalability, security, and ease of integration.
*   **Objective 7.3.15:** Justify the adoption of model-driven telemetry (e.g., using gRPC and YANG models) over traditional SNMP polling for real-time network monitoring.

**Level 6: Create**
*   **Objective 7.3.16:** Design an API integration strategy for a multi-vendor network environment, specifying preferred protocols (NETCONF, RESTCONF, gRPC) for different automation functions (configuration, telemetry, operations).

---

### CCDE Core Technology Topic: 7.4 Automation tools and frameworks (Ansible, Python, NSO, DNA Center, SD-WAN controllers)

**Overall Goal for this Topic:** The candidate should be able to evaluate and select appropriate automation tools, scripting languages, and orchestration frameworks for designing and implementing network automation solutions.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 7.4.1:** List common network automation tools and frameworks (e.g., Ansible, Python with libraries like Netmiko/NAPALM/Nornir, Cisco NSO - Network Services Orchestrator, Cisco DNA Center, SD-WAN controllers like Cisco vManage).
*   **Objective 7.4.2:** Identify the primary purpose of each tool/framework (e.g., configuration management, orchestration, controller-based automation).

**Level 2: Understand**
*   **Objective 7.4.3:** Explain the agentless architecture of Ansible and how it uses modules to interact with network devices.
*   **Objective 7.4.4:** Describe the role of Python as a versatile scripting language for network automation and the purpose of common Python networking libraries.
*   **Objective 7.4.5:** Discuss how network controllers (e.g., DNA Center, SD-WAN controllers) provide centralized automation and abstraction for their respective domains.
*   **Objective 7.4.6:** Explain the concept of service orchestration and how tools like Cisco NSO enable model-driven service provisioning across multi-vendor networks.

**Level 3: Apply**
*   **Objective 7.4.7:** Choose an appropriate automation tool or framework for a given network automation requirement (e.g., using Ansible for configuration drift management, Python for custom scripting, NSO for complex service chaining).
*   **Objective 7.4.8:** Develop a high-level design for using Ansible to automate the deployment of a standard configuration template to multiple network devices.

**Level 4: Analyze**
*   **Objective 7.4.9:** Analyze the scalability and learning curve associated with different automation tools and frameworks.
*   **Objective 7.4.10:** Compare the capabilities of open-source automation tools (e.g., Ansible, Python libraries) versus vendor-specific controllers or commercial orchestration platforms.
*   **Objective 7.4.11:** Differentiate between device-level automation (e.g., scripting individual device configurations) and service-level orchestration (e.g., automating end-to-end service delivery).

**Level 5: Evaluate**
*   **Objective 7.4.12:** Evaluate a proposed automation toolchain for an enterprise network, considering factors like existing skills, integration capabilities, vendor support, and total cost of ownership.
*   **Objective 7.4.13:** Justify the selection of a specific network controller (e.g., DNA Center for campus, vManage for SD-WAN) based on its ability to meet the automation and management needs of that domain.

**Level 6: Create**
*   **Objective 7.4.14:** Design an automation strategy for a large enterprise that integrates multiple tools and platforms (e.g., Ansible for initial provisioning, Python for custom tasks, NSO for service orchestration, DNA Center for campus assurance) into a cohesive automation ecosystem.

---

### CCDE Core Technology Topic: 7.5 Telemetry and analytics

**Overall Goal for this Topic:** The candidate should be able to design solutions that leverage network telemetry and analytics to provide insights into network health, performance, and security, enabling proactive management and closed-loop automation.

#### Learning Objectives by Bloom\"s Taxonomy Level:

**Level 1: Remember**
*   **Objective 7.5.1:** Define network telemetry.
*   **Objective 7.5.2:** List common types of telemetry data (e.g., interface counters, CPU/memory utilization, routing protocol state, flow data - NetFlow/IPFIX, logs).
*   **Objective 7.5.3:** Identify common telemetry collection mechanisms (e.g., SNMP polling, syslog, streaming telemetry - gRPC/NETCONF, NetFlow/IPFIX export).

**Level 2: Understand**
*   **Objective 7.5.4:** Explain the benefits of streaming telemetry over traditional SNMP polling (e.g., higher frequency, richer data, push-based).
*   **Objective 7.5.5:** Describe how telemetry data can be used for network monitoring, capacity planning, troubleshooting, and security incident detection.
*   **Objective 7.5.6:** Discuss the components of a typical telemetry and analytics pipeline (e.g., data collection, transport, storage, processing/analysis, visualization).
*   **Objective 7.5.7:** Explain the concept of closed-loop automation and how telemetry and analytics enable it.

**Level 3: Apply**
*   **Objective 7.5.8:** Choose appropriate telemetry collection methods for different types of network data and monitoring requirements.
*   **Objective 7.5.9:** Develop a basic plan for collecting and analyzing interface utilization data to identify network bottlenecks.

**Level 4: Analyze**
*   **Objective 7.5.10:** Analyze the scalability and storage requirements for different telemetry collection strategies.
*   **Objective 7.5.11:** Compare the insights that can be derived from different types of telemetry data (e.g., SNMP counters vs. flow data vs. model-driven streaming telemetry).

**Level 5: Evaluate**
*   **Objective 7.5.12:** Evaluate a proposed network telemetry and analytics solution for its ability to provide actionable insights and support proactive network management.
*   **Objective 7.5.13:** Justify the adoption of a specific streaming telemetry framework (e.g., gNMI with OpenConfig models) for a modern network environment.

**Level 6: Create**
*   **Objective 7.5.14:** Design a comprehensive network telemetry and analytics architecture for a large enterprise, specifying data sources, collection methods, storage solutions, analysis tools, and use cases for closed-loop automation.

---

**Notes & Considerations for Section 7.0 Automation:**
*   **Interdependencies:** Automation touches every aspect of the network lifecycle and all other technology domains. Secure automation practices are critical. Automation is key to managing complex virtualized networks and SD-WAN solutions. Telemetry from automation feeds into network assurance and operations.
*   **CCDE Exam Focus:** While not a hands-on coding exam, CCDE candidates are expected to understand automation principles from a design perspective. This includes selecting appropriate tools and strategies, understanding how automation impacts network architecture, and designing networks that are amenable to automation. Questions might involve evaluating automation proposals, designing for programmability, or incorporating automation into solutions for scalability and efficiency.
*   **Model-Driven Approach:** Emphasis on model-driven programmability (YANG, NETCONF, RESTCONF) is increasing.
*   **Controllers and Orchestrators:** Understanding the role and capabilities of network controllers (DNA Center, SD-WAN controllers) and orchestrators (NSO) is important.
*   **Not Just Scripting:** Automation is broader than just writing scripts; it involves a strategic approach to processes, tools, and data.

