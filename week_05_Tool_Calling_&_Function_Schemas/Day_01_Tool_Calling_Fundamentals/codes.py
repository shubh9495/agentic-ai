# ============================================================
# Week 05 — Day 01: Tool Calling Fundamentals
# Practice File
# NOTE:
# Questions, tasks, and solutions are commented initially.
# Uncomment them when you are ready to practice.
# ============================================================

# ============================================================
# Q1. Create a Basic Tool
# ============================================================
# Task:
# Create a Python function that returns course information.
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
# print(get_course(10))

# ============================================================
# Q2. Understand LLM vs Application
# ============================================================
# Task:
# Explain the responsibility of each component.
#
# LLM:
# - Understands the user's request.
# - Decides whether a tool is needed.
#
# Application:
# - Receives the tool call.
# - Validates arguments.
# - Executes the tool.
#
# Tool:
# - Represents an external capability.

# ============================================================
# Q3. Function Calling vs Tool Calling
# ============================================================
# Task:
# Write examples of:
#
# Function calling:
# get_course(course_id=10)
#
# Tool calling:
# search_courses()
# get_course()
# get_weather()
# calculate_price()

# ============================================================
# Q4. Create a Tool Definition
# ============================================================
# Task:
# Create a conceptual tool definition for get_course.
#
# tool = {
#     "name": "get_course",
#     "description": "Get course information using a course ID.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "course_id": {
#                 "type": "integer",
#                 "description": "The unique ID of the course."
#             }
#         },
#         "required": ["course_id"]
#     }
# }
# print(tool)

# ============================================================
# Q5. Design a Good Tool Name
# ============================================================
# Task:
# Decide which tool name is better.
#
# Bad:
# do_task()
#
# Good:
# search_courses()
#
# Reason:
# The tool name should clearly communicate what the tool does.

# ============================================================
# Q6. Write a Good Tool Description
# ============================================================
# Task:
# Write a useful description for search_courses.
#
# description = """
# Search available courses based on technology,
# level, and learning goal.
# """
# print(description)

# ============================================================
# Q7. Define Tool Parameters
# ============================================================
# Task:
# Define parameters for:
# search_courses(technology, level)
#
# Expected:
# technology → string
# level → string
#
# parameters = {
#     "technology": {
#         "type": "string"
#     },
#     "level": {
#         "type": "string"
#     }
# }
# print(parameters)

# ============================================================
# Q8. Required and Optional Parameters
# ============================================================
# Task:
# Design a search_courses tool where:
# technology → required
# level → optional
#
# def search_courses(technology: str, level: str | None = None):
#     return {
#         "technology": technology,
#         "level": level
#     }
#
# print(search_courses("Python"))
# print(search_courses("Python", "beginner"))

# ============================================================
# Q9. Tool Parameter Validation
# ============================================================
# Task:
# Validate that course_id is an integer before execution.
#
# def get_course(course_id):
#     if not isinstance(course_id, int):
#         raise ValueError("course_id must be an integer")
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
# print(get_course(10))

# ============================================================
# Q10. Invalid Tool Argument
# ============================================================
# Task:
# Test what happens when the model provides:
# course_id = "hello"
# The application should reject the value.
#
# try:
#     print(get_course("hello"))
# except ValueError as error:
#     print(error)

# ============================================================
# Q11. Tool Call Lifecycle
# ============================================================
# Task:
# Write the complete tool calling lifecycle.
#
# Expected:
# 1. User sends request
# 2. Application sends request + tool definitions to LLM
# 3. LLM decides whether a tool is needed
# 4. LLM generates tool call
# 5. Application receives tool call
# 6. Application validates arguments
# 7. Application executes tool
# 8. Tool returns result
# 9. Result is sent back to LLM
# 10. LLM generates final response

# ============================================================
# Q12. Tool Execution
# ============================================================
# Task:
# Map a tool call to the actual Python function.
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
# tool_call = {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
# result = get_course(tool_call["arguments"]["course_id"])
# print(result)

# ============================================================
# Q13. Tool Result
# ============================================================
# Task:
# Create a tool that returns course data.
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner",
#         "duration": 30
#     }
#
# result = get_course(10)
# print(result)

# ============================================================
# Q14. Multiple Tools
# ============================================================
# Task:
# Create three tools:
# 1. get_course()
# 2. search_courses()
# 3. get_course_price()
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
# def search_courses(technology: str, level: str):
#     return {
#         "technology": technology,
#         "level": level,
#         "courses": ["FastAPI", "Django"]
#     }
#
# def get_course_price(course_id: int):
#     return {
#         "course_id": course_id,
#         "price": 4999
#     }

# ============================================================
# Q15. Simple Tool Selection
# ============================================================
# Task:
# Based on the user's request, select the correct tool.
#
# Request:
# "Find beginner Python courses."
# Expected:
# search_courses()
#
# Request:
# "Tell me about course 10."
# Expected:
# get_course()
#
# Request:
# "What is the price of course 10?"
# Expected:
# get_course_price()

# ============================================================
# Q16. Tool Registry
# ============================================================
# Task:
# Create a simple tool registry.
#
# def get_course(course_id: int):
#     return {"id": course_id, "name": "FastAPI"}
#
# def search_courses(technology: str, level: str):
#     return {"technology": technology, "level": level}
#
# def get_course_price(course_id: int):
#     return {"course_id": course_id, "price": 4999}
#
# tools = {
#     "get_course": get_course,
#     "search_courses": search_courses,
#     "get_course_price": get_course_price
# }
# print(tools)

