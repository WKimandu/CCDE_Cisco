# CCDE Learning Platform

A comprehensive learning system for Cisco Certified Design Expert (CCDE) certification preparation, leveraging LlamaIndex for document processing, knowledge base building, and intelligent querying.

## Overview

The CCDE Learning Platform processes study materials and documentation for CCDE certification and builds an intelligent knowledge base that can be queried conversationally. It uses advanced RAG (Retrieval Augmented Generation) techniques to provide accurate, contextual information from the CCDE curriculum.

## Features

- **Intelligent Document Processing**: Automatically processes Markdown, PDF, and TXT documents
- **Vector-Based Knowledge Storage**: Indexes content for semantic search and retrieval
- **Advanced Query Capabilities**: Supports complex questions with sub-question decomposition
- **Citation Support**: Tracks and provides sources for all information
- **Interactive Learning**: Conversational interface for exploring CCDE topics

## Directory Structure

```
ccde_platform/
├── config/             # Configuration files
├── data/               # Data storage
│   ├── raw/            # Raw source documents
│   ├── processed/      # Processed document data
│   └── embeddings/     # Document embeddings
├── docs/               # Documentation
├── notebooks/          # Jupyter notebooks for analysis
├── src/                # Source code
│   ├── ingestion/      # Document ingestion and processing
│   ├── knowledge_base/ # Vector store and knowledge base
│   ├── query_engine/   # Query processing
│   ├── learning_management/ # Learning path tracking
│   └── frontend/       # User interface
└── storage/            # LlamaIndex storage
```

## Getting Started

### Prerequisites

- Python 3.8+
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ccde-learning-platform.git
cd ccde-learning-platform
```

2. Create and activate a conda environment:
```bash
conda create -n ccde_platform python=3.10
conda activate ccde_platform
```

3. Install dependencies:
```bash
pip install -r ccde_platform/requirements.txt
```

4. Set up OpenAI API key (required for embeddings and LLM):
```bash
# Create a .env file in the project root
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### Running the Platform

Process documents and build the knowledge base:
```bash
python -m ccde_platform.src.main --process
```

Run an interactive query session:
```bash
python -m ccde_platform.src.main --query
```

Do both (process and query):
```bash
python -m ccde_platform.src.main
```

Rebuild the knowledge base from scratch:
```bash
python -m ccde_platform.src.main --process --rebuild
```

## Advanced Configuration

### Using Different Vector Stores

The platform supports multiple vector store backends:

- **Local** (default): Simple file-based storage
- **Qdrant**: High-performance vector database
- **Chroma**: Open-source embedding database

To use a different vector store:
```bash
python -m ccde_platform.src.main --storage-type qdrant
```

### Using Different LLM Models

To specify a different OpenAI model:
```bash
python -m ccde_platform.src.main --llm-model gpt-3.5-turbo
```

## Extending the Platform

The modular architecture makes it easy to extend the platform with new features:

- Add new document loaders in `src/ingestion/`
- Add new query engine types in `src/query_engine/`
- Add new learning management features in `src/learning_management/`

## License

This project is for personal use only and not for distribution.

## Acknowledgments

This project uses LlamaIndex, an advanced RAG framework, and draws on official Cisco CCDE curriculum materials. 