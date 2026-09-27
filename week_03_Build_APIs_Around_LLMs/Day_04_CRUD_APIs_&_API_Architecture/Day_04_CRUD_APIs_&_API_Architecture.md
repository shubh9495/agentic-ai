# Week 03 — Day 04: CRUD APIs & API Architecture

## 1. CRUD

**CRUD** stands for:

| Operation | Meaning              | HTTP Method |
| --------- | -------------------- | ----------- |
| Create    | Add new data         | POST        |
| Read      | Get existing data    | GET         |
| Update    | Modify existing data | PUT / PATCH |
| Delete    | Remove data          | DELETE      |

Example:

```text
POST   /courses       → Create
GET    /courses       → Read all
GET    /courses/1     → Read one
PUT    /courses/1     → Update
PATCH  /courses/1     → Partial update
DELETE /courses/1     → Delete
```

CRUD is a common pattern used in backend APIs.

## 2. Create

The **Create** operation adds a new resource.

Usually, `POST` is used.

```python
@app.post("/courses")
def create_course(course: Course):
    return course
```

## 3. Read

The **Read** operation retrieves existing data.

`GET` is used.

### Get all

```python
@app.get("/courses")
def get_courses():
    return courses
```

### Get one

```python
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {"id": course_id}
```

## 4. Update

The **Update** operation modifies existing data.

* `PUT` → generally replaces the complete resource
* `PATCH` → updates specific fields

```text
PUT   → Complete update
PATCH → Partial update
```

## 5. Delete

The **Delete** operation removes a resource.

```python
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    return {"message": "Course deleted"}
```

## 6. Simple CRUD API

A basic CRUD API can use a Python list as temporary storage.

```python
courses = []

@app.post("/courses")
def create_course(course: Course):
    courses.append(course)
    return course

@app.get("/courses")
def get_courses():
    return courses

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):
    courses[course_id] = course
    return course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    courses.pop(course_id)
    return {"message": "Course deleted"}
```

In real applications, persistent database storage is normally used instead of an in-memory list.

## 7. API Architecture

**API architecture** is the way an API application is organized into different components.

A common flow is:

```text
Client
  ↓
Route
  ↓
Service
  ↓
Database
  ↓
Response
```

Each layer has a specific responsibility.

## 8. Why Separate Responsibilities?

Putting everything inside `main.py` makes large applications difficult to maintain.

Instead, separate:

```text
Routes
Services
Database
Models
Dependencies
```

This makes the application easier to:

* Understand
* Test
* Debug
* Modify
* Scale

## 9. Routes

A **route** defines the endpoint through which a client communicates with the API.

```python
@app.get("/courses")
def get_courses():
    ...
```

Routes should mainly handle:

* Request parameters
* Request models
* Calling services
* Returning responses

Large amounts of business logic should not be placed inside routes.

## 10. Service Layer

The **service layer** contains the main business logic of the application.

Example:

```python
def recommend_courses(goal: str):
    # Business logic
    ...
```

The route calls the service:

```python
@app.post("/recommend")
def recommend(request: RecommendationRequest):
    return recommend_courses(request.goal)
```

This keeps the route simple.

## 11. Database Layer

The database layer handles communication with the database.

```text
Route
  ↓
Service
  ↓
Database
```

The service can ask the database layer for data.

```python
def get_course(course_id):
    return db.get_course(course_id)
```

The source introduces PostgreSQL and SQLAlchemy as technologies that will be used later.

## 12. APIRouter

`APIRouter` is used to organize related FastAPI routes into separate modules.

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/courses")
def get_courses():
    return []
```

The router can then be included in `main.py`:

```python
from fastapi import FastAPI
from routes.courses import router

app = FastAPI()

app.include_router(router)
```

## 13. Recommended Project Structure

A small-to-medium FastAPI application can be organized like this:

```text
app/
├── main.py
├── routes/
│   ├── courses.py
│   └── recommendation.py
├── services/
│   ├── course_service.py
│   └── llm_service.py
├── models/
│   ├── course.py
│   └── recommendation.py
├── database/
│   └── database.py
└── dependencies.py
```

Responsibilities:

```text
main.py
→ Starts the FastAPI application

routes/
→ API endpoints

services/
→ Business logic

models/
→ Request/response/data models

database/
→ Database connection and operations

dependencies.py
→ Shared FastAPI dependencies
```

## 14. Route vs Service

This distinction is important.

### Route

Handles the API request.

```python
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return course_service.get_course(course_id)
```

### Service

Handles application logic.

```python
def get_course(course_id: int):
    # Business logic
    return ...
