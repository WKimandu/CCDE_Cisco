---
title: Comprehensive Cursor Rules for CCDE Cisco Project
date_created: 2025-01-27
last_updated: 2025-01-27
status: Complete
version: 2.0
contributors: [WKimandu]
categories: [Guidelines, Cursor AI, Development Rules]
tags: [cursor-ai, development-rules, gitops, ccde, ai-powered-learning]
related_documents:
  - ../infrastructure/gitops-implementation.md
  - ../project-status-report.md
  - ../architecture/system-architecture.md
  - ../specifications/product-requirements.md
---

# Comprehensive Cursor Rules for CCDE Cisco Project

## Executive Summary

These comprehensive rules define how Cursor AI should assist with the CCDE Cisco Knowledge Base project, ensuring consistency, accuracy, and alignment with the AI-powered learning platform goals. The rules integrate GitOps practices, multi-environment development, and educational technology principles.

## Project Context

### 🎯 Project Mission
Create a comprehensive, AI-powered study system for CCDE certification that organizes materials into logical learning paths, implements advanced document analysis, and provides an adaptive learning environment with modern DevOps practices.

### 🏗️ Architecture Overview
- **7-Layer System**: Document ingestion, content extraction, knowledge processing, storage, retrieval, application, and interface layers
- **AI/ML Foundation**: LlamaIndex, LangChain, OpenAI embeddings, RAG systems
- **Multi-Environment Support**: Windows 11 and Ubuntu Server development environments
- **Dual Repository Strategy**: GitHub (collaboration) and Synology NAS (backup)

## Environment Verification (CRITICAL)

### Mandatory Session Start Protocol
For each new session, Cursor AI MUST:

1. **Verify Working Directory**: Confirm current directory is `C:\Users\kiman\Documents\GitHub\CCDE_Cisco`
2. **Check Conda Environment**: Verify `CCDE_Cisco` environment is active
   ```bash
   conda activate CCDE_Cisco
   ```
3. **Validate Git Status**: Check current branch and working tree status
4. **Confirm Remote Access**: Verify connectivity to both origin (GitHub) and synology (NAS)

### Environment Dependencies
- **Python 3.10+**: Primary development language
- **Conda Environment**: `CCDE_Cisco` with all dependencies
- **Git Configuration**: Dual remote setup (origin + synology)
- **IDE Support**: VS Code with Python extensions preferred

## Core Development Principles

### 1. Documentation-First Approach
- **Always review** relevant documentation before making changes
- **Update documentation** when implementing significant changes
- **Follow metadata standards** for all new documentation
- **Maintain cross-references** between related documents

### 2. GitOps Integration
- **Multi-environment compatibility**: Ensure code works on both Windows and Ubuntu
- **Pre-commit validation**: Respect existing git hooks and quality checks
- **Branch strategy**: Follow established branching model
- **Dual remote synchronization**: Consider both GitHub and Synology remotes

### 3. AI-Powered Learning Focus
- **Educational value**: Every feature should enhance learning outcomes
- **CCDE alignment**: Maintain focus on CCDE v3.1 certification requirements
- **Knowledge base integration**: Leverage existing AI/ML capabilities
- **Practical application**: Bridge theoretical knowledge with real-world scenarios

## Technology Stack Constraints

### Approved Technologies
- **Core Framework**: LlamaIndex 0.9.x for document processing and RAG
- **AI/ML**: LangChain, OpenAI API, spaCy, sentence-transformers
- **Vector Databases**: ChromaDB, Qdrant, FAISS
- **Document Processing**: PyMuPDF, python-pptx, python-docx, markdown-it-py
- **Development**: Python 3.10+, Conda, Git, VS Code

### Technology Selection Rules
- **Prefer existing technologies** over introducing new dependencies
- **Justify new technologies** with clear business requirements
- **Consider performance implications** for large document processing
- **Maintain compatibility** with multi-environment setup

## CCDE Domain Knowledge

### Core Technology Domains
1. **AI Infrastructure**: AI/ML integration with networking technologies
2. **ACI & Data Center**: Cisco ACI comprehensive design and implementation
3. **DevOps & Automation**: Infrastructure as Code and CI/CD practices
4. **Cloud & Hybrid Services**: Multi-cloud and hybrid cloud solutions
5. **Large-Scale Networks**: Enterprise networking design principles
6. **Workforce Mobility**: Mobile and remote access solutions

### Practical Electives
- **AI Infrastructure**: Advanced AI/ML networking applications
- **On-Premises and Cloud Services**: Hybrid infrastructure design
- **Large-Scale Networks**: Enterprise-scale network architecture
- **Workforce Mobility**: Mobile workforce infrastructure

## Code Development Guidelines

### 1. Python Development Standards
```python
# Required imports for new modules
import os
import logging
from typing import List, Optional, Union
from pathlib import Path

# Environment-aware path handling
def get_project_root() -> Path:
    """Get project root path based on environment."""
    if os.name == 'nt':  # Windows
        return Path(r"C:\Users\kiman\Documents\GitHub\CCDE_Cisco")
    else:  # Unix/Linux
        return Path("/home/kimanduw/Documents/CCDE_Cisco")

# Comprehensive error handling
def process_documents(directory: Path) -> List[Document]:
    """Process documents with proper error handling."""
    try:
        # Implementation
        pass
    except FileNotFoundError as e:
        logging.error(f"Directory not found: {directory}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise
```

### 2. Documentation Standards
- **Docstrings**: All functions and classes must have comprehensive docstrings
- **Type hints**: Use type hints for all function parameters and return values
- **Examples**: Include usage examples for complex functions
- **Error handling**: Document exceptions and edge cases

