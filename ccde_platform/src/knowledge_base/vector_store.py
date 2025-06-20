"""
Vector Store Module for CCDE Learning Platform

This module provides functionality to build and manage vector stores
using LlamaIndex, enabling semantic search and retrieval of CCDE concepts.
"""

import os
from typing import List, Optional, Union

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.schema import BaseNode, Document
from llama_index.vector_stores.qdrant import QdrantVectorStore

# Optional imports for different vector stores
try:
    import qdrant_client
    QDRANT_AVAILABLE = True
except ImportError:
    QDRANT_AVAILABLE = False

try:
    from llama_index.vector_stores.chroma import ChromaVectorStore
    import chromadb
    CHROMA_AVAILABLE = True
except ImportError:
    CHROMA_AVAILABLE = False

class CCDEVectorStore:
    """Manages vector storage using LlamaIndex for CCDE content."""
    
    def __init__(
        self,
        storage_type: str = "local",
        persist_dir: str = "./ccde_platform/storage/vector_store",
        collection_name: str = "ccde_knowledge",
        host: Optional[str] = None,
        port: Optional[int] = None,
    ):
        """
        Initialize the vector store.
        
        Args:
            storage_type: Type of vector store ("local", "qdrant", or "chroma")
            persist_dir: Directory to persist the vector store
            collection_name: Name of the collection/index
            host: Host for remote vector stores (Qdrant)
            port: Port for remote vector stores (Qdrant)
        """
        self.storage_type = storage_type
        self.persist_dir = persist_dir
        self.collection_name = collection_name
        self.host = host
        self.port = port
        
        # Create storage directory if it doesn't exist
        if storage_type == "local":
            os.makedirs(persist_dir, exist_ok=True)
        
        # Initialize the appropriate vector store
        self.vector_store = self._init_vector_store()
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        self.index = None
        
    def _init_vector_store(self):
        """
        Initialize the appropriate vector store based on the storage type.
        
        Returns:
            The initialized vector store
        """
        if self.storage_type == "qdrant":
            if not QDRANT_AVAILABLE:
                raise ImportError("Qdrant client not available. Install with 'pip install qdrant-client'")
            
            if self.host and self.port:
                client = qdrant_client.QdrantClient(host=self.host, port=self.port)
            else:
                client = qdrant_client.QdrantClient(location=self.persist_dir)
                
            return QdrantVectorStore(client=client, collection_name=self.collection_name)
        
        elif self.storage_type == "chroma":
            if not CHROMA_AVAILABLE:
                raise ImportError("Chroma not available. Install with 'pip install chromadb'")
            
            chroma_client = chromadb.PersistentClient(path=self.persist_dir)
            chroma_collection = chroma_client.get_or_create_collection(self.collection_name)
            return ChromaVectorStore(chroma_collection=chroma_collection)
        
        # Default to local storage
        return None
    
    def build_index_from_nodes(self, nodes: List[BaseNode], rebuild: bool = False) -> VectorStoreIndex:
        """
        Build a vector store index from processed nodes.
        
        Args:
            nodes: List of nodes to build the index from
            rebuild: Whether to rebuild the index even if it exists
            
        Returns:
            The constructed vector store index
        """
        # Check if index exists and if we should reload it
        if not rebuild and self.storage_type == "local" and os.path.exists(os.path.join(self.persist_dir, "docstore.json")):
            print(f"Loading existing index from {self.persist_dir}")
            self.index = self.load_index()
            return self.index
        
        print(f"Building new index with {len(nodes)} nodes")
        self.index = VectorStoreIndex(nodes, storage_context=self.storage_context)
        
        # Persist the index for future use
        if self.storage_type == "local":
            self.index.storage_context.persist(persist_dir=self.persist_dir)
            print(f"Index persisted to {self.persist_dir}")
        
        return self.index
    
    def build_index_from_documents(self, documents: List[Document], rebuild: bool = False) -> VectorStoreIndex:
        """
        Build a vector store index directly from documents.
        
        Args:
            documents: List of documents to build the index from
            rebuild: Whether to rebuild the index even if it exists
            
        Returns:
            The constructed vector store index
        """
        # Check if index exists and if we should reload it
        if not rebuild and self.storage_type == "local" and os.path.exists(os.path.join(self.persist_dir, "docstore.json")):
            print(f"Loading existing index from {self.persist_dir}")
            self.index = self.load_index()
            return self.index
        
        print(f"Building new index with {len(documents)} documents")
        self.index = VectorStoreIndex.from_documents(
            documents, 
            storage_context=self.storage_context
        )
        
        # Persist the index for future use
        if self.storage_type == "local":
            self.index.storage_context.persist(persist_dir=self.persist_dir)
            print(f"Index persisted to {self.persist_dir}")
        
        return self.index
    
    def load_index(self) -> VectorStoreIndex:
        """
        Load an existing index from storage.
        
        Returns:
            The loaded vector store index
        """
        if self.storage_type == "local":
            storage_context = StorageContext.from_defaults(
                persist_dir=self.persist_dir
            )
            self.index = load_index_from_storage(storage_context)
            return self.index
        else:
            # For non-local storage, we should already have the vector store initialized
            if self.index is None:
                # Create an empty index if needed
                self.index = VectorStoreIndex([], storage_context=self.storage_context)
            return self.index
    
    def update_index(self, nodes: List[BaseNode]) -> VectorStoreIndex:
        """
        Update the index with new nodes.
        
        Args:
            nodes: List of nodes to add to the index
            
        Returns:
            The updated vector store index
        """
        if self.index is None:
            # Build the index if it doesn't exist
            return self.build_index_from_nodes(nodes)
        
        print(f"Updating index with {len(nodes)} nodes")
        for node in nodes:
            self.index.insert(node)
        
        # Persist the updated index
        if self.storage_type == "local":
            self.index.storage_context.persist(persist_dir=self.persist_dir)
            print(f"Updated index persisted to {self.persist_dir}")
        
        return self.index

# Example usage
if __name__ == "__main__":
    from ccde_platform.src.ingestion.document_processor import CCDEDocumentProcessor
    
    # Process documents
    processor = CCDEDocumentProcessor()
    nodes, _ = processor.process_documents()
    
    # Build vector store
    vector_store = CCDEVectorStore()
    index = vector_store.build_index_from_nodes(nodes) 