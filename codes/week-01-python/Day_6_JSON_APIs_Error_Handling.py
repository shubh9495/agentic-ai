# ==================================================
# Day 6 — JSON, APIs & Error Handling
# ==================================================
#
# Topics:
# 1. JSON
# 2. JSON Objects & Arrays
# 3. JSON in Python
# 4. Serialization & Deserialization
# 5. APIs
# 6. HTTP Methods
# 7. HTTP Status Codes
# 8. Calling APIs using requests
# 9. API Parameters
# 10. Exception Handling
# 11. Custom Exceptions
# 12. API Error Handling
# 13. JSON + API
# 14. JSON + Pydantic
# 15. Error Handling in AI Applications
# 16. Practice
#
# ==================================================


# ==================================================
# 1. JSON
# ==================================================

# JSON stands for JavaScript Object Notation.
#
# Example JSON:
#
# {
#     "name": "Shubham",
#     "age": 25,
#     "is_active": true
# }
#
# JSON supports:
# - Strings
# - Numbers
# - Boolean
# - Arrays
# - Objects
# - null


# ==================================================
# 2. JSON Objects and Arrays
# ==================================================

# JSON Object:
#
# user = {
#     "name": "Shubham",
#     "age": 25
# }
#
# print(user)


# JSON Array:
#
# user = {
#     "skills": [
#         "Python",
#         "Java",
#         "React"
#     ]
# }
#
# print(user)

# Nested JSON:
#
# user = {
#     "name": "Shubham",
#     "address": {
#         "city": "Dehradun",
#         "country": "India"
#     }
# }
#
# print(user)


# ==================================================
# 3. JSON in Python
# ==================================================

# Python provides the built-in json module.
#
# import json


# Python dictionary:
#
# user = {
#     "name": "Shubham",
#     "age": 25
# }
#
# Convert Python dictionary into JSON:
#
# data = json.dumps(user)
#
# print(data)


# ==================================================
# 4. Serialization and Deserialization
# ==================================================

# Serialization:
# Python Object -> JSON
#
# import json
#
# user = {
#     "name": "Shubham",
#     "age": 25
# }
#
# json_data = json.dumps(user)
#
# print(json_data)


# Deserialization:
# JSON -> Python Object
#
# import json
#
# json_data = '{"name": "Shubham", "age": 25}'
#
# user = json.loads(json_data)
#
# print(user)
# print(user["name"])


# Remember:
#
# json.dumps() -> Python -> JSON
# json.loads() -> JSON -> Python


# ==================================================
# 5. APIs
# ==================================================

# API allows different applications to communicate.
#
# Example:
#
# Python Application
#        |
#        v
#       API
#        |
#        v
# Weather Service
#        |
#        v
# Weather Data


# Example API request:
#
# GET /users/101


# ==================================================
# 6. HTTP Methods
# ==================================================

# GET
# Retrieve data
#
# POST
# Create data
#
# PUT
# Replace or update data
#
# PATCH
# Partially update data
#
# DELETE
# Delete data


# Example:
#
# GET /users
#
# POST /users
#
# DELETE /users/101


# ==================================================
# 7. HTTP Status Codes
# ==================================================

# 2xx -> Success
#
# 200 -> OK
# 201 -> Created
# 204 -> No Content
#
#
# 4xx -> Client Error
#
# 400 -> Bad Request
# 401 -> Unauthorized
# 403 -> Forbidden
# 404 -> Not Found
#
#
# 5xx -> Server Error
#
# 500 -> Internal Server Error
# 503 -> Service Unavailable


# ==================================================
# 8. Calling APIs from Python
# ==================================================

# Install requests:
#
# pip install requests


# GET request:
#
# import requests
#
# response = requests.get(
#     "https://api.example.com/users"
# )
#
# print(response.status_code)
# print(response.json())


# POST request:
#
# import requests
#
# data = {
#     "name": "Shubham",
#     "age": 25
# }
#
# response = requests.post(
#     "https://api.example.com/users",
#     json=data
# )
#
# print(response.json())


# ==================================================
# 9. API Parameters
# ==================================================

# Path Parameter:
#
# /users/101
#
# Here 101 is the user ID.


# Query Parameter:
#
# /users?age=25
#
# Multiple query parameters:
#
# /users?age=25&city=Dehradun


# Request Body:
#
# data = {
#     "name": "Shubham",
#     "age": 25
# }


# ==================================================
# 10. Exception Handling
# ==================================================

# try:
#     number = int(input("Enter number: "))
#     print(10 / number)
#
# except ValueError:
#     print("Invalid number")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# ==================================================
# 11. else and finally
# ==================================================

