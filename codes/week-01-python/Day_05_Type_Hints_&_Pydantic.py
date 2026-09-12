# DAY 5 — TYPE HINTS + PYDANTIC
#
# Coding Practice
#
# Topics:
# 1. Type Hints
# 2. Basic Type Hints
# 3. Type Hints in Functions
# 4. Lists and Dictionaries
# 5. Optional Values
# 6. Union Types
# 7. Type Aliases
# 8. Pydantic
# 9. Pydantic Models
# 10. Field Validation
# 11. Nested Models
# 12. Pydantic + FastAPI
# 13. Pydantic in Agentic AI
# 14. Practice Problems
#
# Uncomment each section and run it while learning.
# ==================================================


# ==================================================
# 1. TYPE HINTS
# ==================================================

# name: str = "Shubham"
# age: int = 25
# price: float = 99.99
# is_active: bool = True
#
# print(name)
# print(age)
# print(price)
# print(is_active)

# ==================================================
# 2. BASIC TYPE HINTS
# ==================================================

# name: str = "Shubham"
# age: int = 25
# rating: float = 4.5
# is_logged_in: bool = True
#
# print(name)
# print(age)
# print(rating)
# print(is_logged_in)


# ==================================================
# 3. TYPE HINTS IN FUNCTIONS
# ==================================================

# def add(a: int, b: int) -> int:
#     return a + b
#
#
# result = add(10, 20)
# print(result)


# def greet(name: str) -> str:
#     return f"Hello {name}"
#
#
# message = greet("Shubham")
# print(message)


# ==================================================
# 4. LISTS AND DICTIONARIES
# ==================================================

# names: list[str] = ["Rahul", "Aman", "Shubham"]
#
# print(names)


# numbers: list[int] = [1, 2, 3, 4, 5]
#
# print(numbers)

# scores: dict[str, int] = {
#     "Rahul": 90,
#     "Aman": 85,
#     "Shubham": 95
# }
#
# print(scores)


# ==================================================
# 5. OPTIONAL VALUES
# ==================================================

# name: str | None = None
#
# print(name)


# def find_user(user_id: int) -> str | None:
#     if user_id == 1:
#         return "Shubham"
#
#     return None
#
#
# user = find_user(1)
# print(user)


# user = find_user(10)
# print(user)


# ==================================================
# 6. UNION TYPES
# ==================================================

# user_id: int | str = 101
#
# print(user_id)
#
# user_id = "user_101"
#
# print(user_id)


# def process_id(user_id: int | str) -> str:
#     return f"User ID: {user_id}"
#
#
# print(process_id(101))
# print(process_id("user_101"))


# ==================================================
# 7. TYPE ALIASES
# ==================================================

# UserData = dict[str, str]
#
#
# user: UserData = {
#     "name": "Shubham",
#     "email": "test@example.com"
# }
#
# print(user)


# ==================================================
# 8. PYDANTIC
# ==================================================

# Install Pydantic before running this section:
#
# pip install pydantic


# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     name: str
#     age: int
#
#
# user = User(
#     name="Shubham",
#     age=25
# )
#
# print(user)


# ==================================================
# 9. PYDANTIC MODELS
# ==================================================

# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#
#
# user = User(
#     name="Shubham",
#     age=25,
#     email="shubham@example.com"
# )
#
# print(user)
# print(user.name)
# print(user.age)
# print(user.email)


# ==================================================
# 10. FIELD VALIDATION
# ==================================================

# from pydantic import BaseModel, Field
#
#
# class User(BaseModel):
#     name: str
#     age: int = Field(gt=0)
#
#
# valid_user = User(
#     name="Shubham",
#     age=25
# )
#
# print(valid_user)


# Try this after understanding validation:
#
# invalid_user = User(
#     name="Shubham",
#     age=-5
# )
#
# print(invalid_user)


# ==================================================
# 10.1 IMPORTANT FIELD PARAMETERS
# ==================================================

# from pydantic import BaseModel, Field
#
#
# class User(BaseModel):
#     age: int = Field(gt=0)
#     name: str = Field(min_length=3, max_length=20)
#
#
# user = User(
#     age=25,
#     name="Shubham"
# )
#
# print(user)


