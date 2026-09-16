# Week 2 — Day 3: LLM API Coding Practice

# Practice Questions

# 1. What is an LLM API?
# 2. Why do applications use LLM APIs?
# 3. What is an API key?
# 4. Why should API keys not be hardcoded?
# 5. What is an SDK?
# 6. What is an LLM client?
# 7. What are system, user, and assistant messages?
# 8. What is the difference between input and output tokens?
# 9. What does temperature control?
# 10. What can cause an LLM API request to fail?
# 11. What is a rate limit?
# 12. Why are environment variables useful?
# 13. What is the difference between an LLM and an API?
# 14. What is the difference between an LLM, a tool, and an agent?
# 15. Explain the complete flow of an LLM API request.

#Coding prectice

# ------------------------------------------------------------
# Practice 1: Environment Variables
# ------------------------------------------------------------

# Import os and read an environment variable named
# "OPENAI_API_KEY".
#
# Print whether the API key exists without printing
# the actual key.

# Answer:
# import os
#
# api_key = os.getenv("OPENAI_API_KEY")
#
# if api_key:
#     print("API key found")
# else:
#     print("API key is missing")


# ------------------------------------------------------------
# Practice 2: Message Structure
# ------------------------------------------------------------

# Create a list called "messages" containing:
# 1. A system message
# 2. A user message
# 3. An assistant message
#
# Each message should contain:
# - role
# - content
#
# Print all messages.


# Answer:
# messages = [
#     {
#         "role": "system",
#         "content": "You are a helpful assistant."
#     },
#     {
#         "role": "user",
#         "content": "What is Python?"
#     },
#     {
#         "role": "assistant",
#         "content": "Python is a programming language."
#     }
# ]
#
# for message in messages:
#     print(message)


# ------------------------------------------------------------
# Practice 3: Build a Conversation
# ------------------------------------------------------------

# Create a conversation containing:
#
# System: You are a Python tutor.
# User: What is a decorator?
# Assistant: Give a short answer.
# User: Give me an example.
#
# Print the conversation in a readable format.

# Answer:
# conversation = [
#     {
#         "role": "system",
#         "content": "You are a Python tutor."
#     },
#     {
#         "role": "user",
#         "content": "What is a decorator?"
#     },
#     {
#         "role": "assistant",
#         "content": "A decorator modifies or extends the behavior of a function."
#     },
#     {
#         "role": "user",
#         "content": "Give me an example."
#     }
# ]
#
# for message in conversation:
#     print(message["role"], ":", message["content"])


# ------------------------------------------------------------
# Practice 4: Add a New User Message
# ------------------------------------------------------------

# Start with an existing conversation containing:
# system, user, and assistant messages.
#
# Ask the user for another question using input().
# Add the new user message to the conversation.
# Print the complete conversation.

# Answer:
# conversation = [
#     {
#         "role": "system",
#         "content": "You are a Python tutor."
#     },
#     {
#         "role": "user",
#         "content": "What is a function?"
#     },
#     {
#         "role": "assistant",
#         "content": "A function is a reusable block of code."
#     }
# ]
#
# question = input("Enter your question: ")
#
# conversation.append({
#     "role": "user",
#     "content": question
# })
#
# for message in conversation:
#     print(message["role"], ":", message["content"])

# ------------------------------------------------------------
# Practice 5: Count Input Characters
# ------------------------------------------------------------

# Create a user prompt.
# Calculate and print the number of characters in the prompt.
#
# Then print:
# "Approximate input size: <number>"

# Answer:
# prompt = input("Enter your prompt: ")
#
# character_count = len(prompt)
#
# print("Number of characters:", character_count)
# print("Approximate input size:", character_count)


# ------------------------------------------------------------
# Practice 6: Build an LLM Request
# ------------------------------------------------------------

# Create a Python dictionary representing an LLM API request.
#
# Include:
# - model
# - messages
# - temperature
#
# Print the request.

# Answer:
# messages = [
#     {
#         "role": "user",
#         "content": "Explain Python decorators."
#     }
# ]
#
# request = {
#     "model": "example-model",
#     "messages": messages,
#     "temperature": 0.7
# }
#
# print(request)


# ------------------------------------------------------------
# Practice 7: Read an LLM Response
# ------------------------------------------------------------

# Create a dictionary representing a fake LLM API response.
#
# Include:
# - model
# - answer
# - input_tokens
# - output_tokens
#
# Read and print each value separately.

# Answer:
# response = {
#     "model": "example-model",
#     "answer": "A decorator modifies the behavior of a function.",
#     "input_tokens": 20,
#     "output_tokens": 15
# }
#
# print("Model:", response["model"])
# print("Answer:", response["answer"])
# print("Input tokens:", response["input_tokens"])
# print("Output tokens:", response["output_tokens"])


# ------------------------------------------------------------
# Practice 8: Calculate Total Tokens
# ------------------------------------------------------------

# Create variables:
# input_tokens = 120
# output_tokens = 80
#
# Calculate:
# total_tokens = input_tokens + output_tokens
#
# Print the total number of tokens.

# Answer:
# input_tokens = 120
# output_tokens = 80
#
# total_tokens = input_tokens + output_tokens
#
# print("Total tokens:", total_tokens)


# ------------------------------------------------------------
# Practice 9: Handle Missing API Key
# ------------------------------------------------------------

