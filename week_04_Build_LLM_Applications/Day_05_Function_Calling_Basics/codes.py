# Week 04 — Day 05: Function Calling Basics
# Practice
# ============================================================
# Instructions
# ============================================================
#
# All questions and solutions are commented initially.
# Uncomment each section when you want to practice.
#
# The LLM/tool-calling examples are conceptual unless stated
# otherwise. They are not tied to a specific provider SDK.
#
# ============================================================
# ============================================================
# 1. Basic Python Function
# ============================================================
# Question:
# Create a function called get_course().
#
# It should accept course_id as an integer and return:
#
# - id
# - name
# - level
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
#
# result = get_course(10)
# print(result)

# ============================================================
# 2. Calculate Total
# ============================================================
# Question:
# Create a function:
#
# calculate_total(price, quantity)
#
# Return price * quantity.
# def calculate_total(price: float, quantity: int):
#     return price * quantity
#
#
# result = calculate_total(1000, 3)
# print(result)

# ============================================================
# 3. Weather Tool
# ============================================================
# Question:
# Create a function called get_weather().
#
# It should accept city as a string and return a simple
# dictionary containing:
#
# city
# temperature
# condition
# def get_weather(city: str):
#     return {
#         "city": city,
#         "temperature": 25,
#         "condition": "Sunny"
#     }
#
#
# print(get_weather("Dehradun"))

# ============================================================
# 4. Function Schema
# ============================================================
# Question:
# Create a conceptual function schema for:
#
# get_weather(city)
#
# Include:
#
# - name
# - description
# - parameters
# - city type
# weather_schema = {
#     "name": "get_weather",
#     "description": "Get the current weather for a city.",
#     "parameters": {
#         "city": {
#             "type": "string"
#         }
#     }
# }
#
#
# print(weather_schema)

# ============================================================
# 5. Course Function Schema
# ============================================================
# Question:
# Create a function schema for:
#
# get_course(course_id)
#
# course_id should be an integer.
# course_schema = {
#     "name": "get_course",
#     "description": "Get course information using a course ID.",
#     "parameters": {
#         "course_id": {
#             "type": "integer"
#         }
#     }
# }
#
#
# print(course_schema)

# ============================================================
# 6. Tool Call Representation
# ============================================================
# Question:
# Represent this tool call using a Python dictionary:
#
# Function:
# get_course
#
# Argument:
# course_id = 10
# tool_call = {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
#
# print(tool_call)

# ============================================================
# 7. Execute a Tool Call
# ============================================================
# Question:
# Given the following tool call:
#
# {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
# Execute the correct Python function.
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
#
# tool_call = {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
#
# if tool_call["name"] == "get_course":
#     result = get_course(
#         tool_call["arguments"]["course_id"]
#     )
#
# print(result)

# ============================================================
# 8. Multiple Tools
# ============================================================
# Question:
# Create these functions:
#
# - get_course()
# - search_courses()
# - calculate_price()
#
# Then create a dictionary mapping tool names to functions.
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
#
# def search_courses(language: str, level: str):
#     return [
#         {
#             "name": "Python",
#             "language": language,
#             "level": level
#         }
#     ]
#
#
# def calculate_price(price: float, quantity: int):
#     return price * quantity
#
#
# tools = {
#     "get_course": get_course,
#     "search_courses": search_courses,
#     "calculate_price": calculate_price
# }
#
#
# print(tools)

# ============================================================
# 9. Select a Tool
# ============================================================
# Question:
# Given a tool call, find the correct function from the tools
# dictionary and execute it.
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
#
# def calculate_price(price: float, quantity: int):
#     return price * quantity
#
#
# tools = {
#     "get_course": get_course,
#     "calculate_price": calculate_price
# }
#
#
# tool_call = {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
#
# function = tools.get(tool_call["name"])
#
# if function:
#     result = function(**tool_call["arguments"])
#     print(result)

# ============================================================
# 10. Validate Tool Name
# ============================================================
# Question:
# Check whether the requested tool exists before executing it.
#
# If it does not exist, print:
#
# "Unknown tool"
# tools = {
#     "get_course": lambda course_id: {
#         "id": course_id,
#         "name": "FastAPI"
#     }
# }
#
#
# tool_call = {
#     "name": "unknown_tool",
#     "arguments": {}
# }
#
#
# function = tools.get(tool_call["name"])
#
# if function:
#     result = function(**tool_call["arguments"])
#     print(result)
# else:
#     print("Unknown tool")

# ============================================================
# 11. Validate Tool Arguments
# ============================================================
# Question:
# Before executing get_course(), check that course_id exists.
#
# If course_id is missing, print:
#
# "course_id is required"
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
#
# tool_call = {
#     "name": "get_course",
#     "arguments": {}
# }
#
#
# arguments = tool_call["arguments"]
#
# if "course_id" not in arguments:
#     print("course_id is required")
# else:
#     print(get_course(arguments["course_id"]))

