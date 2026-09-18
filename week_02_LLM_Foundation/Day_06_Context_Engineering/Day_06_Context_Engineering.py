# Week 02 — Day 06: Context Engineering
# Practice + Interview Questions + Answers
# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# 1. What is context in an LLM application?
# 2. What is context engineering?
# 3. What is the difference between prompt engineering and context engineering?
# 4. Why is context important for LLM applications?
# 5. What can be included in LLM context?
# 6. What is a context window?
# 7. Why should we avoid unnecessary context?
# 8. What is dynamic context?
# 9. What is static context?
# 10. How are embeddings related to context engineering?
# 11. How is context engineering used in RAG?
# 12. How is context engineering used in agents?
# 13. What is context compression?
# 14. What makes good context?
# 15. Explain the basic context engineering pipeline.
# 16. What is the difference between static and dynamic context?
# 17. Why is context selection important?
# 18. What is context compression?
# 19. Why is context engineering important for Agentic AI?
# 20. Explain context engineering in one sentence.

# ==================================================
# CODING PRACTICE
# ==================================================

# 1. BUILD A BASIC CONTEXT
# Create a Python dictionary containing:
# - system instructions
# - user question
# - context
# Answer:
# context = {
#     "system": "You are a Java tutor.",
#     "question": "What is dependency injection?",
#     "context": "Spring Boot uses dependency injection."
# }
# print(context)

# 2. FORMAT CONTEXT
# Convert the context into a readable string.
# Answer:
# system = "You are a Java tutor."
# context = "Spring Boot uses dependency injection."
# question = "What is dependency injection?"
# prompt = f"""
# SYSTEM:
# {system}
# CONTEXT:
# {context}
# QUESTION:
# {question}
# """
# print(prompt)

# 3. BUILD CONTEXT FROM MULTIPLE SOURCES
# Create context using:
# - user question
# - conversation history
# - memory
# - retrieved documents
# Answer:
# user_question = "What should I learn next?"
# history = "I have completed Java basics."
# memory = "The user wants to become a backend developer."
# documents = [
#     "Spring Boot is a Java backend framework.",
#     "REST APIs are important for backend development."
# ]
# context = f"""
# Conversation History:
# {history}
# Memory:
# {memory}
# Retrieved Documents:
# {documents}
# User Question:
# {user_question}
# """
# print(context)

# 4. FILTER RELEVANT DOCUMENTS
# Given a list of documents, select documents related to the user's question.
# Answer:
# documents = [
#     "Java is a programming language.",
#     "Spring Boot is used for backend development.",
#     "Python is used for data science.",
#     "REST APIs are important in backend systems."
# ]
# query = "Java backend"
# relevant_documents = []
# for document in documents:
#     if "Java" in document or "backend" in document:
#         relevant_documents.append(document)
# print(relevant_documents)

# 5. LIMIT CONTEXT SIZE
# Given multiple documents, keep only the first 3 relevant documents.
# Answer:
# documents = [
#     "Java fundamentals",
#     "Spring Boot",
#     "REST APIs",
#     "Python",
#     "Machine Learning",
#     "Docker"
# ]
# relevant_documents = documents[:3]
# print(relevant_documents)

# 6. REMOVE DUPLICATE CONTEXT
# Remove duplicate pieces of information.
# Answer:
# context = [
#     "Java is a programming language.",
#     "Spring Boot is a Java framework.",
#     "Java is a programming language.",
#     "REST APIs are used by backend applications.",
#     "Spring Boot is a Java framework."
# ]
# unique_context = list(dict.fromkeys(context))
# print(unique_context)

# 7. BUILD A CONTEXT FUNCTION
# Create:
# def build_context(question, history, memory, documents):
# The function should combine the information into one structured context string.
# Answer:
# def build_context(question, history, memory, documents):
#     context = f"""
# HISTORY:
# {history}
# MEMORY:
# {memory}
# DOCUMENTS:
# {documents}
# QUESTION:
# {question}
# """
#     return context
#
# result = build_context(
#     "What should I learn next?",
#     "I completed Java basics.",
#     "I want to become a backend developer.",
#     ["Spring Boot", "REST APIs"]
# )
# print(result)

# 8. STATIC AND DYNAMIC CONTEXT
# Create separate variables for static and dynamic context.
# Answer:
# static_context = {
#     "system": "You are a Java backend tutor.",
#     "rules": "Use simple English."
# }
# dynamic_context = {
#     "question": "What is Spring Boot?",
#     "memory": "The user knows Java basics.",
#     "documents": ["Spring Boot is a Java framework."]
# }
# print(static_context)
# print(dynamic_context)

