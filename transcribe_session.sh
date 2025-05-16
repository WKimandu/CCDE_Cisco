#!/bin/bash

# transcribe_session.sh - Linux equivalent of transcribe_session.bat
# Purpose: Transcribe a single video file using OpenAI Whisper

# Check if argument is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <video_file_path> [output_dir]"
    exit 1
fi

# Get the video file path
VIDEO_PATH="$1"
# Get base file name without extension
FILE_NAME=$(basename "$VIDEO_PATH")
FILE_BASE="${FILE_NAME%.*}"

# Set output directory (default to transcripts if not specified)
OUTPUT_DIR="${2:-../../transcripts}"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Set the output file path
OUTPUT_FILE="$OUTPUT_DIR/${FILE_BASE}.md"

echo "Transcribing $VIDEO_PATH to $OUTPUT_FILE..."

# Activate Conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate CCDE_Cisco

# Start the transcription
whisper "$VIDEO_PATH" --model medium --language en --output_dir "$OUTPUT_DIR" --output_format txt

# If the output file exists, convert it to markdown and add metadata
if [ -f "$OUTPUT_DIR/${FILE_BASE}.txt" ]; then
    # Create markdown file with metadata
    echo "# $FILE_BASE Transcript" > "$OUTPUT_FILE"
    echo "Generated on: $(date)" >> "$OUTPUT_FILE"
    echo "Source: $VIDEO_PATH" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "## Content" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # Append the transcript content
    cat "$OUTPUT_DIR/${FILE_BASE}.txt" >> "$OUTPUT_FILE"
    
    # Remove the txt file if successful
    rm "$OUTPUT_DIR/${FILE_BASE}.txt"
    echo "Transcription completed and saved to $OUTPUT_FILE"
else
    echo "Error: Transcription failed or output file not found."
    exit 1
fi

echo "Done!" 