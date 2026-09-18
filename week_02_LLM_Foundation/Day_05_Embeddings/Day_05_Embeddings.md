# Week 02 — Day 05: Embeddings

- What Are Embeddings?
- Why Do We Need Embeddings?
- Text → Embedding
- What Is a Vector?
- Embedding Model
- Semantic Similarity
- Similarity Search
- Cosine Similarity
- Cosine Similarity Formula
- Embeddings vs LLMs
- Embeddings in RAG
- Document Chunking
- Vector Database
- Top-K Retrieval



## 1. What Are Embeddings?

An **embedding** is a numerical representation of data, usually text, that captures its meaning.

In simple words:

> Embeddings convert text into a list of numbers so that a machine can compare the meaning of different pieces of text.

Example:

```text
"I want to learn Java"
        ↓
[0.21, -0.45, 0.73, 0.12, ...]
```

Another sentence:

```text
"I want to become a Java developer"
        ↓
[0.19, -0.42, 0.71, 0.15, ...]
```

If two texts have similar meanings, their vectors will generally be closer together.

---

## 2. Why Do We Need Embeddings?

Traditional programs do not naturally understand that:

```text
"I want to learn Java"
```

and

```text
"I want to become a Java developer"
```

are related.

Keyword search mainly looks for matching words.

Embeddings allow **semantic search**. 
..Semantic search is a search technique that retrieves information based on the meaning and context of a query rather than matching only exact keywords.

Instead of asking:

```text
Do these texts contain the same words?
```

we can ask:

```text
Do these texts have similar meanings?
```

This is useful in many AI applications.

---

## 3. Text → Embedding

Basic process:

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

Example:

```text
"I want to learn Spring Boot"
        ↓
Embedding Model
        ↓
[0.12, -0.44, 0.81, 0.33, ...]
```

The vector can contain hundreds or thousands of dimensions depending on the embedding model.

---

## 4. What Is a Vector?

A vector is simply a list of numbers.

```python
[0.2, 0.5, -0.1, 0.8]
```

An embedding is a vector whose numbers represent learned semantic information.

You generally should not interpret individual dimensions manually.

For example, do not assume:

```text
Dimension 1 = Java
Dimension 2 = backend
Dimension 3 = programming
```

The meaning is distributed across many dimensions.

---

## 5. Embedding Model

An **embedding model** converts input data into vectors.

```text
Input Text
    ↓
Embedding Model
    ↓
Vector
```

Conceptually:

```python
text = "Spring Boot is a Java backend framework"

vector = embedding_model(text)
```

Different embedding models can produce vectors with different dimensions.

---

## 6. Semantic Similarity

Semantic similarity measures how closely two pieces of data are related in meaning.

Example:

```text
A = "I want to learn Java"

B = "I want to become a Java developer"

C = "The weather is very cold today"
```

Conceptually:

```text
A ───── B

C
```

A and B should be closer because they have similar meanings.

C should be farther away.

This allows applications to find information based on meaning.

---

## 7. Similarity Search

Suppose we have:

```text
Document 1:
"Learn Java fundamentals"

Document 2:
"Spring Boot REST API development"

Document 3:
"Python machine learning"

Document 4:
"Java backend development"
```

User asks:

```text
"I want to become a Java backend developer"
```

First create an embedding for the query:

```text
Query
 ↓
Embedding
 ↓
Query Vector
```

Then compare the query vector with document vectors.

```text
Query
 ↓
Query Vector

Document 1 → similarity
Document 2 → similarity
Document 3 → similarity
Document 4 → similarity
```

The most similar documents are returned.

This is called **semantic search**.

---

## 8. Cosine Similarity

One common method for comparing embeddings is **cosine similarity**.

It measures the angle between two vectors.

If two vectors point in similar directions:

```text
High similarity
```

If they point in very different directions:

```text
Low similarity
```

The commonly used range is:

```text
-1 → completely opposite
 0 → unrelated / orthogonal
 1 → very similar direction
```

For many modern embedding applications, similarity values are often positive, but interpretation depends on the embedding model and data.

---

## 9. Cosine Similarity Formula

For:

```text
A = [a1, a2, a3]
B = [b1, b2, b3]
```

Cosine similarity is:

```text
cosine_similarity(A, B)
=
(A · B)
---------
||A|| × ||B||
```

Where:

```text
A · B
```

is the dot product.

And:

```text
||A||
```

is the magnitude of vector A.

In applications, libraries can calculate this for us.

---

## 10. Embeddings vs LLMs

An LLM and an embedding model have different purposes.

### LLM

Used for language generation and reasoning.

```text
Question
   ↓
LLM
   ↓
Answer
```

### Embedding Model

Used to represent data as vectors.

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

Remember:

```text
LLM
→ generation / reasoning / language tasks

Embedding Model
→ semantic representation / similarity / retrieval
```

---

## 11. Embeddings in RAG

Embeddings are a fundamental component of **RAG — Retrieval-Augmented Generation**.

Instead of sending an entire large document to the LLM every time, documents can be split and indexed.

### Indexing
Indexing in a RAG system is the process of preparing documents for efficient retrieval. We first split the documents into smaller chunks, generate embeddings for each chunk using an embedding model, and store those embeddings along with the original content and metadata in a vector database. Later, these indexed vectors can be searched using semantic similarity to retrieve relevant information.

```text
Document
 ↓
Split into chunks
 ↓
Create embeddings
 ↓
Store vectors
```

### Retrieval
Retrieval is the process of finding and fetching the most relevant information from an indexed knowledge base based on a user's query.

```text
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Context
      ↓
LLM
      ↓
Answer
```

This is the basic RAG pipeline.

---

## 12. Why Do We Chunk Documents?

Large documents are usually divided into smaller pieces called **chunks**.

Example:

```text
Large PDF
   ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

Each chunk gets its own embedding.

```text
Chunk 1 → Vector 1
Chunk 2 → Vector 2
Chunk 3 → Vector 3
```

When the user asks a question, the system searches for the most relevant chunks.

---

## 13. Vector Database

If you have thousands or millions of embeddings, manually comparing every vector is not practical.

A **vector database** is designed to store and search vectors efficiently.

Examples:

```text
Qdrant
Pinecone
Weaviate
Milvus
pgvector
```

Basic architecture:

```text
Documents
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
```

Query:

```text
User Question
      ↓
Query Embedding
      ↓
Vector Database
      ↓
Top-K Similar Chunks
```

---

## 14. Top-K Retrieval

Suppose a vector search returns:

```text
Document A → 0.92
Document B → 0.87
Document C → 0.81
Document D → 0.43
Document E → 0.21
```

If:

```text
K = 3
```

we retrieve:

```text
A
B
C
```

These are the **Top-K results**.

---