```

Remember:

```text
Route   = How the client talks to the application
Service = What the application does
```

## 15. API Architecture Flow

A typical backend request flows through:

```text
Client
  ↓
HTTP Request
  ↓
FastAPI Route
  ↓
Request Validation
  ↓
Service Layer
  ↓
Database / External API / LLM
  ↓
Service Result
  ↓
Response Model
  ↓
HTTP Response
  ↓
Client
```

## 16. CRUD + Service Layer

Separating CRUD logic from routes makes the application easier to maintain.

### Service

```python
courses = []

def create_course(course):
    courses.append(course)
    return course

def get_courses():
    return courses

def delete_course(course_id):
    courses.pop(course_id)
```

### Route

```python
@router.post("/courses")
def create(course):
    return create_course(course)

@router.get("/courses")
def get_all():
    return get_courses()

@router.delete("/courses/{course_id}")
def delete(course_id: int):
    delete_course(course_id)
    return {"message": "Course deleted"}
```

The route handles communication while the service contains the main logic.

## 17. API Architecture for AI Applications

AI applications can have additional components:

```text
Client
  ↓
FastAPI
  ↓
Route
  ↓
Service
  ↓
LLM / Embedding / Vector DB
  ↓
Service
  ↓
Response Model
  ↓
Client
```

For an AI Course Support API:

```text
User
  ↓
FastAPI
  ↓
/recommend
  ↓
Recommendation Service
  ↓
Embedding / Course Search
  ↓
LLM
  ↓
Structured Output
  ↓
Pydantic Validation
  ↓
Response
```

## 18. CRUD in an AI Course Support API

Example endpoints:

```text
GET     /health
GET     /courses
GET     /courses/{course_id}
POST    /courses
POST    /recommend
POST    /ask
PUT     /courses/{course_id}
DELETE  /courses/{course_id}
```

Course endpoints demonstrate CRUD, while AI endpoints provide application-specific functionality.

## 19. RESTful Resource Design

Use **nouns** for resources.

Good:

```text
GET    /courses
GET    /courses/1
POST   /courses
DELETE /courses/1
```

Avoid action-based paths such as:

```text
GET  /getCourses
POST /createCourse
POST /deleteCourse
```

The HTTP method already describes the operation.

## 20. HTTP Status Codes

Common status codes:

```text
200 OK
→ Request successful

201 Created
→ Resource successfully created

204 No Content
→ Request successful with no response body

400 Bad Request
→ Invalid request

404 Not Found
→ Resource does not exist

422 Unprocessable Entity
→ Request validation failed

500 Internal Server Error
→ Server-side error
```

Example:

```python
from fastapi import status

@app.post(
    "/courses",
    status_code=status.HTTP_201_CREATED
)
def create_course(course: Course):
    return course
```

## 21. Error Handling

FastAPI provides `HTTPException` for returning meaningful API errors.

```python
from fastapi import HTTPException

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return courses[course_id]
```

Response:

```json
{
    "detail": "Course not found"
}
```

## 22. Why Architecture Matters for Agentic AI

Agentic applications may contain:

```text
LLM
Tools
Memory
RAG
Database
External APIs
Authentication
Observability
```

Keeping everything inside one route becomes difficult to maintain.

A better structure is:

```text
FastAPI
  ↓
Routes
  ↓
Services
  ↓
Agent
  ↓
Tools / RAG / Memory / LLM
  ↓
Database / External APIs
```

This separation becomes increasingly important as agentic applications become more complex.

## 23. Common Mistakes

### Putting everything in `main.py`

Avoid creating one large file.

### Putting business logic inside routes

Keep routes simple and move application logic into services.

### Using incorrect HTTP methods

Prefer:

```text
GET /courses
```

instead of:

```text
POST /getCourses
```

### Returning inconsistent responses

Keep response structures predictable.

### Ignoring error handling

Handle cases such as:

```text
Resource not found
Invalid input
Database failure
External API failure
```

### Using in-memory data in production

```python
courses = []
```

is useful for learning, but production applications need persistent storage such as PostgreSQL.

## 24. Mental Model

CRUD:

```text
Create → POST
Read   → GET
Update → PUT / PATCH
Delete → DELETE
```

Architecture:

```text
Client
  ↓
Route
  ↓
Service
  ↓
Database / LLM / External API
  ↓
Response
  ↓
Client
```

The main idea:

**Routes handle communication, services handle business logic, and databases handle data.**
