# Week 03 — Day 03: Request & Response Models

# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# Q1. What is a Pydantic model?
# Answer:
# A Pydantic model defines the structure and validates data
# using Python type hints.

# Q2. What is a request model?
# Answer:
# A request model defines and validates the data received
# by an API.

# Q3. What is a response model?
# Answer:
# A response model defines the structure of data returned
# by an API.

# Q4. Why do we use response_model in FastAPI?
# Answer:
# It provides predictable response structure, validation,
# automatic documentation, and control over returned fields.

# Q5. Can request and response models be different?
# Answer:
# Yes. The client and server may send and return different data.

# Q6. What happens when request data is invalid?
# Answer:
# FastAPI/Pydantic validates the data and returns a validation
# error instead of passing invalid data to the route.

# Q7. Why are type hints important in FastAPI?
# Answer:
# FastAPI uses them for validation, parameter types,
# API schemas, and automatic documentation.

# Q8. What is the difference between a request model
# and a path parameter?
# Answer:
# A request model represents structured request body data,
# while a path parameter is part of the URL.

# Q9. What is the difference between a request model
# and a query parameter?
# Answer:
# A request model is normally used for structured body data,
# while a query parameter is passed through the URL.

# Q10. What is a nested Pydantic model?
# Answer:
# A Pydantic model that contains another Pydantic model
# as one of its fields.

# Q11. What is an API contract?
# Answer:
# An API contract defines what the client can send and
# what the server will return.

# Q12. How can response models help protect sensitive data?
# Answer:
# They define which fields should be returned by the API,
# preventing unwanted fields such as password hashes from
# being exposed.

# Q13. How does FastAPI use Pydantic models?
# Answer:
# FastAPI uses Pydantic models to validate request data,
# structure responses, and generate API documentation.

# Q14. What is the difference between required and optional fields?
# Answer:
# Required fields must be provided.
# Optional fields can have a missing value, usually with
# an appropriate optional type and default.

# Q15. What is an Enum used for in a request model?
# Answer:
# An Enum restricts a field to a predefined set of values.

# ============================================================
# CODING PRACTICE
# ============================================================

# ------------------------------------------------------------
# Q16. Create a Pydantic request model for a user.
# Requirements:
# - name: string
# - age: integer
# Answer:
# from pydantic import BaseModel
#
# class UserRequest(BaseModel):
#     name: str
#     age: int

# ------------------------------------------------------------
# Q17. Create a FastAPI POST endpoint using a request model.
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class CourseRequest(BaseModel):
#     name: str
#     level: str
#
# @app.post("/courses")
# def create_course(course: CourseRequest):
#     return course

# ------------------------------------------------------------
# Q18. Create a request model with an optional age field.
# Answer:
# from pydantic import BaseModel
#
# class UserRequest(BaseModel):
#     name: str
#     age: int | None = None

# ------------------------------------------------------------
# Q19. Create a request model with a default value.
# Requirement:
# - name: string
# - level: default "beginner"
# Answer:
# from pydantic import BaseModel
#
# class CourseRequest(BaseModel):
#     name: str
#     level: str = "beginner"

# ------------------------------------------------------------
# Q20. Create nested Pydantic models for a course and instructor.
# Answer:
# from pydantic import BaseModel
#
# class Instructor(BaseModel):
#     name: str
#     experience: int
#
# class CourseRequest(BaseModel):
#     name: str
#     instructor: Instructor

# ------------------------------------------------------------
# Q21. Create a model containing a list of strings.
# Answer:
# from pydantic import BaseModel
#
# class CourseRequest(BaseModel):
#     name: str
#     topics: list[str]

# ------------------------------------------------------------
# Q22. Create a model containing a list of Topic objects.
# Answer:
# from pydantic import BaseModel
#
# class Topic(BaseModel):
#     name: str
#     duration: int
#
# class CourseRequest(BaseModel):
#     name: str
#     topics: list[Topic]

# ------------------------------------------------------------
# Q23. Create an Enum for experience levels.
# Allowed values:
# - beginner
# - intermediate
# - advanced
# Answer:
# from enum import Enum
# from pydantic import BaseModel
#
# class Experience(str, Enum):
#     beginner = "beginner"
#     intermediate = "intermediate"
#     advanced = "advanced"
#
# class UserRequest(BaseModel):
#     experience: Experience

