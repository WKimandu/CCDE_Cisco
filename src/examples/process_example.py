"""
Example script demonstrating how to use the document processing pipeline.
"""

import logging
from src.processing.pipeline import DocumentProcessor
import os
import sys
from pathlib import Path

# Add the parent directory to sys.path to import our modules
sys.path.append(str(Path(__file__).parent.parent.parent))


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Run a simple example of the document processing pipeline."""
    try:
        # Set up paths
        # Update these paths to match your environment
        data_dir = Path("data/sample_docs")
        output_dir = Path("data/processed_index")
        custom_entities_file = Path("config/custom_entities.json")

        # Make sure directories exist
        os.makedirs(data_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        print(f"Processing documents in {data_dir}")
        print(f"Using custom entities from {custom_entities_file}")
        print(f"Saving index to {output_dir}")

        # Check if custom entities file exists
        if not custom_entities_file.exists():
            print(
                f"Warning: Custom entities file not found at {custom_entities_file}")
            print("Processing will continue without custom entities.")
            custom_entities_file = None

        # Create the document processor
        processor = DocumentProcessor(
            spacy_model="en_core_web_sm",
            custom_entities_file=str(
                custom_entities_file) if custom_entities_file else None,
            persist_dir=str(output_dir)
        )

        # Check if the data directory has files
        if not any(data_dir.iterdir()):
            print(
                f"The directory {data_dir} is empty. Please add some documents to process.")
            print("Example document formats: PDF, DOCX, PPTX, MD, JSON, JPG, PNG")
            return

        # Process and index the documents
        print("\nStarting document processing and indexing...")
        index = processor.process_and_index(
            input_path=str(data_dir),
            is_directory=True,
            recursive=True
        )

        # Create a simple query engine
        query_engine = index.as_query_engine()

        # Run a test query
        test_query = "What is Cisco ACI?"
        print(f"\nRunning test query: '{test_query}'")
        response = query_engine.query(test_query)

        print("\nResponse:")
        print(response.response)

        print("\nExample complete! The index has been saved to:", output_dir)

    except ImportError as e:
        print(f"\nError: {str(e)}")
        print("\nLikely cause: LlamaIndex import error")
        print("Make sure you're using the correct import structure for your LlamaIndex version:")
        print("For LlamaIndex v0.9.x+:")
        print("  from llama_index.readers import SimpleDirectoryReader")
        print("  from llama_index.core import Document, VectorStoreIndex")

    except Exception as e:
        print(f"\nError: {str(e)}")
        logger.exception("An error occurred during processing")


if __name__ == "__main__":
    main()
