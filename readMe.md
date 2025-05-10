# CCDE & Cisco ACI Knowledge Base

A comprehensive knowledge base system for CCDE certification and Cisco ACI, leveraging LlamaIndex for document processing and spaCy for named entity recognition.

## System Overview

This system processes various document types (PDF, PPTX, DOCX, etc.) to build a comprehensive knowledge base for CCDE certification and Cisco ACI. It uses:

- **LlamaIndex**: For document loading, processing, and vector storage
- **spaCy**: For named entity recognition, annotation, and concept mapping
- **ChromaDB**: As the vector database for storing embeddings

## Project Structure

```
CCDE_Cisco/
├── config/               # Configuration files
│   └── custom_entities.json  # Custom entities for NER
├── data/                 # Data storage
├── docs/                 # Documentation
│   ├── architecture/     # Architecture documents
│   └── specifications/   # Specifications
├── src/                  # Source code
│   ├── ingestion/        # Document loading modules
│   ├── extraction/       # Content extraction modules
│   ├── processing/       # Processing modules (NER, etc.)
│   ├── storage/          # Storage modules
│   ├── retrieval/        # Retrieval modules
│   ├── application/      # Application modules
│   └── interface/        # User interface modules
└── tests/                # Test cases
```

## Installation

1. Clone the repository
2. Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate CCDE_Cisco
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

### Processing Documents

Use the command-line interface to process documents:

```bash
python src/processing/run_processor.py --input path/to/documents --is_directory --output path/to/output
```

Options:
- `--input`, `-i`: Path to input document or directory
- `--is_directory`, `-d`: Flag indicating the input is a directory
- `--recursive`, `-r`: Process subdirectories recursively
- `--output`, `-o`: Output directory for the index
- `--spacy_model`: spaCy model to use (default: "en_core_web_sm")
- `--custom_entities`: Path to custom entities JSON file

### Adding Custom Entities

Custom entities can be added to the `config/custom_entities.json` file to enhance named entity recognition. The file contains categories like:

- `TECH`: Technical terms related to CCDE and Cisco ACI
- `VENDOR`: Networking vendors
- `PROTOCOL`: Network protocols
- `ARCHITECTURE`: Network architecture patterns
- `COMPONENT`: Network components
- `CONCEPT`: Networking concepts

## Development

### Adding New Document Types

To add support for new document types:

1. Update the `DocumentLoader` class in `src/ingestion/document_loader.py`
2. Add the new file extension to the `supported_extensions` dictionary

### Improving NER Processing

To enhance named entity recognition:

1. Update the `NERProcessor` class in `src/processing/ner_processor.py`
2. Add new extraction methods or improve existing ones

## Troubleshooting

### LlamaIndex Import Errors

If you encounter import errors with LlamaIndex, check your version and update the imports accordingly:

For LlamaIndex v0.9.x or newer:

```python
# Document loading
from llama_index.readers import SimpleDirectoryReader
from llama_index.core import Document

# Indexing
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.node_parser import SimpleNodeParser
```

For older LlamaIndex versions:

```python
# Basic imports
from llama_index import SimpleDirectoryReader, Document
from llama_index import VectorStoreIndex, StorageContext
from llama_index.node_parser import SimpleNodeParser
```

### spaCy Model Issues

If you encounter errors related to spaCy models:

1. Verify the model is installed:
   ```bash
   python -m spacy validate
   ```

2. Install missing models:
   ```bash
   python -m spacy download en_core_web_sm
   # Or for larger models:
   python -m spacy download en_core_web_lg
   ```

3. Check for model compatibility with your spaCy version:
   ```bash
   pip show spacy
   ```

### Document Processing Failures

If document processing fails:

1. Check file permissions and ensure files are not locked
2. Verify the document format is supported
3. For PDFs, ensure they are not password-protected
4. Increase logging level for more details:
   ```python
   logging.basicConfig(level=logging.DEBUG)
   ```

## Version Compatibility

This project requires specific version compatibility:

| Dependency | Required Version | Notes |
|------------|------------------|-------|
| Python     | 3.10+            | Tested with 3.10, 3.11 |
| LlamaIndex  | 0.9.x+           | API changes in 0.9.x require import updates |
| spaCy      | 3.6.0+           | Needed for advanced NER features |
| ChromaDB   | 0.4.13+          | For vector storage |
| PyMuPDF    | 1.22.5+          | For PDF processing |

When updating dependencies, check the compatibility matrix in the [PRD document](docs/specifications/product-requirements.md).

## Maintaining Custom Entities

As the domain knowledge evolves, regularly update the custom entities file:

1. **Regular Reviews**: Schedule quarterly reviews of the custom entities list
2. **User Feedback**: Add new terms based on user query patterns
3. **Documentation Updates**: Track new terminology as Cisco releases updates
4. **Entity Validation**: Periodically validate entity detection accuracy
5. **Category Management**: Organize entities into appropriate categories

To update entities:
```bash
# Export current concepts from processed documents
python src/tools/export_concepts.py --input data/processed_index --output config/extracted_concepts.json

# Merge with custom entities
python src/tools/merge_entities.py --extracted config/extracted_concepts.json --custom config/custom_entities.json --output config/updated_entities.json
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
