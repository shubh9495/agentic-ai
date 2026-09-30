# Week 04 — Day 03: Prompt Templates & Dynamic Prompts
# Practice + Interview Questions
# Uncomment one question/task at a time and solve it.
# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# Q1. What is a prompt template?
# Answer:
# A prompt template is a reusable prompt structure containing
# variables that can be replaced with dynamic values.

# Q2. What is the difference between a static and dynamic prompt?
# Answer:
# A static prompt remains the same, while a dynamic prompt
# changes based on application or user input.

# Q3. Why are prompt templates useful?
# Answer:
# They make prompts reusable, maintainable, consistent,
# and easier to modify.

# Q4. What is a variable in a prompt template?
# Answer:
# A variable is a placeholder whose value is provided
# dynamically when the prompt is created.

# Q5. What is the difference between prompt engineering and prompt templates?
# Answer:
# Prompt engineering focuses on designing effective
# instructions, while prompt templates provide a reusable
# structure for those instructions and dynamic data.

# Q6. How can prompt templates be used with FastAPI?
# Answer:
# FastAPI can receive validated user input, pass it to a
# prompt-building function, and use the generated prompt
# to call an LLM.

# Q7. Why should prompts be separated from API routes?
# Answer:
# Separating prompts from routes keeps application
# responsibilities organized and makes prompts easier
# to modify and reuse.

# Q8. What is the difference between a hardcoded prompt and a prompt template?
# Answer:
# A hardcoded prompt is written for a specific input,
# while a prompt template can be reused with different
# dynamic values.

# Q9. Why should dynamic values be validated?
# Answer:
# Dynamic values can come from users or external systems,
# so they should be validated before being used in the
# application.

# Q10. Why should irrelevant context not be added to a prompt?
# Answer:
# Only information relevant to the task should be provided.
# Adding irrelevant context makes the prompt less focused.

# ============================================================
# BASIC PROMPT TEMPLATE PRACTICE
# ============================================================
# Q11. Create a dynamic prompt using topic and level.
# Answer code:
# topic = "FastAPI"
# level = "beginner"
# prompt = f"""
# Explain {topic} for a {level} learner.

# Use simple English.
# """
# print(prompt)

# Q12. Create a prompt using role and topic.
# Answer code:
# role = "Python tutor"
# topic = "FastAPI"
# prompt = f"""
# You are a helpful {role}.

# Explain {topic} in simple English.
# """
# print(prompt)

# Q13. Create a prompt using three variables.
# Answer code:
# name = "Shubham"
# skill = "Python"
# experience = "beginner"
# prompt = f"""
# Create a learning recommendation for {name}.

# Skill:
# {skill}

# Experience:
# {experience}
# """
# print(prompt)

# ============================================================
# SYSTEM + USER PROMPT PRACTICE
# ============================================================
# Q14. Create a dynamic system prompt.
# Variables:
# - role
# - style
# - language
# - detail_level
# Answer code:
# role = "Python tutor"
# style = "beginner-friendly"
# language = "English"
# detail_level = "concise"
# system_prompt = f"""
# You are a {role}.

# Your answers should be:
# - {style}
# - {language}
# - {detail_level}
# """
# print(system_prompt)

# Q15. Create a dynamic user prompt using question and course.
# Answer code:
# question = "What is FastAPI?"
# course = "Backend Development with Python"
# user_prompt = f"""
# User question:

# {question}

# Relevant course:

# {course}

# Answer the question using the course information.
# """
# print(user_prompt)

# Q16. Create both a system prompt and user prompt.
# Answer code:
# role = "AI course advisor"
# question = "I want to learn backend development."
# level = "beginner"
# system_prompt = f"""
# You are an {role}.
# Give beginner-friendly recommendations.
# """
# user_prompt = f"""
# User question:
# {question}

# My experience is {level} level.
# """
# print(system_prompt)
# print(user_prompt)

# ============================================================
# PROMPT BUILDER FUNCTIONS
# ============================================================
# Q17. Create a reusable course prompt function.
# Answer code:
# def build_course_prompt(goal, level):
#     return f"""
# You are an AI course advisor.

# User goal:
# {goal}

# User level:
# {level}

# Recommend a suitable learning path.
# """
# prompt = build_course_prompt(
#     goal="Learn backend development",
#     level="beginner"
# )
# print(prompt)

# Q18. Create a reusable explanation prompt function.
# Answer code:
# def build_explanation_prompt(topic, level):
#     return f"""
# Explain {topic} to a {level} learner.

# Use simple English.

# Give a practical example.
# """
# print(
#     build_explanation_prompt(
#         "FastAPI",
#         "beginner"
#     )
# )

# Q19. Reuse the same prompt function for two different topics.
# Answer code:
# def build_explanation_prompt(topic, level):
#     return f"""
# Explain {topic} to a {level} learner.

# Use simple English.

# Give a practical example.
# """
# prompt_1 = build_explanation_prompt(
#     "FastAPI",
#     "beginner"
# )
# prompt_2 = build_explanation_prompt(
#     "LangGraph",
#     "intermediate"
# )
# print(prompt_1)
# print(prompt_2)

# ============================================================
# CONTEXT PRACTICE
# ============================================================
# Q20. Create a customer support prompt using:
# - question
# - customer_info
# - documentation
# Answer code:
# question = "How can I reset my password?"
# customer_info = "Premium customer"
# documentation = "Users can reset passwords from account settings."
# prompt = f"""
# You are an AI customer support assistant.

# Customer question:
# {question}

# Customer information:
# {customer_info}

# Relevant documentation:
# {documentation}

# Answer the customer's question using the provided information.
# """
# print(prompt)

