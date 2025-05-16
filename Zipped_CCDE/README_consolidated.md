# CCDE & Cisco ACI Knowledge Base and Study Repository (Consolidated)

## Overview

This repository serves as a comprehensive knowledge base and structured learning environment for the Cisco Certified Design Expert (CCDE) certification and Cisco Application Centric Infrastructure (ACI) technologies. It aims to provide study materials, tools for processing learning resources, and a platform for developing AI-enhanced learning applications.

The study approach emphasizes a modularized, focused learning model based on official Cisco CCDE documentation, covering key technology areas such as AI Infrastructure, On-Prem and Cloud Services, Large-Scale Networks, and Workforce Mobility.

## Repository Structure

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

*   **Study Plan Generator**: Python-based tool that processes CCDE PDF documents to create a structured, prioritized study plan. It extracts content, identifies key topics, categorizes them, and generates both JSON and Markdown outputs.
*   **Content Extraction Utilities**: Scripts and methodologies for processing various document types (PDFs, PowerPoints, Word, Markdown) and multimedia content to build the knowledge base.
*   **AI/NLP Integration**: Implementation of AI subsystems with Retrieval Augmented Generation (RAG), vector databases, and agent-based systems for interactive learning and advanced Q&A.
*   **LlamaIndex RAG Framework**: Framework for document processing and knowledge retrieval to enhance learning experience with real-time and accurate information.

## Development Approach

The project follows a structured development approach:

1. **Foundation Phase**: Building core infrastructure, document processing pipeline, and basic content extraction tools.
2. **Enhancement Phase**: Implementing advanced NLP features, RAG systems, and knowledge graphs.
3. **Application Phase**: Developing user-facing applications such as Q&A systems, course generators, and interactive learning tools.
4. **Refinement Phase**: Optimizing performance, enhancing user experience, and expanding content coverage.

## Technology Stack

- **NLP/ML**: spaCy, Hugging Face Transformers, LlamaIndex, LangChain
- **Infrastructure**: Docker, AWS, Python, Flask/FastAPI
- **Database**: PostgreSQL, vector databases (Pinecone/Milvus/FAISS)
- **Content Processing**: PyMuPDF, python-pptx, python-docx, OCR tools
- **Frontend**: React (for web interfaces)

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/WKimandu/CCDE_Cisco.git
   cd CCDE_Cisco
   ```

2. **Set up the environment:** This repository uses a dedicated conda environment named `CCDE_Cisco`.
   ```bash
   # Ensure you have Anaconda or Miniconda installed
   conda create --name CCDE_Cisco python=3.9
   conda activate CCDE_Cisco
   pip install -r requirements.txt
   ```

3. **Explore the documentation:** Start with the `docs/` directory for study materials and project guidelines.

4. **Utilize the tools:** Explore scripts in the `scripts/` directory. For example, to generate a study plan:
   ```bash
   python scripts/ccde_study_plan.py 
   ```

## Study Approach

The CCDE study approach focuses on:

1. **Structured Learning**: Following a curriculum-aligned path from fundamentals to advanced topics.
2. **Practical Application**: Emphasizing design scenarios and real-world problem-solving.
3. **Progressive Assessment**: Using increasingly complex scenarios to build expertise.
4. **Comprehensive Coverage**: Addressing all exam domains and technology areas.

## CCDE Exam Information

The CCDE (Cisco Certified Design Expert) is Cisco's expert-level certification for network design. Key exam components include:

- **Written Exam (CCDE 400-007)**: Tests theoretical knowledge of network design principles.
- **Practical Exam**: Tests ability to design networks for complex scenarios under time constraints.
- **Key Topics**: Enterprise campus design, WAN design, data center design, security design, and more.

## Future Development

*   Building a comprehensive knowledge base with a GUI frontend.
*   Implementing advanced AI subsystems (RAG, vector databases, agent-based systems).
*   Developing an aligned management system for CCDE course modules.
*   Creating interactive learning experiences with personalized learning paths.

## License

Primarily for personal use and educational purposes. Not for redistribution unless specified otherwise for particular components.

## Contributing

Please follow the established coding standards and project rules when contributing to this repository. See the `docs/guidelines/` directory for detailed contribution guidelines. 