# Week 04 — Day 02: LLM SDKs & Model Interaction
# Practice + Interview Questions
# Uncomment one question/task at a time and solve it.

# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# Q1. What is an LLM SDK?
# Answer:
# An LLM SDK is a software library that simplifies communication between an application and an LLM provider's API.

# Q2. What is the difference between an SDK and an LLM?
# Answer:
# An SDK is a programming library used to communicate with the provider, while an LLM is the model that processes inputs and generates outputs.

# Q3. What is an LLM provider?
# Answer:
# An LLM provider is a company or service that provides access to language models.
# Examples:
# OpenAI
# Google
# Anthropic

# Q4. What is a client in an LLM application?
# Answer:
# A client is the object used by the application to communicate with the LLM provider.

# Q5. What is a system message?
# Answer:
# A system message provides high-level instructions that define the model's behavior, role, or rules.

# Q6. What is a user message?
# Answer:
# A user message contains the user's request or input.

# Q7. What is an assistant message?
# Answer:
# An assistant message represents the model's generated response and can also be included in conversation history.

# Q8. What does temperature control?
# Answer:
# Temperature generally controls the randomness or variation of generated responses.

# Q9. What is max output tokens?
# Answer:
# It defines the maximum amount of output the model can generate for a request, subject to the model and provider's limits.

# Q10. Why should API keys be stored in environment variables?
# Answer:
# To keep sensitive credentials outside the source code and reduce the risk of accidentally exposing them.

# Q11. Why should API keys not be hardcoded?
# Answer:
# Hardcoded API keys can accidentally be exposed through source code, GitHub, logs, or other places.

# Q12. What is the difference between a provider, SDK, and model?
# Answer:
# Provider = Provides the service/model
# SDK = Library used to communicate with the provider
# Model = AI system that processes the request

# Q13. What is conversation history?
# Answer:
# Conversation history is the previous system, user, and assistant messages that can be provided to the model as context.

# Q14. Why can unlimited conversation history be a problem?
# Answer:
# Large conversation histories can increase token usage, cost, latency, and context pressure.

# Q15. Why is error handling important in LLM applications?
# Answer:
# LLM API calls can fail because of invalid API keys, rate limits, network errors, timeouts, invalid requests, provider outages, or token/context limits.

# Q16. How does FastAPI communicate with an LLM?
# Answer:
# A FastAPI route receives the request, prepares the input, uses an LLM SDK to call the provider's API, processes the response, and returns it to the client.

# ============================================================
# BASIC PYTHON PRACTICE
# ============================================================
# Q17. Read an API key from an environment variable.
# Answer code:
# import os
# api_key = os.getenv("LLM_API_KEY")
# print(api_key)

# Q18. Create a simple generic LLM client using an API key.
# Answer code:
# import os
# class LLMClient:
#     def __init__(self, api_key):
#         self.api_key = api_key
# api_key = os.getenv("LLM_API_KEY")
# client = LLMClient(api_key)
# print(client.api_key)

# Q19. Create a function that builds system and user messages.
# Answer code:
# def build_messages(system_message, user_message):
#     return [
#         {
#               "role": "system", 
#               "content": system_message
#          },
#         { 
#               "role": "user", 
#               "content": user_message
#          }
#     ]
# messages = build_messages("You are a helpful Python tutor.", "Explain FastAPI.")
# print(messages)

# Q20. Add an assistant message to conversation history.
# Answer code:
# conversation = [
#     {"role": "system", "content": "You are a Python tutor."},
#     {"role": "user", "content": "What is Python?"},
#     {"role": "assistant", "content": "Python is a programming language."}
# ]
# print(conversation)

# Q21. Create a function that adds a new user message to conversation history.
# Answer code:
# def add_user_message(conversation, message):
#     conversation.append({"role": "user", "content": message})
# conversation = [{"role": "system", "content": "You are a helpful assistant."}]
# add_user_message(conversation, "Explain REST API.")
# print(conversation)

# ============================================================
# LLM RESPONSE PRACTICE
# ============================================================
# Q22. Create a function that extracts text from a simple response dictionary.
# Answer code:
# response = {"text": "FastAPI is a Python web framework."}
# def extract_text(response):
#     return response["text"]
# print(extract_text(response))

# Q23. Create a structured LLM response for a course recommendation.
# Answer code:
# response = {
#     "course": "Python for AI",
#     "level": "Beginner",
#     "reason": "Good starting point for AI development"
# }
# print(response)

# Q24. Validate a structured LLM response using Pydantic.
# Answer code:
# from pydantic import BaseModel
# class CourseRecommendation(BaseModel):
#     course: str
#     level: str
#     reason: str
# response = {
#     "course": "Python for AI",
#     "level": "Beginner",
#     "reason": "Good starting point for AI development"
# }
# validated_response = CourseRecommendation(**response)
# print(validated_response)
# print(validated_response.model_dump())

# ============================================================
# ERROR HANDLING PRACTICE
# ============================================================
# Q25. Create a function that simulates an LLM API call and handles errors.
# Answer code:
# def call_llm():
#     try:
#         response = "Generated response"
#         return response
#     except Exception:
#         return "Unable to process your request."
# print(call_llm())

# Q26. Handle an invalid API key using a custom exception.
# Answer code:
# def call_llm(api_key):
#     if not api_key:
#         raise ValueError("API key is missing")
#     return "LLM response"
# try:
#     response = call_llm("")
#     print(response)
# except ValueError:
#     print("Unable to authenticate with the LLM provider.")

