<!-- # Week 04 — Day 06: LLM Application Patterns
# Practice File
# NOTE:
# Questions and solutions are commented initially.
# Uncomment the code when you are ready to practice.
# ============================================================

# ============================================================
# Q1. Basic Text Generation
# ============================================================
# Task:
# Create a function that generates text using an LLM.

# def call_llm(prompt: str):
#     # Conceptual placeholder for an LLM API call.
#     return "Generated response"

# def generate_text(instruction: str):
#     return call_llm(instruction)

# print(generate_text("Write a short introduction about Python."))

# ============================================================
# Q2. Summarization
# ============================================================
# Task:
# Create a function that creates a summarization prompt.

# def summarize(text: str):
#     prompt = f"""
# Summarize the following text in 5 bullet points:
# {text}
# """
#     return call_llm(prompt)

# ============================================================
# Q3. Classification
# ============================================================
# Task:
# Classify a customer message into one of these categories:
# billing, technical, account, general

# def classify_message(message: str):
#     prompt = f"""
# Classify this customer message.
# Categories:
# - billing
# - technical
# - account
# - general

# Message:
# {message}
# """
#     return call_llm(prompt)

# ============================================================
# Q4. Information Extraction
# ============================================================
# Task:
# Extract the following information from a resume:
# - Name
# - Skills
# - Experience
# - Education

# def extract_resume_info(resume: str):
#     prompt = f"""
# Extract the following information:
# - Name
# - Skills
# - Experience
# - Education

# Resume:
# {resume}
# """
#     return call_llm(prompt)

# ============================================================
# Q5. Question Answering
# ============================================================
# Task:
# Create a function that asks an LLM a question.

# def answer_question(question: str):
#     prompt = f"""
# Answer the following question clearly:
# {question}
# """
#     return call_llm(prompt)

# ============================================================
# Q6. Question Answering with Context
# ============================================================
# Task:
# Create a question-answering function that uses provided context.

# def answer_with_context(question: str, context: str):
#     prompt = f"""
# Answer the question using only the provided context.

# Context:
# {context}

# Question:
# {question}
# """
#     return call_llm(prompt)

# ============================================================
# Q7. Recommendation
# ============================================================
# Task:
# Recommend a course based on the user's goal and level.

# def recommend_course(goal: str, level: str):
#     prompt = f"""
# Recommend a suitable course.

# Goal:
# {goal}

# Level:
# {level}
# """
#     return call_llm(prompt)

# ============================================================
# Q8. Translation
# ============================================================
# Task:
# Translate text into a requested language.

# def translate(text: str, language: str):
#     prompt = f"""
# Translate the following text into {language}.

# Text:
# {text}
# """
#     return call_llm(prompt)

# ============================================================
# Q9. Sentiment Analysis
# ============================================================
# Task:
# Determine whether the text is positive, negative, or neutral.

# def analyze_sentiment(text: str):
#     prompt = f"""
# Determine the sentiment of the following text.
# Return one of:
# - positive
# - negative
# - neutral

# Text:
# {text}
# """
#     return call_llm(prompt)

# ============================================================
# Q10. Content Generation
# ============================================================
# Task:
# Generate a professional email about a given topic.

# def generate_email(topic: str):
#     prompt = f"""
# Write a professional email about:
# {topic}
# """
#     return call_llm(prompt)

# ============================================================
# Q11. Structured Output
# ============================================================
# Task:
# Convert this text into structured information:
# "John has 5 years of Python experience."

# Expected structure:
# {
#   "name": "John",
#   "experience": 5,
#   "skill": "Python"
# }

# def extract_structured_data(text: str):
#     prompt = f"""
# Extract the following information:
# - name
# - experience
# - skill

# Return the result as structured data.

# Text:
# {text}
# """
#     return call_llm(prompt)

# ============================================================
# Q12. Multiple Patterns
# ============================================================
# Task:
# Design the flow for an AI Resume Analyzer.
# It should:
# 1. Extract information from the resume.
# 2. Classify the candidate.
# 3. Compare skills.
# 4. Generate a recommendation.

# Expected flow:
# Resume -> Information Extraction -> Classification -> Skill Comparison -> Recommendation -> Final Report

# ============================================================
# Q13. Customer Support Pattern
# ============================================================
# Task:
# Design the LLM flow for an AI customer support application.

# Expected flow:
# Customer Message -> Classification -> Question Answering -> Recommendation / Action -> Final Response

# ============================================================
# Q14. Course Assistant
# ============================================================
# Task:
# Design the flow for an AI Course Assistant.

# User:
# "I am a beginner and want to learn backend development with Python."

# Expected flow:
# User Request -> Classification -> Understand User Goal -> Course Retrieval -> Recommendation -> LLM -> Final Answer

# ============================================================
# Q15. Course Question Answering
# ============================================================
# Task:
# Design a flow for answering questions about course content.

# Expected flow:
# User Question -> Question Answering -> Course Context -> LLM -> Answer

# ============================================================
# Q16. Course Summarization
# ============================================================
# Task:
# Design a flow that summarizes course content.

# Expected flow:
# Course Content -> Summarization -> Short Summary

# ============================================================
# Q17. Choose the Correct Pattern
# ============================================================
# Task:
# Identify the correct LLM pattern for each problem.

# 1. Make a short version of a document.
# 2. Determine a customer message category.
# 3. Extract information from a resume.
# 4. Answer a user's question.
# 5. Suggest a course.
# 6. Convert English text into Hindi.
# 7. Determine whether feedback is positive or negative.
# 8. Create a professional email.

