import os
import sys
import argparse


def generate_txt_from_tsv(tsv_file_path):
    """Generate a text file from a TSV file containing transcription data."""
    if not os.path.exists(tsv_file_path):
        print(f"Error: TSV file not found: {tsv_file_path}")
        return False

    # Get output file path
    txt_file_path = os.path.splitext(tsv_file_path)[0] + ".txt"

    print(f"Converting {tsv_file_path} to {txt_file_path}...")

    try:
        with open(tsv_file_path, 'r', encoding='utf-8') as tsv_file:
            lines = tsv_file.readlines()

        if len(lines) <= 1:
            print("Error: TSV file is empty or contains only headers")
            return False

        # Skip the header line
        data_lines = lines[1:]

        # Look for the word timestamps section
        word_section_start = -1
        for i, line in enumerate(data_lines):
            if "# Word-level timestamps" in line:
                word_section_start = i
                break

        # If word timestamps exist, only use the segment part
        if word_section_start != -1:
            data_lines = data_lines[:word_section_start]

        # Extract text from each line and write to text file
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            for line in data_lines:
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    txt_file.write(parts[2] + ' ')

        print(f"Successfully created {txt_file_path}")
        print(f"File size: {os.path.getsize(txt_file_path) / 1024:.2f} KB")
        return True

    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate text file from TSV transcription file")
    parser.add_argument("tsv_file", help="Path to the TSV file to convert")

    args = parser.parse_args()

    # If path is relative, make it absolute
    tsv_path = os.path.abspath(args.tsv_file)

    if generate_txt_from_tsv(tsv_path):
        print("Conversion completed successfully")
    else:
        print("Conversion failed")


if __name__ == "__main__":
    main()
