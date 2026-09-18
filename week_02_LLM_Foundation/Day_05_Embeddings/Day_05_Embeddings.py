# Week 02 — Day 05: Embeddings
# Practice + Interview Questions

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================

# 1. What is an embedding?
# 2. Why do we convert text into vectors?
# 3. What is a vector?
# 4. What is an embedding model?
# 5. What is semantic similarity?
# 6. What is cosine similarity?
# 7. What is semantic search?
# 8. Why do we chunk documents?
# 9. What is a vector database?
# 10. What is Top-K retrieval?
# 11. How are embeddings used in RAG?
# 12. How can embeddings be used for agent memory?
# 13. What is the difference between an LLM and an embedding model?
# 14. What is the difference between keyword search and semantic search?
# 15. Why are embeddings useful in Agentic AI?
# 16. Explain the complete embedding pipeline.
# 17. Why should you not interpret individual embedding dimensions directly?
# 18. Why should we not send thousands of documents directly to an LLM?
# 19. Is the highest similarity score always the correct result? Why?
# 20. Explain the role of embeddings in a RAG pipeline.

# ==================================================
# CODING PRACTICE
# ==================================================

# 1. CREATE AND COMPARE VECTORS
# Create two vectors and calculate their dot product manually.
# vector_a = [1, 2, 3]
# vector_b = [1, 2, 4]
# Answer:
# vector_a = [1, 2, 3]
# vector_b = [1, 2, 4]
# dot_product = 0
# for i in range(len(vector_a)):
# dot_product += vector_a[i] * vector_b[i]
# print(dot_product)
# Output:
# 17

# 2. COSINE SIMILARITY FROM SCRATCH
# Calculate cosine similarity without using a ready-made
# cosine similarity function.
# Answer:
# import math
# vector_a = [1, 2, 3]
# vector_b = [1, 2, 4]
# dot_product = 0
# magnitude_a = 0
# magnitude_b = 0
# for i in range(len(vector_a)):
# dot_product += vector_a[i] * vector_b[i]
# magnitude_a += vector_a[i] ** 2
# magnitude_b += vector_b[i] ** 2
# magnitude_a = math.sqrt(magnitude_a)
# magnitude_b = math.sqrt(magnitude_b)
# similarity = dot_product / (magnitude_a * magnitude_b)
# print(similarity)

# 3. COSINE SIMILARITY USING NUMPY
# Calculate cosine similarity using NumPy.
# Answer:
# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([1, 2, 4])
# similarity = np.dot(a, b) / (
# np.linalg.norm(a) * np.linalg.norm(b)
# )
# print(similarity)

# 4. COMPARE MULTIPLE VECTORS
# Compare one query vector with three document vectors.
# Answer:
# import numpy as np
# query = np.array([1, 2, 3])
# documents = {
# "Document 1": np.array([1, 2, 3]),
# "Document 2": np.array([1, 2, 5]),
# "Document 3": np.array([5, 6, 7])
# }
# for name, vector in documents.items():
# similarity = np.dot(query, vector) / (
# np.linalg.norm(query) * np.linalg.norm(vector)
# )
# print(name, similarity)

# 5. FIND THE MOST SIMILAR DOCUMENT
# Find the document with the highest similarity score.
# Answer:
# import numpy as np
# query = np.array([1, 2, 3])
# documents = {
# "Document 1": np.array([1, 2, 3]),
# "Document 2": np.array([1, 2, 5]),
# "Document 3": np.array([5, 6, 7])
# }
# best_document = ""
# best_score = -1
# for name, vector in documents.items():
# similarity = np.dot(query, vector) / (
# np.linalg.norm(query) * np.linalg.norm(vector)
# )
# if similarity > best_score:
# best_score = similarity
# best_document = name
# print(best_document)
# print(best_score)

