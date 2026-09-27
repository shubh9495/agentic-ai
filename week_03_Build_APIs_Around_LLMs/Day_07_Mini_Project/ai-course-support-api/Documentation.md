# Week 03 — Day 07: Mini Project — AI Course Support API

## Points Covered

* Project overview
* Project requirements
* Project architecture
* Project folder structure
* FastAPI application setup
* PostgreSQL database
* SQLAlchemy models
* Pydantic schemas
* CRUD APIs
* User registration
* Password hashing
* JWT authentication
* Protected routes
* Course APIs
* LLM integration
* AI course recommendation
* AI course support / Q&A
* Service layer
* API testing
* Environment variables
* Error handling
* Complete request flow
* Project checklist

---

# 1. Project Overview

We will build an **AI Course Support API**.

The API will allow users to:

* Register an account
* Login
* View available courses
* View a specific course
* Create/update/delete courses
* Get AI-based course recommendations
* Ask questions about courses
* Access protected user-specific features

---

# 2. Technologies Used

```text
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
JWT
Password Hashing
LLM API
Python
```

Main purpose of each:

```text
FastAPI → Build REST APIs
Pydantic → Validate requests and responses
PostgreSQL → Store persistent data
SQLAlchemy → Communicate with PostgreSQL
JWT → Authentication
Password Hashing → Securely store passwords
LLM → AI recommendations and course support
```

# 4. Project Architecture

The high-level architecture is:

```text
                    Client
                      |
                      ↓
                  FastAPI
                      |
          ┌───────────┴───────────┐
          ↓                       ↓
   Authentication             Routes
          |                       |
          ↓                       ↓
        JWT                  Services
                                  |
                    ┌─────────────┼─────────────┐
                    ↓             ↓             ↓
                PostgreSQL       LLM        Other APIs
```

For AI recommendations:

```text
User
 ↓
FastAPI
 ↓
Recommendation Route
 ↓
Recommendation Service
 ↓
LLM
 ↓
Structured Response
 ↓
User
```

---

# 5. Project Folder Structure

Use this structure:

```text
ai-course-support-api/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── course.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── course.py
│   │   └── recommendation.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── courses.py
│   │   └── ai.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── course_service.py
│   │   └── ai_service.py
│   │
│   └── security/
│       └── auth.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 6. Responsibility of Each Folder

### `main.py`

Creates the FastAPI application and includes routers.

### `database.py`

Handles:

* Database engine
* Database session
* Database connection

### `models/`

Contains SQLAlchemy database models.

### `schemas/`

Contains Pydantic request and response models.

### `routes/`

Contains API endpoints.

### `services/`

Contains business logic.

### `security/`

Contains authentication and authorization logic.

---

# 7. Required Packages

Install the required packages:

include the text into your requirements.txt file:-
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
pydantic-settings
python-jose[cryptography]
passlib[bcrypt]

now run :- pip install -r requirements.txt

For your LLM provider, install the appropriate SDK separately.

For example, if using Google Gen AI SDK (google-genai):

```bash
pip install google-genai
```

---

# 8. Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost/course_db

SECRET_KEY=your-secret-key

LLM_API_KEY=your-api-key
```

Never commit `.env` to GitHub.

Add this to `.gitignore`:

```text
.env
__pycache__/
.venv/
```

---

# 9. Database Setup

Create a PostgreSQL database:

```text
course_db
```

The application will connect to:

```text
PostgreSQL
      ↓
course_db
```

The database will contain tables such as:

```text
users
courses
```

Later, more tables can be added for:

```text
conversations
recommendations
user_progress
```

---

# 10. Database Configuration

`database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://username:password@localhost/course_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

For the actual project, load `DATABASE_URL` from the environment instead of hardcoding it.

---

# 11. User Database Model

`models/user.py`:

```python
from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
```

The database stores:

```text
id
email
hashed_password
```

It does not store the plain-text password.

---

# 12. Course Database Model

`models/course.py`:

```python
from sqlalchemy import Column, Integer, String

from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    description = Column(String)
```

Example database:

```text
courses

