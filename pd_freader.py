import os
import pdfplumber  # More reliable than PyPDF2 for text extraction
import re
from pathlib import Path
import pandas as pd
from tqdm import tqdm  # For progress bars


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using pdfplumber with better error handling."""
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                try:
                    text = page.extract_text() or ""
                    full_text += text + "\n\n"
                except Exception as e:
                    print(
                        f"Error on page in {os.path.basename(pdf_path)}: {str(e)}")
        return full_text
    except Exception as e:
        print(f"Failed to process {os.path.basename(pdf_path)}: {str(e)}")
        return ""


def process_neoliberalism_pdfs(folder_path, output_file="neoliberalism_analysis.csv"):
    """Process PDFs and create a structured analysis of neoliberalism content."""

    # Define key concepts to search for
    key_concepts = {
        "free_market": ["free market", "laissez-faire", "market forces", "invisible hand"],
        "privatization": ["privatization", "private sector", "state-owned enterprise"],
        "deregulation": ["deregulation", "regulatory reform", "government intervention"],
        "trade_liberalization": ["free trade", "trade barrier", "protectionism", "trade agreement"],
        "austerity": ["austerity", "fiscal discipline", "budget deficit", "government spending"],
        "critique": ["inequality", "market failure", "externality", "financial crisis", "social cost"]
    }

    results = []

    # Get all PDF files in the directory
    pdf_files = [f for f in os.listdir(
        folder_path) if f.lower().endswith('.pdf')]

    # Process each PDF file
    for filename in tqdm(pdf_files, desc="Processing PDFs"):
        pdf_path = os.path.join(folder_path, filename)

        # Extract text from the PDF
        text = extract_text_from_pdf(pdf_path)

        if not text:
            continue

        # Create result entry for this document
        result = {
            "filename": filename,
            "word_count": len(text.split()),
            "neoliberalism_mentions": len(re.findall(r'\bneoliberal(?:ism)?\b', text, re.IGNORECASE))
        }

        # Count mentions of each concept
        for concept, terms in key_concepts.items():
            count = 0
            for term in terms:
                count += len(re.findall(r'\b' + re.escape(term) +
                             r'\b', text, re.IGNORECASE))
            result[f"{concept}_mentions"] = count

        # Extract key passages about neoliberalism (snippets around the term)
        neoliberalism_snippets = []
        paragraphs = re.split(r'\n\s*\n', text)
        for para in paragraphs:
            if re.search(r'\bneoliberal(?:ism)?\b', para, re.IGNORECASE):
                # Clean the snippet
                clean_para = re.sub(r'\s+', ' ', para).strip()
                if len(clean_para) > 40:  # Only include substantive snippets
                    neoliberalism_snippets.append(clean_para)

        # Store the first 3 snippets (if available)
        for i in range(min(3, len(neoliberalism_snippets))):
            # Limit length
            result[f"snippet_{i+1}"] = neoliberalism_snippets[i][:500]

        results.append(result)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

    # Also create a summary text file with top documents
    with open("neoliberalism_summary.txt", "w", encoding="utf-8") as f:
        f.write("=== NEOLIBERALISM DOCUMENT ANALYSIS ===\n\n")

        # Top documents by neoliberalism mentions
        f.write("TOP DOCUMENTS BY NEOLIBERALISM MENTIONS:\n")
        top_docs = df.sort_values(
            "neoliberalism_mentions", ascending=False).head(10)
        for _, row in top_docs.iterrows():
            f.write(
                f"• {row['filename']}: {row['neoliberalism_mentions']} mentions\n")

        # Documents with most critique content
        f.write("\nDOCUMENTS WITH MOST CRITIQUE CONTENT:\n")
        critique_docs = df.sort_values(
            "critique_mentions", ascending=False).head(10)
        for _, row in critique_docs.iterrows():
            f.write(
                f"• {row['filename']}: {row['critique_mentions']} critique-related terms\n")

    print(
        f"Analysis complete. Results saved to {output_file} and neoliberalism_summary.txt")
    return df


# Usage
if __name__ == "__main__":
    df = process_neoliberalism_pdfs("Documentation+KB")
