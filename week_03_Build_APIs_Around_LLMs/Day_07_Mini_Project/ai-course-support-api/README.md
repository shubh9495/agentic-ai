# AI Course Support API

An AI-powered course management and support API built with FastAPI, PostgreSQL, SQLAlchemy, JWT authentication, and Google GenAI.

## Features

* User registration
* JWT authentication
* Password hashing
* Protected API routes
* Course CRUD operations
* PostgreSQL database
* AI course recommendations
* AI-powered course Q&A
* Pydantic request and response validation
* Error handling
* Interactive Swagger API documentation

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT
* Passlib
* Google GenAI

## Project Structure

```text
ai-course-support-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── course.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── ai.py
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

## Architecture

```text
Client
  ↓
FastAPI Routes
  ↓
Authentication / Validation
  ↓
Service Layer
  ↓
PostgreSQL / Google GenAI
  ↓
Response
```

## API Endpoints

### Authentication

| Method | Endpoint         | Description           |
| ------ | ---------------- | --------------------- |
| POST   | `/auth/register` | Register a new user   |
| POST   | `/auth/login`    | Login and receive JWT |
| GET    | `/auth/me`       | Get current user      |

### Courses

| Method | Endpoint        | Description     |
| ------ | --------------- | --------------- |
| POST   | `/courses/`     | Create a course |
| GET    | `/courses/`     | Get all courses |
| GET    | `/courses/{id}` | Get a course    |
| PUT    | `/courses/{id}` | Update a course |
| DELETE | `/courses/{id}` | Delete a course |

### AI

| Method | Endpoint        | Description                   |
| ------ | --------------- | ----------------------------- |
| POST   | `/ai/recommend` | Get course recommendations    |
| POST   | `/ai/ask`       | Ask a question about a course |

### Health

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/health` | Check API health |

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost/course_db
SECRET_KEY=your-secret-key
LLM_API_KEY=your-google-genai-api-key
```

Never commit the `.env` file to GitHub.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd ai-course-support-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the PostgreSQL database and configure the `.env` file.

## Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger can be used to test all API endpoints.

## AI Recommendation Example

Request:

```json
{
    "goal": "Become a backend developer",
    "current_skills": ["Python", "SQL"],
    "experience": "beginner"
}
```

The API returns course recommendations and suggested next steps.

## AI Course Q&A Example

Request:

```json
{
    "course_id": 1,
    "question": "What will I learn in this course?"
}
```

The API uses the course information stored in PostgreSQL to provide a course-aware answer.

## Future Improvements

* Course ownership
* Role-based authorization
* Refresh tokens
* Better logging
* Automated tests
* RAG with course documents
* Vector database
* Conversation memory
* Tool calling
* Agent workflows
* MCP integrations
* Docker deployment
* CI/CD
* Production monitoring

## Learning Outcome

This project provides a foundation for building AI-powered backend applications using FastAPI, databases, authentication, LLM APIs, structured outputs, and AI services.