# ============================================================
# 12. Function Result to LLM
# ============================================================
# Question:
# Simulate the complete flow:
#
# 1. User asks for course information.
# 2. LLM generates a tool call.
# 3. Application executes the function.
# 4. Function result is produced.
# 5. Result is sent back to the LLM.
#
# Keep the LLM part conceptual.
# user_message = "Tell me about course 10."
#
#
# # Conceptual LLM tool call:
# tool_call = {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
#
# result = get_course(
#     tool_call["arguments"]["course_id"]
# )
#
#
# print("Tool Result:")
# print(result)
#
#
# # Conceptually this result would be sent back to the LLM.

# ============================================================
# 13. Course Price Tool
# ============================================================
# Question:
# Create:
#
# get_course_price(course_id)
#
# Return a price for the requested course.
#
# Then simulate:
#
# User:
# "What is the price of course 101?"
#
# Tool call:
# get_course_price(101)
# def get_course_price(course_id: int):
#     prices = {
#         101: 4999,
#         102: 2999,
#         103: 3999
#     }
#
#     return prices.get(course_id)
#
#
# result = get_course_price(101)
# print(result)

# ============================================================
# 14. Search Courses Tool
# ============================================================
# Question:
# Create:
#
# search_courses(language, level)
#
# Return courses matching the given language and level.
# courses = [
#     {
#         "name": "Python Basics",
#         "language": "Python",
#         "level": "beginner"
#     },
#     {
#         "name": "Advanced Python",
#         "language": "Python",
#         "level": "advanced"
#     },
#     {
#         "name": "FastAPI Basics",
#         "language": "Python",
#         "level": "beginner"
#     }
# ]
#
#
# def search_courses(language: str, level: str):
#     return [
#         course
#         for course in courses
#         if course["language"].lower() == language.lower()
#         and course["level"].lower() == level.lower()
#     ]
#
#
# print(search_courses("Python", "beginner"))

# ============================================================
# 15. External API Tool
# ============================================================
# Question:
# Create a conceptual get_weather(city) tool.
#
# Do not make a real API request.
#
# Return simulated weather data.
# def get_weather(city: str):
#     return {
#         "city": city,
#         "temperature": 25,
#         "condition": "Sunny"
#     }
#
#
# print(get_weather("Dehradun"))

# ============================================================
# 16. Tool Router
# ============================================================
# Question:
# Create a simple tool router.
#
# It should:
#
# 1. Receive a tool call.
# 2. Find the function.
# 3. Execute it.
# 4. Return the result.
#
# Handle an unknown tool.
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
#
# def calculate_price(price: float, quantity: int):
#     return price * quantity
#
#
# tools = {
#     "get_course": get_course,
#     "calculate_price": calculate_price
# }
#
#
# def execute_tool(tool_call):
#     tool_name = tool_call["name"]
#     arguments = tool_call["arguments"]
#
#     function = tools.get(tool_name)
#
#     if function is None:
#         return {
#             "error": "Unknown tool"
#         }
#
#     return function(**arguments)
#
#
# tool_call = {
#     "name": "get_course",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
#
# print(execute_tool(tool_call))

# ============================================================
# 17. Function Calling with FastAPI
# ============================================================
# Question:
# Create a conceptual FastAPI endpoint:
#
# POST /course-info
#
# It should:
#
# 1. Receive a question.
# 2. Send the question to the LLM with get_course as a tool.
# 3. Return the response.
#
# The LLM function is conceptual.
# from fastapi import FastAPI
#
#
# app = FastAPI()
#
#
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "Beginner"
#     }
#
#
# async def call_llm(question, tools):
#     # Conceptual placeholder
#     ...
#
#
# @app.post("/course-info")
# async def course_info(question: str):
#     response = await call_llm(
#         question,
#         tools=[get_course]
#     )
#
#     return response

# ============================================================
# 18. Course Support Tool
# ============================================================
# Question:
# Create a function:
#
# get_course_details(course_name)
#
# It should return:
#
# - course
# - duration
#
# Example:
#
# FastAPI
# 30 hours
# def get_course_details(course_name: str):
#
#     courses = {
#         "FastAPI": {
#             "course": "FastAPI",
#             "duration": "30 hours"
#         },
#         "Python": {
#             "course": "Python",
#             "duration": "40 hours"
#         }
#     }
#
#     return courses.get(course_name)

