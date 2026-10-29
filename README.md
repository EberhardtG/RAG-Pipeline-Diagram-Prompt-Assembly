
# 📘 **Semantic Search Engine (Module 7 — Applied AI: Embeddings & Retrieval)**

A complete semantic search system built using modern embedding‑based retrieval techniques. This project demonstrates how to ingest documents, chunk them, embed them using SentenceTransformers, store them in ChromaDB, and retrieve relevant context through a Streamlit interface. It also includes a chunking experiment and evaluation framework using precision and recall.

---

## 🚀 **Features**

- Document ingestion with configurable chunk size + overlap  
- Embedding generation using `all-MiniLM-L6-v2`  
- Persistent vector storage in ChromaDB  
- Semantic search with ranking, threshold filtering, and source filtering  
- Streamlit UI with metrics, re-index button, and expandable chunk previews  
- Precision/recall evaluation for retrieval quality  
- Chunking experiment comparing multiple chunk sizes  
- Modular architecture (ingest, search, evaluate, UI, prompt builder)

---

## 📁 **Project Structure**

```
semantic-search/
├── app.py               # Streamlit search interface
├── ingest.py            # Document loading, chunking, and ChromaDB storage
├── search.py            # Search functions (query ChromaDB, rank results)
├── evaluate.py          # Precision/recall evaluation
├── prompt_builder.py    # RAG prompt assembly demonstration
├── docs/                # Document collection
├── chroma_data/         # Persistent ChromaDB storage
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 🔧 **Installation**

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd semantic-search
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add documents  
Place `.txt` or `.md` files inside the `docs/` folder.

### 4. Ingest documents
```bash
python ingest.py
```

You can also configure chunk size and overlap:

```bash
python ingest.py --chunk-size 300 --overlap 50
```

---

## 🧠 **How It Works**

### **1. Ingestion (ingest.py)**  
- Loads all `.txt` and `.md` files from `docs/`  
- Splits text into overlapping chunks  
- Generates embeddings using SentenceTransformers  
- Stores chunks + metadata in ChromaDB  

### **2. Search (search.py)**  
- Embeds the user query  
- Retrieves nearest neighbors  
- Applies threshold filtering  
- Supports source filtering  
- Returns ranked results with distance + similarity scores  

### **3. Streamlit UI (app.py)**  
Features include:

- Search bar  
- Sidebar controls  
- Source filter  
- Re-index button  
- Metrics  
- Chunk previews  
- Full edge-case handling  

### **4. Evaluation (evaluate.py)**  
Computes:

- Precision  
- Recall  
- Per-query results  
- Average scores  

Used for the chunking experiment.

### **5. Prompt Assembly (prompt_builder.py)**  
Demonstrates the RAG prompt-building step:

- System prompt  
- Retrieved chunks with source labels  
- User question  
- Citation instructions  
- Token count estimate  

---

## 📊 **Chunking Experiment**

A core part of the project is comparing different chunk sizes.

### **Chunk Sizes Tested**
- **150 characters**  
- **300 characters**  
- **500 characters** (default)

### **Queries Used**
(From `evaluate.py`)

- “What does cosine similarity measure?”  
- “When do background tasks run?”  
- “What is a hallucination?”  
- “What is a decorator?”  
- “What is the base class for errors?”  
- “What does it mean to be stateless?”  
- “What does INNER JOIN accomplish?”  
- “What code supports chat interfaces?”  

### **Results Summary**  
*(Insert your actual numbers here)*

| Chunk Size | Avg Precision | Avg Recall | Notes |
|-----------|---------------|------------|-------|
| 150       | 0.xx          | 0.xx       | Very granular, sometimes loses context |
| 300       | 0.xx          | 0.xx       | Best balance of precision + recall |
| 500       | 0.xx          | 0.xx       | More context, occasionally less precise |

### **Conclusion**  
In my experiment, **300-character chunks** produced the best overall retrieval quality. Smaller chunks improved precision but lost context, while larger chunks improved recall but sometimes returned less relevant matches. This demonstrates the tradeoff between **context size** and **semantic specificity** in embedding-based retrieval.

---

## 🖥️ **Running the App**

Start the Streamlit interface:

```bash
streamlit run app.py
```

Features include:

- Semantic search  
- Source filtering  
- Re-indexing  
- Metrics  
- Chunk previews  

---

## 📈 **Evaluation**

Run precision/recall evaluation:

```bash
python evaluate.py --n-results 5 --threshold 0.4
```

This prints:

- Retrieved chunk IDs  
- Relevant chunk IDs  
- Precision  
- Recall  
- Average scores  

Use this to compare chunk sizes.

---

## 🧩 **Future Improvements**

- Relevance color badges  
- Query history  
- PDF ingestion  
- Embedding model comparison  
- Chunk visualization  
- RAG pipeline integration with an LLM  

---

## 👤 **Author**

**Grant Eberhardt**  
Module 7 — Applied AI: Embeddings & Retrieval  
Semantic Search Engine Project

