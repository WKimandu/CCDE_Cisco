"""
CCDE Cisco Knowledge Base - Main Interface
Unified interface for all LlamaIndex RAG applications
"""

import os
import sys
import importlib.util


def check_module_installed(module_name):
    """Check if a module is installed"""
    return importlib.util.find_spec(module_name) is not None


def check_dependencies():
    """Check if all required dependencies are installed"""
    required_modules = [
        "llama_index",
        "openai",
        "pypdf",
        "numpy"
    ]

    missing_modules = []
    for module in required_modules:
        if not check_module_installed(module):
            missing_modules.append(module)

    if missing_modules:
        print("Missing required dependencies:")
        for module in missing_modules:
            print(f"  - {module}")
        print("\nPlease install the missing dependencies with:")
        print(f"pip install {' '.join(missing_modules)}")
        return False

    return True


def ensure_data_directory():
    """Ensure the data directory exists and contains PDFs"""
    data_dir = "llamaindex-rag/data"
    os.makedirs(data_dir, exist_ok=True)

    pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the data directory.")
        print("Please copy your CCDE and Cisco related PDFs to the following directory:")
        print(os.path.abspath(data_dir))
        return False

    print(f"Found {len(pdf_files)} PDF files in the data directory:")
    for pdf in pdf_files:
        print(f"  - {pdf}")

    return True


def check_index_directory():
    """Check if the index directory exists and contains a valid index"""
    index_dir = "llamaindex-rag/index"

    if not os.path.exists(index_dir) or not os.listdir(index_dir):
        print("Index directory is empty or does not exist.")
        print("You will need to build the index first.")
        return False

    print("Index directory found.")
    return True


def main_menu():
    """Display the main menu and handle user choices"""
    while True:
        print("\n===== CCDE Cisco Knowledge Base =====")
        print("1. Build/Update Index")
        print("2. Q&A System")
        print("3. Summarization System")
        print("4. Course Generator")
        print("5. Exam Generator")
        print("6. Check System Status")
        print("0. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            # Build/Update Index
            from llamaindex_core_setup import setup_llamaindex, create_index
            setup_llamaindex()
            if ensure_data_directory():
                create_index()
        elif choice == "2":
            # Q&A System
            if check_index_directory():
                from qa_system import run_qa_system
                run_qa_system()
        elif choice == "3":
            # Summarization System
            if check_index_directory():
                from summarization_system import run_summarization_system
                run_summarization_system()
        elif choice == "4":
            # Course Generator
            if check_index_directory():
                from course_generator import run_course_generator
                run_course_generator()
        elif choice == "5":
            # Exam Generator
            if check_index_directory():
                from exam_generator import run_exam_generator
                run_exam_generator()
        elif choice == "6":
            # Check System Status
            check_dependencies()
            ensure_data_directory()
            check_index_directory()
        elif choice == "0":
            # Exit
            print("Exiting CCDE Cisco Knowledge Base. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Starting CCDE Cisco Knowledge Base with LlamaIndex...")

    # Check dependencies before starting
    if not check_dependencies():
        sys.exit(1)

    # Run the main menu
    main_menu()
