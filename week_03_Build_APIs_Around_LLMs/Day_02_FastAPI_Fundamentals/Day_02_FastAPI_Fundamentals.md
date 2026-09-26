# Week 03 — Day 02: FastAPI Fundamentals

## 1. FastAPI

**FastAPI** is a modern Python web framework used to build APIs quickly and efficiently.

It uses Python type hints for:

* Request validation
* Response validation
* Automatic API documentation
* Developer-friendly code

---

## 2. Why FastAPI?

FastAPI provides:

* Simple API development
* Automatic validation
* Type-hint support
* Automatic documentation
* Async support
* Good performance
* Easy integration with databases and AI services

For our Agentic AI roadmap, FastAPI acts as the **backend layer around AI applications**.

---

## 3. FastAPI and Uvicorn

### FastAPI

Provides the framework for creating APIs.

### Uvicorn

Runs the FastAPI application as an **ASGI server**.

**ASGI** stands for **Asynchronous Server Gateway Interface**.

Install:

```bash
pip install fastapi uvicorn
```

---

## 4. FastAPI Application

A basic FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()` creates the FastAPI application.

`app` is the main FastAPI application object.

---

## 5. Route

A **route** connects an HTTP method and URL to a Python function.

Example:

```python
@app.get("/")
def home():
    return {"message": "Hello World"}
```

Here:

```python
@app.get("/")
```

means:

```text
GET /
```

When a client sends a GET request to `/`, FastAPI executes the `home()` function.

---

## 6. Running the Application

Run the application using:

```bash
uvicorn main:app --reload
```

Meaning:

```text
main     → main.py
app      → FastAPI application object
--reload → Restart server when code changes
```

The API is normally available at:

```text
http://127.0.0.1:8000
```

---

## 7. API Documentation

FastAPI automatically generates API documentation.

### Swagger UI

Available at:

```text
/docs
```

Example:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

* See endpoints
* View parameters
* Send requests
* See responses
* Test the API

### ReDoc

FastAPI also provides:

```text
/redoc
```

---

## 8. GET Route

A GET route is commonly used to retrieve data.

```python
@app.get("/courses")
def get_courses():
    return {
        "courses": [
            "Python",
            "Java",
            "Spring Boot"
        ]
    }
```

Request:

```text
GET /courses
```

---

## 9. POST Route

POST routes are commonly used when the client sends data to the server.

```python
@app.post("/courses")
def create_course():
    return {
        "message": "Course created"
    }
```

Request:

```text
POST /courses
```

Request bodies will later be handled properly using Pydantic models.

---

## 10. Path Parameters

Path parameters allow us to access a specific resource.

```python
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {
        "course_id": course_id
    }
```

Request:

```text
GET /courses/10
```

Here:

```text
{course_id}
```

is the path parameter.

FastAPI uses the type hint:

```python
course_id: int
```

to convert and validate the value.

---

## 11. Query Parameters

Query parameters are values added after `?` in the URL.

Example:

```python
@app.get("/courses")
def get_courses(level: str | None = None):
    return {
        "level": level
    }
```

Request:

```text
GET /courses?level=beginner
```

Here:

```text
level=beginner
```

is a query parameter.

---

## 12. Path vs Query Parameters

### Path Parameter

Used to identify a specific resource.

```text
GET /courses/10
```

```python
course_id: int
```

### Query Parameter

Usually used for filtering or controlling the request.

```text
GET /courses?level=beginner
```

```python
level: str
```

---

## 13. Multiple Query Parameters

A route can have multiple query parameters.

```python
@app.get("/courses")
def get_courses(
    level: str | None = None,
    limit: int = 10
):
    return {
        "level": level,
        "limit": limit
    }
```

Request:

```text
GET /courses?level=beginner&limit=5
```

---

## 14. Default Values

FastAPI supports default values through Python function parameters.

```python
@app.get("/courses")
def get_courses(limit: int = 10):
    return {
        "limit": limit
    }
```

If the client sends:

```text
/courses
```

then:

```text
limit = 10
```

If the client sends:

```text
/courses?limit=20
```

then:

```text
limit = 20
```

---

## 15. Required Parameters

A parameter without a default value is generally required.

```python
@app.get("/courses")
def get_courses(category: str):
    return {
        "category": category
    }
