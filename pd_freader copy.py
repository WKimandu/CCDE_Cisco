import os
import PyPDF2
import re
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        return f"Error extracting text from {pdf_path}: {str(e)}"


def search_keywords_in_text(text, keywords):
    """Search for keywords in text and return relevant snippets."""
    snippets = []
    paragraphs = re.split(r'\n\s*\n', text)

    for paragraph in paragraphs:
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', paragraph, re.IGNORECASE):
                # Add paragraph to snippets if it contains the keyword
                snippets.append(paragraph.strip())
                break

    return snippets


def analyze_neoliberalism_documents(folder_path, output_folder="extracted_texts"):
    """Process all PDF files in the given folder related to neoliberalism."""
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Keywords related to neoliberalism
    keywords = ["neoliberal", "free market", "privatization", "deregulation",
                "washington consensus", "globalization", "market fundamentalism",
                "austerity", "economic liberalization"]

    results = {}

    # Iterate through PDF files
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            print(f"Processing {filename}...")

            # Extract text from PDF
            text = extract_text_from_pdf(pdf_path)

            # Save full text to file
            with open(os.path.join(output_folder, f"{filename}.txt"), "w", encoding="utf-8") as text_file:
                text_file.write(text)

            # Find relevant snippets
            snippets = search_keywords_in_text(text, keywords)
            results[filename] = snippets

            # Save snippets to a separate file
            with open(os.path.join(output_folder, f"{filename}_snippets.txt"), "w", encoding="utf-8") as snippets_file:
                snippets_file.write(f"Relevant snippets from {filename}:\n\n")
                snippets_file.write("\n\n---\n\n".join(snippets))

    return results


# Main execution
if __name__ == "__main__":
    folder_path = "Documentation+KB"
    results = analyze_neoliberalism_documents(folder_path)

    # Print summary
    print("\nAnalysis Summary:")
    for filename, snippets in results.items():
        print(f"{filename}: {len(snippets)} relevant snippets found")