# Answers:
# 1. Summarization
# 2. Classification
# 3. Information ExtractionHere is the completed practice file with full Python implementations, structured models, clean architectural flows, and answers to all theory/interview questions.

---

### Python Implementation (Questions 1–11, 20–23)

```python
import json
import re
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

# Mock LLM Caller for demonstration purposes
def call_llm(prompt: str) -> str:
    """Mock implementation representing an LLM API invocation."""
    return f"[LLM Response generated for prompt of length {len(prompt)}]"

# ============================================================
# Q1. Basic Text Generation
# ============================================================
def generate_text(instruction: str) -> str:
    return call_llm(instruction)

# ============================================================
# Q2. Summarization
# ============================================================
def summarize(text: str) -> str:
    prompt = f"""Summarize the following text in exactly 5 concise bullet points:

{text}"""
    return call_llm(prompt)

# ============================================================
# Q3. Classification
# ============================================================
def classify_message(message: str) -> str:
    prompt = f"""Classify the customer message into exactly one of these categories:
- billing
- technical
- account
- general

Return only the category name in lowercase.

Message:
{message}"""
    return call_llm(prompt)

# ============================================================
# Q4. Information Extraction
# ============================================================
def extract_resume_info(resume: str) -> str:
    prompt = f"""Extract the following information from the resume below:
- Full Name
- Primary Skills
- Years/Details of Experience
- Highest Education

Resume Text:
{resume}"""
    return call_llm(prompt)

# ============================================================
# Q5. Question Answering
# ============================================================
def answer_question(question: str) -> str:
    prompt = f"""Answer the following question accurately and concisely:

Question: {question}"""
    return call_llm(prompt)

# ============================================================
# Q6. Question Answering with Context (RAG Pattern)
# ============================================================
def answer_with_context(question: str, context: str) -> str:
    prompt = f"""You are a helpful assistant. Answer the question using ONLY the provided context.
If the answer cannot be deduced from the context, state "I cannot answer based on the provided context."

Context:
{context}

Question:
{question}"""
    return call_llm(prompt)

# ============================================================
# Q7. Recommendation
# ============================================================
def recommend_course(goal: str, level: str) -> str:
    prompt = f"""Recommend a suitable learning course based on the user's background:
Target Goal: {goal}
Current Proficiency Level: {level}

Provide the top 2 course recommendations with a brief justification for each."""
    return call_llm(prompt)

# ============================================================
# Q8. Translation
# ============================================================
def translate(text: str, target_language: str) -> str:
    prompt = f"""Translate the following text into {target_language}. Maintain the tone and nuances of the original text.

Text:
{text}"""
    return call_llm(prompt)

# ============================================================
# Q9. Sentiment Analysis
# ============================================================
def analyze_sentiment(text: str) -> str:
    prompt = f"""Determine the sentiment of the following text.
Respond with strictly one word: 'positive', 'negative', or 'neutral'.

Text:
{text}"""
    return call_llm(prompt)

# ============================================================
# Q10. Content Generation
# ============================================================
def generate_email(topic: str) -> str:
    prompt = f"""Write a professional email regarding:
{topic}

Include a clear Subject line, formal Salutation, Body, Call to Action, and Sign-off."""
    return call_llm(prompt)

# ============================================================
# Q11 & Q23. Structured Output with Pydantic
# ============================================================
class CandidateProfile(BaseModel):
    name: str = Field(description="Full name of the candidate")
    experience_years: float = Field(description="Total years of professional experience")
    skills: List[str] = Field(description="List of primary technical or domain skills")
    education: Optional[str] = Field(None, description="Highest degree or educational institution")

def extract_structured_data(text: str) -> Dict[str, Any]:
    prompt = f"""Extract structured information from the text and format it as a valid JSON object.

JSON Schema:
{json.dumps(CandidateProfile.model_json_schema(), indent=2)}

Input Text:
{text}"""
    # LLM execution step
    raw_response = call_llm(prompt)
    # In practice: return CandidateProfile.model_validate_json(raw_response).model_dump()
    return {"name": "John", "experience_years": 5.0, "skills": ["Python"]}

# ============================================================
# Q20 & Q21. Separating Business Logic from LLM Explanations
# ============================================================
def calculate_price(unit_price: float, quantity: int, discount_rate: float = 0.0) -> float:
    """Deterministic business logic handles exact arithmetic calculations."""
    subtotal = unit_price * quantity
    return subtotal * (1.0 - discount_rate)

def explain_price(unit_price: float, quantity: int, discount_rate: float, total_price: float) -> str:
    """LLM is restricted to generating natural language explanations of pre-computed data."""
    prompt = f"""Explain this price breakdown to the customer in a clear, friendly tone:
- Unit Price: ${unit_price:.2f}
- Quantity: {quantity}
- Applied Discount: {discount_rate * 100}%
- Total Calculated Price: ${total_price:.2f}"""
    return call_llm(prompt)

# ============================================================
# Q22. Context Scope Control
# ============================================================
def answer_course_question(question: str, relevant_chunks: List[str]) -> str:
    """Passes only targeted vector-retrieved context chunks to minimize latency and token usage."""
    joined_context = "\n---\n".join(relevant_chunks)
    prompt = f"""Answer the user's question using ONLY the provided course excerpts.

Context:
{joined_context}

Question:
{question}"""
    return call_llm(prompt) -->