# Read the API key from an environment variable.
#
# If the key does not exist:
# print("API key is missing")
#
# Otherwise:
# print("API key found")

# Answer:
# import os
#
# api_key = os.getenv("OPENAI_API_KEY")
#
# if not api_key:
#     print("API key is missing")
# else:
#     print("API key found")


# ------------------------------------------------------------
# Practice 10: Handle API Request Errors
# ------------------------------------------------------------

# Write a try/except block for an API request.
#
# Handle:
# - connection error
# - general exception
#
# Print a useful error message instead of allowing
# the program to crash.

# Answer:
# try:
#     # Simulated API request
#     print("Sending API request...")
#
# except ConnectionError:
#     print("Connection error. Check your internet connection.")
#
# except Exception as e:
#     print("API request failed:", e)


# ------------------------------------------------------------
# Practice 11: Retry Logic
# ------------------------------------------------------------

# Write a simple retry loop that attempts an API request
# up to 3 times.
#
# If the request succeeds:
# stop retrying
#
# If it fails:
# try again
#
# After 3 failures:
# print an error message.

# Answer:
# for attempt in range(3):
#     try:
#         print("Attempt:", attempt + 1)
#
#         # Simulated API request
#         # Replace this with an actual request later.
#
#         print("Request successful")
#         break
#
#     except Exception as e:
#         print("Request failed:", e)
#
# else:
#     print("API request failed after 3 attempts.")


# ------------------------------------------------------------
# Practice 12: Temperature Configuration
# ------------------------------------------------------------

# Create a variable called "temperature".
# Ask the user to enter a temperature.
#
# Validate that the value is between 0 and 2.
#
# Print the valid temperature.
# If it is outside the range, print an error message.

# Answer:
# temperature = float(input("Enter temperature: "))
#
# if 0 <= temperature <= 2:
#     print("Valid temperature:", temperature)
# else:
#     print("Temperature must be between 0 and 2.")


# ------------------------------------------------------------
# Practice 13: Build a Prompt Dynamically
# ------------------------------------------------------------

# Ask the user for:
# - name
# - question
#
# Build a prompt using both values.

# Answer:
# name = input("Enter your name: ")
# question = input("Enter your question: ")
#
# prompt = f"Hello, I am {name}. Please answer this question: {question}"
#
# print(prompt)


# ------------------------------------------------------------
# Practice 14: Simple LLM Client Class
# ------------------------------------------------------------

# Create a class called "LLMClient".
#
# The class should:
# - accept an API key in __init__()
# - store the API key
# - contain a method called "send_request()"
#
# The method can simply print the request for now.
#
# Do not connect to a real API.

# Answer:
# class LLMClient:
#
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     def send_request(self, request):
#         print("Sending request:")
#         print(request)
#
#
# client = LLMClient("example-api-key")
#
# request = {
#     "model": "example-model",
#     "messages": [
#         {
#             "role": "user",
#             "content": "Hello"
#         }
#     ],
#     "temperature": 0.7
# }
#
# client.send_request(request)


# ------------------------------------------------------------
# Practice 15: Complete Request Flow
# ------------------------------------------------------------

# Build a small program representing this flow:
#
# User Input
#      ↓
# API Key
#      ↓
# LLM Client
#      ↓
# Request
#      ↓
# Response
#
# The program should:
# 1. Take a question from the user.
# 2. Read an API key from an environment variable.
# 3. Create a request dictionary.
# 4. Pass the request to an LLM client.
# 5. Return a simulated response.
#
# Do not use a real API for this practice.

# Answer:
# import os
#
#
# class LLMClient:
#
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     def send_request(self, request):
#         print("\nRequest sent to LLM:")
#         print(request)
#
#         response = {
#             "model": request["model"],
#             "answer": "This is a simulated LLM response.",
#             "input_tokens": 20,
#             "output_tokens": 10
#         }
#
#         return response
#
#
# question = input("Enter your question: ")
#
# api_key = os.getenv("OPENAI_API_KEY")
#
# messages = [
#     {
#         "role": "user",
#         "content": question
#     }
# ]
#
# request = {
#     "model": "example-model",
#     "messages": messages,
#     "temperature": 0.7
# }
#
# client = LLMClient(api_key)
#
# response = client.send_request(request)
#
# print("\nResponse:")
# print(response["answer"])


# ------------------------------------------------------------
# Practice 16: Real LLM API Request
# ------------------------------------------------------------

# Install and use the LLM provider SDK you are learning.
#
# Read the API key from an environment variable.
# Create an LLM client.
# Send a simple user prompt.
# Print the model response.
#
# Keep the API key outside the source code.

# Answer:
#
# For OpenAI, install the SDK:
#
# pip install openai
#
# Then:
#
# import os
# from openai import OpenAI
#
#
# api_key = os.getenv("OPENAI_API_KEY")
#
# client = OpenAI(api_key=api_key)
#
# response = client.responses.create(
#     model="gpt-5.6-mini",
#     input="Explain Python decorators in simple words."
# )
#
# print(response.output_text)
#
# IMPORTANT:
# Never write your real API key directly inside the Python file.
#
# Use an environment variable such as:
#
# OPENAI_API_KEY=your_secret_key
#
# The exact model/API syntax can change, so check the current
# provider SDK documentation when you implement this step.