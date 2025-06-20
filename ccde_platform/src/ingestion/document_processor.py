"""
Document Processing Module for CCDE Learning Platform

This module provides functionality to process CCDE documentation using 
LlamaIndex ingestion pipeline, which handles chunking, embedding, and 
document management.
"""

import os
from typing import List, Tuple, Optional

from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor, QuestionsAnsweredExtractor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.schema import BaseNode


class CCDEDocumentProcessor:
    """Handles CCDE document processing using LlamaIndex."""

    def __init__(
        self,
        cache_dir: str = "./ccde_platform/storage/ingestion_cache",
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        embedding_model: str = "text-embedding-ada-002"
    ):
        """
        Initialize the document processor.

        Args:
            cache_dir: Directory to store the ingestion cache
            chunk_size: Size of text chunks for splitting documents
            chunk_overlap: Overlap between chunks
            embedding_model: OpenAI embedding model to use
        """
        self.cache_dir = cache_dir
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_model = embedding_model

        # Create cache directory if it doesn't exist
        os.makedirs(os.path.dirname(cache_dir), exist_ok=True)

        # Initialize the ingestion cache
        self.cache = IngestionCache(
            cache_dir=cache_dir,
        )

        # Initialize the pipeline
        self.pipeline = self._create_pipeline()

    def _create_pipeline(self) -> IngestionPipeline:
        """
        Create an ingestion pipeline with the appropriate transformations.

        Returns:
            IngestionPipeline: Configured ingestion pipeline
        """
        return IngestionPipeline(
            transformations=[
                # Split documents into chunks
                SentenceSplitter(
                    chunk_size=self.chunk_size,
                    chunk_overlap=self.chunk_overlap
                ),
                # Extract titles from content
                TitleExtractor(),
                # Extract potential questions/answers from content
                QuestionsAnsweredExtractor(),
                # Create embeddings for each node
                OpenAIEmbedding(model=self.embedding_model),
            ],
            cache=self.cache
        )

    def process_documents(
        self,
        directory_path: str = "./Zipped_CCDE",
        file_extentions: List[str] = [".md", ".pdf", ".txt"]
    ) -> Tuple[List[BaseNode], IngestionPipeline]:
        """
        Process documents from a directory using LlamaIndex.

        Args:
            directory_path: Path to the directory containing documents
            file_extentions: List of file extensions to include

        Returns:
            Tuple containing the processed nodes and the pipeline
        """
        # Load documents
        documents = SimpleDirectoryReader(
            directory_path,
            filename_as_id=True,
            required_exts=file_extentions
        ).load_data()

        print(f"Loaded {len(documents)} documents from {directory_path}")

        # Run the ingestion pipeline
        nodes = self.pipeline.run(documents=documents)

        print(f"Created {len(nodes)} nodes from the documents")

        return nodes, self.pipeline

    def process_specific_files(
        self,
        file_paths: List[str]
    ) -> Tuple[List[BaseNode], IngestionPipeline]:
        """
        Process specific document files.

        Args:
            file_paths: List of file paths to process

        Returns:
            Tuple containing the processed nodes and the pipeline
        """
        # Load only specified documents
        documents = []
        for file_path in file_paths:
            if os.path.exists(file_path):
                doc_id = os.path.basename(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append(Document(text=content, doc_id=doc_id))

        print(f"Loaded {len(documents)} documents from specified files")

        # Run the ingestion pipeline
        nodes = self.pipeline.run(documents=documents)

        print(f"Created {len(nodes)} nodes from the documents")

        return nodes, self.pipeline

    def save_pipeline(self, save_path: Optional[str] = None) -> None:
        """
        Save the ingestion pipeline to disk.

        Args:
            save_path: Path to save the pipeline to, defaults to cache_dir
        """
        save_location = save_path or self.cache_dir
        os.makedirs(os.path.dirname(save_location), exist_ok=True)
        self.pipeline.persist(save_location)
        print(f"Pipeline saved to {save_location}")

    def load_pipeline(self, load_path: Optional[str] = None) -> None:
        """
        Load the ingestion pipeline from disk.

        Args:
            load_path: Path to load the pipeline from, defaults to cache_dir
        """
        load_location = load_path or self.cache_dir
        if os.path.exists(load_location):
            self.pipeline.load(load_location)
            print(f"Pipeline loaded from {load_location}")
        else:
            print(f"No pipeline found at {load_location}")


# Example usage when run directly
if __name__ == "__main__":
    processor = CCDEDocumentProcessor()
    nodes, pipeline = processor.process_documents()
    processor.save_pipeline()
