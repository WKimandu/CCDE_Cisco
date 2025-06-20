"""
CCDE Cisco Knowledge Base - Exam Generator
Implements an exam and test generator with LlamaIndex
"""

import os
import json
from datetime import datetime
from llamaindex_core_setup import load_index, setup_llamaindex


def create_exam_engine(index=None, index_dir="llamaindex-rag/index"):
    """Create an exam generation engine from the index"""

    # Set up LlamaIndex
    setup_llamaindex()

    # Load index if not provided
    if index is None:
        index = load_index(index_dir)
        if index is None:
            print("Failed to load index. Please create an index first.")
            return None

    # Create the exam generation engine
    exam_engine = index.as_query_engine(
        response_mode="tree_summarize",
        similarity_top_k=7,  # Use more chunks for comprehensive exam generation
        verbose=True
    )

    print("Exam generation engine created successfully.")
    return exam_engine


def generate_exam(engine, topic, num_questions=5, exam_type="mixed"):
    """Generate an exam based on topic, number of questions, and type"""

    # Define the exam generation prompt based on exam type
    if exam_type == "multichoice":
        prompt = f"""
        Generate {num_questions} multiple-choice questions about {topic} for CCDE exam preparation.
        For each question:
        1. Create a challenging but fair technical question
        2. Provide 4 possible answers (A, B, C, D)
        3. Indicate the correct answer
        4. Include a brief explanation of why the answer is correct
        Format the output as a valid JSON array where each object contains:
        - question: The question text
        - options: Array of 4 answer options
        - correct: The correct answer letter (A, B, C, D)
        - explanation: Why this is the correct answer
        """
    elif exam_type == "fillblank":
        prompt = f"""
        Generate {num_questions} fill-in-the-blank questions about {topic} for CCDE exam preparation.
        For each question:
        1. Create a technical statement with a key term or concept removed and replaced with a blank
        2. Provide the correct answer for the blank
        3. Include a brief explanation of the concept
        Format the output as a valid JSON array where each object contains:
        - question: The statement with a blank indicated by "______"
        - answer: The correct word or phrase for the blank
        - explanation: Brief explanation of this concept
        """
    elif exam_type == "dragdrop":
        prompt = f"""
        Generate {num_questions} drag-and-drop matching questions about {topic} for CCDE exam preparation.
        For each question:
        1. Create a scenario or concept that requires matching items
        2. Provide 4-5 items to be matched on the left side
        3. Provide 4-5 corresponding items for the right side
        4. Indicate the correct matches
        Format the output as a valid JSON array where each object contains:
        - scenario: Brief description of the matching scenario
        - left_items: Array of items on the left side
        - right_items: Array of items on the right side
        - correct_matches: Array of objects with left_index and right_index showing the correct pairings
        """
    else:  # mixed type
        prompt = f"""
        Generate {num_questions} mixed question types about {topic} for CCDE exam preparation.
        Include multiple-choice, fill-in-the-blank, and scenario-based questions.
        For each question:
        1. Specify the question type (multiple_choice, fill_blank, or scenario)
        2. Create a challenging but fair technical question
        3. Provide appropriate answers based on the question type
        4. Indicate the correct answer
        5. Include a brief explanation of why the answer is correct
        Format the output as a valid JSON array where each object contains:
        - type: The question type (multiple_choice, fill_blank, or scenario)
        - question: The question text
        - options: Array of answer options (for multiple choice)
        - answer: The correct answer
        - explanation: Why this is the correct answer
        """

    # Get exam from the engine
    print(f"Generating {exam_type} exam on {topic}...")
    response = engine.query(prompt)

    # Try to parse the JSON response
    try:
        # Find the JSON part in the response (it may contain explanatory text)
        response_text = response.response
        # Look for [ which would indicate the start of a JSON array
        json_start = response_text.find('[')
        json_end = response_text.rfind(']') + 1

        if json_start >= 0 and json_end > json_start:
            json_str = response_text[json_start:json_end]
            questions = json.loads(json_str)
            return {
                "topic": topic,
                "type": exam_type,
                "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "questions": questions
            }
        else:
            print("Could not find valid JSON in the response. Using raw response.")
            return {
                "topic": topic,
                "type": exam_type,
                "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "raw_response": response_text
            }
    except json.JSONDecodeError:
        print("Error parsing JSON from the response. Using raw response.")
        return {
            "topic": topic,
            "type": exam_type,
            "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "raw_response": response.response
        }


def run_exam_generator():
    """Run an interactive exam generator"""

    # Create exam generator engine
    exam_engine = create_exam_engine()
    if exam_engine is None:
        return

    print("\n===== CCDE Knowledge Base Exam Generator =====")
    print("Generate different types of exam questions for CCDE preparation.")
    print("Available exam types:")
    print("  - multichoice: Multiple-choice questions")
    print("  - fillblank: Fill-in-the-blank questions")
    print("  - dragdrop: Drag-and-drop matching questions")
    print("  - mixed: Combination of different question types")
    print("Type 'exit' to quit.\n")

    # Interactive exam generation loop
    while True:
        topic = input("Exam topic (or 'exit' to quit): ")
        if topic.lower() in ["exit", "quit"]:
            break

        # Get exam type
        exam_type = input(
            "Exam type (multichoice/fillblank/dragdrop/mixed) [default: mixed]: ").lower() or "mixed"
        if exam_type not in ["multichoice", "fillblank", "dragdrop", "mixed"]:
            print("Invalid exam type. Using 'mixed' as default.")
            exam_type = "mixed"

        # Get number of questions
        try:
            num_questions = int(
                input("Number of questions [default: 5]: ") or "5")
        except ValueError:
            print("Invalid number. Using 5 questions as default.")
            num_questions = 5

        # Generate exam
        exam = generate_exam(exam_engine, topic, num_questions, exam_type)

        # Display and save exam
        print("\n===== Generated Exam =====\n")

        # Format and display the exam based on structure
        if "raw_response" in exam:
            print(exam["raw_response"])
        else:
            for i, q in enumerate(exam["questions"]):
                print(f"Question {i+1}: {q['question']}")
                if exam_type == "multichoice" or (exam_type == "mixed" and q.get('type') == "multiple_choice"):
                    for j, option in enumerate(q['options']):
                        print(f"  {chr(65+j)}. {option}")
                    print(f"Correct answer: {q['correct']}")
                elif exam_type == "fillblank" or (exam_type == "mixed" and q.get('type') == "fill_blank"):
                    print(f"Answer: {q['answer']}")
                elif exam_type == "dragdrop":
                    print("Left items:")
                    for j, item in enumerate(q['left_items']):
                        print(f"  {j+1}. {item}")
                    print("Right items:")
                    for j, item in enumerate(q['right_items']):
                        print(f"  {chr(65+j)}. {item}")
                    print("Matches:")
                    for match in q['correct_matches']:
                        left_idx = match['left_index']
                        right_idx = match['right_index']
                        print(f"  {left_idx+1} -> {chr(65+right_idx)}")

                print(f"Explanation: {q['explanation']}")
                print()

        # Option to save the exam
        save_option = input(
            "Would you like to save this exam to a file? (y/n): ")
        if save_option.lower() == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"exam_{topic.replace(' ', '_').lower()}_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(exam, f, indent=2)
            print(f"Exam saved to {filename}")


if __name__ == "__main__":
    run_exam_generator()
