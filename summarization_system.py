"""
CCDE Cisco Knowledge Base - Summarization System
Implements a document summarization system with LlamaIndex
"""

import os
from llamaindex_core_setup import load_index, setup_llamaindex
from llama_index.core.response_synthesizers import TreeSummarize


def create_summarization_engine(index=None, index_dir="llamaindex-rag/index"):
    """Create a summarization engine from the index"""

    # Set up LlamaIndex
    setup_llamaindex()

    # Load index if not provided
    if index is None:
        index = load_index(index_dir)
        if index is None:
            print("Failed to load index. Please create an index first.")
            return None

    # Create a custom summary template
    summary_template = (
        "Provide a comprehensive technical summary of the following content. "
        "Focus on key concepts, technologies, and design principles. "
        "Include relevant details and avoid general information. "
        "Structure the summary with sections and bullet points. "
        "Content: {context}"
    )

    # Create the summarization engine with TreeSummarize strategy
    summarize_engine = index.as_query_engine(
        response_synthesizer=TreeSummarize(
            verbose=True,
            summary_template=summary_template
        )
    )

    print("Summarization engine created successfully.")
    return summarize_engine


def run_summarization_system():
    """Run a document summarization system"""

    # Create summarization engine
    summarize_engine = create_summarization_engine()
    if summarize_engine is None:
        return

    print("\n===== CCDE Knowledge Base Summarization System =====")
    print("Enter a topic to summarize from the CCDE knowledge base.")
    print("Example topics: 'ACI', 'VXLAN', 'Network Design', 'Data Center Architecture'")
    print("Type 'exit' to quit.\n")

    # Interactive summarization loop
    while True:
        topic = input("Topic to summarize: ")
        if topic.lower() in ["exit", "quit"]:
            break

        # Create the query
        query = f"Provide a comprehensive technical summary about {topic} in the context of Cisco networking and CCDE certification."

        # Get summary
        print(f"\nGenerating summary about '{topic}'...")
        response = summarize_engine.query(query)

        # Display summary
        print("\nSummary:")
        print(f"{response.response}\n")


if __name__ == "__main__":
    run_summarization_system()
