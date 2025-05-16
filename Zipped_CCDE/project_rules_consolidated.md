# CCDE Project: Development and Management Rules (Consolidated)

## Core Principles

1. **Clarity**: All code, documentation, and communications should be clear and understandable.
2. **Consistency**: Maintain consistent approaches throughout the project.
3. **Modularity**: Design components that are loosely coupled but highly cohesive.
4. **Documentation**: Document all significant decisions, components, and processes.
5. **Testing**: Test thoroughly before integrating any new component.

## Project Governance Structure

### Management Structure
- **Product Owner**: Responsible for prioritizing features and representing stakeholder interests
- **Scrum Master**: Facilitates agile processes and removes impediments
- **Development Team**: Cross-functional team with expertise in programming, NLP/NER, and CCDE content
- **Content SMEs**: Subject matter experts for CCDE curriculum validation
- **UX/UI Specialists**: Focused on learner experience and Moodle integration

### Decision-Making Framework
- **Technical Decisions**: Development team with architecture review
- **Content Decisions**: Content team with CCDE SME validation
- **Priority Decisions**: Product owner with stakeholder input
- **Design Decisions**: UX/UI specialists with user testing validation

## Environment Setup

### Conda Environment

- **Always check** the current working directory is `C:\Users\kiman\Downloads\Zipped_CCDE`
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

## Agile Implementation Framework

### Sprint Structure
- **Sprint Duration**: Two weeks (10 working days)
- **Planning Meeting**: Day 1, maximum 4 hours
- **Daily Stand-ups**: 15 minutes, focused on progress and impediments
- **Sprint Review**: Day 10, demonstration of completed work
- **Sprint Retrospective**: Day 10, process improvement discussion
- **Backlog Refinement**: Ongoing, dedicated session on Day 5

### User Story Guidelines
- **Format**: "As a [role], I want [feature] so that [benefit]"
- **Roles**: Learner, Instructor, Administrator, Content Creator
- **Acceptance Criteria**: Minimum 3, maximum 7 per story
- **Story Points**: Fibonacci sequence (1, 2, 3, 5, 8, 13)
- **Definition of Ready**: Clear requirements, acceptance criteria, design mockups
- **Definition of Done**: Code reviewed, tested, documented, deployed to staging

### Task Breakdown Rules
- **Granularity**: Tasks should be completable within 1-2 days
- **Technical Tasks**: Development, testing, documentation
- **Content Tasks**: Creation, review, metadata tagging, assessment development
- **Integration Tasks**: API development, Moodle compatibility, data synchronization
- **Task Assignment**: Self-assignment within team capacity

## Development Workflow

### Branching Strategy

- **main**: Production-ready code
- **develop**: Integration branch for feature work
- **feature/name**: Individual feature branches
- **fix/name**: Bug fix branches

### Commit Guidelines

- Use descriptive commit messages
- Begin with a verb in present tense (Add, Fix, Update, etc.)
- Reference relevant issue numbers
- Keep commits focused on a single logical change
- Example: `Add domain-specific NER for network terms (#23)`

### Code Review Requirements

- All PRs require at least one reviewer
- Check for:
  - Functionality (does it work as intended?)
  - Style consistency
  - Documentation completeness
  - Test coverage
  - Performance considerations

### Testing Requirements

- Unit tests for all core functions
- Integration tests for component interactions
- Document test procedures for manual testing
- Maintain >80% test coverage for core modules

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

### 3. RAG Implementation

- Follow the RAG architecture layers defined in documentation
- Use appropriate models based on cost, privacy, and performance considerations
- Implement agent-based systems using frameworks like LangChain
- Enable swarm coordination for complex tasks
- Optimize retrieval mechanisms for CCDE-specific content

### 4. Study System

- Validate alignment with CCDE exam topics
- Include metadata for study time estimates
- Tag content with difficulty levels
- Provide navigational aids between related topics
- Include knowledge check components

### 5. API Development

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
- 80% test coverage minimum for core modules

### 2. Content Quality

- SME review for technical accuracy
- Bloom's alignment verification
- Technical accuracy check
- Consistency with CCDE curriculum
- Metadata completeness and accuracy

### 3. Integration Quality

- End-to-end testing with Moodle LMS
- API compatibility verification
- Data synchronization validation
- User authentication testing
- Cross-platform functionality testing

### 4. Performance Metrics

- Response time < 2s for user interactions
- NLP processing time < 5s per document
- Search query response time < 1s
- Bulk operations optimized for efficiency
- Scalability testing for growing content volume

## Project Management

### 1. Issue Tracking

- Use GitHub issues for all tasks and bugs
- Label issues by component and priority
- Assign clear ownership for each issue
- Document dependencies between issues
- Include acceptance criteria

### 2. Milestones and Releases

- Follow the phase-based implementation plan
- Create milestones aligned with the development phases
- Document release notes for each significant version
- Tag releases in the repository
- Include backward compatibility notes

### 3. Team Communication

- Daily updates on current work
- Weekly planning meetings
- Technical discussions documented in issues or PRs
- Design decisions documented in ADRs (Architecture Decision Records)
- Knowledge sharing sessions for complex components

## Risk Management

### Technical Risks
- NLP accuracy limitations mitigated through human review processes
- Integration challenges addressed through early proof-of-concept
- Performance issues identified through regular performance testing
- Scalability concerns addressed through design for growth
- Security vulnerabilities monitored with regular security assessments

### Content Risks
- Curriculum alignment gaps checked through regular validation
- Quality inconsistency prevented through standardized review process
- Bloom's misalignment verified through cognitive level mapping
- Assessment effectiveness validated through user testing
- Content coverage gaps tracked through curriculum coverage metrics

### Project Risks
- Scope creep managed through strict change management process
- Resource constraints monitored through team capacity tracking
- Timeline pressure managed by building buffer into sprint planning
- Stakeholder alignment maintained through regular communication
- Technical debt controlled by allocating time for refactoring in each sprint

## Continuous Improvement

- Review these rules quarterly
- Collect feedback on process effectiveness
- Adapt based on project evolution
- Document process improvements
- Share best practices and lessons learned 