# Bloom's Taxonomy: Objectives & Assessments for AI Concepts

This document provides explicit learning objectives and sample assessment items aligned with Bloom's Taxonomy for the `/home/ubuntu/CCDE_Cisco/docs/study-materials/ai-concepts.md` document. These are based on the audit performed in `blooms_taxonomy_audit_ai_concepts.md`.

## Section 0: Core AI/ML Concepts for Infrastructure Engineers

### 0.1. What are AI, Machine Learning (ML), and Deep Learning (DL)?

**Learning Objectives:**

*   **Remember:** Define Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in your own words.
*   **Understand:** Explain the hierarchical relationship between AI, ML, and DL, highlighting key distinctions.
*   **Understand:** Differentiate Machine Learning from traditional programming approaches.
*   **Apply:** Given a technological scenario, classify it as primarily an example of AI, ML, or DL, and justify your classification.

**Sample Assessment Items:**

1.  **(Remember - MCQ):** Which of the following best describes Machine Learning?
    a)  A system explicitly programmed for every possible contingency.
    b)  A broad field of computer science focused on creating systems with human-like intelligence.
    c)  A subset of AI where systems learn from data to perform tasks without explicit programming for each specific input.
    d)  A type of neural network with many layers.
    *Answer: c*

2.  **(Understand - Short Answer):** Briefly explain how Deep Learning is related to Machine Learning and Artificial Intelligence.

3.  **(Understand - Short Answer):** What is the fundamental difference in how a problem is solved using traditional programming versus Machine Learning?

4.  **(Apply - Scenario):** A company develops a system that analyzes thousands of medical images to identify early signs of a specific disease. The system was trained on a large dataset of labeled images and improves its accuracy as it processes more images. Is this system best described as an example of general AI, Machine Learning, or Deep Learning? Justify your answer.

---

### 0.2. Common Machine Learning Model Types (Overview)

**Learning Objectives:**

*   **Remember:** List at least five common types of Machine Learning models.
*   **Understand:** For each of the five listed ML model types, summarize its primary characteristic or a common use case.
*   **Analyze:** Compare and contrast the suitability of Convolutional Neural Networks (CNNs) versus Recurrent Neural Networks (RNNs) for processing image data versus sequential text data.

**Sample Assessment Items:**

1.  **(Remember - List):** Name five common types of Machine Learning models discussed in this section.

2.  **(Understand - Matching):** Match the ML model type on the left with its most appropriate description or use case on the right:
    *   A) CNNs                         1) Primarily used for sequential data like text or time series.
    *   B) Transformers                 2) Effective for image and video analysis.
    *   C) K-Means Clustering           3) Revolutionized NLP using attention mechanisms.
    *   D) RNNs                         4) Groups unlabeled data points based on similarity.

3.  **(Analyze - Short Essay):** Explain why CNNs are generally more suitable for image classification tasks, while RNNs are better suited for tasks like natural language translation. Discuss the architectural differences that contribute to this suitability.

---

### 0.3. The Machine Learning Lifecycle

**Learning Objectives:**

*   **Remember:** List the seven key stages of the Machine Learning lifecycle.
*   **Understand:** Explain the main purpose and activities involved in each stage of the ML lifecycle.
*   **Understand:** Describe at least one significant infrastructure implication for each of the following ML lifecycle stages: Data Collection, Model Training, and Model Deployment.
*   **Apply:** Given a description of a specific task in an ML project (e.g., "Cleaning a dataset to remove outliers and handle missing values"), identify which stage of the ML lifecycle it belongs to.
*   **Analyze:** Analyze how a poorly executed "Data Preprocessing & Preparation" stage can negatively impact the "Model Training" and "Model Evaluation" stages.

**Sample Assessment Items:**

1.  **(Remember - Ordering):** Place the following stages of the ML lifecycle in their typical order: Model Evaluation, Data Collection, Model Deployment, Model Training, Data Preprocessing.

2.  **(Understand - Short Answer):** What is the primary goal of the "Model Evaluation" stage in the ML lifecycle, and why is it important?

3.  **(Understand - Short Answer):** Describe a key network infrastructure consideration for the "Model Training" stage when dealing with large datasets and distributed training.

4.  **(Apply - Scenario):** An ML team is currently focused on setting up servers to host their trained model so that it can receive real-time requests from a mobile application and return predictions. Which stage of the ML lifecycle are they primarily working on?

5.  **(Analyze - Explanation):** Explain two potential negative consequences for the model training process if the data preprocessing stage is not performed adequately.

---



### 0.4. AI Workloads: Training vs. Inference

**Learning Objectives:**

*   **Remember:** Define AI model training and AI model inference.
*   **Understand:** Explain at least three key differences between AI training and inference workloads regarding their demands on data, compute, network, and storage infrastructure.
*   **Analyze:** For a given AI application scenario (e.g., a real-time translation service), differentiate the primary network design considerations for its training phase versus its inference phase.
*   **Evaluate:** Justify why an organization might choose a converged infrastructure for both training and inference versus dedicated, optimized clusters for each, considering cost, utilization, and performance.