# 9. SIMPLE CONTEXT COMPRESSION
# Given a conversation, create a short summary containing only the important information.
# Answer:
# conversation = [
#     "User is learning Java.",
#     "User asked about variables.",
#     "Assistant explained variables.",
#     "User asked about loops.",
#     "User completed Java basics.",
#     "User wants to learn backend development."
# ]
# summary = [
#     "User knows Java basics.",
#     "User wants to learn backend development."
# ]
# print(summary)

# 10. RAG-STYLE CONTEXT BUILDING
# Simulate:
# User Question -> Retrieved Chunks -> Context -> LLM Input
# Answer:
# question = "How does Spring Boot help backend development?"
# retrieved_chunks = [
#     "Spring Boot simplifies Java backend application development.",
#     "Spring Boot can be used to create REST APIs."
# ]
# context = "\n".join(retrieved_chunks)
# llm_input = f"""
# CONTEXT:
# {context}
# QUESTION:
# {question}
# """
# print(llm_input)

# 11. TOOL RESULT AS CONTEXT
# Simulate a tool returning information and add the result to the context.
# Answer:
# tool_result = {
#     "temperature": 25,
#     "city": "Dehradun"
# }
# question = "What is the current temperature?"
# context = f"""
# TOOL RESULT:
# City: {tool_result["city"]}
# Temperature: {tool_result["temperature"]}°C
# QUESTION:
# {question}
# """
# print(context)

# 12. MEMORY AS CONTEXT
# Retrieve a relevant memory and add it to the current request.
# Answer:
# memory = "The user is learning Java and Spring Boot."
# question = "What should I learn next?"
# context = f"""
# RELEVANT MEMORY:
# {memory}
# QUESTION:
# {question}
# """
# print(context)

# 13. LIMIT CONTEXT BY WORD COUNT
# Simulate a simple context limit by keeping only a fixed number of words.
# Answer:
# context = """
# Java is a programming language used for backend development.
# Spring Boot makes it easier to build Java applications.
# REST APIs are commonly used in backend applications.
# """
# words = context.split()
# max_words = 12
# limited_context = " ".join(words[:max_words])
# print(limited_context)

# 14. BUILD AN AGENT CONTEXT
# Simulate an agent receiving:
# - user request
# - memory
# - retrieved information
# - tool result
# Build one final context string.
# Answer:
# user_request = "Recommend the next topic I should learn."
# memory = "User has completed Java basics."
# retrieved_info = [
#     "Spring Boot is used for Java backend development.",
#     "REST APIs are important in backend development."
# ]
# tool_result = "Current project uses Java and Spring Boot."
# final_context = f"""
# USER REQUEST:
# {user_request}
# MEMORY:
# {memory}
# RETRIEVED INFORMATION:
# {retrieved_info}
# TOOL RESULT:
# {tool_result}
# """
# print(final_context)

# 15. FINAL MINI PROJECT
# Build a simple context engineering system.
# Requirements:
# 1. Accept a user question.
# 2. Store conversation history.
# 3. Store user memory.
# 4. Store documents.
# 5. Select relevant documents.
# 6. Remove duplicate information.
# 7. Build the final context.
# 8. Print the final context.
# Final context should contain:
# SYSTEM
# HISTORY
# MEMORY
# RETRIEVED CONTEXT
# QUESTION
# Answer:
# def run_context_pipeline(user_question):
#     system_instruction = "You are an intelligent assistant."
#     conversation_history = "User completed Java basics."
#     user_memory = "User wants to become a backend developer."
#     documents = [
#         "Java is a programming language.",
#         "Spring Boot is used for backend development.",
#         "REST APIs are important in backend systems.",
#         "Java is a programming language."
#     ]
#     
#     # 5. Select relevant documents
#     relevant_docs = [doc for doc in documents if any(k in doc.lower() for k in user_question.lower().split())]
#     
#     # 6. Remove duplicate information
#     unique_docs = list(dict.fromkeys(relevant_docs))
#     retrieved_context = "\n".join(unique_docs)
#     
#     # 7. Build the final context
#     final_context = f"""SYSTEM:
# {system_instruction}
# 
# HISTORY:
# {conversation_history}
# 
# MEMORY:
# {user_memory}
# 
# RETRIEVED CONTEXT:
# {retrieved_context}
# 
# QUESTION:
# {user_question}"""
#     
#     # 8. Print the final context
#     print(final_context)
#
# run_context_pipeline("What backend topics should I learn in Java?")