# Comprehensive Bloom's Taxonomy Framework for CCDE Certification

**Date:** May 12, 2025

## 1. Introduction

This document outlines a comprehensive framework for applying Bloom's Taxonomy to the Cisco Certified Design Expert (CCDE) certification study materials. The goal is to create a structured, effective, and deep learning experience for CCDE candidates by aligning content, learning objectives, and assessments with varying cognitive skill levels. This framework builds upon the initial review of CCDE v3.1 exam materials and the cognitive level analysis performed for each exam domain.

### 1.1. What is Bloom's Taxonomy?

Bloom's Taxonomy is a hierarchical model that categorizes learning objectives into different levels of complexity and specificity. The revised taxonomy (Anderson & Krathwohl, 2001) includes six levels: Remembering, Understanding, Applying, Analyzing, Evaluating, and Creating. Moving up the hierarchy signifies a deeper level of learning and cognitive engagement.

### 1.2. Relevance to CCDE

The CCDE certification targets expert-level network design engineers. Success in the CCDE exams, particularly the practical exam, requires not just recalling facts but also applying knowledge in complex scenarios, analyzing trade-offs, evaluating design choices, and creating robust network solutions. A Bloom's Taxonomy-aligned approach ensures that study materials actively cultivate these higher-order thinking skills, preparing candidates for the real-world challenges and the exam itself.

## 2. The Six Levels of Bloom's Taxonomy (Revised) for CCDE

Below are the six levels, with descriptions and CCDE-relevant action verbs to guide the development of learning objectives and assessments.

*   **Level 1: Remember**
    *   **Description:** Recalling facts, basic concepts, definitions, and specific information related to CCDE topics and technologies.
    *   **CCDE Action Verbs:** Define, list, identify, name, recall, recognize, state, describe (basic features), label, match.
    *   **CCDE Example:** "List the key components of an SD-WAN architecture."

*   **Level 2: Understand**
    *   **Description:** Explaining ideas or concepts; interpreting information; summarizing; classifying; comparing (basic differences).
    *   **CCDE Action Verbs:** Explain, summarize, describe (in detail), discuss, interpret, classify, compare (pros/cons), differentiate, illustrate, paraphrase, infer.
    *   **CCDE Example:** "Explain the function of the control plane in a software-defined network."

*   **Level 3: Apply**
    *   **Description:** Using information, concepts, theories, and methods in new or concrete situations; implementing, executing, solving problems.
    *   **CCDE Action Verbs:** Apply, choose, demonstrate, implement, use, solve, calculate, modify, prepare, show, relate, develop (a basic plan).
    *   **CCDE Example:** "Given a set of business requirements, apply appropriate QoS mechanisms to prioritize critical application traffic."

*   **Level 4: Analyze**
    *   **Description:** Breaking information into constituent parts to explore relationships and organizational principles; differentiating, organizing, attributing, comparing, contrasting complex systems or solutions.
    *   **CCDE Action Verbs:** Analyze, compare (in-depth), contrast, differentiate, distinguish, examine, organize, break down, categorize, investigate, determine, deconstruct.
    *   **CCDE Example:** "Analyze the trade-offs between using a centralized versus a decentralized control plane for a large enterprise WAN."

*   **Level 5: Evaluate**
    *   **Description:** Making judgments about the value of ideas, materials, or methods based on criteria and standards; checking, critiquing, justifying a decision or course of action.
    *   **CCDE Action Verbs:** Evaluate, justify, recommend, critique, assess, defend, judge, select, support, validate, argue, appraise, prioritize.
    *   **CCDE Example:** "Evaluate a proposed network design for a hybrid cloud environment against stated business continuity and security requirements, and justify your assessment."

*   **Level 6: Create**
    *   **Description:** Putting elements together to form a coherent or functional whole; reorganizing elements into a new pattern or structure; generating, planning, or producing new solutions.
    *   **CCDE Action Verbs:** Design, develop (a comprehensive solution), formulate, construct, produce, assemble, generate, plan, devise, propose, synthesize.
    *   **CCDE Example:** "Design a resilient and scalable network architecture for an AI training cluster, considering specific workload characteristics and business objectives."

## 3. Guidelines for Writing Learning Objectives (LOs)

Learning Objectives should be clear, concise, and measurable, stating what the learner will be able to do upon completing a module or section. Each LO should target a specific Bloom's level.