# ============================================================
# Q17. Execute a Tool from Registry
# ============================================================
# Task:
# Use a tool name to find and execute the corresponding function.
#
# def get_course(course_id: int):
#     return {"id": course_id, "name": "FastAPI"}
#
# tools = {
#     "get_course": get_course
# }
#
# tool_name = "get_course"
# arguments = {
#     "course_id": 10
# }
#
# result = tools[tool_name](**arguments)
# print(result)

# ============================================================
# Q18. Validate Before Execution
# ============================================================
# Task:
# Validate arguments before executing the tool.
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
# arguments = {
#     "course_id": 10
# }
#
# if not isinstance(arguments["course_id"], int):
#     raise ValueError("Invalid course_id")
#
# result = get_course(**arguments)
# print(result)

# ============================================================
# Q19. Tool Result to LLM
# ============================================================
# Task:
# Imagine the tool returns:
# {
#     "id": 10,
#     "name": "FastAPI",
#     "level": "Beginner"
# }
# Create a prompt that asks the LLM to convert the result
# into a user-friendly response.
#
# def call_llm(prompt: str):
#     # Conceptual placeholder.
#     return "Course 10 is FastAPI, a beginner-level course."
#
# tool_result = {
#     "id": 10,
#     "name": "FastAPI",
#     "level": "Beginner"
# }
#
# prompt = f"""
# Explain the following course information to the user:
# {tool_result}
# """
#
# response = call_llm(prompt)
# print(response)

# ============================================================
# Q20. Weather Tool
# ============================================================
# Task:
# Create a simple conceptual weather tool.
#
# def get_weather(city: str):
#     return {
#         "city": city,
#         "temperature": 25,
#         "condition": "Clear"
#     }
#
# print(get_weather("Dehradun"))

# ============================================================
# Q21. Course Search Tool
# ============================================================
# Task:
# Create a simple course search tool.
#
# courses = [
#     {"name": "FastAPI", "technology": "Python", "level": "beginner"},
#     {"name": "Django", "technology": "Python", "level": "intermediate"},
#     {"name": "Spring Boot", "technology": "Java", "level": "beginner"}
# ]
#
# def search_courses(technology: str, level: str):
#     results = []
#     for course in courses:
#         if (
#             course["technology"].lower() == technology.lower()
#             and course["level"].lower() == level.lower()
#         ):
#             results.append(course)
#     return results
#
# print(search_courses("Python", "beginner"))

# ============================================================
# Q22. Course Price Tool
# ============================================================
# Task:
# Create a tool that returns the price of a course.
#
# course_prices = {
#     10: 4999,
#     11: 5999,
#     12: 3999
# }
#
# def get_course_price(course_id: int):
#     if course_id not in course_prices:
#         return {"error": "Course not found"}
#     return {
#         "course_id": course_id,
#         "price": course_prices[course_id]
#     }
#
# print(get_course_price(10))

# ============================================================
# Q23. Security Check
# ============================================================
# Task:
# Think about why dangerous tools should not be freely executable.
#
# Examples:
# delete_user()
# send_payment()
# send_email()
#
# Safer flow:
# LLM Tool Request
# ↓
# Validate
# ↓
# Check Permissions
# ↓
# Execute

# ============================================================
# Q24. Permission Check
# ============================================================
# Task:
# Create a simple permission check before executing a tool.
#
# def delete_user(user_id: int):
#     return f"User {user_id} deleted"
#
# is_admin = False
#
# if not is_admin:
#     print("Permission denied")
# else:
#     print(delete_user(10))

# ============================================================
# Q25. FastAPI Tool Architecture
# ============================================================
# Task:
# Write the project structure for a FastAPI application
# that uses tool calling.
#
# Expected:
# app/
# ├── routes/
# │   └── chat.py
# │
# ├── services/
# │   └── llm_service.py
# │
# └── tools/
#     ├── course_tools.py
#     └── weather_tools.py

# ============================================================
# Q26. Conceptual Tool Calling Flow
# ============================================================
# Task:
# Write the complete flow for:
# User:
# "What is the price of course 10?"
#
# Expected:
# User
# ↓
# LLM
# ↓
# get_course_price(10)
# ↓
# Application
# ↓
# Database
# ↓
# ₹4,999
# ↓
# LLM
# ↓
# Final Answer

# ============================================================
# Q27. Agent Loop Preparation
# ============================================================
# Task:
# Design a simple multi-tool flow.
#
# Example:
# User
# ↓
# LLM
# ↓
# Tool A
# ↓
# Result
# ↓
# LLM
# ↓
# Tool B
# ↓
# Result
# ↓
# LLM
# ↓
# Final Answer
#
# Remember:
# This repeated decision process is called an agent loop.

# ============================================================
# Q28. Interview Practice
# ============================================================
# Answer these without looking at the notes:
# 1. What is tool calling?
# 2. What is a tool schema?
# 3. Does the LLM execute the tool?
# 4. Why are tool descriptions important?
# 5. What are tool parameters?
# 6. What happens after a tool executes?
# 7. Can an application have multiple tools?
# 8. Why should tool arguments be validated?
# 9. How is tool calling related to agents?


# ============================================================
# Q29. Final Mini Project Challenge
# ============================================================
# Build a conceptual Tool-Enabled AI Course Assistant.
# The assistant should provide:
# 1. Course search
# 2. Course details
# 3. Course price
# 4. Weather information
#
# Suggested tools:
# search_courses()
# get_course()
# get_course_price()
# get_weather()
#
# Expected architecture:
# User
# ↓
# FastAPI
# ↓
# LLM
# ↓
# Tool Selection
# ↓
# Validate Arguments
# ↓
# Execute Tool
# ↓
# Tool Result
# ↓
# LLM
# ↓
# Final Answer
#
