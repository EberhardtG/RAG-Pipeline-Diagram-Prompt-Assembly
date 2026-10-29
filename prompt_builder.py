from sentence_transformers import SentenceTransformer, util
import chromadb

"""
prompt_builder.py — Build a complete RAG prompt for testing

This script simulates retrieved document chunks and assembles
a full prompt containing:
- System instructions
- Retrieved context (with source labels)
- User question
- Citation instructions
"""

def build_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    """
    Assemble a complete RAG prompt from a question and retrieved chunks.
    """

    system_prompt = (
        "You are a helpful AI assistant. Answer the user's question "
        "using ONLY the provided context. If the answer is not in the "
        "context, say 'I don't know.' Cite sources using [source] format."
    )
    #Build context blocks
    context_blocks = []
    for chunk in retrieved_chunks:
        block = f"[Source: {chunk['source']}]\n{chunk['text']}"
        context_blocks.append(block)

    #Join all chunks into one context section
    context_section = "\n\n".join(context_blocks)


    print("----- RAG PROMPT -----\n")

    #Assemble the final RAG prompt
    final_prompt = (
        f"### SYSTEM PROMPT ###\n{system_prompt}\n\n"
        f"### CONTEXT ###\n{context_section}\n\n"
        f"### QUESTION ###\n{question}\n\n"
        f"### INSTRUCTIONS ###\n"
        "Provide a concise answer and cite sources like this: [python_basics.txt]."
    )

    return final_prompt


def estimate_tokens(prompt: str) -> int:
    """Rough token estimate: characters / 4."""
    return len(prompt) // 4


# ---------------------------------------------------------------------------
# Simulated document chunks (safe, original)
# ---------------------------------------------------------------------------

CHUNKS = [
    {
        "source": "python_basics.txt",
        "text": "A Python decorator is a higher-order function that wraps another function to modify its behavior."
    },
    {
        "source": "embeddings_intro.txt",
        "text": "Cosine similarity measures how close two vectors are in direction."
    },
    {
        "source": "api_design.md",
        "text": "A REST API is stateless, meaning each request contains all the information needed for the server to process it."
    },
    {
        "source": "llm_behavior.txt",
        "text": "A hallucination occurs when a language model produces information not grounded in the provided context."
    }
]


# ---------------------------------------------------------------------------
# Test Cases
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("\n=== Test 1 ===")
    question1 = "What does cosine similarity measure?"
    retrieved1 = CHUNKS[1:3] if len(CHUNKS) > 5 else [CHUNKS[1]]
    prompt1 = build_prompt(question1, retrieved1)
    print(prompt1)
    print("Estimated tokens:", estimate_tokens(prompt1))

    print("\n=== Test 2 ===")
    question2 = "What is a Python decorator?"
    retrieved2 = [CHUNKS[0]]
    prompt2 = build_prompt(question2, retrieved2)
    print(prompt2)
    print("Estimated tokens:", estimate_tokens(prompt2))
