What's that, man? Dial. To check on me. Call me helper. Call. 
# CCDE Certification Study Repository

## Overview
This repository serves as a structured learning environment for studying the Cisco Certified Design Expert (CCDE) examination. Rather than working through labs in a traditional manner, this approach follows a modularized, focused learning model based on the official Cisco CCDE documentation.

## Study Approach
The study plan follows a focused progression through key CCDE technology areas:
1. **AI Infrastructure**
2. **On-Prem and Cloud Services Technology**
3. **Large-Scale Network Technology**
4. **Workforce Mobility**

This approach allows for targeted learning in the context of the broader CCDE exam scope, prioritizing areas most relevant to current network design challenges.

## Repository Contents
- **Study Plan Generator**: Python-based tool that processes CCDE PDF documents to create a structured, prioritized study plan
- **Extracted Knowledge Base**: JSON-formatted data extracted from official Cisco documentation
- **Weekly Learning Modules**: Topic-focused learning units organized by priority and relevance

## Tools and Features
The repository includes a comprehensive study plan generator (`ccde_study_plan.py`) that:
- Extracts content from CCDE certification materials
- Identifies key topics and technologies
- Categorizes content into focused study areas
- Generates a weekly study plan based on topic importance
- Creates both structured data (JSON) and human-readable (Markdown) outputs

## Future Development
Future plans for this repository include:
- Building a knowledge base with a GUI frontend to share with colleagues
- Implementing AI subsystems with retrieval augmented generation (RAG)
- Creating a vector database for efficient information retrieval
- Developing an aligned management system for CCDE course modules

## Practical Application
The knowledge and tools in this repository are designed to be immediately applicable to real-world network design challenges. For example, the structured information can be leveraged for data center design projects and other enterprise networking initiatives.

## Getting Started
1. Clone this repository
2. Install dependencies from `requirements.txt`
3. Activate the CCDE_Cisco conda environment
4. Run the study plan generator: `python ccde_study_plan.py`
5. Follow the generated study plan in `ccde_study_materials/CCDE_Study_Plan.md` 