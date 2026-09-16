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

# Coding Practice

# Practice 1: Environment Variables
# Import os and read an environment variable named "OPENAI_API_KEY".
# Print whether the API key exists without printing the actual key.

# Practice 2: Message Structure

# Create a list called "messages" containing
# 1. A system message
# 2. A user message
# 3. An assistant message
# Each message should contain:
# - role
# - content
# Print all messages.


# Practice 3: Build a Conversation

# Create a conversation containing:
# System: You are a Python tutor.
# User: What is a decorator?
# Assistant: Give a short answer.
# User: Give me an example.

# Print the conversation in a readable format.
# Practice 4: Add a New User Message
# Start with an existing conversation containing:
# system, user, and assistant messages.
# Ask the user for another question using input().
# Add the new user message to the conversation.
# Print the complete conversation.


# Practice 5: Count Input Characters

# Create a user prompt.
# Calculate and print the number of characters in the prompt.
# Then print:
# "Approximate input size: <number>"


# Practice 6: Build an LLM Request


# Create a Python dictionary representing an LLM API request.
# Include:
# - model
# - messages
# - temperature
# Print the request.


# Practice 7: Read an LLM Response

# Create a dictionary representing a fake LLM API response.
# Include:
# - model
# - answer
# - input_tokens
# - output_tokens
# Read and print each value separately.


# Practice 8: Calculate Total Tokens

# Create variables:
# input_tokens = 120
# output_tokens = 80
# Calculate:
# total_tokens = input_tokens + output_tokens
# Print the total number of tokens.


# Practice 9: Handle Missing API Key

# Read the API key from an environment variable.
# If the key does not exist:
# print("API key is missing")
# Otherwise:
# print("API key found")


# Practice 10: Handle API Request Errors

# Write a try/except block for an API request.
# Handle:
# - connection error
# - general exception
# Print a useful error message instead of allowing
# the program to crash.

# Practice 11: Retry Logic

# Write a simple retry loop that attempts an API request

# up to 3 times.
# If the request succeeds:
# stop retrying
# If it fails:
# try again
# After 3 failures:
# print an error message.

# Practice 12: Temperature Configuration

# Create a variable called "temperature".
# Ask the user to enter a temperature.
# Validate that the value is between 0 and 2.
# Print the valid temperature.
# If it is outside the range, print an error message.


# Practice 13: Build a Prompt Dynamically

# Ask the user for:
# - name
# - question
# Build a prompt using both values.


# Practice 14: Simple LLM Client Class

# Create a class called "LLMClient".

# The class should:
# - accept an AP key in **init**()
# - store the API key
# - contain a method called "send_request()"
# The method can simply print the request for now.
# Do not connect to a real API.


# Practice 15: Complete Request Flow

# Build a small program representing this flow:

# User Input
# ↓
# API Key
# ↓
# LLM Client
# ↓
# Request
# ↓
# Response

# The program should:
# 1. Take a question from the user.
# 2. Read an API key from an environment variable.
# 3. Create a request dictionary.
# 4. Pass the request to an LLM client.
# 5. Return a simulated response.
# Do not use a real API for this practice.

# Practice 16: Real LLM API Request


# Install and use the LLM provider SDK you are learning.
# Read the API key from an environment variable.
# Create an LLM client.
# Send a simple user prompt.
# Print the model response.
# Keep the API key outside the source code.