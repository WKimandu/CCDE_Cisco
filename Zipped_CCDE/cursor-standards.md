# Cursor AI Rules for CCDE Project

## Primary Objectives

These rules define how Cursor AI should assist with the CCDE Study System project, ensuring consistency, accuracy, and alignment with project goals.

## Environment Verification

For each new session, Cursor AI should:

1. **Verify Working Directory**: Check that the current working directory is `C:\Users\kiman\Documents\GitHub\CCDE_Cisco`

2. **Check Conda Environment**: Verify that the user is in the `CCDE_Cisco` Conda environment
   - If not in the correct environment, suggest activating it with `conda activate CCDE_Cisco`
   - This verification must be the first action in any development session

3. **Monitor Environment Dependencies**: When suggesting new code that requires additional packages, ensure they're compatible with the existing Conda environment and suggest appropriate installation commands

## General Guidelines

1. **Documentation First**: Always review relevant documentation (PRD, README files, implementation plans) before providing assistance with any component of the project.

2. **Modular Focus**: When working on code or documentation, stay within the scope of the specific module (NLP, transcript processing, study system). Avoid making changes that affect multiple systems without explicit authorization.

3. **Implementation Consistency**: Follow existing patterns and conventions in the codebase. Maintain consistent coding style, naming conventions, and architectural approaches.

4. **Documentation Updates**: When implementing significant changes, ensure documentation is updated to reflect those changes, including:
   - README files
   - Implementation plans
   - API documentation
   - Code comments

5. **Technology Constraints**: Only suggest or implement technologies explicitly mentioned in the project documentation (LlamaIndex, LangChain, SpaCy, etc.). Avoid introducing new dependencies without clear justification.

## Course Development Assistance

When assisting with course development, Cursor AI should:

1. **Learning Objective Formulation**:
   - Follow Bloom's Taxonomy (Remember, Understand, Apply, Analyze, Evaluate, Create)
   - Ensure objectives are measurable and aligned with CCDE exam requirements
   - Match difficulty level to the target audience (beginner, intermediate, advanced)

2. **Content Structure**:
   - Organize material into logical learning sequences
   - Break complex topics into digestible modules (15-30 minute completion time)
   - Include both theoretical foundations and practical applications
   - Maintain progressive difficulty throughout learning paths

3. **Assessment Generation**:
   - Create knowledge checks aligned with learning objectives
   - Develop multiple question types (multiple choice, scenario-based, design exercises)
   - Include detailed answer explanations that reinforce key concepts
   - Design practical exercises that apply theoretical knowledge

4. **Case Study Development**:
   - Base case studies on realistic network design scenarios
   - Include business requirements and technical constraints
   - Provide multiple solution options with trade-offs
   - Create scaffolded exercises for different skill levels

5. **Content Enhancement**:
   - Suggest visual aids for complex concepts (diagrams, flowcharts)
   - Include relevant real-world examples from transcripts
   - Recommend supplementary materials (cheat sheets, reference guides)
   - Ensure terminology consistency throughout materials

## Specific Rules by Component

### 1. Transcript Processing Pipeline

- Preserve original transcript data during transformations
- Maintain both raw (.txt) and timestamped (.tsv) formats
- Follow the multi-stage processing workflow (cleaning, enhancement, enrichment, metadata extraction)
- Use consistent naming conventions for processed files

### 2. NLP Implementation

- Follow the 12-week implementation plan when developing NLP components
- Implement domain-specific NER using SpaCy as specified
- Use the sentence-transformers framework for embeddings
- Follow chunking strategies defined in the knowledge base enhancement plan
- Implement vector storage using Chroma or Qdrant as specified

### 3. Study System Generation

- Organize content by CCDE technology domains
- Maintain alignment with official CCDE exam topics
- Structure content in progressive difficulty levels
- Include estimated completion times for study modules
- Preserve metadata relationships (prerequisites, dependencies)

### 4. Code Quality Standards

- Include error handling in all data processing functions
- Add logging for critical operations
- Write unit tests for core functionality
- Ensure backward compatibility when modifying existing functions
- Document API endpoints and parameters

### 5. Data Management

- Follow established data transformation patterns
- Preserve original source data
- Include data provenance information in processed outputs
- Implement incremental processing where possible
- Add versioning to generated knowledge bases

## AI-Assisted Operations

### 1. Code Generation

When generating code, Cursor AI should:
- Create complete, working solutions (not code snippets)
- Include all necessary imports
- Add appropriate error handling
- Follow project-specific naming conventions
- Include docstrings and type hints
- Consider performance implications for large data operations

### 2. Documentation Generation

When generating documentation, Cursor AI should:
- Use consistent Markdown formatting
- Include relevant code examples
- Explain complex concepts with appropriate technical depth
- Add diagrams or visualization descriptions where helpful
- Include references to related components

### 3. Troubleshooting

When helping troubleshoot issues, Cursor AI should:
- Analyze log output and error messages
- Check for common issues in similar systems
- Provide explanations, not just solutions
- Document the solution process for similar future issues
- Suggest preventative measures when appropriate

### 4. Architecture Recommendations

When making architectural recommendations, Cursor AI should:
- Consider scalability requirements
- Evaluate consistency with existing architecture
- Assess impact on related systems
- Provide clear rationale for recommendations
- Include alternatives and trade-offs

## Project-Specific Knowledge

Cursor AI should maintain awareness of:

1. **CCDE Domains**: AI Infrastructure, ACI & Data Center, DevOps & Automation, Cloud Services, Container Networking, Large-Scale Networks, Workforce Mobility

2. **Documentation Structure**:
   - Study materials organized by technology domain
   - Implementation plans for NLP and knowledge base components
   - Transcript processing workflows
   - Data transformation patterns

3. **Implementation Timeline**:
   - Follow phase-based approach defined in documentation
   - Recognize dependencies between components
   - Prioritize foundation elements before advanced features

## Continuous Improvement

These rules should be periodically reviewed and updated as the project evolves. As new components are added or existing ones are modified, the rules should be expanded to cover new scenarios and use cases.