**Sample Assessment Items:**

1.  **(Remember - MCQ):** What is the primary objective of the AI model inference phase?
    a) To learn patterns from a large dataset.
    b) To adjust the model's internal parameters.
    c) To make predictions on new, unseen data using a pre-trained model.
    d) To collect and preprocess data.
    *Answer: c*

2.  **(Understand - Comparison Table):** Create a table comparing AI Training and AI Inference workloads across the following dimensions: Primary Goal, Data Volume, Compute Intensity, Network Latency Sensitivity, Network Bandwidth Needs.

3.  **(Analyze - Scenario):** A company is developing a sophisticated AI model for climate change prediction. The training process involves petabytes of historical weather data and takes several weeks on a large GPU cluster. Once trained, the model will be used by researchers to run simulations, which are computationally intensive but less frequent. Describe the distinct network requirements you would anticipate for the training cluster versus the environment where researchers run inference simulations.

4.  **(Evaluate - Short Essay):** Discuss the pros and cons of designing a single, large AI cluster intended to handle both training and inference workloads for a variety of AI projects, versus building separate, specialized clusters for training and inference. Consider factors like resource utilization, cost-effectiveness, and performance optimization.

---

### 0.5. Distributed Training: Data and Model Parallelism

**Learning Objectives:**

*   **Remember:** Define data parallelism and model parallelism as strategies for distributed AI training.
*   **Understand:** Explain the core process of data parallelism, including gradient aggregation, and its primary network implications.
*   **Understand:** Explain the core process of model parallelism, including how a model is partitioned, and its primary network implications.
*   **Apply:** Given a scenario describing either an extremely large model or an extremely large dataset with a model that fits on a single accelerator, recommend whether data parallelism or model parallelism would be the more appropriate initial strategy, and why.
*   **Analyze:** Compare the typical communication patterns and primary network bottlenecks encountered in data parallelism versus model parallelism.

**Sample Assessment Items:**

1.  **(Remember - Definitions):** In the context of distributed AI training, briefly define (a) Data Parallelism and (b) Model Parallelism.

2.  **(Understand - MCQ):** Which of the following is a key characteristic of the network traffic in data parallelism?
    a) Primarily involves transferring large model segments between specific worker pairs.
    b) Dominated by collective communication operations like AllReduce for gradient synchronization.
    c) Low bandwidth but extremely sensitive to jitter.
    d) Infrequent, large data transfers from a central storage to all workers simultaneously.
    *Answer: b*

3.  **(Understand - Explanation):** Explain why model parallelism is typically employed when training very large neural networks.

4.  **(Apply - Scenario):** You need to train a deep learning model that has 500 billion parameters, making it too large to fit into the memory of any single GPU available in your cluster. Which distributed training strategy (data parallelism or model parallelism) would be essential to even begin training this model, and why?

5.  **(Analyze - Short Essay):** Discuss the differences in network traffic characteristics and potential bottlenecks when using data parallelism compared to model parallelism for distributed training. How might these differences influence network design choices?

---

### 0.6. Network Implications of AI/ML Workloads

**Learning Objectives:**

*   **Remember:** List at least five critical network implications or requirements driven by AI/ML workloads.
*   **Understand:** For each of the listed network implications (e.g., high bandwidth, low latency, lossless transport), explain its importance in the context of AI/ML training or inference.
*   **Analyze:** Analyze how a failure to address a specific network requirement (e.g., providing a lossless fabric) would negatively impact a large-scale distributed AI training job.
*   **Evaluate:** Given a proposed network design for an AI cluster, evaluate its suitability by assessing how well it addresses at least three key network implications of AI/ML workloads (e.g., scalability, QoS, support for RDMA).

**Sample Assessment Items:**

1.  **(Remember - List):** Identify five distinct network characteristics that are critical for supporting AI/ML workloads effectively.

2.  **(Understand - Explanation):** Explain why lossless transport (e.g., using RoCEv2 with PFC and ECN) is often considered a requirement for high-performance distributed AI training clusters.

3.  **(Analyze - Scenario):** An AI training cluster is experiencing significantly longer job completion times than expected. Preliminary investigation reveals intermittent packet drops on the network fabric during periods of high traffic. Analyze how these packet drops could be contributing to the poor performance, especially if the training uses an RDMA-based protocol.

4.  **(Evaluate - Design Review):** A network architect proposes a leaf-spine topology for a new AI training cluster using switches that support 100GbE, basic QoS, but have no specific features for RDMA optimization or advanced congestion control. Evaluate the potential strengths and weaknesses of this design for supporting demanding distributed training workloads. What recommendations might you offer?

---