### 3. Testing Requirements
- **Unit tests**: Write tests for all core functionality
- **Integration tests**: Test component interactions
- **Test coverage**: Maintain >80% coverage for core modules
- **Test documentation**: Document test procedures and expected outcomes

## GitOps Workflow Integration

### Branch Strategy
- **main**: Production-ready code (requires PR review)
- **develop**: Integration branch for feature work
- **feature/name**: Feature-specific branches
- **env/windows**: Windows-specific changes
- **env/ubuntu**: Ubuntu-specific changes
- **gitops-learning**: Current experimental branch

### Pre-Commit Hook Compliance
- **Path validation**: No hardcoded Windows/Unix paths
- **File size checks**: Warn about large files (>1MB)
- **Line ending consistency**: Ensure proper line endings
- **Environment variables**: Use env files for path configuration

### Synchronization Protocol
1. **Before ending session**: Push completed work to both remotes
2. **Before starting work**: Pull latest changes from origin
3. **New branches**: Set upstream tracking immediately
4. **Conflict resolution**: Follow established strategies

## AI-Powered Learning Development

### 1. Knowledge Base Enhancement
- **Content processing**: Follow established document processing pipeline
- **Vector storage**: Use appropriate vector database for content type
- **Query optimization**: Ensure fast and accurate retrieval
- **Metadata preservation**: Maintain source attribution and relationships

### 2. Learning Path Development
- **Bloom's Taxonomy**: Structure content by cognitive levels
- **Progressive difficulty**: Build from basic to advanced concepts
- **Practical application**: Include real-world scenarios and case studies
- **Assessment integration**: Create knowledge checks and practice exercises

### 3. Educational Technology Integration
- **Adaptive learning**: Implement personalized learning paths
- **Progress tracking**: Monitor user progress and learning outcomes
- **Collaborative features**: Support group study and peer review
- **Analytics**: Provide insights into learning effectiveness

## Quality Assurance Standards

### 1. Code Quality
- **Static analysis**: Run pylint, flake8, mypy
- **Code formatting**: Use black for consistent formatting
- **Complexity monitoring**: Maintain reasonable cyclomatic complexity
- **Security review**: Regular dependency updates and security audits

### 2. Documentation Quality
- **Metadata compliance**: Follow established metadata standards
- **Cross-referencing**: Maintain links between related documents
- **Version control**: Track documentation changes and updates
- **Accessibility**: Ensure documentation is clear and accessible

### 3. System Quality
- **Performance monitoring**: Track response times and throughput
- **Error handling**: Comprehensive error logging and recovery
- **Scalability**: Design for growth and increased usage
- **Reliability**: Ensure system stability and uptime

## Troubleshooting and Support

### 1. Common Issues
- **Environment setup**: Verify conda environment and dependencies
- **Git synchronization**: Check remote connectivity and branch status
- **Path issues**: Use environment variables instead of hardcoded paths
- **Performance problems**: Monitor resource usage and optimize accordingly

### 2. Debugging Guidelines
- **Log analysis**: Review logs for error patterns and root causes
- **Environment validation**: Confirm all dependencies and configurations
- **Step-by-step testing**: Isolate issues through systematic testing
- **Documentation review**: Check relevant documentation for solutions

### 3. Support Resources
- **Project documentation**: Comprehensive guides in docs/ directory
- **GitOps implementation**: Detailed workflow documentation
- **Architecture documentation**: System design and component relationships
- **External resources**: Cisco documentation and community resources

## Project-Specific Knowledge

### Current Implementation Status
- **Core Infrastructure**: Document processing pipeline and vector store implementation
- **GitOps Implementation**: Multi-environment development with automated quality checks
- **Documentation System**: Comprehensive documentation with metadata standards
- **Content Repository**: CCDE v3.1 materials and learning objectives

### Key Achievements
- ✅ **Comprehensive Architecture**: 7-layer system design with clear separation of concerns
- ✅ **GitOps Implementation**: Multi-environment development with automated quality assurance
- ✅ **AI-Powered Learning**: Advanced RAG capabilities with semantic search
- ✅ **Content Organization**: Structured learning materials aligned with CCDE requirements
- ✅ **Documentation Standards**: Professional-grade documentation with metadata management

### Future Roadmap
- **Phase 1**: Complete learning management system implementation
- **Phase 2**: Deploy frontend interface for user interaction
- **Phase 3**: Implement comprehensive testing and CI/CD pipeline
- **Phase 4**: Scale to production environment with monitoring

## Continuous Improvement

### Rule Updates
- **Periodic review**: Update rules based on project evolution
- **Feedback integration**: Incorporate lessons learned from development
- **Technology updates**: Adapt to new technologies and best practices
- **Team input**: Consider feedback from all project contributors

### Learning Integration
- **Best practices**: Document and share successful patterns
- **Lessons learned**: Capture insights from challenges and solutions
- **Knowledge sharing**: Promote collaboration and knowledge transfer
- **Process improvement**: Continuously refine development workflows

## Conclusion

These comprehensive cursor rules provide a foundation for consistent, high-quality development of the CCDE Cisco Knowledge Base project. By following these guidelines, Cursor AI can effectively support the project's mission to create an AI-powered learning platform that demonstrates modern DevOps practices while serving as a practical example of educational technology innovation.

The rules emphasize the integration of GitOps principles, AI/ML technologies, and educational best practices, ensuring that every contribution aligns with the project's goals and maintains the high standards required for a professional-grade learning platform. 