id | name       | level       | description
---|------------|-------------|----------------
1  | Python     | beginner    | Python basics
2  | FastAPI    | intermediate| API development
3  | LangGraph  | advanced    | Agent workflows
```

---

# 13. Pydantic User Schemas

`schemas/user.py`:

```python
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
```

The response does not contain:

```text
hashed_password
```

This is important for security.

---

# 14. Pydantic Course Schemas

`schemas/course.py`:

```python
from pydantic import BaseModel


class CourseCreate(BaseModel):
    name: str
    level: str
    description: str


class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    description: str

    class Config:
        from_attributes = True
```

---

# 15. User Registration

The registration flow is:

```text
User
 ↓
POST /auth/register
 ↓
Validate request
 ↓
Hash password
 ↓
Store user
 ↓
Return user
```

Example request:

```json
{
    "email": "user@example.com",
    "password": "mypassword"
}
```

The password should be hashed before storing it.

---

# 16. Password Hashing

A password hashing function can be created in the security layer.

Conceptually:

```python
def hash_password(password: str):
    return password_hash_function(password)
```

When registering:

```text
Plain Password
      ↓
Hash
      ↓
Database
```

Never store:

```text
password = "mypassword"
```

directly in the database.

---

# 17. Login

Login endpoint:

```text
POST /auth/login
```

Request:

```json
{
    "email": "user@example.com",
    "password": "mypassword"
}
```

Flow:

```text
Email + Password
       ↓
Find User
       ↓
Verify Password
       ↓
Generate JWT
       ↓
Return Access Token
```

Example response:

```json
{
    "access_token": "eyJhbGciOi...",
    "token_type": "bearer"
}
```

---

# 18. JWT Authentication

The client sends the token with protected requests:

```http
Authorization: Bearer <access_token>
```

For example:

```text
GET /users/me
```

The API:

```text
Receives Token
      ↓
Validates Token
      ↓
Identifies User
      ↓
Allows Request
```

---

# 19. Course CRUD APIs

The project will provide:

```text
POST   /courses
GET    /courses
GET    /courses/{course_id}
PUT    /courses/{course_id}
DELETE /courses/{course_id}
```

These demonstrate complete CRUD functionality.

---

# 20. Create Course

Request:

```http
POST /courses
```

Body:

```json
{
    "name": "FastAPI",
    "level": "beginner",
    "description": "Learn how to build APIs with FastAPI."
}
```

Flow:

```text
Request
 ↓
Pydantic Validation
 ↓
Service
 ↓
SQLAlchemy
 ↓
PostgreSQL
 ↓
Response
```

---

# 21. Get All Courses

```http
GET /courses
```

Response:

```json
[
    {
        "id": 1,
        "name": "Python",
        "level": "beginner",
        "description": "Learn Python."
    },
    {
        "id": 2,
        "name": "FastAPI",
        "level": "intermediate",
        "description": "Build APIs."
    }
]
```

---

# 22. Get One Course

```http
GET /courses/1
```

The API searches the database for:

```text
course_id = 1
```

If found:

```text
200 OK
```

If not found:

```text
404 Not Found
```

---

# 23. Update Course

```http
PUT /courses/1
```

Request:

```json
{
    "name": "Advanced FastAPI",
    "level": "advanced",
    "description": "Advanced FastAPI development."
}
```

Flow:

```text
Find Course
 ↓
Update Fields
 ↓
Commit
 ↓
Return Updated Course
```

---

# 24. Delete Course

```http
DELETE /courses/1
```

Flow:

```text
Find Course
 ↓
Delete
 ↓
Commit
 ↓
Return Response
```

---

# 25. AI Recommendation Endpoint

Now we connect the backend to an LLM.

Endpoint:

```text
POST /ai/recommend
```

Request:

```json
{
    "goal": "I want to become a Java backend developer",
    "current_skills": [
        "Java",
        "SQL"
    ],
    "experience": "beginner"
}
```

---

# 26. Recommendation Schema

`schemas/recommendation.py`:

```python
from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    goal: str
    current_skills: list[str]
    experience: str


class Recommendation(BaseModel):
    course: str
    reason: str