```

The client must provide:

```text
/courses?category=backend
```

---

## 16. Type Validation

FastAPI uses Python type hints to validate request data.

Example:

```python
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {
        "course_id": course_id
    }
```

Valid:

```text
/courses/10
```

Invalid:

```text
/courses/abc
```

FastAPI automatically returns a validation error.

---

## 17. Returning JSON

FastAPI automatically converts Python dictionaries into JSON responses.

Python:

```python
@app.get("/health")
def health():
    return {
        "status": "ok"
    }
```

Response:

```json
{
    "status": "ok"
}
```

Lists and other supported Python data structures can also be returned.

---

## 18. HTTP Status Codes

FastAPI allows you to specify response status codes.

Example:

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post(
    "/courses",
    status_code=status.HTTP_201_CREATED
)
def create_course():
    return {
        "message": "Course created"
    }
```

Common status codes:

```text
200 → Success
201 → Created
204 → No Content
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
422 → Validation Error
500 → Server Error
```

---

## 19. Tags

Tags help organize endpoints in Swagger documentation.

Example:

```python
@app.get(
    "/courses",
    tags=["Courses"]
)
def get_courses():
    return {
        "courses": []
    }
```

Swagger will group this endpoint under:

```text
Courses
```

Tags become useful when an API contains many endpoints.

---

## 20. Multiple Routes

A FastAPI application can contain many routes.

```python
@app.get("/courses")
def get_courses():
    return {"message": "All courses"}


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {"course_id": course_id}


@app.post("/courses")
def create_course():
    return {"message": "Course created"}
```

The application can handle:

```text
GET  /courses
GET  /courses/10
POST /courses
```

---

## 21. Basic FastAPI Project Structure

For a small project:

```text
project/
├── main.py
├── requirements.txt
└── .env
```

Basic flow:

```text
main.py
   ↓
FastAPI Application
   ↓
Routes
   ↓
Business Logic
```

For larger applications, routes, services, models, and database code should be separated.

---

## 22. FastAPI + AI Application

FastAPI can be used as the backend for an AI application.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend():
    return {
        "message": "Recommendation generated"
    }
```

Future architecture:

```text
Client
   ↓
FastAPI
   ↓
API Route
   ↓
Service Layer
   ↓
LLM / Vector DB / Database
   ↓
Response
```

---

## 23. FastAPI Request Flow

When a request arrives:

```text
Client
   ↓
HTTP Request
   ↓
FastAPI
   ↓
Find Matching Route
   ↓
Validate Parameters
   ↓
Execute Python Function
   ↓
Generate Response
   ↓
HTTP Response
   ↓
Client
```

Later, validation and business logic can be structured using Pydantic models and service layers.

---

## 24. FastAPI vs Flask

| FastAPI                       | Flask                                              |
| ----------------------------- | -------------------------------------------------- |
| Modern API-focused framework  | Lightweight web framework                          |
| Uses type hints heavily       | Type hints are optional                            |
| Automatic validation          | Usually requires additional setup                  |
| Automatic API documentation   | Usually needs extra tools                          |
| Built-in async support        | Async support exists but is not its primary design |
| Excellent for API/AI backends | Flexible for many web applications                 |

For this roadmap, FastAPI is used for building AI backends.

---

## 25. Common Mistakes

### Forgetting to Start the Server

```bash
uvicorn main:app --reload
```

### Wrong Module Name

If the file is:

```text
main.py
```

use:

```bash
uvicorn main:app --reload
```

### Wrong Parameter Type

If:

```python
def get_course(course_id: int):
```

receives:

```text
/courses/abc
```

FastAPI validation will fail.

### Putting Everything in `main.py`

Small projects can use one file.

Larger applications should separate:

* Routes
* Services
* Models
* Database logic

---

## 26. Mini Practice

Create these endpoints:

```text
GET  /health
GET  /courses
GET  /courses/{course_id}
GET  /courses?level=beginner
POST /courses
```

Test them through:

```text
/docs
```

The basic flow is:

```text
Route
  ↓
HTTP Method
  ↓
Parameters
  ↓
Python Function
  ↓
Response
```