"""
CCDE Cisco Knowledge Base - Course Generator
Implements a course module generator with LlamaIndex
"""

import os
from llamaindex_core_setup import load_index, setup_llamaindex


def create_course_engine(index=None, index_dir="llamaindex-rag/index"):
    """Create a course generation engine from the index"""

    # Set up LlamaIndex
    setup_llamaindex()

    # Load index if not provided
    if index is None:
        index = load_index(index_dir)
        if index is None:
            print("Failed to load index. Please create an index first.")
            return None

    # Define the course generation template
    course_template = """
    Based on the provided technical documentation, create a comprehensive training module with:
    
    # Module Title: {query}
    
    ## Learning Objectives
    [Generate 3-5 specific learning objectives that participants should achieve after completing this module]
    
    ## Key Concepts
    [Identify and explain the main concepts, technologies, protocols, or architectures relevant to the topic]
    
    ## Technical Details
    [Provide detailed technical explanation with diagrams/illustrations recommendations where appropriate]
    
    ## Hands-on Exercises
    [Create 2-3 practical exercises that reinforce the key concepts, including step-by-step procedures]
    
    ## Assessment
    [Develop 5 assessment questions (mix of multiple-choice and scenario-based) to test understanding]
    
    ## Additional Resources
    [Recommend further reading or practice resources]
    """

    # Create the course generation engine
    course_engine = index.as_query_engine(
        text_qa_template=course_template,
        response_mode="tree_summarize",
        similarity_top_k=10,  # Use more chunks for comprehensive course generation
        verbose=True
    )

    print("Course generation engine created successfully.")
    return course_engine


def run_course_generator():
    """Run a course module generator"""

    # Create course generation engine
    course_engine = create_course_engine()
    if course_engine is None:
        return

    print("\n===== CCDE Knowledge Base Course Generator =====")
    print("Enter a topic to generate a training module.")
    print("Example topics: 'ACI Fundamentals', 'VXLAN in the Data Center', 'Network Design Principles'")
    print("Type 'exit' to quit.\n")

    # Interactive course generation loop
    while True:
        topic = input("Course module topic: ")
        if topic.lower() in ["exit", "quit"]:
            break

        # Get course module
        print(f"\nGenerating course module for '{topic}'...")
        response = course_engine.query(topic)

        # Display course module
        print("\n===== Generated Course Module =====\n")
        print(response.response)
        print("\n====================================\n")

        # Option to save the course module
        save_option = input(
            "Would you like to save this course module to a file? (y/n): ")
        if save_option.lower() == 'y':
            filename = f"course_module_{topic.replace(' ', '_').lower()}.md"
            with open(filename, 'w') as f:
                f.write(f"# Course Module: {topic}\n\n")
                f.write(response.response)
            print(f"Course module saved to {filename}")


if __name__ == "__main__":
    run_course_generator()