# Q27. Create a safe error handler for an LLM request.
# Answer code:
# def safe_llm_call():
#     try:
#         raise TimeoutError()
#     except TimeoutError:
#         return {"error": "The LLM request timed out."}
#     except Exception:
#         return {"error": "Unable to process the request."}
# print(safe_llm_call())

# ============================================================
# FASTAPI + LLM PRACTICE
# ============================================================
# Q28. Create a FastAPI /chat endpoint that accepts a user message.
# Answer code:
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class ChatRequest(BaseModel):
#     message: str
# @app.post("/chat")
# def chat(request: ChatRequest):
#     return {"message": request.message}

# Q29. Create a placeholder LLM client function.
# Answer code:
# def call_llm(messages):
#     return {"text": "This is a generated response."}
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Explain FastAPI."}
# ]
# response = call_llm(messages)
# print(response["text"])

# Q30. Build a complete basic FastAPI + LLM flow.
# Expected flow:
# Frontend -> POST /chat -> FastAPI -> Validate Request -> Build Messages -> LLM Client -> LLM -> Response -> Frontend
# Answer code:
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class ChatRequest(BaseModel):
#     message: str
# class ChatResponse(BaseModel):
#     answer: str
# def call_llm(messages):
#     return "This is a generated response."
# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     messages = [
#         {"role": "system", "content": "You are a helpful AI assistant."},
#         {"role": "user", "content": request.message}
#     ]
#     response = call_llm(messages)
#     return ChatResponse(answer=response)

# Q31. Add conversation history to the FastAPI chat flow.
# Answer code:
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class ChatRequest(BaseModel):
#     message: str
# conversation_history = [{"role": "system", "content": "You are a helpful AI assistant."}]
# def call_llm(messages):
#     return "Generated response"
# @app.post("/chat")
# def chat(request: ChatRequest):
#     conversation_history.append({"role": "user", "content": request.message})
#     response = call_llm(conversation_history)
#     conversation_history.append({"role": "assistant", "content": response})
#     return {"answer": response}

# ============================================================
# APPLICATION STRUCTURE PRACTICE
# ============================================================
# Q32. Create the following project structure:
# llm-app/
# ├── app/
# │   ├── main.py
# │   ├── llm_client.py
# │   └── prompts.py
# ├── .env
# ├── .gitignore
# └── requirements.txt
# Answer:
# Create the directories and files manually:
# llm-app/
# app/
# main.py
# llm_client.py
# prompts.py
# .env
# .gitignore
# requirements.txt

# Q33. Separate the following responsibilities:
# - API route
# - LLM communication
# - Prompt definition
# Answer:
# main.py -> API routes
# llm_client.py -> LLM communication
# prompts.py -> Prompt definitions

# ============================================================
# MODEL PARAMETERS PRACTICE
# ============================================================
# Q34. Create a configuration dictionary for an LLM request.
# Include:
# - model
# - temperature
# - max_output_tokens
# Answer code:
# config = {
#     "model": "model-name",
#     "temperature": 0.2,
#     "max_output_tokens": 200
# }
# print(config)

# Q35. Create two configurations:
# one for predictable output and one for creative output.
# Answer code:
# predictable_config = {
#     "temperature": 0.2,
#     "max_output_tokens": 200
# }
# creative_config = {
#     "temperature": 0.8,
#     "max_output_tokens": 500
# }
# print(predictable_config)
# print(creative_config)

# ============================================================
# MINI PROJECT
# ============================================================
# Q36. Build a simple FastAPI LLM Chat API.
# Requirements:
# 1. Create a FastAPI application.
# 2. Create POST /chat.
# 3. Accept a user message.
# 4. Create system + user messages.
# 5. Use a placeholder LLM client.
# 6. Handle possible errors.
# 7. Return a structured response.
# Expected architecture:
# Frontend -> POST /chat -> FastAPI -> Request Validation -> Build Messages -> LLM Client -> LLM -> Response Processing -> FastAPI -> Frontend
# Answer code:
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# app = FastAPI()
# class ChatRequest(BaseModel):
#     message: str
# class ChatResponse(BaseModel):
#     answer: str
# def call_llm(messages):
#     try:
#         return "This is a generated response."
#     except Exception:
#         raise RuntimeError("LLM request failed")
# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     messages = [
#         {"role": "system", "content": "You are a helpful AI assistant."},
#         {"role": "user", "content": request.message}
#     ]
#     try:
#         response = call_llm(messages)
#     except RuntimeError:
#         raise HTTPException(
#             status_code=500,
#             detail="Unable to process the request."
#         )
#     return ChatResponse(answer=response)

# ============================================================
# FINAL REVISION
# ============================================================
# Q37. Complete the flow:
# User -> ________ -> ________ -> LLM API -> ________ -> Response
# Answer:
# User -> Application -> LLM SDK -> LLM API -> Model -> Response

# Q38. Complete the message roles:
# ________ -> Defines model behavior
# ________ -> Contains user's request
# ________ -> Represents model response
# Answer:
# System -> Defines model behavior
# User -> Contains user's request
# Assistant -> Represents model response

# Q39. Complete the mental model:
# Provider = __________
# SDK = __________
# Client = __________
# Model = __________
# Answer:
# Provider = Provides the service/model
# SDK = Library used to communicate with provider
# Client = Object used by application to communicate
# Model = Processes the request

# Q40. Complete the parameter meanings:
# Temperature = __________
# Max Output Tokens = __________
# Answer:
# Temperature = Controls output randomness/variation
# Max Output Tokens = Limits generated output

# Q41. Write the complete LLM application flow.
# Answer:
# User -> Frontend -> FastAPI -> Validate Request -> Build Messages -> LLM SDK -> LLM API -> Model -> Response -> Process Response -> FastAPI -> Frontend -> User