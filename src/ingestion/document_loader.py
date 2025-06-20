"""
Document loader module for ingesting various document types.
This module provides a unified interface for loading different document formats.
"""

import os
from typing import List, Dict, Any, Optional
from pathlib import Path
import logging

# LlamaIndex imports - updated for v0.9.x
from llama_index.readers import SimpleDirectoryReader
from llama_index.core import Document

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentLoader:
    """
    A unified document loader that supports multiple formats.

    Supported formats:
    - PDF (.pdf)
    - Word (.docx)
    - PowerPoint (.pptx)
    - Markdown (.md)
    - JSON (.json)
    - Images (.jpg, .jpeg, .png)
    """

    def __init__(self):
        """Initialize document loader with appropriate readers."""
        # Map file extensions to LlamaIndex supported formats
        self.supported_extensions = {
            ".pdf": "pdf",
            ".docx": "docx",
            ".pptx": "pptx",
            ".md": "markdown",
            ".json": "json",
            ".jpg": "image",
            ".jpeg": "image",
            ".png": "image",
        }

    def load_document(self, file_path: str, metadata: Optional[Dict[str, Any]] = None) -> List[Document]:
        """
        Load a document from a file path and return LlamaIndex Document objects.

        Args:
            file_path (str): Path to the document file
            metadata (dict, optional): Additional metadata to attach to the document

        Returns:
            List[Document]: List of LlamaIndex Document objects
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Get file extension and check if supported
        ext = file_path.suffix.lower()
        if ext not in self.supported_extensions:
            raise ValueError(f"Unsupported file format: {ext}")

        # Add basic metadata if not provided
        if metadata is None:
            metadata = {}

        # Add file metadata
        file_metadata = {
            "file_name": file_path.name,
            "file_type": ext,
            "file_size": os.path.getsize(file_path),
            "file_path": str(file_path),
        }

        # Merge metadata
        metadata.update(file_metadata)

        # Load document using SimpleDirectoryReader
        logger.info(f"Loading document: {file_path}")
        try:
            # Create a temporary directory with just this file
            reader = SimpleDirectoryReader(
                input_files=[str(file_path)],
                filename_as_id=True,
            )
            documents = reader.load_data()

            # Add metadata to all documents
            for doc in documents:
                doc.metadata.update(metadata)

            logger.info(
                f"Successfully loaded {len(documents)} document chunks from {file_path}")
            return documents
        except Exception as e:
            logger.error(f"Error loading document {file_path}: {str(e)}")
            raise

    def load_documents_from_directory(
        self, directory_path: str, recursive: bool = True,
        file_extns: List[str] = None, metadata: Dict[str, Any] = None
    ) -> List[Document]:
        """
        Load all supported documents from a directory.

        Args:
            directory_path (str): Path to the directory
            recursive (bool): Whether to search recursively (default: True)
            file_extns (List[str], optional): File extensions to filter by
            metadata (dict, optional): Additional metadata to attach to all documents

        Returns:
            List[Document]: List of LlamaIndex Document objects
        """
        directory_path = Path(directory_path)
        if not directory_path.exists() or not directory_path.is_dir():
            raise ValueError(f"Directory not found: {directory_path}")

        # Define which file extensions to load
        supported_extns = list(
            self.supported_extensions.keys()) if file_extns is None else file_extns

        # Use SimpleDirectoryReader to load all documents
        logger.info(f"Loading documents from {directory_path}")
        try:
            reader = SimpleDirectoryReader(
                input_dir=str(directory_path),
                recursive=recursive,
                required_exts=supported_extns,
                filename_as_id=True,
            )
            documents = reader.load_data()

            # Add metadata to all documents
            if metadata is not None:
                for doc in documents:
                    # Add directory metadata
                    doc.metadata["directory"] = str(directory_path)
                    # Add custom metadata
                    doc.metadata.update(metadata)

            logger.info(
                f"Successfully loaded {len(documents)} document chunks from {directory_path}")
            return documents
        except Exception as e:
            logger.error(
                f"Error loading documents from {directory_path}: {str(e)}")
            raise
