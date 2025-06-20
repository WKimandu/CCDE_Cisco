import os
import re


def clean_text_files(directory):
    """Remove copyright and page number lines from extracted text files."""
    # Lines to remove - patterns in regex format
    patterns_to_remove = [
        r'^\d{4} Cisco Systems, Inc\. This document is Cisco Public\. Page \d+$',
        r'^- *$',  # Dash lines often used as separators
        r'^2024 Cisco Systems, Inc\. This document is Cisco Public\. \d{2,4} Page \d+$',
        r'^Cisco Systems, Inc\. This document is Cisco Public\. Page \d+$'
    ]

    # Get all text files in the directory
    text_files = [f for f in os.listdir(directory) if f.endswith('_text.txt')]

    for filename in text_files:
        filepath = os.path.join(directory, filename)
        print(f"Cleaning {filename}...")

        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Filter out the lines matching any of the patterns
        filtered_lines = []
        removed_count = 0

        for line in lines:
            line_stripped = line.strip()
            should_remove = False

            for pattern in patterns_to_remove:
                if re.match(pattern, line_stripped):
                    should_remove = True
                    removed_count += 1
                    break

            if not should_remove:
                filtered_lines.append(line)

        # Write the cleaned content back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(filtered_lines)

        print(f"  Removed {removed_count} lines")

    print(f"Cleaned {len(text_files)} files")


if __name__ == "__main__":
    clean_text_files("ccde_study_materials")
