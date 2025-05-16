# Advanced Document Processing for CCDE Study System

## Document Processing Framework

### Multi-Format Document Loaders
- **Markdown (.md)**: Direct parsing with metadata extraction
- **PDF (.pdf)**: PyMuPDF/PDFPlumber with layout preservation
- **PowerPoint (.pptx)**: Slide-by-slide extraction
- **Word (.docx)**: Structure-aware parsing
- **Images (.jpeg, .png)**: OCR + CLIP embeddings

### LlamaIndex vs. LangChain Strategy

**Recommended Approach**: Use LlamaIndex for document processing and LangChain for orchestration.

```python
# Basic integration example
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from langchain.agents import initialize_agent, Tool

# Document processing with LlamaIndex
documents = SimpleDirectoryReader('./transcripts').load_data()
index = VectorStoreIndex.from_documents(documents)
retriever = index.as_retriever()

# Workflow orchestration with LangChain
tools = [
    Tool(
        name="CCDE Knowledge Base",
        func=lambda q: retriever.retrieve(q),
        description="Useful for CCDE questions"
    )
]

agent = initialize_agent(tools, llm, agent="conversational-react-description")
```

## RAG Enhancements

### Query Enhancement
```python
def enhance_query(query):
    # Generate hypothetical answer
    expansion = llm(f"Write a detailed answer about: {query}")
    
    # Create combined embedding
    original_emb = embedder.encode(query)
    expansion_emb = embedder.encode(expansion)
    enhanced_emb = original_emb * 0.3 + expansion_emb * 0.7
    
    return enhanced_emb
```

### Re-ranking
```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_results(query, results, top_k=5):
    # Create pairs of query and results
    pairs = [[query, result.text] for result in results]
    
    # Get scores
    scores = reranker.predict(pairs)
    
    # Sort by score
    reranked = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)
    
    return [item[0] for item in reranked[:top_k]]
```

## Vector Database Implementation

```python
import chromadb

# Set up ChromaDB client
client = chromadb.Client()
collection = client.create_collection("ccde_documents")

# Add documents
def add_documents(chunks, metadata_list):
    collection.add(
        documents=chunks,
        metadatas=metadata_list,
        ids=[f"doc_{i}" for i in range(len(chunks))]
    )

# Query
def semantic_search(query, n_results=5):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results
```

## Learning System Integration

### Curriculum Mapping
```python
# Map content to CCDE curriculum areas
def map_to_curriculum(content):
    topics = extract_topics(content)
    
    curriculum_areas = {
        "network_design": ["topology", "redundancy", "scalability"],
        "protocols": ["routing", "switching", "mpls", "bgp"],
        "security": ["firewall", "encryption", "access-control"],
        "automation": ["api", "scripting", "orchestration"]
    }
    
    mappings = {}
    for area, keywords in curriculum_areas.items():
        score = sum(1 for topic in topics if any(k in topic.lower() for k in keywords))
        if score > 0:
            mappings[area] = score / len(topics)
    
    return mappings
```

### Assessment Generation
```python
def generate_assessment(topic, difficulty="intermediate", count=5):
    prompt = f"""
    Create {count} {difficulty} level questions on {topic} for CCDE exam preparation.
    For each question include:
    1. A scenario-based problem
    2. Four possible answers (A-D)
    3. The correct answer
    4. Brief explanation
    """
    
    response = llm(prompt)
    structured_questions = parse_assessment_response(response)
    
    return structured_questions
```

## Lab Environment Integration

```python
def generate_topology(requirements):
    # Create network topology
    prompt = f"""
    Design a network topology that meets these requirements:
    {requirements}
    
    Include devices, connections, IP addressing, and protocols.
    """
    
    topology_description = llm(prompt)
    
    # Generate device configurations
    configs = {}
    devices = extract_devices(topology_description)
    
    for device in devices:
        config_prompt = f"Generate Cisco configuration for {device['type']} named {device['name']}"
        configs[device['name']] = llm(config_prompt)
    
    return {
        "topology": topology_description,
        "configurations": configs
    }
```

## Implementation Roadmap

1. **Phase 1: Setup (Weeks 1-2)**
   - Document processing pipeline
   - Vector database configuration

2. **Phase 2: RAG Enhancement (Weeks 3-4)**
   - Query enhancement
   - Re-ranking implementation

3. **Phase 3: Learning Integration (Weeks 5-6)**
   - Curriculum mapping system
   - Assessment generator

4. **Phase 4: Lab Environment (Weeks 7-8)**
   - Topology generator
   - Configuration builder 