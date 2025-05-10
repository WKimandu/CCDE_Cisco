# CCDE Cisco Repository Structure

This document outlines the recommended structure for the CCDE Cisco Knowledge Base repository.

## Directory Structure

```
CCDE_Cisco/
├── docs/
│   ├── certification_guides/    # Certification-related documents
│   ├── exam_topics/             # CCDE exam topics and guidelines
│   ├── technology_lists/        # Technology lists for different CCDE domains
│   └── notes/                   # Study notes and summaries
│
├── scripts/
│   ├── transcription/           # Scripts for video transcription
│   ├── processing/              # Scripts for processing and analyzing content
│   └── utilities/               # Utility scripts
│
├── transcripts/
│   ├── cisco_live/              # Transcripts from Cisco Live sessions
│   ├── devnet/                  # Transcripts from DevNet sessions
│   └── cisco_university/        # Transcripts from Cisco University content
│
├── resources/
│   ├── aci/                     # ACI-related resources (references only, not PDFs)
│   ├── networking/              # General networking resources
│   └── ai_infrastructure/       # AI infrastructure resources
│
└── tools/                       # Tools for working with the repository
```

## File Organization Guidelines

1. **Documentation Files**
   - Use Markdown (.md) for all documentation
   - Follow consistent naming conventions (lowercase, hyphens for spaces)
   - Include appropriate metadata and tags

2. **Script Files**
   - Include header comments explaining purpose and usage
   - Follow PEP 8 style guide for Python code
   - Keep functions modular and reusable

3. **Transcripts**
   - Use consistent naming format: `[EVENT_CODE]-[SESSION_NAME].md`
   - Include metadata section at the top with source information
   - Organize by event type/source

4. **Git Rules**
   - Do not commit large binary files (PDFs, videos, etc.)
   - Keep commits atomic (one logical change per commit)
   - Write meaningful commit messages

## Implementation Steps

1. Create the directory structure
2. Move files to appropriate locations
3. Update references in documentation
4. Ensure .gitignore excludes large files and sensitive data
5. Update README.md to reflect new structure