# Examples to practice:
#
# Field(gt=0)
# Field(ge=18)
# Field(lt=100)
# Field(le=100)
# Field(min_length=3)
# Field(max_length=20)


# ==================================================
# 11. NESTED MODELS
# ==================================================

# from pydantic import BaseModel
#
#
# class Address(BaseModel):
#     city: str
#     country: str
#
#
# class User(BaseModel):
#     name: str
#     address: Address
#
#
# user = User(
#     name="Shubham",
#     address={
#         "city": "Dehradun",
#         "country": "India"
#     }
# )
#
# print(user)
# print(user.name)
# print(user.address.city)
# print(user.address.country)


# ==================================================
# 12. PYDANTIC + FASTAPI
# ==================================================

# Install FastAPI:
#
# pip install fastapi uvicorn


# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# app = FastAPI()
#
#
# class Question(BaseModel):
#     question: str
#
#
# @app.post("/ask")
# def ask_question(data: Question):
#     return {
#         "question": data.question
#     }


# Run the FastAPI application:
#
# uvicorn day5:app --reload


# ==================================================
# 13. PYDANTIC IN AGENTIC AI
# ==================================================

# from pydantic import BaseModel
#
#
# class AgentResponse(BaseModel):
#     answer: str
#     confidence: float
#     source: str
#
#
# response = AgentResponse(
#     answer="RAG retrieves relevant information before generating an answer.",
#     confidence=0.95,
#     source="Knowledge Base"
# )
#
# print(response)
# print(response.answer)
# print(response.confidence)
# print(response.source)


# ==================================================
# 14. PRACTICE 1 — PRODUCT MODEL
# ==================================================

# Create a Product model with:
#
# name
# price
# quantity

# from pydantic import BaseModel
#
#
# class Product(BaseModel):
#     name: str
#     price: float
#     quantity: int
#
#
# product = Product(
#     name="Laptop",
#     price=50000,
#     quantity=2
# )
#
# print(product)


# ==================================================
# 15. PRACTICE 2 — PRODUCT PRICE VALIDATION
# ==================================================

# Add validation so price must be greater than 0.
#
#
# from pydantic import BaseModel, Field
#
#
# class Product(BaseModel):
#     name: str
#     price: float = Field(gt=0)
#     quantity: int
#
#
# product = Product(
#     name="Laptop",
#     price=50000,
#     quantity=2
# )
#
# print(product)


# ==================================================
# 16. PRACTICE 3 — USER MODEL
# ==================================================

# Create a User model with:
#
# name
# age
# email

# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#
#
# user = User(
#     name="Shubham",
#     age=25,
#     email="shubham@example.com"
# )
#
# print(user)


# ==================================================
# 17. PRACTICE 4 — NESTED ADDRESS
# ==================================================

# Create:
#
# Address
#     city
#     country
#
# User
#     name
#     age
#     address
#
# Address should be nested inside User.

# from pydantic import BaseModel
# class Address(BaseModel):
#     city:str
#     country:str

# class User(BaseModel):
#     name:str
#     age:int
#     address:Address

# user = User(
#     name = "Shubham",
#     age = 12,
#     address = Address(
#         city="Dehradun",
#         country = "India"
#     )
# )

# print(user)


# ==================================================
# 18. PRACTICE 5 — AGENT RESPONSE
# ==================================================

# Create an AgentResponse model with:
#
# answer
# confidence
# source
#
# Example:
#
# class AgentResponse(BaseModel):
#     answer: str
#     confidence: float
#     source: str


# ==================================================
# DAY 5 PRACTICE GOAL
# ==================================================

# By the end of Day 5, you should be able to:
#
# 1. Write basic type hints.
# 2. Add type hints to functions.
# 3. Type lists and dictionaries.
# 4. Use Optional values.
# 5. Use Union types.
# 6. Create type aliases.
# 7. Create Pydantic models.
# 8. Add Field validation.
# 9. Create nested Pydantic models.
# 10. Use Pydantic with FastAPI.
# 11. Use Pydantic to structure AI agent responses.