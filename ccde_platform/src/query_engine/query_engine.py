"""
Query Engine Module for CCDE Learning Platform

This module provides functionality for querying the CCDE knowledge base
using various LlamaIndex query engines optimized for different types of queries.
"""

import os
from typing import Dict, List, Any, Optional, Union

from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import (
    RetrieverQueryEngine, 
    SubQuestionQueryEngine,
    RouterQueryEngine,
)
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.retrievers import VectorIndexRetriever, BM25Retriever
from llama_index.llms.openai import OpenAI
from llama_index.core.response_synthesizers import (
    CompactAndRefine, 
    TreeSummarize,
    ResponseMode
)

class CCDEQueryEngine:
    """Manages query engines for the CCDE knowledge base."""
    
    def __init__(
        self,
        index: VectorStoreIndex,
        llm_model: str = "gpt-4",
        similarity_top_k: int = 5,
        enable_hybrid_search: bool = True,
    ):
        """
        Initialize the query engine.
        
        Args:
            index: The vector store index to query
            llm_model: The LLM model to use for query processing
            similarity_top_k: Number of top results to retrieve for each query
            enable_hybrid_search: Whether to enable hybrid search (vector + keyword)
        """
        self.index = index
        self.llm_model = llm_model
        self.similarity_top_k = similarity_top_k
        self.enable_hybrid_search = enable_hybrid_search
        
        # Initialize the LLM
        self.llm = OpenAI(model=llm_model)
        
        # Create the query engines
        self.basic_engine = self._create_basic_engine()
        self.advanced_engine = self._create_advanced_engine()
        self.router_engine = self._create_router_engine()
    
    def _create_basic_engine(self) -> RetrieverQueryEngine:
        """
        Create a basic retriever query engine.
        
        Returns:
            RetrieverQueryEngine: A basic query engine
        """
        # Create retriever
        retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=self.similarity_top_k,
        )
        
        # Configure response synthesis
        response_synthesizer = CompactAndRefine(
            llm=self.llm,
            response_mode=ResponseMode.TREE_SUMMARIZE,
        )
        
        # Create and return the query engine
        return RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
            node_postprocessors=[
                SimilarityPostprocessor(similarity_cutoff=0.7)
            ]
        )
    
    def _create_advanced_engine(self) -> SubQuestionQueryEngine:
        """
        Create an advanced sub-question query engine for complex queries.
        
        Returns:
            SubQuestionQueryEngine: An advanced query engine that breaks complex
            questions into simpler sub-questions
        """
        return SubQuestionQueryEngine.from_defaults(
            self.index,
            llm=self.llm,
            similarity_top_k=self.similarity_top_k,
            # Use more sophisticated response synthesis
            response_synthesizer=TreeSummarize(llm=self.llm)
        )
    
    def _create_router_engine(self) -> RouterQueryEngine:
        """
        Create a router query engine that selects the appropriate engine based on the query.
        
        Returns:
            RouterQueryEngine: A router query engine
        """
        # Create a hybrid retriever if enabled
        if self.enable_hybrid_search:
            from llama_index.core.retrievers import BM25Retriever
            from llama_index.core.query_engine import RetrieverQueryEngine
            
            # BM25 Retriever (keyword-based)
            bm25_retriever = BM25Retriever.from_defaults(
                docstore=self.index.docstore,
                similarity_top_k=self.similarity_top_k,
            )
            
            # Create a keyword-based query engine
            keyword_engine = RetrieverQueryEngine.from_args(
                retriever=bm25_retriever,
                response_synthesizer=CompactAndRefine(
                    llm=self.llm,
                    response_mode=ResponseMode.TREE_SUMMARIZE,
                )
            )
            
            # Define the router query engine
            from llama_index.question_gen.llm_generators import LLMQuestionGenerator
            from llama_index.core.selectors import LLMSingleSelector
            from llama_index.core.tools import QueryEngineTool
            
            # Define the available engines as tools
            query_engine_tools = [
                QueryEngineTool.from_defaults(
                    query_engine=self.basic_engine,
                    description=(
                        "Useful for answering specific questions about CCDE topics, "
                        "network design concepts, and technical details."
                    ),
                ),
                QueryEngineTool.from_defaults(
                    query_engine=keyword_engine,
                    description=(
                        "Useful for searching specific keywords and terms in the CCDE materials."
                    ),
                ),
                QueryEngineTool.from_defaults(
                    query_engine=self.advanced_engine,
                    description=(
                        "Useful for answering complex, multi-part questions that require "
                        "decomposition into simpler questions."
                    ),
                ),
            ]
            
            # Create the router query engine
            from llama_index.core.query_engine import RouterQueryEngine
            
            return RouterQueryEngine(
                selector=LLMSingleSelector.from_defaults(llm=self.llm),
                query_engine_tools=query_engine_tools,
            )
        else:
            # If hybrid search is not enabled, use a simpler router
            # that just chooses between basic and advanced engines
            query_engine_tools = [
                QueryEngineTool.from_defaults(
                    query_engine=self.basic_engine,
                    description=(
                        "Useful for answering specific questions about CCDE topics, "
                        "network design concepts, and technical details."
                    ),
                ),
                QueryEngineTool.from_defaults(
                    query_engine=self.advanced_engine,
                    description=(
                        "Useful for answering complex, multi-part questions that require "
                        "decomposition into simpler questions."
                    ),
                ),
            ]
            
            # Create the router query engine
            from llama_index.core.query_engine import RouterQueryEngine
            from llama_index.core.selectors import LLMSingleSelector
            
            return RouterQueryEngine(
                selector=LLMSingleSelector.from_defaults(llm=self.llm),
                query_engine_tools=query_engine_tools,
            )
    
    def query(
        self, 
        query_text: str, 
        engine_type: str = "router",
        metadata_filters: Optional[Dict[str, Union[str, List[str]]]] = None
    ) -> Any:
        """
        Query the CCDE knowledge base.
        
        Args:
            query_text: The query text
            engine_type: The type of engine to use (basic, advanced, or router)
            metadata_filters: Optional metadata filters to apply to the retrieval
            
        Returns:
            The query response
        """
        # Apply metadata filters if provided
        if metadata_filters:
            # Create a custom retriever with metadata filters
            from llama_index.core.retrievers import VectorIndexRetriever
            retriever = VectorIndexRetriever(
                index=self.index,
                similarity_top_k=self.similarity_top_k,
                filters=metadata_filters
            )
            
            # Create a custom query engine with this retriever
            custom_engine = RetrieverQueryEngine.from_args(
                retriever=retriever,
                response_synthesizer=CompactAndRefine(
                    llm=self.llm,
                    response_mode=ResponseMode.TREE_SUMMARIZE,
                )
            )
            
            return custom_engine.query(query_text)
        
        # Otherwise, use the specified engine
        if engine_type == "basic":
            response = self.basic_engine.query(query_text)
        elif engine_type == "advanced":
            response = self.advanced_engine.query(query_text)
        else:  # Default to router
            response = self.router_engine.query(query_text)
            
        return response
    
    def query_with_citation(self, query_text: str) -> Any:
        """
        Query the CCDE knowledge base with source citations.
        
        Args:
            query_text: The query text
            
        Returns:
            The query response with source citations
        """
        from llama_index.core.response.notebook_utils import display_response
        from llama_index.core.settings import Settings
        
        # Enable source attribution
        Settings.llm = self.llm
        Settings.node_parser.chunk_size = 512
        
        # Use the retriever query engine with source citations
        response = self.basic_engine.query(query_text)
        
        return response

# Example usage
if __name__ == "__main__":
    from ccde_platform.src.ingestion.document_processor import CCDEDocumentProcessor
    from ccde_platform.src.knowledge_base.vector_store import CCDEVectorStore
    
    # Process documents
    processor = CCDEDocumentProcessor()
    nodes, _ = processor.process_documents()
    
    # Build vector store
    vector_store = CCDEVectorStore()
    index = vector_store.build_index_from_nodes(nodes)
    
    # Create query engine
    query_engine = CCDEQueryEngine(index)
    
    # Run a query
    response = query_engine.query(
        "What are the key learning objectives for CCDE automation concepts?"
    )
    print(response) 