class RecommendationResponse(BaseModel):
    goal: str
    recommendations: list[Recommendation]
    next_steps: list[str]
```

This ensures that the AI response follows a predictable structure.

---

# 27. AI Recommendation Flow

```text
User
 ↓
POST /ai/recommend
 ↓
Request Validation
 ↓
AI Service
 ↓
Build Prompt
 ↓
LLM
 ↓
Structured Response
 ↓
Pydantic Validation
 ↓
API Response
```

Example response:

```json
{
    "goal": "Become a Java backend developer",
    "recommendations": [
        {
            "course": "Spring Boot Fundamentals",
            "reason": "You already know Java, so Spring Boot is a natural next step."
        },
        {
            "course": "REST API Development",
            "reason": "REST APIs are essential for backend development."
        }
    ],
    "next_steps": [
        "Learn Spring Boot",
        "Build REST APIs",
        "Build a backend project"
    ]
}
```

---

# 28. AI Course Support Endpoint

Another endpoint:

```text
POST /ai/ask
```

Request:

```json
{
    "question": "What should I learn before Spring Boot?"
}
```

The LLM can return:

```json
{
    "answer": "You should be comfortable with Java basics, OOP, collections and exception handling before starting Spring Boot."
}
```

Later, this endpoint can be upgraded to use RAG.

---

# 29. Service Layer

The application should not put all logic inside routes.

For example:

```text
routes/ai.py
      ↓
services/ai_service.py
      ↓
LLM
```

The route handles the HTTP request.

The service handles the AI logic.

---

# 30. Example AI Service

`services/ai_service.py`:

```python
def generate_recommendation(request):
    prompt = f"""
    User goal: {request.goal}

    Current skills: {request.current_skills}

    Experience: {request.experience}

    Recommend suitable courses and next steps.
    """

    # Call LLM here

    return result
```

The actual LLM SDK code will depend on the provider you choose.

---

# 31. Route Example

`routes/ai.py`:

```python
from fastapi import APIRouter

from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)

router = APIRouter()


@router.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend(request: RecommendationRequest):
    return generate_recommendation(request)
```

The route stays simple.

---

# 32. Main Application

`main.py`:

```python
from fastapi import FastAPI

from app.database import Base, engine

from app.routes import auth
from app.routes import courses
from app.routes import ai

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Course Support API"
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    courses.router,
    prefix="/courses",
    tags=["Courses"]
)

app.include_router(
    ai.router,
    prefix="/ai",
    tags=["AI"]
)
```

---

# 33. Final API Endpoints

The project should have endpoints such as:

```text
Authentication
────────────────────────────
POST /auth/register
POST /auth/login


Courses
────────────────────────────
POST   /courses
GET    /courses
GET    /courses/{course_id}
PUT    /courses/{course_id}
DELETE /courses/{course_id}


AI
────────────────────────────
POST /ai/recommend
POST /ai/ask


Health
────────────────────────────
GET /health
```

---

# 34. Health Endpoint

A simple health endpoint:

```python
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
```

Response:

```json
{
    "status": "healthy"
}
```

This can later be used by deployment and monitoring systems.

---

# 35. API Documentation

Run the application:

```bash
uvicorn app.main:app --reload
```

Open:

```text
/docs
```

FastAPI automatically provides interactive Swagger documentation.

You can test:

```text
Register
Login
CRUD
AI Recommendation
AI Q&A
```

directly from the browser.

---

# 36. Complete Project Flow

### User Registration

```text
User
 ↓
POST /auth/register
 ↓
Validate
 ↓
Hash Password
 ↓
PostgreSQL
 ↓
User Created
```

### User Login

```text
User
 ↓
POST /auth/login
 ↓
Verify Password
 ↓
Generate JWT
 ↓
Access Token
```

### Protected API

```text
Client
 ↓
Bearer Token
 ↓
FastAPI
 ↓
Validate JWT
 ↓
Identify User
 ↓
Authorization
 ↓
Service
 ↓
Database
```

### AI Recommendation

```text
User
 ↓
POST /ai/recommend
 ↓