# ============================================================
# 19. Tool Argument Validation
# ============================================================
# Question:
# Create get_course(course_id).
#
# Validate that course_id is an integer before executing the
# function.
#
# If invalid, return an error.
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }
#
#
# def validate_course_id(course_id):
#     if not isinstance(course_id, int):
#         return False
#
#     return True
#
#
# course_id = "10"
#
#
# if validate_course_id(course_id):
#     print(get_course(course_id))
# else:
#     print("Invalid course_id")

# ============================================================
# 20. Multiple Tool Selection
# ============================================================
# Question:
# Simulate two different user requests:
#
# Request 1:
# "Find Python courses for beginners."
#
# Request 2:
# "What is the price of course 10?"
#
# Create conceptual tool calls for both.
# request_1_tool_call = {
#     "name": "search_courses",
#     "arguments": {
#         "language": "Python",
#         "level": "beginner"
#     }
# }
#
#
# request_2_tool_call = {
#     "name": "get_course_price",
#     "arguments": {
#         "course_id": 10
#     }
# }
#
#
# print(request_1_tool_call)
# print(request_2_tool_call)

# ============================================================
# 21. Interview Question
# ============================================================
# Question:
# What is function calling?
#
# Answer:
# Function calling allows an LLM to request that a specific
# function in the application be executed using structured
# arguments.

# ============================================================
# 22. Interview Question
# ============================================================
# Question:
# Does the LLM execute the function?
#
# Answer:
# No.
#
# The LLM generates a tool/function request, while the
# application executes the actual function.

# ============================================================
# 23. Interview Question
# ============================================================
# Question:
# Why is function calling useful?
#
# Answer:
# It allows LLM applications to interact with databases,
# APIs, external services, and application logic.

# ============================================================
# 24. Interview Question
# ============================================================
# Question:
# What is a function schema?
#
# Answer:
# A function schema describes the function's name, purpose,
# arguments, and argument types so the LLM knows how the
# function can be used.

# ============================================================
# 25. Interview Question
# ============================================================
# Question:
# What is a tool call?
#
# Answer:
# A tool call is the structured request generated by the LLM
# asking the application to execute a particular tool with
# specific arguments.

# ============================================================
# 26. Interview Question
# ============================================================
# Question:
# What happens after a function is executed?
#
# Answer:
# The application sends the function result back to the LLM,
# which can use that result to generate the final response.

# ============================================================
# 27. Interview Question
# ============================================================
# Question:
# Can an LLM use multiple functions?
#
# Answer:
# Yes.
#
# An application can provide multiple tools, and the model can
# request the tool that is appropriate for the user's request.

# ============================================================
# 28. Interview Question
# ============================================================
# Question:
# How is function calling related to AI agents?
#
# Answer:
# Function calling provides the mechanism through which agents
# interact with external tools and systems.

# ============================================================
# 29. Mini Project
# ============================================================
# Build:
#
# AI Course Support Tool Calling API
#
# Requirements:
#
# 1. Create a FastAPI application.
# 2. Create course-related Python functions.
# 3. Define conceptual tool schemas.
# 4. Provide the tools to the LLM.
# 5. Receive a tool call.
# 6. Validate the tool arguments.
# 7. Execute the requested function.
# 8. Send the function result back to the LLM.
# 9. Return the final response.
#
# Suggested tools:
#
# - get_course()
# - get_course_price()
# - search_courses()
# - get_course_details()
#
# Architecture:
#
# User -> FastAPI -> LLM -> Tool Call -> Validate Arguments -> Execute Function -> Tool Result -> LLM -> Final Response
#
# Starter structure:
#
# from fastapi import FastAPI
#
#
# app = FastAPI()
#
#
# def get_course(course_id: int):
#     ...
#
#
# def get_course_price(course_id: int):
#     ...
#
#
# def search_courses(language: str, level: str):
#     ...
#
#
# async def call_llm(question, tools):
#     # Conceptual placeholder
#     ...
#
#
# @app.post("/course-support")
# async def course_support(question: str):
#
#     response = await call_llm(
#         question,
#         tools=[
#             get_course,
#             get_course_price,
#             search_courses
#         ]
#     )
#
#     return response

# ============================================================
# Final Revision
# ============================================================
#
# Function Calling
# -> LLM requests a function.
#
# Tool
# -> External capability available through the application.
#
# Function Schema
# -> Describes the function and its arguments.
#
# Tool Call
# -> Structured request generated by the LLM.
#
# Function Execution
# -> Performed by the application.
#
# Tool Result
# -> Result returned from the function.
#
# Final Response
# -> LLM uses the tool result to answer the user.
#
#
# Main mental model:
#
# User -> LLM -> Tool Call -> Application -> Function -> Tool Result -> LLM -> Final Answer
#
#
# Most important concept:
#
# LLM
# -> Decides what tool to request.
#
# Application
# -> Controls and executes the tool.
#
# ============================================================