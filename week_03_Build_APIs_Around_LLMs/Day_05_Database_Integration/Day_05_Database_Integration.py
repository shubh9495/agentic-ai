# Week 03 — Day 05: Database Integration
# Practice + Interview Questions

# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# Q1. What is PostgreSQL?
# Answer:
# PostgreSQL is a relational database management system
# that uses SQL to store and manage structured data.

# Q2. What is SQLAlchemy?
# Answer:
# SQLAlchemy is a Python library used to interact with SQL databases.

# Q3. What is ORM?
# Answer:
# ORM (Object-Relational Mapping) maps objects in a programming
# language to tables in a relational database.

# Q4. What is a database session?
# Answer:
# A database session manages interaction with the database
# during a unit of work.

# Q5. What is the difference between Pydantic and SQLAlchemy?
# Answer:
# Pydantic is mainly used for API validation and schemas.
# SQLAlchemy is used for database interaction.

# Q6. Why do we use Depends() in FastAPI?
# Answer:
# Depends() allows FastAPI to provide dependencies,
# such as a database session, to a route.

# Q7. Why do we use yield in get_db()?
# Answer:
# yield provides the database session to the route and
# allows the session to be closed after the request finishes.

# Q8. What does db.commit() do?
# Answer:
# db.commit() saves the current transaction changes
# to the database.

# Q9. What does db.refresh() do?
# Answer:
# db.refresh() refreshes the object with the latest values
# from the database.

# Q10. Why should database credentials not be hardcoded?
# Answer:
# Database credentials are sensitive information and should
# not be exposed in source code or Git repositories.

# Q11. What is a primary key?
# Answer:
# A primary key uniquely identifies each row in a database table.

# Q12. What is the difference between SQL and NoSQL?
# Answer:
# SQL databases generally store structured data in tables.
# NoSQL databases use different data models depending on the database.

# Q13. What is a database engine?
# Answer:
# A database engine manages the connection between the
# application and the database.

# Q14. What is the difference between a SQLAlchemy model
# and a Pydantic model?
# Answer:
# A SQLAlchemy model represents database data.
# A Pydantic model validates API input and output.

# Q15. What is the purpose of Base.metadata.create_all()?
# Answer:
# It creates the database tables represented by the
# SQLAlchemy models.

# Q16. What are the main CRUD operations?
# Answer:
# Create → POST
# Read   → GET
# Update → PUT/PATCH
# Delete → DELETE

# ============================================================
# CODING PRACTICE
# ============================================================

# ------------------------------------------------------------
# Q17. Import the required SQLAlchemy components and create
# a declarative Base.
# Answer:
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base
#
# Base = declarative_base()

# ------------------------------------------------------------
# Q18. Create a SQLAlchemy Course model with:
# id, name, and level.
# Answer:
# from sqlalchemy import Column, Integer, String
#
# class Course(Base):
#     __tablename__ = "courses"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     level = Column(String)

# ------------------------------------------------------------
# Q19. Create a database engine using a PostgreSQL URL.
# Answer:
# from sqlalchemy import create_engine
#
# DATABASE_URL = "postgresql://user:password@localhost/course_db"
# engine = create_engine(DATABASE_URL)

# ------------------------------------------------------------
# Q20. Create a database session factory.
# Answer:
# from sqlalchemy.orm import sessionmaker
#
# SessionLocal = sessionmaker(
#     bind=engine,
#     autoflush=False,
#     autocommit=False
# )

# ------------------------------------------------------------
# Q21. Create a get_db() dependency that creates and closes
# a database session.
# Answer:
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# ------------------------------------------------------------
# Q22. Create the database tables from the SQLAlchemy models.
# Answer:
# Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# Q23. Create a new Course object and add it to the session.
# Answer:
# course = Course(
#     name="FastAPI",
#     level="beginner"
# )
# db.add(course)
# db.commit()
# db.refresh(course)

# ------------------------------------------------------------
# Q24. Retrieve all courses from the database.
# Answer:
# courses = db.query(Course).all()

# ------------------------------------------------------------
# Q25. Retrieve one course using its ID.
# Answer:
# course = db.query(Course).filter(
#     Course.id == course_id
# ).first()

# ------------------------------------------------------------
# Q26. Update a course name.
# Answer:
# course = db.query(Course).filter(
#     Course.id == course_id
# ).first()
# course.name = "Advanced FastAPI"
# db.commit()
# db.refresh(course)

# ------------------------------------------------------------
# Q27. Delete a course.
# Answer:
# course = db.query(Course).filter(
#     Course.id == course_id
# ).first()
# db.delete(course)
# db.commit()

