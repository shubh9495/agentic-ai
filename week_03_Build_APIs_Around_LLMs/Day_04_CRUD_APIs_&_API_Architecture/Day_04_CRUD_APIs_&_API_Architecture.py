# Week 03 — Day 04: CRUD APIs & API Architecture
# All questions and solutions are commented initially.
# Uncomment them one by one while practicing.
# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# Q1. What is CRUD?
# Answer:
# CRUD stands for Create, Read, Update, and Delete.

# Q2. Which HTTP methods are commonly used for CRUD?
# Answer:
# POST   → Create
# GET    → Read
# PUT    → Update
# PATCH  → Partial Update
# DELETE → Delete

# Q3. What is the difference between PUT and PATCH?
# Answer:
# PUT generally replaces the complete resource.
# PATCH updates specific fields of a resource.

# Q4. What is API architecture?
# Answer:
# API architecture is the way an API application is
# organized into different components and layers.

# Q5. What is a service layer?
# Answer:
# The service layer contains the main business logic
# of an application.

# Q6. Why should business logic not be placed directly
# inside routes?
# Answer:
# Separating business logic makes the application easier
# to maintain, test, debug, and scale.

# Q7. What is APIRouter in FastAPI?
# Answer:
# APIRouter is used to organize related API routes
# into separate modules.

# Q8. Why is API architecture important?
# Answer:
# It separates responsibilities and makes the application
# easier to maintain and scale.

# Q9. What is the difference between a route and a service?
# Answer:
# A route handles the HTTP request, while a service handles
# the application's business logic.

# Q10. What status code is commonly returned when a resource
# is created?
# Answer:
# 201 Created.

# Q11. What status code is commonly used when a resource
# is not found?
# Answer:
# 404 Not Found.

# Q12. Why should REST APIs use nouns in URLs?
# Answer:
# The HTTP method already describes the operation, so the
# URL can represent the resource.
# Example:
# GET /courses
# POST /courses

# Q13. What is the purpose of HTTPException in FastAPI?
# Answer:
# It is used to return meaningful HTTP errors with a
# status code and detail message.

# Q14. Why should in-memory lists not normally be used
# in production?
# Answer:
# In-memory data is temporary and is lost when the
# application restarts. Production applications normally
# use persistent storage such as a database.

# Q15. What is the role of the database layer?
# Answer:
# The database layer handles communication with the
# application's database.

# Q16. Why is API architecture especially important
# for Agentic AI applications?
# Answer:
# Agentic applications may contain LLMs, tools, RAG,
# memory, databases, and external APIs. Separating these
# responsibilities makes the application easier to maintain.

# ============================================================
# CODING PRACTICE
# ============================================================

# ------------------------------------------------------------
# Q17. Create a basic Course model.
# Requirements:
# - name: string
# - level: string
# Answer:
# from pydantic import BaseModel
#
# class Course(BaseModel):
#     name: str
#     level: str

# ------------------------------------------------------------
# Q18. Create a POST endpoint to create a course.
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class Course(BaseModel):
#     name: str
#     level: str
#
# @app.post("/courses")
# def create_course(course: Course):
#     return course

# ------------------------------------------------------------
# Q19. Create a GET endpoint that returns all courses.
# Answer:
# courses = [
#     {"id": 1, "name": "Python"},
#     {"id": 2, "name": "FastAPI"}
# ]
#
# @app.get("/courses")
# def get_courses():
#     return courses

# ------------------------------------------------------------
# Q20. Create a GET endpoint that returns one course
# using a path parameter.
# Answer:
# @app.get("/courses/{course_id}")
# def get_course(course_id: int):
#     return {
#         "id": course_id,
#         "name": "FastAPI"
#     }

# ------------------------------------------------------------
# Q21. Create a PUT endpoint to update a course.
# Answer:
# @app.put("/courses/{course_id}")
# def update_course(course_id: int, course: Course):
#     return {
#         "id": course_id,
#         "name": course.name,
#         "level": course.level
#     }

# ------------------------------------------------------------
# Q22. Create a DELETE endpoint.
# Answer:
# @app.delete("/courses/{course_id}")
# def delete_course(course_id: int):
#     return {
#         "message": "Course deleted"
#     }

# ------------------------------------------------------------
# Q23. Create a simple in-memory CRUD API.
# Requirements:
# - POST /courses
# - GET /courses
# - GET /courses/{course_id}
# - PUT /courses/{course_id}
# - DELETE /courses/{course_id}
# Answer:
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class Course(BaseModel):
#     name: str
#     level: str
#
# courses = []
#
# @app.post("/courses")
# def create_course(course: Course):
#     courses.append(course)
#     return course
#
# @app.get("/courses")
# def get_courses():
#     return courses
#
# @app.get("/courses/{course_id}")
# def get_course(course_id: int):
#     return courses[course_id]
#
# @app.put("/courses/{course_id}")
# def update_course(course_id: int, course: Course):
#     courses[course_id] = course
#     return course
#
# @app.delete("/courses/{course_id}")
# def delete_course(course_id: int):
#     courses.pop(course_id)
#     return {"message": "Course deleted"}

