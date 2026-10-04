# Week 04 — Day 04: Streaming & Async LLM Applications
# Practice
# ============================================================
# Instructions
# ============================================================
# All questions and solutions are commented initially.
# Uncomment each section when you want to practice.
# The LLM client functions used below are conceptual placeholders.
# They are not tied to a specific LLM provider SDK.
# ============================================================
# ============================================================
# 1. Basic Generator
# ============================================================
# Question:
# Create a generator that yields three values one by one:
# "first"
# "second"
# "third"
# Expected output:
# first
# second
# third
# def get_data():
#     yield "first"
#     yield "second"
#     yield "third"
# for value in get_data():
#     print(value)

# ============================================================
# 2. Understand yield
# ============================================================
# Question:
# Create a generator that yields:
# "Hello"
# "World"
# "AI"
# Print each value separately.
# def messages():
#     yield "Hello"
#     yield "World"
#     yield "AI"
# for message in messages():
#     print(message)

# ============================================================
# 3. Synchronous LLM Call
# ============================================================
# Question:
# Create a synchronous function called chat().
# It should call:
# response = call_llm()
# and return the response.
# call_llm() is a conceptual placeholder.
# def chat():
#     response = call_llm()
#     return response

# ============================================================
# 4. Asynchronous LLM Call
# ============================================================
# Question:
# Convert the previous synchronous function into an
# asynchronous function.
# Use async and await.
# async def chat():
#     response = await call_llm()
#     return response

# ============================================================
# 5. async Function
# ============================================================
# Question:
# Create an async function called get_response().
# It should:
# 1. Call an async function named call_llm()
# 2. Await the result
# 3. Return the response
# async def get_response():
#     response = await call_llm()
#     return response

# ============================================================
# 6. Async Streaming Function
# ============================================================
# Question:
# Create an async generator called stream_response().
# It should:
# 1. Get an async stream from call_llm_stream()
# 2. Iterate over it using async for
# 3. Yield every chunk
# async def stream_response():
#     stream = await call_llm_stream()
#     async for chunk in stream:
#         yield chunk

# ============================================================
# 7. Simulate LLM Streaming
# ============================================================
# Question:
# Create a simple generator that simulates an LLM stream.
# Yield:
# "FastAPI"
# " is"
# " a"
# " Python"
# " framework."
# def simulate_stream():
#     yield "FastAPI"
#     yield " is"
#     yield " a"
#     yield " Python"
#     yield " framework."
# for chunk in simulate_stream():
#     print(chunk, end="")

# ============================================================
# 8. Build Complete Response from Chunks
# ============================================================
# Question:
# Create a function that receives streamed chunks and combines
# them into one complete response.
# Example:
# ["FastAPI", " is", " a", " framework."]
# Output:
# "FastAPI is a framework."
# def combine_chunks(chunks):
#     return "".join(chunks)
# chunks = [
#     "FastAPI",
#     " is",
#     " a",
#     " framework."
# ]
# print(combine_chunks(chunks))

# ============================================================
# 9. FastAPI StreamingResponse
# ============================================================
# Question:
# Create a FastAPI endpoint:
# GET /chat
# It should return a StreamingResponse using stream_response().
# Use text/plain as the media type.
# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# app = FastAPI()
# async def stream_response():
#     yield "Hello "
#     yield "from "
#     yield "AI."
# @app.get("/chat")
# async def chat():
#     return StreamingResponse(
#         stream_response(),
#         media_type="text/plain"
#     )



# ============================================================
# 10. Async FastAPI Endpoint
# ============================================================
# Question:
# Create:
# GET /answer
# The endpoint should:
# 1. Call an async LLM function
# 2. Await the response
# 3. Return the answer as JSON
# from fastapi import FastAPI
# app = FastAPI()
# async def call_llm():
#     return "Python is a programming language."
# @app.get("/answer")
# async def answer():
#     response = await call_llm()
#     return {
#         "answer": response
#     }

# ============================================================
# 11. Streaming Chat Endpoint
# ============================================================
# Question:
# Create a streaming endpoint:
# POST /chat
# The endpoint should:
# 1. Receive a user message
# 2. Build a prompt
# 3. Call an async LLM stream
# 4. Yield chunks
# 5. Return them using StreamingResponse
# Keep the LLM implementation conceptual.
# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# app = FastAPI()
# async def call_llm_stream(prompt):
#     # Conceptual placeholder
#     ...
# async def stream_response(prompt):
#     stream = await call_llm_stream(prompt)
#     async for chunk in stream:
#         yield chunk
# @app.post("/chat")
# async def chat(message: str):
#     prompt = f"Answer this question: {message}"
#     return StreamingResponse(
#         stream_response(prompt),
#         media_type="text/plain"
#     )

# ============================================================
# 12. Streaming vs Normal Response
# ============================================================
# Question:
# Explain in comments the difference between:
# Normal response
# Streaming response
# Write a small example for both.
# Normal response:
# def normal_response():
#     return "Complete answer"
# Streaming response:
# def streaming_response():
#     yield "First "
#     yield "part "
#     yield "of answer"

# ============================================================
# 13. async for Practice
# ============================================================
# Question:
# Assume async_stream() returns an asynchronous stream.
# Use async for to print every chunk.
# async def process_stream():
#     stream = await async_stream()
#     async for chunk in stream:
#         print(chunk)

# ============================================================
# 14. Client-Side Chunk Simulation
# ============================================================
# Question:
# Simulate how a frontend receives chunks.
# Given:
# chunks = [
#     "Hello",
#     " from",
#     " the",
#     " AI",
#     " assistant."
# ]
# Print the final response progressively.
# chunks = [
#     "Hello",
#     " from",
#     " the",
#     " AI",
#     " assistant."
# ]
# response = ""
# for chunk in chunks:
#     response += chunk
#     print(response)

