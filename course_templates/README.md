# CCDE Course Development Guide

This guide explains the process and standards for developing course content for the CCDE Study System.

## Course Structure

The CCDE course is organized into modules covering the key technology domains:

1. **AI Infrastructure**: Networking for AI/ML workloads
2. **ACI & Data Center**: Cisco ACI architecture and design
3. **DevOps & Automation**: Network automation and programmability
4. **Cloud & Hybrid Services**: Multi-cloud networking
5. **Container Networking**: Kubernetes and container connectivity
6. **Large-Scale Networks**: Enterprise and service provider design
7. **Workforce Mobility**: Remote access and campus design

## Module Types

Modules are categorized into three types:

1. **Foundational**: Core concepts and terminology
2. **Design Principles**: Best practices and architectural approaches
3. **Implementation**: Technical details and deployment considerations

## Development Process

### 1. Module Planning

1. Review CCDE exam topics relevant to the module
2. Identify learning objectives using Bloom's Taxonomy
3. Outline key concepts and practical exercises
4. Define prerequisite knowledge and module dependencies

### 2. Content Creation

1. Develop content following the module template structure
2. Include knowledge checks after each key concept
3. Create practical scenarios that apply theoretical knowledge
4. Design assessment questions of increasing complexity

### 3. AI-Assisted Development

1. Use the transcript knowledge base to identify real-world examples
2. Leverage LlamaIndex for content retrieval and organization
3. Generate initial drafts using AI assistance
4. Validate technical accuracy against authoritative sources

### 4. Review and Refinement

1. Technical review by subject matter experts
2. Instructional design review for learning effectiveness
3. Content refinement based on feedback
4. Creation of supplementary materials (diagrams, cheat sheets)

### 5. Integration and Publication

1. Add module to the course structure
2. Update cross-references and learning paths
3. Create module metadata for search and discovery
4. Publish to the learning environment

## Templates and Examples

This directory contains templates and examples for course development:

- **module_template.md**: Standard template for course modules
- **sample_module-ACI_Multi_Site.md**: Example module showing the expected structure and depth
- **assessment_template.md**: Template for standalone assessments
- **learning_path_template.md**: Template for defining learning sequences

## Instructional Design Principles

### Bloom's Taxonomy

Modules should include learning objectives at multiple cognitive levels:

1. **Remember/Understand**: Define, describe, identify
2. **Apply/Analyze**: Implement, differentiate, troubleshoot
3. **Evaluate/Create**: Design, optimize, develop

### Microlearning

- Break complex topics into digestible units
- Target 15-30 minutes per module
- Include frequent knowledge checks
- Use progressive disclosure for complex concepts

### Scaffolded Learning

- Build complexity gradually
- Provide guided practice before independent application
- Include worked examples with explanations
- Offer varying levels of assistance based on difficulty

## Quality Benchmarks

All modules should meet these quality criteria:

- **Technical Accuracy**: Validated against Cisco documentation
- **Instructional Effectiveness**: Clear structure and examples
- **Practical Relevance**: Real-world scenarios and applications
- **Assessment Alignment**: Questions match learning objectives
- **Engagement**: Interactive elements and varied content types

## Getting Started

1. Review the [`PROJECT_RULES.md`](../PROJECT_RULES.md) document for course development guidelines
2. Examine the module template and sample module
3. Select a topic from the development roadmap
4. Create a new module using the template as a foundation
5. Follow the development process outlined above 