# Week 03 — Day 02: FastAPI Fundamentals
# Interview Questions + Coding Practice
# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# Q1. What is FastAPI?
#
# Answer:
# FastAPI is a modern Python web framework used to build APIs
# quickly and efficiently.
#
# It provides type hints, validation, automatic documentation,
# and async support.

# Q2. Why is FastAPI useful?
#
# Answer:
# FastAPI provides:
# - Simple API development
# - Automatic validation
# - Type-hint support
# - Automatic documentation
# - Async support
# - Good performance
# - Easy integration with databases and AI services

# Q3. What is Uvicorn?
#
# Answer:
# Uvicorn is an ASGI server used to run FastAPI applications.

# Q4. What does ASGI stand for?
#
# Answer:
# ASGI stands for Asynchronous Server Gateway Interface.

# Q5. What is a route in FastAPI?
#
# Answer:
# A route connects an HTTP method and URL to a Python function.

# Q6. How do you create a GET endpoint?
#
# Answer:
# @app.get("/courses")
# def get_courses():
#     return {"courses": []}

# Q7. How do you run a FastAPI application?
#
# Answer:
# uvicorn main:app --reload
#
# main   -> main.py
# app    -> FastAPI application object
# reload -> Restart server when code changes

# Q8. What are /docs and /redoc?
#
# Answer:
# They are automatically generated API documentation interfaces
# provided by FastAPI.
#
# /docs  -> Swagger UI
# /redoc -> ReDoc

# Q9. What is the difference between path and query parameters?
#
# Answer:
# Path parameters identify a specific resource.
#
# Query parameters are commonly used for filtering, searching,
# sorting, pagination, or controlling a request.

# Q10. How does FastAPI perform validation?
#
# Answer:
# FastAPI uses Python type hints and Pydantic to validate
# request data.

# Q11. What happens when a path parameter has the wrong type?
#
# Answer:
# FastAPI automatically returns a validation error.
#
# Example:
# course_id: int
#
# /courses/10 -> valid
# /courses/abc -> validation error

# Q12. How does FastAPI return JSON?
#
# Answer:
# FastAPI automatically converts Python dictionaries and other
# supported Python data structures into JSON responses.

# Q13. How can you set a response status code in FastAPI?
#
# Answer:
# Use the status_code parameter.
#
# Example:
# @app.post("/courses", status_code=status.HTTP_201_CREATED)
# def create_course():
#     return {"message": "Course created"}

# Q14. What are FastAPI tags?
#
# Answer:
# Tags organize endpoints in Swagger documentation.

# Q15. What is the basic FastAPI request flow?
#
# Answer:
# Client -> HTTP Request -> FastAPI -> Find Matching Route
# -> Validate Parameters -> Execute Python Function
# -> Generate Response -> HTTP Response -> Client

# Q16. What is the difference between FastAPI and Flask?
#
# Answer:
# FastAPI is API-focused, uses type hints heavily, provides
# automatic validation and documentation, and has built-in async support.
#
# Flask is a lightweight and flexible web framework where
# these features generally require additional setup.

# Q17. Why is FastAPI useful for Agentic AI?
#
# Answer:
# FastAPI can act as the backend layer for AI applications.
# It can expose APIs that communicate with:
# - LLMs
# - Databases
# - Vector databases
# - Tools
# - Agents

# ============================================================
# CODING PRACTICE
# ============================================================

# ------------------------------------------------------------
# 1. CREATE A BASIC FASTAPI APPLICATION
# ------------------------------------------------------------
# Create a FastAPI application with a GET / endpoint.
#
# Answer:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# ------------------------------------------------------------
# 2. CREATE A HEALTH ENDPOINT
# ------------------------------------------------------------
# Create:
# GET /health
# Response:
# {"status": "ok"}
#
# Answer:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/health")
# def health():
#     return {"status": "ok"}

# ------------------------------------------------------------
# 3. CREATE A GET /courses ENDPOINT
# ------------------------------------------------------------
# Return:
# {"courses": ["Python", "Java", "Spring Boot"]}
#
# Answer:
# @app.get("/courses")
# def get_courses():
#     return {"courses": ["Python", "Java", "Spring Boot"]}

# ------------------------------------------------------------
# 4. CREATE A POST /courses ENDPOINT
# ------------------------------------------------------------
# Return:
# {"message": "Course created"}
#
# Answer:
# @app.post("/courses")
# def create_course():
#     return {"message": "Course created"}

