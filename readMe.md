# CCDE & Cisco ACI Knowledge Base and Study Repository

## Overview

This repository serves as a comprehensive knowledge base and structured learning environment for the Cisco Certified Design Expert (CCDE) certification and Cisco Application Centric Infrastructure (ACI) technologies. It aims to provide study materials, tools for processing learning resources, and a platform for developing AI-enhanced learning applications.

The study approach emphasizes a modularized, focused learning model based on official Cisco CCDE documentation, covering key technology areas such as AI Infrastructure, On-Prem and Cloud Services, Large-Scale Networks, and Workforce Mobility.

## Repository Structure (Planned - Post Reorganization)

-   **`docs/`**: Contains all curated documentation, including:
    -   `architecture/`: System architecture for the AI knowledge base.
    -   `study-materials/`: CCDE and ACI study guides, topic summaries, and key takeaways.
    -   `guidelines/`: Project rules, coding standards, and contribution guidelines.
    -   `specifications/`: Detailed plans for NLP, document processing, etc.
-   **`data/`**: Raw and processed data, including:
    -   `extracted_content/`: Text and JSON extracted from official CCDE PDFs.
    -   `transcripts/`: Transcriptions of relevant videos and audio sessions.
-   **`scripts/`**: Python utilities and other scripts for tasks like:
    -   Downloading videos (e.g., `yt_dwnld.py`).
    -   Transcribing video/audio content (e.g., `transcribe_session.ps1`, `transcribe_all_sessions.ps1`).
    -   Generating study plans (e.g., `ccde_study_plan.py`).
-   **`course_templates/`**: Templates for creating learning modules.

## Key Features & Tools

*   **Study Plan Generator (`scripts/ccde_study_plan.py`)**: A Python-based tool that processes CCDE PDF documents to create a structured, prioritized study plan. It extracts content, identifies key topics, categorizes them, and generates both JSON and Markdown outputs.
*   **Content Extraction Utilities**: Scripts and methodologies for processing various document types (PDFs, PowerPoints, Word, Markdown) and multimedia content to build the knowledge base.
*   **AI/NLP Integration (Planned)**: Future development includes implementing AI subsystems with Retrieval Augmented Generation (RAG), vector databases, and agent-based systems for interactive learning and advanced Q&A.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/WKimandu/CCDE_Cisco.git
    cd CCDE_Cisco
    ```
2.  **Set up the environment:** This repository uses a dedicated conda environment named `CCDE_Cisco`.
    ```bash
    # Ensure you have Anaconda or Miniconda installed
    # Create and activate the environment (if requirements.txt is comprehensive)
    # conda create --name CCDE_Cisco python=3.9 (example)
    conda activate CCDE_Cisco
    # Install dependencies
    pip install -r requirements.txt
    ```
3.  **Explore the documentation:** Start with the `docs/` directory for study materials and project guidelines.
4.  **Utilize the tools:** Explore scripts in the `scripts/` directory. For example, to generate a study plan:
    ```bash
    python scripts/ccde_study_plan.py 
    ```
    (Note: Ensure `ccde_study_plan.py` is correctly placed and paths are adjusted if necessary after reorganization).
    Follow the generated study plan, which might be located in `docs/study-materials/ccde/CCDE_Study_Plan.md` after reorganization.

## Future Development

*   Building a knowledge base with a GUI frontend.
*   Implementing advanced AI subsystems (RAG, vector databases).
*   Developing an aligned management system for CCDE course modules.

## License

Primarily for personal use and educational purposes. Not for redistribution unless specified otherwise for particular components.

## Contributing

(Details to be added in a `CONTRIBUTING.md` file if the repository becomes open to public contributions beyond the current user.)