# ------------------------------------------------------------
# Q24. Add a 201 Created status code to the POST endpoint.
# Answer:
# from fastapi import status
#
# @app.post(
#     "/courses",
#     status_code=status.HTTP_201_CREATED
# )
# def create_course(course: Course):
#     return course

# ------------------------------------------------------------
# Q25. Handle a course-not-found error using HTTPException.
# Answer:
# from fastapi import HTTPException
#
# @app.get("/courses/{course_id}")
# def get_course(course_id: int):
#     if course_id not in courses:
#         raise HTTPException(
#             status_code=404,
#             detail="Course not found"
#         )
#     return courses[course_id]

# ------------------------------------------------------------
# Q26. Create an APIRouter for course routes.
# Answer:
# from fastapi import APIRouter
#
# router = APIRouter()
#
# @router.get("/courses")
# def get_courses():
#     return []
#
# @router.post("/courses")
# def create_course():
#     return {"message": "Course created"}

# ------------------------------------------------------------
# Q27. Include a course router inside main.py.
# Answer:
# from fastapi import FastAPI
# from routes.courses import router
#
# app = FastAPI()
# app.include_router(router)

# ------------------------------------------------------------
# Q28. Create a simple service layer for courses.
# Answer:
# courses = []
#
# def create_course(course):
#     courses.append(course)
#     return course
#
# def get_courses():
#     return courses
#
# def delete_course(course_id):
#     courses.pop(course_id)

# ------------------------------------------------------------
# Q29. Create routes that call the service layer.
# Answer:
# from fastapi import APIRouter
# from services.course_service import (
#     create_course,
#     get_courses,
#     delete_course
# )
#
# router = APIRouter()
#
# @router.post("/courses")
# def create(course):
#     return create_course(course)
#
# @router.get("/courses")
# def get_all():
#     return get_courses()
#
# @router.delete("/courses/{course_id}")
# def delete(course_id: int):
#     delete_course(course_id)
#     return {"message": "Course deleted"}

# ------------------------------------------------------------
# Q30. Design RESTful endpoints for a course resource.
# Answer:
# GET    /courses
# GET    /courses/{course_id}
# POST   /courses
# PUT    /courses/{course_id}
# PATCH  /courses/{course_id}
# DELETE /courses/{course_id}

# ------------------------------------------------------------
# Q31. Create a basic AI recommendation service.
# Requirement:
# The service should receive a goal and return a course
# recommendation.
# Answer:
# def recommend_courses(goal: str):
#     return {
#         "goal": goal,
#         "course": "Spring Boot"
#     }

# ------------------------------------------------------------
# Q32. Create a route that calls the recommendation service.
# Answer:
# @app.post("/recommend")
# def recommend(request: RecommendationRequest):
#     return recommend_courses(request.goal)

# ------------------------------------------------------------
# Q33. Design the architecture for an AI Course Support API.
# Answer:
# Client
#   ↓
# FastAPI
#   ↓
# Route
#   ↓
# Service
#   ↓
# Embedding / Course Search
#   ↓
# LLM
#   ↓
# Structured Output
#   ↓
# Pydantic Validation
#   ↓
# Response
#
# The route handles communication while the service handles
# the application logic.

# ============================================================
# MINI PROJECT PRACTICE
# ============================================================
# Build a Course API with:
# 1. POST /courses
# 2. GET /courses
# 3. GET /courses/{course_id}
# 4. PUT /courses/{course_id}
# 5. DELETE /courses/{course_id}
#
# Then:
# 6. Add HTTPException for missing courses.
# 7. Add a 201 status code for course creation.
# 8. Move course logic into course_service.py.
# 9. Move routes into courses.py using APIRouter.
# 10. Connect the router to main.py.
# ============================================================
# RECOMMENDED PROJECT STRUCTURE
# ============================================================
# app/
# ├── main.py
# ├── routes/
# │   ├── courses.py
# │   └── recommendation.py
# ├── services/
# │   ├── course_service.py
# │   └── llm_service.py
# ├── models/
# │   ├── course.py
# │   └── recommendation.py
# ├── database/
# │   └── database.py
# └── dependencies.py
# ============================================================
# RUN
# ============================================================
# Install:
# pip install fastapi uvicorn
# Run:
# uvicorn main:app --reload
# Open API documentation:
# http://127.0.0.1:8000/docs