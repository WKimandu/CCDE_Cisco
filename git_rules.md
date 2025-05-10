# Git Rules and Best Practices

## Purpose

This document outlines the essential rules and best practices for managing this repository using Git (GitHub, GitLab, etc.). The goal is to ensure only relevant files are tracked, versioned, and pushed to the remote repository, supporting collaborative and efficient development.

## What to Track and Push

- **Track and push:**
  - Markdown files (README, project rules, documentation, etc.)
  - Project rules, PRD, and instructions
  - Scripts and code relevant to the project
- **Never track or push:**
  - Large binary files (PDFs, PowerPoint, audio, video, raw data, etc.)
  - Any files not necessary for collaboration or public review

## Why These Rules Matter

Pushing large or unnecessary files (e.g., MP4, PDF, raw data) can:
- Cause push failures due to size limits
- Slow down repository operations
- Expose sensitive or irrelevant data

## .gitignore Usage

- Always maintain an up-to-date `.gitignore` file
- Exclude all large, binary, or sensitive files
- Example entries:
  ```
  *.mp4
  *.pdf
  *.pptx
  *.zip
  *.raw
  ```

## Workflow

1. **Read Documentation First**
   - Always review the PRD, README, and project rules before making changes.
2. **Add Only Relevant Files**
   - Stage only files needed for collaboration and review.
3. **Atomic Commits**
   - Make one logical change per commit with a clear message.
4. **Branching and Collaboration**
   - Use branches for features, fixes, or experiments.
   - Submit pull requests for review and feedback.
5. **Human-in-the-Loop**
   - If unsure, seek approval before pushing or merging.

## Future Directions

- This repository will serve as a foundation for AI-driven, platform-oriented workflows.
- Future work will include development environments, pipelines, and advanced NLP tools (LlamaIndex, LangChain, spaCy, etc.).
- The goal is to enable collaborative, scalable, and intelligent knowledge management.

## Key Principles (Summary)

- **Never push large or irrelevant files**
- **Keep the repository clean and focused**
- **Collaborate and review before major changes**
- **Document everything clearly**