# 6. TOP-K RETRIEVAL
# Given similarity scores, return the Top-3 documents.
# Answer:
# documents = {
# "Document A": 0.92,
# "Document B": 0.87,
# "Document C": 0.81,
# "Document D": 0.43,
# "Document E": 0.21
# }
# k = 3
# results = sorted(
# documents.items(),
# key=lambda x: x[1],
# reverse=True
# )
# top_k = results[:k]
# for document, score in top_k:
# print(document, score)
# 7. SIMPLE SEMANTIC SEARCH
# Create document vectors and find the documents most similar
# to the query vector.
# Answer:
# import numpy as np
# query = np.array([1, 2, 3])
# documents = {
# "Learn Java fundamentals": np.array([1, 2, 3]),
# "Spring Boot REST API development": np.array([1, 2, 4]),
# "Python machine learning": np.array([5, 6, 7]),
# "Java backend development": np.array([1, 3, 3])
# }
# results = []
# for text, vector in documents.items():
# similarity = np.dot(query, vector) / (
# np.linalg.norm(query) * np.linalg.norm(vector)
# )
# results.append((text, similarity))
# results.sort(key=lambda x: x[1], reverse=True)
# for text, score in results:
# print(text, score)

# 8. EMBEDDING MODEL SIMULATION
# Create a function that converts text into a vector.
# Answer:
# def create_embedding(text):
# if "java" in text.lower():
# return [1, 0, 0]
# if "python" in text.lower():
# return [0, 1, 0]
# return [0, 0, 1]
# text = "I want to learn Java"
# vector = create_embedding(text)
# print(vector)

# 9. SIMPLE DOCUMENT CHUNKING
# Split a large text into smaller chunks.
# Answer:
# text = """
# Java is a programming language.
# Spring Boot is used for backend development.
# REST APIs allow applications to communicate.
# Databases store application data.
# """
# chunks = text.strip().split(".")
# chunks = [
# chunk.strip()
# for chunk in chunks
# if chunk.strip()
# ]
# for chunk in chunks:
# print(chunk)
# # Flow:
# # Document -> Chunks -> Embeddings

# 10. SIMPLE RAG RETRIEVAL FLOW
# Create document chunks, vectors, a query vector,
# and retrieve the Top-2 chunks.
# Answer:
# import numpy as np
# chunks = [
# "Java is a programming language.",
# "Spring Boot is used for Java backend development.",
# "Python is commonly used for data science.",
# "REST APIs are used for communication between applications."
# ]
# vectors = [
# np.array([1, 0, 0]),
# np.array([1, 1, 0]),
# np.array([0, 0, 1]),
# np.array([1, 0, 1])
# ]
# query = np.array([1, 1, 0])
# results = []
# for i in range(len(chunks)):
# similarity = np.dot(query, vectors[i]) / (
# np.linalg.norm(query) * np.linalg.norm(vectors[i])
# )
# results.append((chunks[i], similarity))
# results.sort(key=lambda x: x[1], reverse=True)
# top_k = results[:2]
# for chunk, score in top_k:
# print(chunk)
# print(score)

# 11. COURSE RECOMMENDATION SEARCH
# Find the Top-2 courses for:
# "I want to become a Java backend developer"
# Answer:
# import numpy as np
# query = np.array([1, 1, 0])
# courses = {
# "Java Fundamentals": np.array([1, 0, 0]),
# "Spring Boot Fundamentals": np.array([1, 1, 0]),
# "Python Fundamentals": np.array([0, 1, 0]),
# "Machine Learning": np.array([0, 0, 1])
# }
# results = []
# for course, vector in courses.items():
# similarity = np.dot(query, vector) / (
# np.linalg.norm(query) * np.linalg.norm(vector)
# )
# results.append((course, similarity))
# results.sort(key=lambda x: x[1], reverse=True)
# for course, score in results[:2]:
# print(course, score)

# 12. EMBEDDING MEMORY SEARCH
# Find the most relevant memory for:
# "What should I learn next for Java backend?"
# Answer:
# import numpy as np
# query = np.array([1, 1, 0])
# memories = {
# "I am learning Java and Spring Boot": np.array([1, 1, 0]),
# "I want to learn machine learning": np.array([0, 0, 1]),
# "I am preparing for backend development": np.array([1, 1, 0])
# }
# best_memory = ""
# best_score = -1
# for memory, vector in memories.items():
# similarity = np.dot(query, vector) / (
# np.linalg.norm(query) * np.linalg.norm(vector)
# )
# if similarity > best_score:
# best_score = similarity
# best_memory = memory
# print(best_memory)
# print(best_score)

