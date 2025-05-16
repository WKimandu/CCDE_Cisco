# Bloom's Taxonomy Audit for AI Concepts Document (ai-concepts.md)

This document outlines the audit findings and recommendations for integrating Bloom's Taxonomy into `/home/ubuntu/CCDE_Cisco/docs/study-materials/ai-concepts.md`.

## Audit Date: May 11 2025

## Overall Goal:

To structure learning objectives, develop assessments, and organize/tag content according to Bloom's Taxonomy to enhance the pedagogical value of the AI Concepts document for CCDE preparation.

## General Observations:

The `ai-concepts.md` document, after recent content enhancements, provides a solid foundation of information. Currently, it primarily supports the lower levels of Bloom's Taxonomy (Remember, Understand). The opportunity lies in explicitly defining objectives for each section and creating activities/questions that push learners towards higher-order thinking skills (Apply, Analyze, Evaluate, Create) relevant to a CCDE candidate.

## Section-by-Section Audit and Recommendations:

### Section 0: Core AI/ML Concepts for Infrastructure Engineers

This entire section is foundational and lends itself well to objectives across multiple Bloom's levels.

**0.1. What are AI, Machine Learning (ML), and Deep Learning (DL)?**
*   **Current State:** Provides definitions and distinctions.
*   **Potential Learning Objectives & Bloom's Level:**
    *   **Remember:** Define Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL).
    *   **Understand:** Explain the hierarchical relationship between AI, ML, and DL. Differentiate between ML and traditional programming.
    *   **Apply:** Given a scenario, classify it as an example of AI, ML, or DL.
*   **Assessment Ideas:** Multiple-choice questions (MCQs) for definitions, short answer questions for explanations, scenario-based classification questions.
*   **Tagging:** `AI_Fundamentals`, `ML_Basics`, `DL_Introduction`, `Bloom_Remember`, `Bloom_Understand`, `Bloom_Apply`.

**0.2. Common Machine Learning Model Types (Overview)**
*   **Current State:** Lists and briefly describes various ML models.
*   **Potential Learning Objectives & Bloom's Level:**
    *   **Remember:** List at least five common types of ML models (e.g., Linear Regression, CNN, RNN, Transformers).
    *   **Understand:** Summarize the primary use case or characteristic for each listed ML model type.
    *   **Analyze:** Compare and contrast the suitability of two different model types (e.g., CNNs vs. RNNs) for a given type of data (e.g., images vs. sequential text).
*   **Assessment Ideas:** Matching model types to descriptions/use cases, MCQs, short answer comparison questions.
*   **Tagging:** `ML_Models`, `CNN`, `RNN`, `Transformers`, `Bloom_Remember`, `Bloom_Understand`, `Bloom_Analyze`.

**0.3. The Machine Learning Lifecycle**
*   **Current State:** Details the stages of the ML lifecycle and their infrastructure implications.
*   **Potential Learning Objectives & Bloom's Level:**
    *   **Remember:** List the key stages of the ML lifecycle.
    *   **Understand:** Explain the purpose of each stage in the ML lifecycle. Describe the primary infrastructure implications for each stage.
    *   **Apply:** Given a description of an activity, identify which stage of the ML lifecycle it belongs to.
    *   **Analyze:** Analyze how a bottleneck in one stage of the ML lifecycle (e.g., data preprocessing) could impact subsequent stages and overall project timelines.
*   **Assessment Ideas:** Sequencing tasks according to the lifecycle, MCQs, scenario-based identification, short essay on impact analysis.
*   **Tagging:** `ML_Lifecycle`, `MLOps`, `Infrastructure_Implications`, `Bloom_Remember`, `Bloom_Understand`, `Bloom_Apply`, `Bloom_Analyze`.

**0.4. AI Workloads: Training vs. Inference**
*   **Current State:** Compares and contrasts training and inference workloads across various characteristics.
*   **Potential Learning Objectives & Bloom's Level:**
    *   **Remember:** Define AI model training and inference.
    *   **Understand:** Explain the key differences between AI training and inference workloads in terms of data, compute, network, and storage requirements.
    *   **Analyze:** For a given AI application scenario, differentiate the network requirements for its training phase versus its inference phase.
    *   **Evaluate:** Justify why different infrastructure design choices might be made for a system primarily focused on AI training versus one focused on AI inference.
*   **Assessment Ideas:** Comparison tables, MCQs, scenario analysis, short essay on design justification.
*   **Tagging:** `AI_Workloads`, `Training`, `Inference`, `Network_Requirements`, `Compute_Requirements`, `Bloom_Remember`, `Bloom_Understand`, `Bloom_Analyze`, `Bloom_Evaluate`.

