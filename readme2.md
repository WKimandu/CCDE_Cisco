# CCDE Certification Study Plan Generator

This tool automatically processes Cisco CCDE certification PDFs and generates a comprehensive study plan focused on key areas including AI Infrastructure, On-Prem Services, Cloud Services, Large Scale Networks, and Workforce Mobility.

## Features

- Extracts and analyzes content from CCDE certification PDF files
- Identifies key topics and technologies across all documents
- Categorizes content into focused study areas
- Generates a weekly study plan based on topic importance
- Creates both JSON and Markdown versions of the study plan
- Preserves extracted content for reference

## Requirements

- Python 3.6+
- Required Python packages:
  - pdfplumber
  - pandas
  - tqdm
  - textwrap
  - pathlib

## Installation

1. Ensure you have Python 3.6 or newer installed
2. Install required dependencies:
   ```
   pip install pdfplumber pandas tqdm
   ```
3. Place the CCDE PDF files in the same directory as the script

## Usage

1. Place all CCDE certification PDF files in the same directory as the script
2. Run the script:
   ```
   python ccde_study_plan.py
   ```
3. The script will create a `ccde_study_materials` directory containing:
   - Extracted text from each PDF
   - JSON files with exam topics and technologies
   - A topic analysis summary
   - The complete study plan in both JSON and Markdown formats

## Output Structure

- `ccde_study_materials/`: Main output directory
  - `CCDE_Study_Plan.md`: Comprehensive study plan in Markdown format
  - `ccde_study_plan.json`: Structured data version of the study plan
  - `exam_topics.json`: Extracted exam topics
  - `topic_analysis.json`: Analysis of key topic frequencies
  - `*_text.txt`: Extracted text from each PDF file
  - `*_technologies.json`: Technology lists extracted from each technology list document

## How It Works

The script follows these steps:
1. Extracts text from all CCDE PDF files
2. Identifies exam topics from the unified exam topics document
3. Extracts technology lists from technology list documents
4. Analyzes content to identify key topics related to AI, On-Prem, Cloud, etc.
5. Categorizes all content into focus areas
6. Creates a weekly study plan based on topic importance
7. Generates both JSON and Markdown outputs

## Customization

You can customize the script by:
- Modifying the `focus_areas` list to change study areas
- Adjusting the `topic_patterns` dictionary to search for different keywords
- Changing the weekly study load by modifying the topics per week threshold
- Editing the output directory by changing the `output_dir` parameter

## Troubleshooting

If you encounter issues:
- Ensure all PDF files are in the same directory as the script
- Check that you have installed all required dependencies
- Verify that the PDF files are not password protected
- For large PDFs, be patient as text extraction can take time 