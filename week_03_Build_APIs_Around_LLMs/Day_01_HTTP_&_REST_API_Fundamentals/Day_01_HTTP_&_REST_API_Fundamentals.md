# Day 01: HTTP & REST API Fundamentals

## 1. API

**API (Application Programming Interface)** is a defined interface that allows one software system to communicate with another.

Basic flow:

```text
Frontend
   ↓
 API Request
   ↓
 Backend
   ↓
 Database
   ↓
 API Response
   ↓
 Frontend
```

In an AI application:

```text
Frontend → FastAPI → Agent / LLM → Response
```

The client does not need to know how the backend works internally. It only needs to know how to communicate with the API.

---

## 2. Client and Server

**Client** sends a request.

Examples:

* Browser
* React frontend
* Mobile app
* Postman
* Python program

**Server** receives the request, processes it, and returns a response.

```text
Client
  ↓
HTTP Request
  ↓
Server
  ↓
HTTP Response
  ↓
Client
```

---

## 3. HTTP

**HTTP (HyperText Transfer Protocol)** is a communication protocol used to exchange requests and responses between clients and servers.

```text
Client
  ↓
HTTP Request
  ↓
Server
  ↓
HTTP Response
  ↓
Client
```

**HTTPS** is HTTP with encryption provided by TLS.

---

## 4. HTTP Request

An HTTP request is the message sent by the client to the server.

It can contain:

```text
Method
URL
Headers
Query Parameters
Path Parameters
Body
```

Example:

```http
POST /recommend
Content-Type: application/json
```

```json
{
  "goal": "Java backend developer"
}
```

---

## 5. HTTP Response

An HTTP response is the message returned by the server after processing a request.

It commonly contains:

```text
Status Code
Headers
Body
```

Example:

```http
200 OK
Content-Type: application/json
```

```json
{
  "message": "Recommendation generated"
}
```

---

## 6. HTTP Methods

| Method | Common Use                  |
| ------ | --------------------------- |
| GET    | Retrieve data               |
| POST   | Create or submit data       |
| PUT    | Replace/update a resource   |
| PATCH  | Partially update a resource |
| DELETE | Delete a resource           |

Examples:

```http
GET /courses
POST /courses
PUT /courses/1
PATCH /courses/1
DELETE /courses/1
```

### PUT vs PATCH

**PUT** generally replaces the existing resource.

**PATCH** partially updates the resource.

---

## 7. REST

**REST (Representational State Transfer)** is an architectural style for designing networked applications.

REST APIs commonly use:

* Resources
* URLs
* HTTP methods
* HTTP status codes
* Stateless requests
* JSON or other data representations

The basic idea is to represent application data as **resources** and use HTTP methods to operate on them.

---

## 8. Resource

A **resource** is an entity managed or exposed by an API.

Examples:

```text
/users
/courses
/products
/orders
/documents
/agents
```

A specific resource can be identified using an ID:

```text
/courses/10
/users/25
```

---

## 9. REST Resource URLs

REST-style URLs usually use **nouns** to represent resources.

Less REST-like:

```text
/getCourses
/createCourse
/deleteCourse
```

Better:

```http
GET /courses
POST /courses
DELETE /courses/10
```

The **HTTP method describes the operation**, while the **URL identifies the resource**.

---

## 10. JSON

**JSON (JavaScript Object Notation)** is a common data format used to exchange structured data between applications.

Example:

```json
{
  "name": "Spring Boot",
  "level": "Beginner",
  "duration": 30
}
```

JSON supports:

* String
* Number
* Boolean
* Array
* Object
* null

---

## 11. Request Body

The **request body** contains data sent by the client to the server.

Example:

```http
POST /recommend
```

```json
{
  "goal": "Java backend developer",
  "experience": "beginner"
}
```

The backend reads and validates this data before processing the request.

---

## 12. Query Parameters

Query parameters are optional values added to the URL after `?`.

Example:

```http
GET /courses?level=beginner
```

Multiple parameters:

```http
GET /courses?level=beginner&limit=10
```

Common uses:

* Filtering
* Searching
* Sorting
* Pagination
* Optional configuration

---

## 13. Path Parameters

A path parameter is a value in the URL used to identify a specific resource.

Example:

```http
GET /courses/10
```

Here, `10` identifies the course.

### Query vs Path

```text
Path:
GET /courses/10

Query:
GET /courses?level=beginner
```

Use a **path parameter** to identify a specific resource.

Use **query parameters** for optional filtering or configuration.

---

## 14. HTTP Headers

HTTP headers carry additional information about a request or response.

