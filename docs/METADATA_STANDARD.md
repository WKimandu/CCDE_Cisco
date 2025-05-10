# Documentation Metadata Standard

This document defines the standard metadata format for all documentation files in the CCDE Cisco Knowledge Base project.

## Purpose

Consistent metadata enables better organization, searchability, and maintenance of documentation. Following this standard ensures that all documentation can be properly indexed, tracked, and updated.

## Metadata Format

All documentation files should include a YAML front matter block at the beginning of the file, enclosed by triple dashes (`---`):

```markdown
---
title: Document Title
date_created: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: [Draft|Review|Complete|Archived]
version: 1.0
contributors: [Name1, Name2]
categories: [Category1, Category2]
tags: [Tag1, Tag2, Tag3]
related_documents: 
  - path/to/related-doc1.md
  - path/to/related-doc2.md
---

# Document Title

Document content starts here...
```

## Required Fields

- **title**: The full title of the document (should match the H1 heading)
- **date_created**: When the document was first created (YYYY-MM-DD format)
- **last_updated**: When the document was last substantively changed (YYYY-MM-DD format)
- **status**: Current status of the document

## Optional Fields

- **version**: Version number of the document
- **contributors**: List of contributors to the document
- **categories**: Broad categories the document belongs to
- **tags**: Specific topics covered in the document
- **related_documents**: Relative paths to related documents in the repository

## Status Values

- **Draft**: Initial version, still being actively developed
- **Review**: Complete enough for review by others
- **Complete**: Reviewed and approved
- **Archived**: No longer actively maintained but kept for reference

## Implementation

1. Add this metadata block to the top of all new documentation
2. Gradually update existing documentation to include this metadata
3. Use automated validation to ensure compliance with the standard

## Example

```markdown
---
title: CCDE Study Plan
date_created: 2025-05-10
last_updated: 2025-05-10
status: Draft
version: 0.1
contributors: [John Doe, Jane Smith]
categories: [Study Materials, CCDE]
tags: [Study Plan, v3.1, Certification]
related_documents:
  - ../exam_topics/ccde-v3.1-topics.md
  - ../certification_guides/practical-exam-guide.md
---

# CCDE Study Plan

This document provides a comprehensive study plan for the CCDE certification...
``` 