Authentication
 ↓
Request Validation
 ↓
AI Service
 ↓
LLM
 ↓
Structured Output
 ↓
Response Validation
 ↓
User
```

---

# 37. Complete Architecture

```text
                         Client
                           |
                           ↓
                        FastAPI
                           |
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
          Auth          Courses          AI
             |             |             |
             ↓             ↓             ↓
            JWT         Services      AI Service
                           |             |
                           ↓             ↓
                       PostgreSQL       LLM
```

More detailed:

```text
                         Client
                           |
                           ↓
                     FastAPI Routes
                           |
                    Request Validation
                           |
                           ↓
                       Services
                     /     |      \
                    /      |       \
                   ↓       ↓        ↓
             PostgreSQL   LLM    External APIs
                   |
                   ↓
                Response
```

---

# 38. What You Have Built

After completing this project, you will have a backend that demonstrates:

```text
✓ REST API
✓ FastAPI
✓ Pydantic
✓ CRUD
✓ API architecture
✓ PostgreSQL
✓ SQLAlchemy
✓ Database sessions
✓ Password hashing
✓ JWT authentication
✓ Protected routes
✓ Authorization
✓ LLM integration
✓ Structured AI responses
```

---

# 39. Suggested Development Order

Build the project in this order:

### Step 1

Create the FastAPI application.

### Step 2

Connect PostgreSQL.

### Step 3

Create SQLAlchemy models.

### Step 4

Create Pydantic schemas.

### Step 5

Build course CRUD APIs.

### Step 6

Add user registration.

### Step 7

Add password hashing.

### Step 8

Add login + JWT.

### Step 9

Protect required routes.

### Step 10

Connect the LLM.

### Step 11

Build `/ai/recommend`.

### Step 12

Build `/ai/ask`.

### Step 13

Test everything using `/docs`.

### Step 14

Write the README.

---

# 40. Project Checklist

```text
[ ] FastAPI application created
[ ] PostgreSQL connected
[ ] SQLAlchemy configured
[ ] User model created
[ ] Course model created
[ ] Pydantic schemas created
[ ] Course CRUD implemented
[ ] User registration implemented
[ ] Password hashing implemented
[ ] JWT login implemented
[ ] Protected routes implemented
[ ] LLM connected
[ ] AI recommendation endpoint created
[ ] AI Q&A endpoint created
[ ] Error handling added
[ ] Environment variables configured
[ ] Swagger API tested
[ ] README written
[ ] Code pushed to GitHub
```

---

# 41. Future Improvements

This is the basic version of the project.

Later, you can add:

```text
Vector Database
      ↓
RAG
      ↓
Course Knowledge Base
```

Then:

```text
Authentication
      ↓
FastAPI
      ↓
Agent
 ├── LLM
 ├── Course Database
 ├── Vector Database
 ├── Tools
 └── Memory
```

You can also add:

* Redis
* Background jobs
* Rate limiting
* Logging
* OpenTelemetry
* Agent workflows
* LangGraph
* MCP tools
* Conversation memory
* Evaluation

These topics will be covered in later weeks.

---

# 42. Week 03 Final Mental Model

The complete Week 03 backend progression is:

```text
HTTP
 ↓
REST
 ↓
FastAPI
 ↓
Pydantic
 ↓
CRUD
 ↓
API Architecture
 ↓
PostgreSQL
 ↓
SQLAlchemy
 ↓
Authentication
 ↓
JWT
 ↓
LLM
```

And the final application:

```text
                         AI Course Support API
                                  |
             ┌────────────────────┼────────────────────┐
             ↓                    ↓                    ↓
       Authentication          Courses                AI
             ↓                    ↓                    ↓
            JWT                 CRUD              LLM Service
                                  ↓                    ↓
                             PostgreSQL              LLM
                                  |
                                  ↓
                               Response
```

### Final Idea

> **Week 03 turns your LLM knowledge from Week 02 into a real backend application with APIs, database persistence, authentication, and AI functionality.**

This project also becomes the foundation for future weeks where you will add **tools, agents, memory, RAG, MCP, and multi-agent workflows**.