Example:

```http
Content-Type: application/json
Authorization: Bearer <token>
Accept: application/json
```

Common headers:

* `Content-Type` — format of the body
* `Accept` — response formats accepted by the client
* `Authorization` — authentication credentials
* `User-Agent` — identifies the client software

---

## 15. Content-Type

`Content-Type` tells the receiver what format the message body uses.

Example:

```http
Content-Type: application/json
```

This means the body contains JSON.

---

## 16. HTTP Status Codes

Status codes tell the client the result of its request.

```text
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error
```

Important codes:

| Code | Meaning                              |
| ---- | ------------------------------------ |
| 200  | Request successful                   |
| 201  | Resource created                     |
| 204  | Success with no response body        |
| 400  | Bad request                          |
| 401  | Authentication required/invalid      |
| 403  | Request understood but not permitted |
| 404  | Resource not found                   |
| 422  | Request validation failed            |
| 500  | Unexpected server error              |

Examples:

```text
GET /courses
→ 200 OK

POST /courses
→ 201 Created

DELETE /courses/10
→ 204 No Content

GET /courses/9999
→ 404 Not Found
```

FastAPI commonly uses `422` for request validation errors.

---

## 17. Statelessness

**Statelessness** means each request should contain the information needed by the server to process it.

The server should not depend on hidden state from a previous request to understand the current request.

For example:

```http
GET /courses/10
GET /courses/20
```

Each request can be understood independently.

Authentication information, such as a token, can be included in each request when required.

---

## 18. API Endpoint

An **endpoint** is a specific combination of an HTTP method and URL through which a client interacts with an API.

Examples:

```http
GET  /courses
POST /courses
GET  /courses/{id}
POST /recommend
POST /chat
```

An endpoint defines:

```text
HTTP Method
+
URL
+
Expected Input
+
Response
```

---

## 19. API vs REST API

**API** is a general concept describing an interface through which software components communicate.

**REST API** is an API designed around REST principles, commonly using HTTP methods and resource-based URLs.

Other API styles include:

```text
API
├── REST
├── GraphQL
├── gRPC
└── Other API styles
```

REST is one way of designing an API.

---

## 20. REST API vs LLM API

### REST API

A web API designed around HTTP and REST principles.

```http
GET /courses
POST /recommend
```

### LLM API

An API provided by an LLM provider that allows an application to interact with a language model.

```text
Your Application
      ↓
    LLM API
      ↓
 Language Model
      ↓
   Response
```

They can be combined:

```text
Frontend
   ↓
Your REST API
   ↓
LLM API
   ↓
LLM
   ↓
Your REST API
   ↓
Frontend
```

---

## 21. AI Course Recommendation API

Example endpoint:

```http
POST /recommend
```

Request:

```json
{
  "goal": "Become a Java backend developer",
  "skills": ["Java", "SQL"]
}
```

Possible backend flow:

```text
FastAPI
   ↓
Validate Request
   ↓
Retrieve Relevant Courses
   ↓
Build Context
   ↓
Call LLM
   ↓
Generate Recommendation
```

Response:

```json
{
  "goal": "Become a Java backend developer",
  "recommendations": [
    {
      "course": "Spring Boot",
      "reason": "Build backend applications using Java"
    },
    {
      "course": "REST API Development",
      "reason": "Learn how to build backend APIs"
    }
  ]
}
```

---

## 22. Basic API Architecture

Typical backend:

```text
Client
  ↓
HTTP Request
  ↓
API Layer
  ↓
Validation
  ↓
Business Logic
  ↓
Database / LLM / External APIs
  ↓
HTTP Response
  ↓
Client
```

Agentic AI backend:

```text
Client
  ↓
FastAPI
  ↓
Request Validation
  ↓
Agent
  ↓
Tools / RAG / Memory
  ↓
LLM
  ↓
Response
```

---

## 23. Why FastAPI?

**FastAPI** is a Python web framework for building APIs.

Important features:

* Python type hints
* Request validation
* Automatic API documentation
* Async support
* Pydantic integration
* Dependency injection

The HTTP and REST concepts learned here are the foundation for understanding FastAPI.

---

## 24. Complete API Request Flow

```text
CLIENT
  ↓
HTTP REQUEST
  ├── Method
  ├── URL
  ├── Headers
  ├── Query Parameters
  ├── Path Parameters
  └── Body
  ↓
SERVER
  ↓
Process Request
  ↓
Database / LLM / Agent
  ↓
HTTP RESPONSE
  ├── Status Code
  ├── Headers
  └── Response Body
  ↓
CLIENT
```