# ============================================================
# 15. Error Handling During Streaming
# ============================================================
# Question:
# Create a streaming function that handles an error.
# Simulate:
# 1. First chunk is received
# 2. An error occurs
# 3. The error is caught
# 4. A message is returned
# def stream_response():
#     try:
#         yield "First chunk"
#         raise RuntimeError("LLM provider error")
#         yield "Second chunk"
#     except RuntimeError as error:
#         yield f"Error: {error}"

# ============================================================
# 16. Async Error Handling
# ============================================================
# Question:
# Create an async function that calls an async LLM function.
# Handle:
# - TimeoutError
# - General exception
# Keep the implementation simple.
# async def chat():
#     try:
#         response = await call_llm()
#         return response
#     except TimeoutError:
#         return "LLM request timed out."
#     except Exception as error:
#         return f"LLM request failed: {error}"

# ============================================================
# 17. Streaming with Context
# ============================================================
# Question:
# Build a prompt using:
# user_question
# user_context
# Then pass the prompt to the conceptual streaming function.
# user_question = "What should I learn next?"
# user_context = """
# Current skills:
# Python
# FastAPI
# SQL
# Current goal:
# AI Engineer
# """
# prompt = f"""
# Answer the user's question using the provided context.
# Context:
# {user_context}
# Question:
# {user_question}
# """
# async def stream_response():
#     stream = await call_llm_stream(prompt)
#     async for chunk in stream:
#         yield chunk

# ============================================================
# 18. AI Course Assistant
# ============================================================
# Question:
# Create a conceptual streaming architecture for an AI Course
# Assistant.
# The flow should be:
# User -> FastAPI -> Build Prompt -> Async LLM -> Stream Chunks -> Frontend
# Implement the backend portion.
# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# app = FastAPI()
# async def call_llm_stream(prompt):
#     # Conceptual placeholder
#     ...
# async def course_stream(question):
#     prompt = f"""
# You are an AI course assistant.
# User question:
# {question}
# """
#     stream = await call_llm_stream(prompt)
#     async for chunk in stream:
#         yield chunk
# @app.post("/course/chat")
# async def course_chat(question: str):
#     return StreamingResponse(
#         course_stream(question),
#         media_type="text/plain"
#     )

# ============================================================
# 19. Interview Question
# ============================================================
# Question:
# What is streaming in an LLM application?
# Answer:
# Streaming is the process of delivering an LLM's generated
# response incrementally as it becomes available instead of
# waiting for the complete response.

# ============================================================
# 20. Interview Question
# ============================================================
# Question:
# Why is streaming useful?
# Answer:
# It allows users to see the beginning of the response earlier
# and provides a more interactive experience.

# ============================================================
# 21. Interview Question
# ============================================================
# Question:
# What is asynchronous programming?
# Answer:
# Asynchronous programming allows an application to efficiently
# handle operations that spend time waiting for I/O.

# ============================================================
# 22. Interview Question
# ============================================================
# Question:
# What do async and await mean?
# Answer:
# async defines an asynchronous function, while await waits for
# an asynchronous operation inside that function.

# ============================================================
# 23. Interview Question
# ============================================================
# Question:
# Are streaming and async the same?
# Answer:
# No.
# Streaming controls how the response is delivered.
# Async controls how the application handles asynchronous
# operations.

# ============================================================
# 24. Interview Question
# ============================================================
# Question:
# What is yield used for in streaming?
# Answer:
# yield allows a function to produce and send values
# incrementally instead of returning all values at once.

# ============================================================
# 25. Interview Question
# ============================================================
# Question:
# What is StreamingResponse in FastAPI?
# Answer:
# StreamingResponse is a FastAPI response class used to send
# response data progressively to the client.

# ============================================================
# 26. Interview Question
# ============================================================
# Question:
# Why are async LLM calls useful?
# Answer:
# LLM API calls involve network I/O and waiting. Async calls can
# help an application handle other concurrent work efficiently
# while waiting for the LLM response.

# ============================================================
# 27. Interview Question
# ============================================================
# Question:
# Does async always make an application faster?
# Answer:
# No.
# Async mainly improves how I/O-bound operations are handled
# concurrently. It does not automatically make every operation
# faster.

# ============================================================
# 28. Interview Question
# ============================================================
# Question:
# Does streaming reduce LLM generation time?
# Answer:
# Not necessarily.
# Streaming mainly reduces perceived latency because the user
# receives output before the complete response is generated.

# ============================================================
# 29. Final Mini Project
# ============================================================
# Build:
# AI Streaming Course Assistant
# Requirements:
# 1. Create a FastAPI application.
# 2. Create POST /chat.
# 3. Accept a user question.
# 4. Build a prompt.
# 5. Call a conceptual async LLM stream.
# 6. Iterate over chunks using async for.
# 7. Yield every chunk.
# 8. Return StreamingResponse.
# 9. Use text/plain.
# 10. Handle possible streaming errors.
# Architecture:
# User -> FastAPI -> Prompt -> Async LLM -> Stream Chunks -> StreamingResponse -> Frontend
# Starter structure:
# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# app = FastAPI()
# async def call_llm_stream(prompt):
#     # Implement using your chosen LLM provider later.
#     ...
# async def generate_response(question):
#     prompt = f"""
# You are an AI course assistant.
# Answer this question:
# {question}
# """
#     stream = await call_llm_stream(prompt)
#     async for chunk in stream:
#         yield chunk
# @app.post("/chat")
# async def chat(question: str):
#     return StreamingResponse(
#         generate_response(question),
#         media_type="text/plain"
#     )