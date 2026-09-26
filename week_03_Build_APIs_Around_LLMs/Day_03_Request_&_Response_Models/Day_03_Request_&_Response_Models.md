# Week 03 — Day 03: Request & Response Models

## 1. Request Model

A **request model** defines the structure and data types that an API expects from the client.

Pydantic models are commonly used as request models in FastAPI.

```python
class CourseRequest(BaseModel):
    name: str
    level: str
    duration: int
```

FastAPI receives the JSON request, validates it using the model, and passes a Python object to the route.



## 2. Pydantic

**Pydantic** is a Python library used for data validation and data modeling using Python type hints.

FastAPI uses Pydantic extensively.

```python
class User(BaseModel):
    name: str
    age: int
```

Pydantic validates the incoming data according to the defined types.

## 3. Request Body

A Pydantic model used as a route parameter represents structured request body data.

```python
class CourseRequest(BaseModel):
    name: str
    level: str

@app.post("/courses")
def create_course(course: CourseRequest):
    return course
```

FastAPI automatically converts the JSON request body into a Pydantic object.

## 4. Type Validation

Pydantic validates data according to the model.

```python
class UserRequest(BaseModel):
    name: str
    age: int
```

For example:

```json
{
    "name": "Alex",
    "age": "hello"
}
```

is invalid because `age` should be an integer.

FastAPI returns a validation error instead of passing invalid data to the route.

## 5. Required Fields

Fields without default values are required.

```python
class UserRequest(BaseModel):
    name: str
    age: int
```

Both `name` and `age` are required.

## 6. Optional Fields

A field can be optional using an appropriate optional type and default value.

```python
class UserRequest(BaseModel):
    name: str
    age: int | None = None
```

If `age` is not provided, its value is `None`.

## 7. Default Values

Fields can have default values.

```python
class CourseRequest(BaseModel):
    name: str
    level: str = "beginner"
```

If `level` is not provided, it becomes `"beginner"`.

## 8. Nested Models

A Pydantic model can contain another Pydantic model.

```python
class Instructor(BaseModel):
    name: str
    experience: int

class CourseRequest(BaseModel):
    name: str
    instructor: Instructor
```

This is useful for structured and nested API data.

## 9. Lists of Values

A model can contain a list.

```python
class CourseRequest(BaseModel):
    name: str
    topics: list[str]
```

## 10. Lists of Models

A list can also contain structured Pydantic objects.

```python
class Topic(BaseModel):
    name: str
    duration: int

class CourseRequest(BaseModel):
    name: str
    topics: list[Topic]
```

## 11. Enum / Allowed Values

Sometimes a field should accept only specific values.

```python
from enum import Enum

class Experience(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"
```

The model can then use:

```python
class UserRequest(BaseModel):
    experience: Experience
```

Only the defined values are accepted.

## 12. Field Validation

Pydantic allows additional validation rules using `Field`.

```python
from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    name: str
    age: int = Field(ge=0)
```

`ge=0` means **greater than or equal to 0**.

So:

```text
20  → valid
-5  → invalid
```

## 13. String Constraints

String fields can also have constraints.

```python
class UserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=20)
```

This means:

```text
Minimum length → 3
Maximum length → 20
```

## 14. Request Model vs Path Parameter

A path parameter is part of the URL.

```python
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {"id": course_id}
```

Example:

```text
GET /courses/10
```

A request model represents structured body data.

```python
class CourseRequest(BaseModel):
    name: str
    level: str
```

## 15. Request Model vs Query Parameter

A query parameter is passed in the URL.

```python
@app.get("/courses")
def get_courses(level: str):
    return {"level": level}
```

Example:

```text
GET /courses?level=beginner
```

A request model is normally used for structured request body data.

## 16. Response Model

A **response model** defines the structure and type of data that an API should return to the client.

```python
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
```

## 17. Using a Response Model

FastAPI uses `response_model` to define the expected response structure.

```python
@app.get(
    "/courses/{course_id}",
    response_model=CourseResponse
)
def get_course(course_id: int):
    return {
        "id": course_id,
        "name": "FastAPI",
        "level": "beginner"
    }
```

## 18. Why Use Response Models?

Response models provide:

* Predictable response structure
* Response validation
* Automatic API documentation
* Better API contracts
* Control over returned fields

Flow:

```text
Python Data
    ↓
Response Model
    ↓
Validation / Filtering
    ↓
JSON Response
    ↓
Client
```

## 19. Request Model vs Response Model

### Request Model

Defines what the **client sends**.

```text
Client
  ↓
Request Model
  ↓
API
```

### Response Model

Defines what the **server returns**.

```text
API
  ↓
Response Model
  ↓
Client
```

They can be different because the client does not always send the same data that the server returns.

For example, the server may generate an `id`.

## 20. Hiding Sensitive Data

Response models can control which fields are returned.

Suppose database data contains:

```text
id
name
email
password_hash
```

A response model can exclude the sensitive field:

```python
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
```

This helps prevent unwanted fields from being exposed through the API response.

## 21. Nested Response Models

Response models can also contain other models.

```python
class InstructorResponse(BaseModel):
    name: str

class CourseResponse(BaseModel):
    id: int
    name: str
    instructor: InstructorResponse
```

## 22. API Contract

An **API contract** defines what the client can send and what the server will return.

Request and response models make this contract explicit.

```text
Client
  ↓
Request Model
  ↓
API
  ↓
Response Model
  ↓
Client
```

## 23. Automatic Documentation

FastAPI uses request and response models to generate API documentation.

For example:

```text
/docs
```

shows the API endpoints, request bodies, response models, and their schemas.

## 24. AI Application Example

For an AI Course Support API:

```python
class RecommendationRequest(BaseModel):
    goal: str
    current_skills: list[str]
    experience: str
```

Response models can define structured recommendations:

```python
class Recommendation(BaseModel):
    course: str
    reason: str

class RecommendationResponse(BaseModel):
    goal: str
    recommendations: list[Recommendation]
    next_steps: list[str]
```

This gives the AI API a predictable contract.

## 25. Complete Data Flow

```text
Client
   ↓
JSON Request
   ↓
FastAPI
   ↓
Pydantic Request Model
   ↓
Validation
   ↓
Route Function
   ↓
Business Logic
   ↓
Response Model
   ↓
JSON Response
   ↓
Client
```

## 26. Common Mistakes

### Mixing Request and Response Models

Keep them separate when they represent different data.

### Returning Sensitive Data

Do not expose passwords or internal database information.

### Not Defining Types

Use meaningful type hints:

```python
name: str
age: int
skills: list[str]
```