"""
Command-line interface to run the document processing pipeline.
"""

from src.processing.pipeline import DocumentProcessor
import argparse
import logging
import os
from pathlib import Path
import sys

# Add the parent directory to sys.path to import our modules
sys.path.append(str(Path(__file__).parent.parent.parent))

# Import our pipeline

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Run the document processing pipeline from command line arguments."""
    parser = argparse.ArgumentParser(
        description="Process documents with LlamaIndex and spaCy NER."
    )

    # Input arguments
    parser.add_argument(
        "--input", "-i", required=True,
        help="Path to input document or directory"
    )
    parser.add_argument(
        "--is_directory", "-d", action="store_true",
        help="Whether the input is a directory"
    )
    parser.add_argument(
        "--recursive", "-r", action="store_true",
        help="Process directories recursively"
    )

    # Output arguments
    parser.add_argument(
        "--output", "-o", required=True,
        help="Path to output directory for the index"
    )

    # Processing arguments
    parser.add_argument(
        "--spacy_model", default="en_core_web_sm",
        help="spaCy model to use (default: en_core_web_sm)"
    )
    parser.add_argument(
        "--custom_entities",
        help="Path to custom entities JSON file"
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Create output directory if it doesn't exist
        os.makedirs(args.output, exist_ok=True)

        # Initialize document processor
        processor = DocumentProcessor(
            spacy_model=args.spacy_model,
            custom_entities_file=args.custom_entities,
            persist_dir=args.output
        )

        # Process and index documents
        index = processor.process_and_index(
            input_path=args.input,
            is_directory=args.is_directory,
            recursive=args.recursive
        )

        # Report success
        logger.info(
            f"Successfully processed and indexed documents from {args.input}")
        logger.info(f"Index saved to {args.output}")

        # Return success
        return 0

    except Exception as e:
        logger.error(f"Error processing documents: {str(e)}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