# ------------------------------------------------------------
# Q28. Create a Pydantic model for creating a course.
# Answer:
# from pydantic import BaseModel
#
# class CourseCreate(BaseModel):
#     name: str
#     level: str

# ------------------------------------------------------------
# Q29. Create a FastAPI POST endpoint that receives a
# Pydantic CourseCreate model and stores it in the database.
# Answer:
# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
#
# app = FastAPI()
#
# @app.post("/courses")
# def create_course(
#     course: CourseCreate,
#     db: Session = Depends(get_db)
# ):
#     new_course = Course(
#         name=course.name,
#         level=course.level
#     )
#     db.add(new_course)
#     db.commit()
#     db.refresh(new_course)
#     return new_course

# ------------------------------------------------------------
# Q30. Create a GET endpoint that returns all courses.
# Answer:
# @app.get("/courses")
# def get_courses(
#     db: Session = Depends(get_db)
# ):
#     return db.query(Course).all()

# ------------------------------------------------------------
# Q31. Create a GET endpoint that returns one course by ID.
# Answer:
# @app.get("/courses/{course_id}")
# def get_course(
#     course_id: int,
#     db: Session = Depends(get_db)
# ):
#     course = db.query(Course).filter(
#         Course.id == course_id
#     ).first()
#     return course

# ------------------------------------------------------------
# Q32. Create a DELETE endpoint that removes a course.
# Answer:
# @app.delete("/courses/{course_id}")
# def delete_course(
#     course_id: int,
#     db: Session = Depends(get_db)
# ):
#     course = db.query(Course).filter(
#         Course.id == course_id
#     ).first()
#     db.delete(course)
#     db.commit()
#     return {"message": "Course deleted"}

# ------------------------------------------------------------
# Q33. Write the complete database flow of a FastAPI request.
# Answer:
# Client
#   ↓
# FastAPI Route
#   ↓
# Pydantic Request Model
#   ↓
# Service Layer
#   ↓
# SQLAlchemy
#   ↓
# PostgreSQL
#   ↓
# SQLAlchemy
#   ↓
# Pydantic Response Model
#   ↓
# Client

# ============================================================
# MINI PRACTICE
# ============================================================
# Q34. Build a simple FastAPI + PostgreSQL CRUD API for courses.
# Requirements:
# 1. Create a Course SQLAlchemy model.
# 2. Create a PostgreSQL database connection.
# 3. Create a get_db() dependency.
# 4. Create the database table.
# 5. Create POST /courses.
# 6. Create GET /courses.
# 7. Create GET /courses/{course_id}.
# 8. Create PUT /courses/{course_id}.
# 9. Create DELETE /courses/{course_id}.
#
# Answer structure:
# database.py
#   ↓
# SQLAlchemy engine
#   ↓
# SessionLocal
#   ↓
# get_db()
#
# models/course.py
#   ↓
# Course model
#
# schemas/course.py
#   ↓
# CourseCreate
#
# routes/courses.py
#   ↓
# CRUD endpoints
#
# services/course_service.py
#   ↓
# Database business logic
#
# main.py
#   ↓
# FastAPI application

# ------------------------------------------------------------
# Q35. Design the database architecture for an AI Course
# Support API.
# Requirements:
# Store:
# - Users
# - Courses
# - Course history
# - Recommendations
# - Conversations
#
# Answer:
# FastAPI
#   ↓
# Routes
#   ↓
# Services
#   ↓
# SQLAlchemy
#   ↓
# PostgreSQL
#
# AI-related flow:
# User
#   ↓
# FastAPI
#   ↓
# Recommendation Service
#   ↓
# PostgreSQL
#   ↓
# User Information
#   ↓
# LLM
#   ↓
# Recommendation

# ------------------------------------------------------------
# Q36. Design a database setup for a RAG application.
# Answer:
# PostgreSQL
#   ↓
# Application data
#
# Vector Database
#   ↓
# Embeddings
#   ↓
# Semantic search
#
# Both databases can be used by the same AI application.

# ============================================================
# IMPORTANT COMMANDS TO REMEMBER
# ============================================================
# Create engine:
# engine = create_engine(DATABASE_URL)
#
# Create session factory:
# SessionLocal = sessionmaker(
#     bind=engine,
#     autoflush=False,
#     autocommit=False
# )
#
# Create session:
# db = SessionLocal()
#
# Add:
# db.add(course)
#
# Save:
# db.commit()
#
# Refresh:
# db.refresh(course)
#
# Read:
# db.query(Course).all()
#
# Find one:
# db.query(Course).filter(
#     Course.id == course_id
# ).first()
#
# Delete:
# db.delete(course)
#
# Close:
# db.close()
#
# Create tables:
# Base.metadata.create_all(bind=engine)