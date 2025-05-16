#!/bin/bash

# transcribe_one_by_one.sh - Linux equivalent of transcribe_one_by_one.bat
# Purpose: Process a directory of video files one by one

# Check if argument is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <video_directory> [output_directory]"
    exit 1
fi

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VIDEO_DIR="$1"
OUTPUT_DIR="${2:-../../transcripts}"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

echo "Starting processing of all videos in directory: $VIDEO_DIR"
echo "Transcripts will be saved to: $OUTPUT_DIR"

# Find all video files in the directory
VIDEO_FILES=()
for ext in mp4 mkv avi mov wmv flv webm; do
    while IFS= read -r file; do
        VIDEO_FILES+=("$file")
    done < <(find "$VIDEO_DIR" -type f -name "*.$ext" -print)
done

# Count total videos
TOTAL_VIDEOS=${#VIDEO_FILES[@]}
echo "Found $TOTAL_VIDEOS videos to process"

# Process each video file
COUNT=0
for video in "${VIDEO_FILES[@]}"; do
    COUNT=$((COUNT + 1))
    echo "Processing video $COUNT/$TOTAL_VIDEOS: $video"
    
    # Call the single transcription script
    bash "$SCRIPT_DIR/transcribe_session.sh" "$video" "$OUTPUT_DIR"
    
    # Check the result
    if [ $? -ne 0 ]; then
        echo "Warning: Transcription failed for $video"
    else
        echo "Completed video $COUNT/$TOTAL_VIDEOS"
    fi
    
    echo "---------------------------------------------------"
done

echo "Batch transcription process completed!"
echo "$COUNT out of $TOTAL_VIDEOS videos processed." 