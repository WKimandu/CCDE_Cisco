


## Transcript 4: "LlamaParse_super-charging parsing of complex documents.txt" / "A quick walk-through of LlamaParse..."

**Associated CCDE Domains/Topics:** Domain 3 (Network Design for AI/ML - data pipelines), Core Technology List 7.0 (Automation - broader concepts of APIs/tools), Emerging Technologies (AI/LLMs).

### Learning Objectives:

**Remembering (Knowledge):**
*   Define LlamaParse and its primary function as a document parsing API for LLMs.
*   List the types of documents LlamaParse can process (with an emphasis on PDFs).
*   Recall that LlamaParse can output content in Markdown format.
*   Identify that LlamaParse can extract structured elements like tables.

**Understanding (Comprehension):**
*   Explain the purpose of providing "parsing instructions" to LlamaParse.
*   Describe how LlamaParse integrates with the LlamaIndex framework.
*   Summarize the benefit of using LlamaParse for preprocessing complex documents before feeding them to an LLM for RAG.
*   Explain why LLMs might struggle with complex documents without tools like LlamaParse.

**Applying (Application):**
*   Given a scenario involving an LLM needing to answer questions from a complex technical manual (PDF), illustrate how LlamaParse could be used in the data ingestion pipeline.
*   Develop a conceptual set of parsing instructions for LlamaParse to extract key network configuration parameters from a sample network design document.
*   Outline the steps to integrate LlamaParse output into a LlamaIndex vector store.

**Analyzing (Analysis):**
*   Compare the quality of LLM responses to queries on a complex document before and after processing with LlamaParse (based on the transcript example).
*   Analyze how the "parsing instructions" feature of LlamaParse allows for tailored data extraction for specific LLM tasks.
*   Break down the role of LlamaParse in a typical RAG architecture.

**Evaluating (Evaluation):**
*   Assess the potential impact of tools like LlamaParse on the efficiency and accuracy of AI-driven knowledge management systems.
*   Justify the use of specialized parsing tools like LlamaParse when building LLM applications that rely on information from diverse and complex document sources.
*   Critique the limitations of relying solely on an LLM's inherent parsing capabilities for complex PDFs versus using a dedicated parser.

**Creating (Synthesis):**
*   Propose a strategy for using LlamaParse to create a structured knowledge base from a collection of unstructured network incident reports, suitable for LLM-based trend analysis.
*   Design a workflow that incorporates LlamaParse to enable an LLM to answer CCDE-style design questions based on a library of Cisco design guides and whitepapers.

---



## Transcript 5: "Infrastructure as code for NXOS and NDFC with Ansible.txt"

**Associated CCDE Domains/Topics:** Core Technology List 7.0 (Automation), Network Operations and Management (Domain 5), Design for Programmability & Automation, NX-OS Environments (Domain 3 & Electives).

### Learning Objectives:

**Remembering (Knowledge):**
*   Define Infrastructure as Code (IaC) and its core principle of making infrastructure configuration the source of truth.
*   List the key components of an IaC ecosystem (SCM, CI/CD pipelines, execution software).
*   Identify the difference between continuous delivery and continuous deployment in a CI/CD pipeline.
*   Recall the three connection methods Ansible supports for direct NX-OS device interaction (CLI/SSH, NetConf, NX-API).
*   State the purpose of Ansible collections and how they relate to modules.

**Understanding (Comprehension):**
*   Explain the workflow of a CI/CD pipeline for network infrastructure (code commit → staging environment → production).
*   Describe the benefits of using Python virtual environments when working with Ansible.
*   Summarize the difference between `pip install ansible-core` and `pip install ansible`.
*   Explain the concept of Fully Qualified Collection Name (FQCN) and why it's considered best practice.
*   Distinguish between Ansible connecting directly to NX-OS devices versus connecting to NDFC.

**Applying (Application):**
*   Given a VXLAN EVPN fabric scenario, outline how you would organize common and role-specific configurations using Ansible.
*   Illustrate how Ansible roles can be used to structure automation code for different device types in a network.
*   Develop a conceptual plan for implementing a staging environment to test network automation code.
*   Demonstrate how to use Ansible's FQCN syntax to reference a specific NX-OS module.