# Q21. Create a RAG-style prompt using question and context.
# Answer code:
# context = "FastAPI is a Python framework for building APIs."
# question = "What is FastAPI?"
# prompt = f"""
# Context:

# {context}

# Question:

# {question}

# Instruction:

# Answer using the provided context.
# """
# print(prompt)

# Q22. Create a prompt that combines:
# - system instructions
# - conversation history
# - current user message
# Answer code:
# system_instructions = "You are a helpful AI tutor."
# conversation_history = """
# User: What is Python?
# Assistant: Python is a programming language.
# """
# current_message = "What can I build with it?"
# prompt = f"""
# System:
# {system_instructions}

# Conversation:
# {conversation_history}

# User:
# {current_message}
# """
# print(prompt)

# ============================================================
# FASTAPI PRACTICE
# ============================================================
# Q23. Create a Pydantic request model for a recommendation API.
# Answer code:
# from pydantic import BaseModel
# class RecommendationRequest(BaseModel):
#     goal: str
#     level: str

# Q24. Create a FastAPI endpoint that builds a dynamic prompt.
# Answer code:
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class RecommendationRequest(BaseModel):
#     goal: str
#     level: str
# def build_prompt(goal: str, level: str) -> str:
#     return f"""
# You are an AI course advisor.

# User goal:
# {goal}

# User level:
# {level}

# Recommend a suitable learning path.
# """
# @app.post("/recommend")
# def recommend(request: RecommendationRequest):
#     prompt = build_prompt(
#         request.goal,
#         request.level
#     )
#     return {
#         "prompt": prompt
#     }

# Q25. Separate the prompt-building logic from the API route.
# Expected structure:
# app/
# │
# ├── routes/
# │   └── recommendation.py
# │
# ├── services/
# │   └── llm_service.py
# │
# └── prompts/
#     └── recommendation.py
# Answer:
# routes/ -> Handles API requests
# services/ -> Handles application/LLM service logic
# prompts/ -> Contains reusable prompt templates

# ============================================================
# RESUME ANALYZER PRACTICE
# ============================================================
# Q26. Create a dynamic resume analyzer prompt.
# Variables:
# - name
# - role
# - skills
# Answer code:
# name = "Shubham"
# role = "Backend Developer"
# skills = "Python, FastAPI, SQL"
# prompt = f"""
# You are a technical recruiter.

# Candidate:
# {name}

# Target Role:
# {role}

# Skills:
# {skills}

# Analyze the candidate's skills against the target role.

# Identify missing skills and suggest improvements.
# """
# print(prompt)

# ============================================================
# PRACTICE: FIND THE MISTAKE
# ============================================================
# Q27. What is wrong with this approach?
# prompt = "Explain FastAPI."
# Answer:
# The prompt is hardcoded, so it is designed for one specific
# input. A prompt template can make it reusable.
# Better:
# topic = "FastAPI"
# prompt = f"Explain {topic}."

# Q28. What is wrong with this approach?
# def recommend(request):
#     prompt = f"""
# You are an AI course advisor.
# Goal: {request.goal}
# Level: {request.level}
# """
#     response = call_llm(prompt)
#     return response
# Answer:
# The approach works, but prompt logic is mixed directly
# inside the API route.
# A separate prompt-building function or prompts module
# makes the application easier to maintain.

# Q29. What is wrong with these variable names?
# x = "FastAPI"
# data = "beginner"
# value = "Python"
# Answer:
# The names do not clearly describe their purpose.
# Better:
# topic = "FastAPI"
# user_level = "beginner"
# preferred_language = "Python"

# ============================================================
# MINI PROJECT
# ============================================================
# Q30. Build a Dynamic Course Recommendation API.
# Requirements:
# 1. Create a FastAPI application.
# 2. Create POST /recommend.
# 3. Create a Pydantic request model.
# 4. Accept:
#    goal
#    level
#    preferred_language
# 5. Create a reusable prompt-building function.
# 6. Generate a dynamic prompt.
# 7. Return the generated prompt.
# Expected flow:
# POST /recommend -> Pydantic Validation -> Prompt Template -> Final Prompt -> LLM -> Response
# Answer code:
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class RecommendationRequest(BaseModel):
#     goal: str
#     level: str
#     preferred_language: str
# def build_recommendation_prompt(
#     goal: str,
#     level: str,
#     preferred_language: str
# ) -> str:
#     return f"""
# You are an AI course advisor.

# User goal:
# {goal}

# Experience:
# {level}

# Preferred language:
# {preferred_language}

# Recommend a suitable learning path.
# """
# @app.post("/recommend")
# def recommend(request: RecommendationRequest):
#     prompt = build_recommendation_prompt(
#         request.goal,
#         request.level,
#         request.preferred_language
#     )
#     return {
#         "prompt": prompt
#     }

# ============================================================
# FINAL REVISION
# ============================================================
# Q31. Complete the flow:
# User Input -> __________ -> __________ -> Final Prompt -> LLM -> Response
# Answer:
# User Input -> Application Data -> Prompt Template -> Final Prompt -> LLM -> Response

# Q32. Complete the definition:
# Prompt Template = ______________________________
# Answer:
# Prompt Template = A reusable prompt structure containing
# variables that can be replaced with dynamic values.

# Q33. Complete the difference:
# Static Prompt = ______________________________
# Dynamic Prompt = ______________________________
# Answer:
# Static Prompt = Remains the same
# Dynamic Prompt = Changes based on application or user input

# Q34. Complete the difference:
# Prompt Engineering = ___________________________
# Prompt Template = ______________________________
# Answer:
# Prompt Engineering = Designing effective instructions for an LLM
# Prompt Template = Creating a reusable structure with variables

# Q35. Write the architecture for separating prompts from application logic.
# Answer:
# Route -> Service -> Prompt -> LLM