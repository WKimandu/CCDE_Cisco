import os
import sys
import pdfplumber
import PyPDF2
import re
import textwrap
from pathlib import Path


def extract_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber which handles layouts better."""
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n\n"
        return text
    except Exception as e:
        print(f"Error with pdfplumber: {str(e)}")
        return None


def extract_with_pypdf2(pdf_path):
    """Extract text using PyPDF2 as a backup method."""
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        print(f"Error with PyPDF2: {str(e)}")
        return None


def analyze_neoliberalism_content(text):
    """Extract and analyze content related to neoliberalism and internationalization."""
    if not text:
        return "No text could be extracted from the PDF."

    # Find paragraphs containing both neoliberalism and internationalization terms
    relevant_paragraphs = []
    paragraphs = re.split(r'\n\s*\n', text)

    neoliberal_terms = ['neoliberal', 'neoliberalism',
                        'free market', 'privatization', 'deregulation']
    international_terms = ['international', 'globalization',
                           'globalisation', 'transnational', 'world market']

    for para in paragraphs:
        # Clean up paragraph
        clean_para = re.sub(r'\s+', ' ', para).strip()
        if len(clean_para) < 50:  # Skip short paragraphs
            continue

        has_neoliberal = any(re.search(r'\b' + re.escape(term) + r'\b',
                             clean_para, re.IGNORECASE) for term in neoliberal_terms)
        has_international = any(re.search(r'\b' + re.escape(term) + r'\b',
                                clean_para, re.IGNORECASE) for term in international_terms)

        if has_neoliberal and has_international:
            relevant_paragraphs.append(clean_para)

    # Generate a summary
    analysis = "=== ANALYSIS OF NEOLIBERALISM AND INTERNATIONALIZATION ===\n\n"

    # Word frequency
    neoliberal_count = sum(len(re.findall(
        r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE)) for term in neoliberal_terms)
    international_count = sum(len(re.findall(
        r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE)) for term in international_terms)

    analysis += f"Word frequency:\n"
    analysis += f"- Neoliberalism-related terms: {neoliberal_count} mentions\n"
    analysis += f"- Internationalization-related terms: {international_count} mentions\n\n"

    # Add relevant paragraphs
    analysis += f"Found {len(relevant_paragraphs)} paragraphs discussing both neoliberalism and internationalization:\n\n"

    for i, para in enumerate(relevant_paragraphs[:10], 1):  # Limit to first 10
        # Format paragraph nicely with word wrapping
        wrapped_text = textwrap.fill(para, width=80)
        analysis += f"Paragraph {i}:\n{wrapped_text}\n\n"

    if len(relevant_paragraphs) > 10:
        analysis += f"(+ {len(relevant_paragraphs) - 10} more paragraphs...)\n"

    return analysis


def main():
    folder_path = "Documentation+KB"
    target_file = "Neoliberalism_internationalisation_and_h.pdf"
    pdf_path = os.path.join(folder_path, target_file)

    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        # List similar files
        similar_files = [f for f in os.listdir(
            folder_path) if "neoliberal" in f.lower() and "international" in f.lower()]
        if similar_files:
            print("Similar files found:")
            for file in similar_files:
                print(f"- {file}")
            target_file = similar_files[0]
            pdf_path = os.path.join(folder_path, target_file)
            print(f"Using {target_file} instead.")
        else:
            print("No similar files found.")
            return

    print(f"Extracting text from {target_file}...")

    # Try extraction methods in order
    text = extract_with_pdfplumber(pdf_path)
    if not text:
        print("Trying alternate extraction method...")
        text = extract_with_pypdf2(pdf_path)

    if not text or len(text.strip()) < 100:
        print("Failed to extract meaningful text from the PDF.")
        return

    # Save the full text
    output_dir = "extracted_texts"
    os.makedirs(output_dir, exist_ok=True)

    full_text_path = os.path.join(output_dir, f"{target_file}_full.txt")
    with open(full_text_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Full text saved to {full_text_path}")

    # Analyze content
    analysis = analyze_neoliberalism_content(text)
    analysis_path = os.path.join(output_dir, f"{target_file}_analysis.txt")
    with open(analysis_path, "w", encoding="utf-8") as f:
        f.write(analysis)

    print(f"Analysis saved to {analysis_path}")
    print("First 500 characters of analysis:")
    print(analysis[:500] + "...")


if __name__ == "__main__":
    main()
