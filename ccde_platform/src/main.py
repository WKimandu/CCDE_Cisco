"""
Main Application Module for CCDE Learning Platform

This module brings together all components of the CCDE learning platform,
serving as the main entry point for processing documents, building knowledge
bases, and querying the CCDE content.
"""

import os
import argparse
from typing import List, Optional

from ccde_platform.src.ingestion.document_processor import CCDEDocumentProcessor
from ccde_platform.src.knowledge_base.vector_store import CCDEVectorStore
from ccde_platform.src.query_engine.query_engine import CCDEQueryEngine

def process_documents(
    source_dir: str = "./Zipped_CCDE",
    file_extensions: List[str] = [".md", ".pdf", ".txt"],
    cache_dir: str = "./ccde_platform/storage/ingestion_cache",
    chunk_size: int = 512,
    chunk_overlap: int = 50,
    rebuild: bool = False
) -> None:
    """
    Process documents and build the knowledge base.
    
    Args:
        source_dir: Directory containing source documents
        file_extensions: List of file extensions to process
        cache_dir: Directory to store the ingestion cache
        chunk_size: Size of text chunks for splitting documents
        chunk_overlap: Overlap between chunks
        rebuild: Whether to rebuild the knowledge base from scratch
    """
    print(f"Processing documents from {source_dir}...")
    
    # Initialize the document processor
    processor = CCDEDocumentProcessor(
        cache_dir=cache_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    # Check if we need to load an existing pipeline
    pipeline_path = os.path.join(cache_dir, "pipeline")
    if os.path.exists(pipeline_path) and not rebuild:
        print(f"Loading existing pipeline from {pipeline_path}")
        processor.load_pipeline(pipeline_path)
    
    # Process documents
    nodes, pipeline = processor.process_documents(
        directory_path=source_dir,
        file_extentions=file_extensions
    )
    
    # Save the pipeline for future use
    processor.save_pipeline()
    
    print(f"Processed {len(nodes)} nodes from documents")
    
    # Build the knowledge base
    build_knowledge_base(nodes, rebuild=rebuild)

def build_knowledge_base(
    nodes: Optional[List] = None,
    storage_type: str = "local",
    persist_dir: str = "./ccde_platform/storage/vector_store",
    collection_name: str = "ccde_knowledge",
    rebuild: bool = False
) -> CCDEVectorStore:
    """
    Build the knowledge base from processed nodes.
    
    Args:
        nodes: List of nodes to build the knowledge base from
        storage_type: Type of vector store to use
        persist_dir: Directory to persist the vector store
        collection_name: Name of the collection/index
        rebuild: Whether to rebuild the knowledge base from scratch
        
    Returns:
        The initialized vector store
    """
    print(f"Building knowledge base in {persist_dir}...")
    
    # Initialize the vector store
    vector_store = CCDEVectorStore(
        storage_type=storage_type,
        persist_dir=persist_dir,
        collection_name=collection_name
    )
    
    # Build the index from nodes if provided
    if nodes is not None:
        vector_store.build_index_from_nodes(nodes, rebuild=rebuild)
    else:
        # Try to load an existing index
        vector_store.load_index()
    
    print("Knowledge base ready")
    
    return vector_store

def create_query_engine(
    vector_store: CCDEVectorStore,
    llm_model: str = "gpt-4",
    similarity_top_k: int = 5
) -> CCDEQueryEngine:
    """
    Create a query engine for the knowledge base.
    
    Args:
        vector_store: The vector store containing the knowledge base
        llm_model: The LLM model to use
        similarity_top_k: Number of similar documents to retrieve
        
    Returns:
        The initialized query engine
    """
    print(f"Creating query engine with model {llm_model}...")
    
    # Ensure the index is loaded
    if vector_store.index is None:
        vector_store.load_index()
    
    # Create the query engine
    query_engine = CCDEQueryEngine(
        index=vector_store.index,
        llm_model=llm_model,
        similarity_top_k=similarity_top_k
    )
    
    print("Query engine ready")
    
    return query_engine

def interactive_query_session(query_engine: CCDEQueryEngine) -> None:
    """
    Run an interactive query session.
    
    Args:
        query_engine: The query engine to use
    """
    print("\n=== CCDE Knowledge Base Interactive Query Session ===")
    print("Enter your questions about CCDE topics, or 'exit' to quit")
    print("You can also type 'advanced:' before your query to use the advanced query engine")
    print("Or type 'citation:' to get responses with source citations")
    
    while True:
        query = input("\nEnter query: ")
        
        if query.lower() in ["exit", "quit", "q"]:
            break
        
        # Check for special query types
        if query.lower().startswith("advanced:"):
            query_text = query[len("advanced:"):].strip()
            print("\nUsing advanced query engine...")
            response = query_engine.query(query_text, engine_type="advanced")
        elif query.lower().startswith("citation:"):
            query_text = query[len("citation:"):].strip()
            print("\nUsing citation query...")
            response = query_engine.query_with_citation(query_text)
        else:
            # Use the router query engine by default
            response = query_engine.query(query)
        
        print(f"\nResponse: {response}")

def main():
    """Main entry point for the CCDE Learning Platform."""
    parser = argparse.ArgumentParser(description="CCDE Learning Platform")
    
    # Command arguments
    parser.add_argument(
        "--process",
        action="store_true",
        help="Process documents and build knowledge base"
    )
    parser.add_argument(
        "--query",
        action="store_true",
        help="Run interactive query session"
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Rebuild knowledge base from scratch"
    )
    
    # Configuration arguments
    parser.add_argument(
        "--source-dir",
        type=str,
        default="./Zipped_CCDE",
        help="Directory containing source documents"
    )
    parser.add_argument(
        "--storage-type",
        type=str,
        default="local",
        choices=["local", "qdrant", "chroma"],
        help="Type of vector store to use"
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        default="gpt-4",
        help="LLM model to use"
    )
    
    args = parser.parse_args()
    
    # Default behavior if no specific action is specified
    if not (args.process or args.query):
        args.process = True
        args.query = True
    
    vector_store = None
    
    # Process documents if requested
    if args.process:
        processor = CCDEDocumentProcessor()
        nodes, _ = processor.process_documents(directory_path=args.source_dir)
        vector_store = build_knowledge_base(
            nodes=nodes,
            storage_type=args.storage_type,
            rebuild=args.rebuild
        )
    
    # Run query session if requested
    if args.query:
        if vector_store is None:
            vector_store = build_knowledge_base(storage_type=args.storage_type)
        
        query_engine = create_query_engine(
            vector_store=vector_store,
            llm_model=args.llm_model
        )
        
        interactive_query_session(query_engine)

if __name__ == "__main__":
    main() 