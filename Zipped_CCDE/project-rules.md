# CCDE Project: Development and Management Rules

## Core Principles

1. **Clarity**: All code, documentation, and communications should be clear and understandable.
2. **Consistency**: Maintain consistent approaches throughout the project.
3. **Modularity**: Design components that are loosely coupled but highly cohesive.
4. **Documentation**: Document all significant decisions, components, and processes.
5. **Testing**: Test thoroughly before integrating any new component.

## Environment Setup

### Conda Environment

- **Always check** the current working directory is `C:\Users\kiman\Documents\GitHub\CCDE_Cisco`
- **Always verify** you're using the `CCDE_Cisco` Conda environment
- If not in the correct environment, activate it with `conda activate CCDE_Cisco`
- Environment verification should be the first step of any development session
- All dependencies must be installed within this environment using `conda install` or `pip install`
- Document any new dependencies by updating `requirements.txt`

### Development Environment

- VSCode with Python extensions is the preferred IDE
- Use Cursor AI for code assistance when appropriate
- Configure linters according to project standards
- Set up pre-commit hooks for code quality checks
- Keep environment configurations synchronized across team members

## Course Development Guidelines

### 1. Instructional Design

- Follow Bloom's Taxonomy for learning objective development
- Structure content in progressive difficulty levels (beginner → intermediate → advanced)
- Include both theoretical knowledge and practical application
- Create assessments aligned with learning objectives
- Develop case studies based on real-world network design scenarios

### 2. Content Creation Standards

- Organize content into modular learning units (15-30 minute completion time)
- Include visual aids (diagrams, flowcharts) for complex concepts
- Maintain consistent terminology throughout course materials
- Provide reference links to supporting documentation
- Add knowledge check questions at key points

### 3. Course Structure Requirements

- Begin each module with clear learning objectives
- Include prerequisite knowledge and dependencies
- Provide estimated completion times
- End each module with summary and next steps
- Create supplementary materials (cheat sheets, quick reference guides)

### 4. Course Generation Process

- Use AI-assisted content generation to create initial drafts
- Validate AI-generated content against authoritative sources
- Review and refine content for accuracy and clarity
- Test modules with sample learners before full release
- Iterate based on feedback and assessment results

### 5. Quality Benchmarks

- Technical accuracy verified by subject matter experts
- Instructional effectiveness measured via assessment outcomes
- Learner satisfaction tracked through feedback mechanisms
- Content coverage mapped to CCDE exam requirements
- Learning efficiency measured through time-to-proficiency metrics

## Development Workflow

### 1. Branching Strategy

- **main**: Production-ready code
- **develop**: Integration branch for feature work
- **feature/name**: Individual feature branches
- **fix/name**: Bug fix branches

### 2. Commit Guidelines

- Use descriptive commit messages
- Begin with a verb in present tense (Add, Fix, Update, etc.)
- Reference relevant issue numbers
- Keep commits focused on a single logical change
- Example: `Add domain-specific NER for network terms (#23)`

### 3. Code Review Requirements

- All PRs require at least one reviewer
- Check for:
  - Functionality (does it work as intended?)
  - Style consistency
  - Documentation completeness
  - Test coverage
  - Performance considerations

### 4. Testing Requirements

- Unit tests for all core functions
- Integration tests for component interactions
- Document test procedures for manual testing
- Maintain >80% test coverage for core modules

## Module-Specific Guidelines

### 1. Transcript Processing

- Run validation checks on all processed transcripts
- Include source traceability in processed outputs
- Document format conversions and transformations
- Follow the defined enhancement pipeline
- Log all processing steps for debugging

### 2. NLP Components

- Document model selection decisions
- Include benchmark results for model performance
- Version control training data and model weights
- Provide sample input/output examples
- Add graceful fallbacks for edge cases

### 3. Study System

- Validate alignment with CCDE exam topics
- Include metadata for study time estimates
- Tag content with difficulty levels
- Provide navigational aids between related topics
- Include knowledge check components

### 4. API Development

- Follow RESTful design principles
- Version all APIs in the URI path
- Document endpoints with OpenAPI/Swagger
- Implement proper error handling and status codes
- Include rate limiting for resource-intensive operations

## Documentation Standards

### 1. Code Documentation

- Add docstrings to all functions and classes
- Include parameter and return type descriptions
- Document exceptions and edge cases
- Add examples for complex functions
- Comment non-obvious implementations

### 2. Project Documentation

- Maintain up-to-date README files for each module
- Document system architecture with diagrams
- Create setup and installation guides
- Include troubleshooting sections
- Document API usage with examples

### 3. Knowledge Base Documentation

- Version knowledge base artifacts
- Document data sources and processing steps
- Include data quality metrics
- Add guidelines for content contribution
- Document search and retrieval patterns

## Quality Assurance

### 1. Code Quality

- Run static analysis tools (pylint, flake8)
- Maintain consistent code formatting (black)
- Check for type correctness (mypy)
- Measure and monitor cyclomatic complexity
- Review dependencies regularly for security updates

### 2. Data Quality

- Validate data before processing
- Include data quality metrics in outputs
- Document data cleaning procedures
- Implement checks for data consistency
- Version control data transformation scripts

### 3. System Quality

- Monitor system performance metrics
- Document load testing results
- Measure and optimize query response times
- Test with representative data volumes
- Validate output quality with subject matter experts

## Project Management

### 1. Issue Tracking

- Use GitHub issues for all tasks and bugs
- Label issues by component and priority
- Assign clear ownership for each issue
- Document dependencies between issues
- Include acceptance criteria

### 2. Milestones and Releases

- Follow the phase-based implementation plan
- Create milestones aligned with the 12-week NLP plan
- Document release notes for each significant version
- Tag releases in the repository
- Include backward compatibility notes

### 3. Team Communication

- Daily updates on current work
- Weekly planning meetings
- Technical discussions documented in issues or PRs
- Design decisions documented in ADRs (Architecture Decision Records)
- Knowledge sharing sessions for complex components

## Continuous Improvement

- Review these rules quarterly
- Collect feedback on process effectiveness
- Adapt based on project evolution
- Document process improvements
- Share best practices and lessons learned 