# else runs when no exception occurs.
#
# try:
#     number = int("10")
#
# except ValueError:
#     print("Invalid number")
#
# else:
#     print("Conversion successful")


# finally always runs.
#
# try:
#     print("Processing")
#
# except Exception:
#     print("Error")
#
# finally:
#     print("Finished")


# ==================================================
# 12. Custom Exceptions
# ==================================================

# Create a custom exception:
#
# class InsufficientBalanceError(Exception):
#     pass


# Use custom exception:
#
# balance = 500
#
# if balance < 1000:
#     raise InsufficientBalanceError(
#         "Insufficient balance"
#     )


# ==================================================
# 13. API Error Handling
# ==================================================

# import requests
#
# try:
#     response = requests.get(
#         "https://api.example.com/users"
#     )
#
#     response.raise_for_status()
#
#     data = response.json()
#
#     print(data)
#
# except requests.RequestException:
#     print("API request failed")


# raise_for_status() raises an exception
# when the API returns an error status.


# ==================================================
# 14. JSON + API Example
# ==================================================

# Example request:
#
# {
#     "question": "What is RAG?",
#     "user_id": 101
# }


# Example response:
#
# {
#     "answer": "RAG combines retrieval with generation.",
#     "source": "knowledge_base"
# }


# Python processing:
#
# import json
#
# response = '''
# {
#     "answer": "RAG combines retrieval with generation.",
#     "source": "knowledge_base"
# }
# '''
#
# data = json.loads(response)
#
# print(data["answer"])
# print(data["source"])


# ==================================================
# 15. JSON + Pydantic
# ==================================================

# from pydantic import BaseModel
#
#
# class ChatRequest(BaseModel):
#     question: str
#     user_id: int
#
#
# request = ChatRequest(
#     question="What is RAG?",
#     user_id=101
# )
#
# print(request.question)
# print(request.user_id)


# Flow:
#
# JSON
#   ↓
# API Request
#   ↓
# Pydantic Validation
#   ↓
# Python Application
#   ↓
# AI Agent / RAG
#   ↓
# API Response
#   ↓
# JSON


# ==================================================
# 16. Error Handling in AI Applications
# ==================================================

# AI applications can fail because of:
#
# - API unavailable
# - Invalid user input
# - LLM timeout
# - Invalid JSON
# - Database error
# - Vector database error
# - Authentication failure


# Example:
#
# try:
#     result = ask_agent("Explain RAG")
#
# except Exception as error:
#     print(f"Agent failed: {error}")


# In production applications,
# specific exceptions should generally be handled
# instead of catching every error with Exception.


# ==================================================
# 17. Practice — JSON
# ==================================================

# A Python dictionary is a Python object.
# JSON is a format for representing data, 
# commonly as a string when transmitted or stored.

# Create a Python dictionary containing:
#
# name
# age
# skills
# city
#
# Convert it into JSON.
#
# Convert the JSON back into a Python object.
#
# Print the values.

# import json
# user = {
#     "name":"Shubham",
#     "age":12,
#     "skills":["java", "python", "cpp"],
#     "city":"dehradun"
# }

# json_data = json.dumps(user)
# python_object = json.loads(json_data)

# print(json_data)
# print(python_object)


# ==================================================
# 18. Practice — API
# ==================================================

# Write Python code to:
#
# 1. Send a GET request
# 2. Print the status code
# 3. Print the JSON response

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# try:
#     response = requests.get(url)

#     print("status codee: ", response.status_code)
#     print("response:", response.json())

# except requests.RequestException:
#     print("not found")


# ==================================================
# 19. Practice — Exception Handling
# ==================================================

# Create a calculator that handles:
#
# 1. Invalid input
# 2. Division by zero

#
# Example:
#
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#
#     print(a / b)
#
# except ValueError:
#     print("Invalid input")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# ==================================================
# 20. Practice — Custom Exception
# ==================================================

# Create:
#
# class InvalidAgeError(Exception):
#     pass
#
#
# Raise the exception when age is less than 18.


# ==================================================
# 21. Practice — AI API Structure
# ==================================================

# Create a Pydantic model:
#
# from pydantic import BaseModel
#
#
# class ChatRequest(BaseModel):
#     question: str
#     user_id: int


# Create another model:
#
# class ChatResponse(BaseModel):
#     answer: str
#     source: str


# ==================================================
# Day 6 Practice Goal
# ==================================================
#
# Practice this flow:
#
# JSON
#   ↓
# Python JSON Handling
#   ↓
# APIs
#   ↓
# HTTP Methods
#   ↓
# HTTP Status Codes
#   ↓
# API Requests
#   ↓
# Exception Handling
#   ↓
# Custom Exceptions
#   ↓
# FastAPI + AI Applications
#
# ==================================================