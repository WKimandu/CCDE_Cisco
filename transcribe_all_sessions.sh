#!/bin/bash

# transcribe_all_sessions.sh - Linux equivalent of transcribe_all_sessions.bat
# Purpose: Transcribe all video files listed in video_queue.txt

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
REPO_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
QUEUE_FILE="$REPO_ROOT/video_queue.txt"
TRANSCRIPTS_DIR="$REPO_ROOT/transcripts"

# Check if video_queue.txt exists
if [ ! -f "$QUEUE_FILE" ]; then
    echo "Error: video_queue.txt not found at $QUEUE_FILE"
    exit 1
fi

# Ensure transcripts directory exists
mkdir -p "$TRANSCRIPTS_DIR"

echo "Starting batch transcription process..."
echo "Reading video paths from $QUEUE_FILE"
echo "Transcripts will be saved to $TRANSCRIPTS_DIR"

# Count total videos
TOTAL_VIDEOS=$(grep -v '^#' "$QUEUE_FILE" | grep -v '^$' | wc -l)
echo "Found $TOTAL_VIDEOS videos to process"

# Process each video file
COUNT=0
while IFS= read -r line || [ -n "$line" ]; do
    # Skip empty lines and comments
    if [[ -z "$line" || "$line" == \#* ]]; then
        continue
    fi
    
    COUNT=$((COUNT + 1))
    echo "Processing video $COUNT/$TOTAL_VIDEOS: $line"
    
    # Call the single transcription script
    bash "$SCRIPT_DIR/transcribe_session.sh" "$line" "$TRANSCRIPTS_DIR"
    
    # Check the result
    if [ $? -ne 0 ]; then
        echo "Warning: Transcription failed for $line"
    else
        echo "Completed video $COUNT/$TOTAL_VIDEOS"
    fi
    
    echo "---------------------------------------------------"
done < "$QUEUE_FILE"

echo "Batch transcription process completed!"
echo "$COUNT out of $TOTAL_VIDEOS videos processed." 