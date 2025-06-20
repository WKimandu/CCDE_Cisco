"""
Document processing pipeline that integrates LlamaIndex with spaCy NER.
This module provides a pipeline for processing documents with entity extraction and indexing.
"""

import logging
import os
from typing import List, Dict, Any, Optional
from pathlib import Path

# Import our own modules
from src.ingestion.document_loader import DocumentLoader
from src.processing.ner_processor import NERProcessor

# LlamaIndex imports - updated for v0.9.x
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core import Document

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """
    Pipeline for processing documents with entity extraction and indexing.
    """

    def __init__(self,
                 spacy_model: str = "en_core_web_sm",
                 custom_entities_file: Optional[str] = None,
                 persist_dir: Optional[str] = None):
        """
        Initialize the document processor.

        Args:
            spacy_model (str): Name of the spaCy model to use
            custom_entities_file (str, optional): Path to custom entities file
            persist_dir (str, optional): Directory to persist the index
        """
        # Initialize components
        self.document_loader = DocumentLoader()
        self.ner_processor = NERProcessor(model_name=spacy_model,
                                          custom_entities_file=custom_entities_file)

        # Set persistence directory
        self.persist_dir = persist_dir
        if persist_dir:
            self.persist_dir = Path(persist_dir)
            os.makedirs(self.persist_dir, exist_ok=True)

    def process_document(self, file_path: str) -> List[Document]:
        """
        Process a single document.

        Args:
            file_path (str): Path to the document

        Returns:
            List[Document]: Processed documents with enhanced metadata
        """
        logger.info(f"Processing document: {file_path}")

        # Load document
        documents = self.document_loader.load_document(file_path)

        # Process each document chunk
        for doc in documents:
            # Extract entities and concepts
            entities = self.ner_processor.extract_entities(doc.text)
            concepts = self.ner_processor.extract_concepts(doc.text)
            technical_terms = self.ner_processor.extract_technical_terms(
                doc.text)

            # Add entity and concept metadata
            doc.metadata["entities"] = entities
            doc.metadata["concepts"] = {
                k: list(v) for k, v in concepts.items()}
            doc.metadata["technical_terms"] = technical_terms

            # Create annotated text
            annotated_text, _ = self.ner_processor.annotate_text(doc.text)
            doc.metadata["annotated_text"] = annotated_text

        logger.info(f"Processed {len(documents)} document chunks")
        return documents

    def process_directory(self, directory_path: str, recursive: bool = True) -> List[Document]:
        """
        Process all documents in a directory.

        Args:
            directory_path (str): Path to the directory
            recursive (bool): Whether to process subdirectories

        Returns:
            List[Document]: Processed documents with enhanced metadata
        """
        logger.info(f"Processing directory: {directory_path}")

        # Load documents
        documents = self.document_loader.load_documents_from_directory(
            directory_path, recursive=recursive)

        # Process each document
        for doc in documents:
            # Extract entities and concepts
            entities = self.ner_processor.extract_entities(doc.text)
            concepts = self.ner_processor.extract_concepts(doc.text)
            technical_terms = self.ner_processor.extract_technical_terms(
                doc.text)

            # Add entity and concept metadata
            doc.metadata["entities"] = entities
            doc.metadata["concepts"] = {
                k: list(v) for k, v in concepts.items()}
            doc.metadata["technical_terms"] = technical_terms

            # Create annotated text
            annotated_text, _ = self.ner_processor.annotate_text(doc.text)
            doc.metadata["annotated_text"] = annotated_text

        logger.info(
            f"Processed {len(documents)} document chunks from directory")
        return documents

    def create_index(self, documents: List[Document]) -> VectorStoreIndex:
        """
        Create a vector index from processed documents.

        Args:
            documents (List[Document]): Processed documents

        Returns:
            VectorStoreIndex: Vector index for querying
        """
        logger.info(f"Creating index from {len(documents)} documents")

        # Create node parser
        node_parser = SimpleNodeParser.from_defaults()

        # Parse nodes
        nodes = node_parser.get_nodes_from_documents(documents)

        # Create index
        storage_context = None
        if self.persist_dir:
            storage_context = StorageContext.from_defaults(
                persist_dir=str(self.persist_dir))

        index = VectorStoreIndex(nodes, storage_context=storage_context)

        # Persist index
        if self.persist_dir:
            index.storage_context.persist()
            logger.info(f"Persisted index to {self.persist_dir}")

        return index

    def process_and_index(self, input_path: str, is_directory: bool = False, recursive: bool = True) -> VectorStoreIndex:
        """
        Process documents and create an index.

        Args:
            input_path (str): Path to document or directory
            is_directory (bool): Whether the input path is a directory
            recursive (bool): Whether to process subdirectories

        Returns:
            VectorStoreIndex: Vector index for querying
        """
        # Process documents
        if is_directory:
            documents = self.process_directory(input_path, recursive=recursive)
        else:
            documents = self.process_document(input_path)

        # Create index
        index = self.create_index(documents)

        return index