*   **Start with an Action Verb:** Use verbs from the corresponding Bloom's level (see Section 2).
*   **Specify the Content/Context:** Clearly state the CCDE topic or concept the LO relates to.
*   **Measurable Outcome:** The LO should describe an observable behavior or outcome.
*   **Learner-Centric:** Focus on what the learner will do, not what the instructor will teach.
*   **Alignment:** Ensure LOs align with the CCDE exam blueprint domains and the cognitive demands of an expert designer.
*   **Progression:** For a given topic, aim for a progression of LOs from lower to higher Bloom's levels where appropriate.

**Example LOs for a topic like "BGP Route Reflectors":**
*   **(Remember):** Define the role of a BGP Route Reflector (RR).
*   **(Understand):** Explain the problem that BGP Route Reflectors solve in a full-mesh IBGP environment.
*   **(Apply):** Given a network topology, identify suitable locations for deploying BGP Route Reflectors.
*   **(Analyze):** Compare the scalability implications of using BGP Route Reflectors versus BGP Confederations.
*   **(Evaluate):** Justify the use of a hierarchical Route Reflector design in a large-scale network based on specific design goals.
*   **(Create):** Design a BGP Route Reflector topology for a multi-AS network that meets given resilience and scalability requirements.

## 4. Guidelines for Creating Assessment Items (AIs)

Assessment Items should directly measure the achievement of the Learning Objectives and align with the targeted Bloom's level.

*   **Direct Alignment:** Each AI must map to one or more LOs.
*   **Match Cognitive Level:** The task required by the AI should match the Bloom's level of the LO.
    *   **Remember/Understand:** MCQs, true/false, matching, short answer definitions/explanations.
    *   **Apply:** Scenario-based questions requiring application of a concept, calculations, simple design tasks.
    *   **Analyze:** Comparative essays, scenario analysis requiring identification of components/relationships, troubleshooting scenarios, case studies.
    *   **Evaluate:** Design critiques, justification essays, decision-making scenarios requiring defense of a choice, prioritization tasks.
    *   **Create:** Comprehensive design scenarios, problem-solving tasks requiring novel solutions, proposal development.
*   **CCDE Context:** AIs should reflect the complexity and style of CCDE exam questions, focusing on design principles, trade-offs, and justification, especially for higher Bloom's levels.
*   **Clarity and Unambiguity:** Questions should be clearly worded and avoid ambiguity.
*   **Variety:** Use a variety of AI formats to assess different facets of understanding and skill.

## 5. Content Tagging Strategy

A consistent tagging strategy is crucial for organizing materials, LOs, and AIs, and for allowing learners to navigate based on topics and cognitive depth.

*   **Tags to Include:**
    *   `ccde_domain`: (e.g., `Business_Strategy_Design`, `Network_Design`, `Security_Design`)
    *   `ccde_topic_id`: (e.g., `1.4` for AI/ML in Business Strategy, `3.1.a` for Technical Constraints in Network Design - map to official blueprint numbering)
    *   `ccde_technology`: (e.g., `BGP`, `SD-WAN`, `VXLAN`, `RoCEv2`, `ACI`)
    *   `blooms_level`: (e.g., `Remember`, `Understand`, `Apply`, `Analyze`, `Evaluate`, `Create`)
    *   `content_type`: (e.g., `Learning_Objective`, `Assessment_Item`, `Study_Note`, `Diagram`, `External_Resource`)
    *   `difficulty`: (Optional, e.g., `Foundational`, `Intermediate`, `Advanced_Expert` - could map to Bloom's or be separate)

*   **Implementation:** Tags can be implemented using:
    *   Markdown frontmatter (if using a static site generator).
    *   Comments within documents.
    *   A separate relational database or spreadsheet mapping content items to tags.

## 6. Application of the Framework

This framework will be applied as follows:

1.  **Existing Content Audit:** Review existing knowledge base materials (e.g., `ai-concepts.md`) and map current content to CCDE topics and potential Bloom's levels.
2.  **LO Development:** For each key topic within the CCDE blueprint, develop a set of LOs spanning appropriate Bloom's levels, using the guidelines in Section 3.
3.  **Content Enhancement/Creation:** Enhance existing content or create new content to explicitly support the achievement of these LOs.
4.  **AI Development:** Create a bank of AIs for each LO, following the guidelines in Section 4.
5.  **Tagging:** Apply the tagging strategy (Section 5) to all content, LOs, and AIs.
6.  **Integration:** Structure the knowledge base to allow users to navigate by CCDE domain/topic and to see the associated LOs and AIs at different Bloom's levels.
7.  **Iterative Refinement:** Continuously review and refine LOs, AIs, and content based on user feedback and evolving CCDE exam requirements.

This framework provides a systematic approach to building a robust and pedagogically sound CCDE study resource that fosters deep understanding and expert-level design skills.
