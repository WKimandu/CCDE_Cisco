#!/bin/bash

# Bash script to transcribe Cisco Live session videos one by one
echo -e "\e[32mTranscribing Cisco Live session videos one by one...\e[0m"

# Activate the conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate CCDE_Cisco

# Get all MP4 files in the current directory
VIDEO_FILES=(*.mp4)

echo -e "\e[36mFound ${#VIDEO_FILES[@]} video files to transcribe\e[0m"

# Output directory
OUTPUT_DIR="transcripts"
mkdir -p "$OUTPUT_DIR"

# Process each video file one by one
for video in "${VIDEO_FILES[@]}"; do
    echo -e "\e[33mStarting transcription of $video...\e[0m"
    
    # Run the direct_whisper.py script for this video 
    # Using the large model for better accuracy
    python direct_whisper.py "$video" --output_dir "$OUTPUT_DIR" --model large
    
    echo -e "\e[32mCompleted transcription of $video\e[0m"
    echo -e "\e[90m-----------------------------------------------------\e[0m"
done

echo -e "\e[32mAll transcriptions complete! Check the transcripts directory for results.\e[0m"
echo "Press Enter to exit"
read 