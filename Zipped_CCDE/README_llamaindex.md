# CCDE Cisco Knowledge Base with LlamaIndex

This directory contains a set of tools for building a comprehensive knowledge base using LlamaIndex for the Cisco CCDE certification.

## Features

- **Optimized for Technical Documentation**: Fine-tuned for processing Cisco networking documentation
- **Multiple Use Cases**: 
  - Question-Answering system for specific technical queries
  - Document summarization for condensed topic overviews
  - Course generation for structured learning modules
  - Exam generation with multiple question formats

## Getting Started

### Prerequisites

- Python 3.8+ 
- OpenAI API key (set in environment variable `OPENAI_API_KEY`)
- Required Python packages (automatically checked by the system):
  - llama-index and related packages
  - openai
  - pypdf
  - numpy

### Installation

1. Ensure your conda environment is activated:
   ```
   conda activate CCDE_Cisco
   ```

2. Install the required dependencies:
   ```
   pip install llama-index-core llama-index-readers-file llama-index-llms-openai llama-index-embeddings-openai openai pypdf numpy
   ```

### Adding Documents

1. Place your Cisco CCDE related PDFs in the `llamaindex-rag/data` directory.
2. Supported file types: PDF
3. Recommended content: Cisco documentation, CCDE exam topics, design guides, whitepapers

### Running the System

1. Launch the main interface:
   ```
   python main_interface.py
   ```

2. From the menu, choose option 1 to build the index (first time only or when adding new documents)

3. Then select any of the knowledge base applications:
   - Q&A System
   - Summarization System  
   - Course Generator
   - Exam Generator

## Individual Components

### Core Setup (`llamaindex_core_setup.py`)
Handles the basic LlamaIndex configuration, document loading, and index creation. This is the foundation for all other components.

### Q&A System (`qa_system.py`)
Interactive system for technical questions about CCDE and Cisco networking topics. Provides sourced answers with references to documents.

### Summarization System (`summarization_system.py`)
Creates comprehensive summaries of technical topics, structured for clarity and completeness.

### Course Generator (`course_generator.py`)
Generates complete training modules including learning objectives, key concepts, technical details, hands-on exercises, and assessments.

### Exam Generator (`exam_generator.py`)
Creates various types of exam questions including:
- Multiple choice
- Fill-in-the-blank
- Drag-and-drop matching
- Mixed question formats

### Main Interface (`main_interface.py`)
Unified interface for accessing all the knowledge base tools.

## License

This project is for educational purposes only and should be used in compliance with OpenAI's terms of service and Cisco's copyright policies.

## Next Steps

Future enhancements planned:
- Adding LangChain implementation for comparison
- Improving document preprocessing for better chunk creation
- Supporting more document formats
- Adding chat-based interaction 