# ------------------------------------------------------------
# Q24. Add validation so age cannot be negative.
# Answer:
# from pydantic import BaseModel, Field
#
# class UserRequest(BaseModel):
#     name: str
#     age: int = Field(ge=0)

# ------------------------------------------------------------
# Q25. Add username validation.
# Requirement:
# - minimum length: 3
# - maximum length: 20
# Answer:
# from pydantic import BaseModel, Field
#
# class UserRequest(BaseModel):
#     username: str = Field(min_length=3, max_length=20)

# ------------------------------------------------------------
# Q26. Create a response model for a course.
# Fields:
# - id: integer
# - name: string
# - level: string
# Answer:
# from pydantic import BaseModel
#
# class CourseResponse(BaseModel):
#     id: int
#     name: str
#     level: str

# ------------------------------------------------------------
# Q27. Create a GET endpoint using response_model.
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class CourseResponse(BaseModel):
#     id: int
#     name: str
#     level: str
#
# @app.get(
#     "/courses/{course_id}",
#     response_model=CourseResponse
# )
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI",
#         "level": "beginner"
#     }

# ------------------------------------------------------------
# Q28. Create separate request and response models.
# Request:
# - name
# - level
# Response:
# - id
# - name
# - level
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class CourseRequest(BaseModel):
#     name: str
#     level: str
#
# class CourseResponse(BaseModel):
#     id: int
#     name: str
#     level: str
#
# @app.post(
#     "/courses",
#     response_model=CourseResponse
# )
# def create_course(course: CourseRequest):
#     return {
#         "id": 1,
#         "name": course.name,
#         "level": course.level
#     }

# ------------------------------------------------------------
# Q29. Create an AI course recommendation request model.
# Fields:
# - goal: string
# - current_skills: list of strings
# - experience: string
# Answer:
# from pydantic import BaseModel
#
# class RecommendationRequest(BaseModel):
#     goal: str
#     current_skills: list[str]
#     experience: str

# ------------------------------------------------------------
# Q30. Create structured response models for course
# recommendations.
# Answer:
# from pydantic import BaseModel
#
# class Recommendation(BaseModel):
#     course: str
#     reason: str
#
# class RecommendationResponse(BaseModel):
#     goal: str
#     recommendations: list[Recommendation]
#     next_steps: list[str]

# ------------------------------------------------------------
# Q31. Create the complete AI recommendation endpoint.
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class RecommendationRequest(BaseModel):
#     goal: str
#     current_skills: list[str]
#     experience: str
#
# class Recommendation(BaseModel):
#     course: str
#     reason: str
#
# class RecommendationResponse(BaseModel):
#     goal: str
#     recommendations: list[Recommendation]
#     next_steps: list[str]
#
# @app.post(
#     "/recommend",
#     response_model=RecommendationResponse
# )
# def recommend(request: RecommendationRequest):
#     return {
#         "goal": request.goal,
#         "recommendations": [
#             {
#                 "course": "Spring Boot",
#                 "reason": "Useful for Java backend development."
#             }
#         ],
#         "next_steps": [
#             "Learn Spring Boot",
#             "Build a REST API"
#         ]
#     }

# ------------------------------------------------------------
# Q32. Build a complete Course API using request and response
# models.
# Requirements:
# - POST /courses
# - CourseRequest with name, level, duration
# - CourseResponse with id, name, level, duration
# - Use response_model
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class CourseRequest(BaseModel):
#     name: str
#     level: str
#     duration: int
#
# class CourseResponse(BaseModel):
#     id: int
#     name: str
#     level: str
#     duration: int
#
# @app.post(
#     "/courses",
#     response_model=CourseResponse
# )
# def create_course(course: CourseRequest):
#     return {
#         "id": 1,
#         "name": course.name,
#         "level": course.level,
#         "duration": course.duration
#     }

# ============================================================
# PRACTICE FLOW
# ============================================================
# 1. Start with basic Pydantic models.
# 2. Practice required and optional fields.
# 3. Practice nested models and lists.
# 4. Practice Enum and Field validation.
# 5. Create request models.
# 6. Create response models.
# 7. Use request_model + response_model together.
# 8. Build the recommendation API.
# 9. Open /docs and test the endpoints.
# 10. Try invalid input and observe validation errors.
# ============================================================
# RUN
# ============================================================
# Install:
# pip install fastapi uvicorn
# Run:
# uvicorn practice:app --reload
# Open:
# http://127.0.0.1:8000/docs
# Note:
# Uncomment the required imports, models, and endpoint before
# running the file.