**Analyzing (Analysis):**
*   Compare the benefits and challenges of using direct-to-device automation (NX-OS) versus controller-based automation (NDFC).
*   Analyze the role of test automation in ensuring the reliability of network infrastructure code.
*   Break down the components of an Ansible playbook for configuring a VXLAN EVPN fabric.
*   Differentiate between the responsibilities of SCM tools, CI/CD pipelines, and execution software in an IaC workflow.

**Evaluating (Evaluation):**
*   Assess the impact of implementing IaC principles on network operations and change management processes.
*   Justify the need for a staging environment when implementing network automation.
*   Critique the statement: "Network engineers don't need to understand version control to implement network automation."
*   Evaluate the trade-offs between the "batteries included" approach (`pip install ansible`) versus the more selective approach (`pip install ansible-core` + specific collections).

**Creating (Synthesis):**
*   Design a comprehensive CI/CD pipeline for automating the deployment of a VXLAN EVPN fabric using Ansible.
*   Propose a strategy for transitioning a traditional CLI-based network operations team to an IaC approach using Ansible.
*   Develop a framework for organizing Ansible roles, playbooks, and variables for a multi-site NX-OS deployment.
*   Create guidelines for implementing test automation for network infrastructure code.

---



## Transcript 6: "Infrastructure as Code for ACI with Ansible and Terraform.txt"

**Associated CCDE Domains/Topics:** Core Technology List 7.0 (Automation), ACI Design (Domain 3 & Electives), Network Operations and Management (Domain 5), Design for Programmability & Automation.

### Learning Objectives:

**Remembering (Knowledge):**
*   Define Infrastructure as Code (IaC) in the context of ACI.
*   List the key components of an IaC ecosystem relevant to ACI automation (SCM, CI/CD, Ansible, Terraform).
*   Recall the primary benefit of Ansible for network engineers automating ACI (data structures over programming).
*   Identify that both Ansible and Terraform can be used for ACI automation.
*   State the importance of Python virtual environments for managing Ansible/Terraform dependencies.

**Understanding (Comprehension):**
*   Explain the ideal IaC workflow involving SCM, CI/CD, and execution tools like Ansible/Terraform for ACI.
*   Describe why IaC is becoming increasingly important for managing ACI environments.
*   Summarize the difference in approach between Ansible (procedural/imperative) and Terraform (declarative) when automating ACI (conceptual, based on general knowledge if not explicit in transcript excerpt).
*   Explain the role of the ACI REST API as the foundation for tools like Ansible and Terraform to interact with the APIC.

**Applying (Application):**
*   Given an ACI configuration task (e.g., deploying a new tenant), outline how this could be approached using IaC principles with Ansible or Terraform.
*   Illustrate how version control (e.g., Git) can be used to manage ACI configurations defined as code.
*   Develop a conceptual plan for setting up an Ansible environment for ACI automation, including virtual environment considerations.

**Analyzing (Analysis):**
*   Compare and contrast the use of Ansible versus Terraform for ACI automation, highlighting potential strengths of each for different scenarios (if inferable or based on general IaC knowledge).
*   Analyze the benefits of using a CI/CD pipeline for deploying ACI configurations defined as code.
*   Break down the key considerations for network engineers when transitioning from CLI-based ACI management to an IaC model.

**Evaluating (Evaluation):**
*   Assess the suitability of an IaC approach for managing a large, multi-site ACI deployment.
*   Justify the investment in learning IaC tools like Ansible and Terraform for ACI network engineers.
*   Critique the potential challenges and pitfalls of adopting IaC for ACI without proper planning and training.

**Creating (Synthesis):**
*   Design a high-level strategy for implementing IaC for an existing ACI fabric, including tool selection (Ansible/Terraform), SCM setup, and a phased rollout plan.
*   Propose a set of best practices for developing and maintaining ACI configurations as code using Ansible or Terraform.
*   Develop a template for an Ansible playbook or Terraform configuration file for a common ACI object (e.g., Bridge Domain, EPG).

---