# 13. BUILD A RETRIEVAL FUNCTION
# Create:
# retrieve_top_k(query_vector, document_vectors, k)
# Answer:
# import numpy as np
# def retrieve_top_k(query_vector, document_vectors, k):
# results = []
# for document, vector in document_vectors.items():
# similarity = np.dot(query_vector, vector) / (
# np.linalg.norm(query_vector) * np.linalg.norm(vector)
# )
# results.append((document, similarity))
# results.sort(key=lambda x: x[1], reverse=True)
# return results[:k]
# query = np.array([1, 2, 3])
# documents = {
# "Document A": np.array([1, 2, 3]),
# "Document B": np.array([1, 2, 4]),
# "Document C": np.array([5, 6, 7]),
# "Document D": np.array([1, 1, 3]),
# "Document E": np.array([0, 1, 2])
# }
# results = retrieve_top_k(query, documents, 3)
# for document, score in results:
# print(document, score)
# 14. EMBEDDING + RAG PIPELINE
# Build a small end-to-end retrieval pipeline:
# Documents
# -> Chunks
# -> Embeddings
# -> Similarity Search
# -> Top-K Results
# -> Context
# Answer:
# import numpy as np
# chunks = [
# "Java is used for backend development.",
# "Spring Boot simplifies Java backend applications.",
# "Python is popular for machine learning.",
# "REST APIs allow applications to communicate."
# ]
# chunk_vectors = [
# np.array([1, 0, 0]),
# np.array([1, 1, 0]),
# np.array([0, 0, 1]),
# np.array([1, 0, 1])
# ]
# query = np.array([1, 1, 0])
# results = []
# for i in range(len(chunks)):
# similarity = np.dot(query, chunk_vectors[i]) / (
# np.linalg.norm(query) *
# np.linalg.norm(chunk_vectors[i])
# )
# results.append((chunks[i], similarity))
# results.sort(key=lambda x: x[1], reverse=True)
# top_k = results[:2]
# context = "\n".join(
# chunk for chunk, score in top_k
# )
# print("Retrieved Context:")
# print(context)

# 15. USE A REAL EMBEDDING MODEL
# If you have an embedding API/model available:
# 1. Generate embeddings for two related sentences.
# 2. Generate an embedding for an unrelated sentence.
# 3. Calculate cosine similarity.
# 4. Compare the scores.
# Example sentences:
# text_1 = "I want to learn Java"
# text_2 = "I want to become a Java backend developer"
# text_3 = "The weather is cold today"
# Answer:
# # Use the embedding model/API available in your environment.
# # embedding_1 = create_embedding(text_1)
# # embedding_2 = create_embedding(text_2)
# # embedding_3 = create_embedding(text_3)
# # Calculate:
# # similarity_1_2
# # similarity_1_3
# # The related sentences should generally have a higher
# # semantic similarity than the unrelated sentence.

# ==================================================
# FINAL MINI PROJECT
# ==================================================
# Build a small semantic course search system.
# Requirements:
# 1. Store at least 5 course descriptions.
# 2. Create embeddings for the courses.
# 3. Accept a user query.
# 4. Create an embedding for the query.
# 5. Calculate similarity.
# 6. Sort courses by similarity.
# 7. Return the Top-3 courses.
# Answer:
# import numpy as np
# courses = {
# "Java Fundamentals": np.array([1, 0, 0]),
# "Spring Boot Backend": np.array([1, 1, 0]),
# "Python Fundamentals": np.array([0, 1, 0]),
# "Machine Learning": np.array([0, 0, 1]),
# "REST API Development": np.array([1, 1, 0])
# }
# query = np.array([1, 1, 0])
# results = []
# for course, vector in courses.items():
# similarity = np.dot(query, vector) / (
# np.linalg.norm(query) * np.linalg.norm(vector)
# )
# results.append((course, similarity))
# results.sort(key=lambda x: x[1], reverse=True)
# print("Top 3 Courses:")
# for course, score in results[:3]:
# print(course, score)