# ------------------------------------------------------------
# 5. CREATE A PATH PARAMETER
# ------------------------------------------------------------
# Create:
# GET /courses/{course_id}
# course_id should be an integer.
#
# Answer:
# @app.get("/courses/{course_id}")
# def get_course(course_id: int):
#     return {"course_id": course_id}

# ------------------------------------------------------------
# 6. CREATE A QUERY PARAMETER
# ------------------------------------------------------------
# Create:
# GET /courses?level=beginner
#
# Answer:
# @app.get("/courses")
# def get_courses(level: str | None = None):
#     return {"level": level}

# ------------------------------------------------------------
# 7. CREATE MULTIPLE QUERY PARAMETERS
# ------------------------------------------------------------
# Create:
# GET /courses?level=beginner&limit=5
#
# Answer:
# @app.get("/courses")
# def get_courses(level: str | None = None, limit: int = 10):
#     return {"level": level, "limit": limit}

# ------------------------------------------------------------
# 8. CREATE A REQUIRED QUERY PARAMETER
# ------------------------------------------------------------
# Create an endpoint where category is required.
# Example:
# GET /courses?category=backend
#
# Answer:
# @app.get("/courses")
# def get_courses(category: str):
#     return {"category": category}

# ------------------------------------------------------------
# 9. CREATE AN ENDPOINT WITH A DEFAULT VALUE
# ------------------------------------------------------------
# Create an endpoint where limit defaults to 10.
#
# Answer:
# @app.get("/courses")
# def get_courses(limit: int = 10):
#     return {"limit": limit}

# ------------------------------------------------------------
# 10. SET HTTP STATUS CODE
# ------------------------------------------------------------
# Create a POST endpoint that returns HTTP 201.
#
# Answer:
# from fastapi import FastAPI, status
#
# app = FastAPI()
#
# @app.post("/courses", status_code=status.HTTP_201_CREATED)
# def create_course():
#     return {"message": "Course created"}

# ------------------------------------------------------------
# 11. ADD TAGS
# ------------------------------------------------------------
# Add the Courses tag to a GET /courses endpoint.
#
# Answer:
# @app.get("/courses", tags=["Courses"])
# def get_courses():
#     return {"courses": []}

# ------------------------------------------------------------
# 12. CREATE MULTIPLE ROUTES
# ------------------------------------------------------------
# Create:
# GET  /courses
# GET  /courses/{course_id}
# POST /courses
#
# Answer:
# @app.get("/courses")
# def get_courses():
#     return {"message": "All courses"}
#
# @app.get("/courses/{course_id}")
# def get_course(course_id: int):
#     return {"course_id": course_id}
#
# @app.post("/courses")
# def create_course():
#     return {"message": "Course created"}

# ------------------------------------------------------------
# 13. CREATE AN AI RECOMMENDATION API
# ------------------------------------------------------------
# Create:
# GET  /health
# POST /recommend
#
# /health should return:
# {"status": "ok"}
#
# /recommend should return:
# {"message": "Recommendation generated"}
#
# Answer:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/health")
# def health():
#     return {"status": "ok"}
#
# @app.post("/recommend")
# def recommend():
#     return {"message": "Recommendation generated"}

# ------------------------------------------------------------
# 14. MINI PRACTICE
# ------------------------------------------------------------
# Create a FastAPI application with:
# GET  /health
# GET  /courses
# GET  /courses/{course_id}
# GET  /courses?level=beginner
# POST /courses
#
# Also:
# - Use an integer path parameter.
# - Use a query parameter.
# - Add a default value to one query parameter.
# - Return HTTP 201 for POST /courses.
# - Add "Courses" as a Swagger tag.
#
# Answer:
# from fastapi import FastAPI, status
#
# app = FastAPI()
#
# @app.get("/health")
# def health():
#     return {"status": "ok"}
#
# @app.get("/courses", tags=["Courses"])
# def get_courses(level: str | None = None, limit: int = 10):
#     return {"level": level, "limit": limit}
#
# @app.get("/courses/{course_id}", tags=["Courses"])
# def get_course(course_id: int):
#     return {"course_id": course_id}
#
# @app.post("/courses", status_code=status.HTTP_201_CREATED, tags=["Courses"])
# def create_course():
#     return {"message": "Course created"}

# ------------------------------------------------------------
# 15. RUN AND TEST THE APPLICATION
# ------------------------------------------------------------
# Save the application as:
# main.py
#
# Install:
# pip install fastapi uvicorn
#
# Run:
# uvicorn main:app --reload
#
# Then test:
# http://127.0.0.1:8000/docs
#
# Use Swagger UI to test all endpoints.