**0.5. Distributed Training: Data and Model Parallelism**
*   **Current State:** Explains data parallelism, model parallelism, and hybrid approaches.
*   **Potential Learning Objectives & Bloom's Level:**
    *   **Remember:** Define data parallelism and model parallelism.
    *   **Understand:** Explain the core concepts and processes of data parallelism and model parallelism. Describe the primary network implications for each.
    *   **Apply:** Given a scenario (e.g., very large model vs. very large dataset), suggest whether data or model parallelism (or hybrid) would be more appropriate.
    *   **Analyze:** Compare the communication patterns and network demands of data parallelism versus model parallelism.
*   **Assessment Ideas:** MCQs, scenario-based problem solving, diagram interpretation/explanation (if diagrams were added).
*   **Tagging:** `Distributed_Training`, `Data_Parallelism`, `Model_Parallelism`, `Network_Implications`, `Bloom_Remember`, `Bloom_Understand`, `Bloom_Apply`, `Bloom_Analyze`.

**0.6. Network Implications of AI/ML Workloads**
*   **Current State:** Details various network demands like bandwidth, latency, lossless transport, etc.
*   **Potential Learning Objectives & Bloom's Level:**
    *   **Remember:** List key network implications of AI/ML workloads (e.g., high bandwidth, low latency, lossless transport).
    *   **Understand:** Explain why each listed network implication is critical for AI/ML workloads.
    *   **Analyze:** Analyze how specific network characteristics (e.g., high latency, packet loss) would impact a distributed AI training job.
    *   **Evaluate:** Given a set of network design choices for an AI cluster, evaluate their suitability in addressing the key network implications of AI/ML workloads.
*   **Assessment Ideas:** MCQs, short answer explanations, impact analysis questions, design evaluation scenarios.
*   **Tagging:** `Network_Design_AI`, `Bandwidth`, `Latency`, `Lossless_Fabric`, `QoS_AI`, `Bloom_Remember`, `Bloom_Understand`, `Bloom_Analyze`, `Bloom_Evaluate`.

### Section 1: Learning Path Overview
*   **Current State:** Lists stages of learning.
*   **Recommendation:** This section is meta-level. Could be enhanced by phrasing each step as an overarching learning outcome for that phase, potentially mapped to a higher Bloom's level (e.g., "Evaluate different network architectures for AI after completing Infrastructure Design studies").

### Section 2: Key AI Infrastructure Topics to Master
*   **Current State:** Lists key topics with placeholders for brief explanations.
*   **Recommendation:** Once explanations are added (as per previous content enhancement plan), each sub-topic (2.1 to 2.6) should have its own set of learning objectives and assessment ideas, similar to Section 0. For example:
    *   **2.1. Network Fabric Design:**
        *   **Understand:** Explain the importance of lossless fabrics for AI.
        *   **Apply:** Describe how QoS mechanisms can be applied in an AI environment.
        *   **Analyze:** Compare different fabric topologies for AI clusters based on latency considerations.

### Sections 3-9 (Core Study Materials, Supplementary, Advanced, Cisco Live, Study Progression, CCDE Alignment, Additional Resources)
*   **Current State:** These sections primarily list external resources or provide study guidance.
*   **Recommendation for Bloom's Integration:**
    *   **Learning Objectives for Resource Usage:** For sections listing resources (3, 4, 5, 6, 9), objectives could focus on *how* to use these resources effectively (e.g., "Analyze a Cisco Validated Design to extract key network design principles for AI/ML workloads" - Bloom_Analyze).
    *   **Study Progression (Section 7):** Each week's focus could be tied to specific Bloom's level achievements (e.g., "Week 1-2: Remember and Understand core AI/ML concepts and fundamental infrastructure requirements.", "Week 9-10: Evaluate and Synthesize knowledge to prepare for CCDE design scenarios.").
    *   **Tagging Resources:** External resources themselves could be tagged with the primary Bloom's levels they support or the learning objectives they help achieve.

## General Recommendations for Implementation:

1.  **Explicitly State Objectives:** Add a dedicated "Learning Objectives" subsection at the beginning of each major content section (especially Section 0 and Section 2 once populated). Use action verbs aligned with Bloom's Taxonomy.
2.  **Develop Assessment Bank:** Create a separate document or system for assessment questions (MCQs, short answers, scenario-based questions, design challenges) tagged by section and Bloom's level.
3.  **Incorporate Activities:** Where appropriate, suggest small activities or thought experiments within the text to encourage higher-order thinking (e.g., "Consider how you would modify this network design if the primary workload shifted from training to inference. What factors would change?").
4.  **Content Tagging Strategy:** Develop a consistent tagging system that includes topic keywords and Bloom's levels. This can be implemented using comments in Markdown, frontmatter (if a static site generator is used later), or a separate mapping document.
5.  **Iterative Review:** After drafting objectives and assessments, review them to ensure they are clear, measurable, and truly reflect the intended cognitive skill level.

## Next Steps (based on this audit):

*   Begin drafting explicit learning objectives for each subsection of `ai-concepts.md`.
*   Start developing sample assessment questions for these objectives.
*   Consider a tagging schema for content and objectives.
*   Extend this audit process to other key technical documents in the repository.

