# Day 6 — JSON, APIs & Error Handling

JSON is commonly used to exchange data between applications.

APIs allow different applications or services to communicate with each other.

Error handling helps us handle unexpected situations without crashing the entire application.

These concepts are important for FastAPI, LLM applications, RAG systems, and Agentic AI.

## Topics Covered

1. **JSON** — Understanding JSON data format
2. **JSON Objects & Arrays** — Working with JSON structures
3. **JSON in Python** — Using the `json` module
4. **Serialization & Deserialization** — Converting between Python and JSON
5. **APIs** — Understanding how applications communicate
6. **HTTP Methods** — GET, POST, PUT, PATCH, DELETE
7. **HTTP Status Codes** — Understanding common API responses
8. **Requests** — Calling APIs from Python
9. **API Parameters** — Query parameters, path parameters, and request bodies
10. **Exception Handling** — Handling errors using `try`, `except`, `else`, and `finally`
11. **Custom Exceptions** — Creating application-specific errors
12. **Practical Usage** — Using APIs and error handling in AI applications

## 1. JSON

JSON stands for **JavaScript Object Notation**.

It is a common format used to store and exchange data.

Example:

```json
{
    "name": "Shubham",
    "age": 25,
    "is_active": true
}
```

JSON uses:

* Key-value pairs
* Strings
* Numbers
* Boolean values
* Arrays
* Objects
* `null`

## 2. JSON Objects and Arrays

A JSON object looks like:

```json
{
    "name": "Shubham",
    "age": 25
}
```

A JSON array contains multiple values:

```json
{
    "skills": [
        "Python",
        "Java",
        "React"
    ]
}
```

Nested JSON:

```json
{
    "name": "Shubham",
    "address": {
        "city": "Dehradun",
        "country": "India"
    }
}
```

JSON is commonly used in API requests and responses.

## 3. JSON in Python

Python provides the built-in `json` module.

```python
import json
```

Convert a Python dictionary into JSON:

```python
user = {
    "name": "Shubham",
    "age": 25
}

data = json.dumps(user)

print(data)
```

Output:

```text
{"name": "Shubham", "age": 25}
```

`json.dumps()` converts Python data into a JSON string.

## 4. Serialization and Deserialization

### Serialization

Converting Python data into JSON.

```python
import json

user = {
    "name": "Shubham",
    "age": 25
}

json_data = json.dumps(user)
```

Flow:

```text
Python Object → JSON
```

### Deserialization

Converting JSON back into Python data.

```python
import json

json_data = '{"name": "Shubham", "age": 25}'

user = json.loads(json_data)

print(user["name"])
```

Output:

```text
Shubham
```

Flow:

```text
JSON → Python Object
```

Remember:

```text
dumps() → Python → JSON
loads() → JSON → Python
```

## 5. APIs

API stands for **Application Programming Interface**.

An API allows two applications to communicate with each other.

For example:

```text
Python Application
       ↓
      API
       ↓
Weather Service
       ↓
Weather Data
```

Your application sends a request.

The API processes it and returns a response.

Example:

```text
Request
   ↓
GET /users/101
   ↓
Server
   ↓
Response
```

## 6. HTTP Methods

Common HTTP methods are:

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Retrieve data         |
| POST   | Create data           |
| PUT    | Replace/update data   |
| PATCH  | Partially update data |
| DELETE | Delete data           |

Example:

```text
GET /users
```

Gets users.

```text
POST /users
```

Creates a new user.

```text
DELETE /users/101
```

Deletes user `101`.

## 7. HTTP Status Codes

APIs use status codes to indicate the result of a request.

### 2xx — Success

```text
200 → OK
201 → Created
204 → No Content
```

### 4xx — Client Error

```text
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
```

### 5xx — Server Error

```text
500 → Internal Server Error
503 → Service Unavailable
```

A simple way to remember:

```text
2xx → Success
4xx → Client problem
5xx → Server problem
```

## 8. Calling APIs from Python

The `requests` library can be used to call APIs.

Install:

```bash
pip install requests
```

Example:

```python
import requests

response = requests.get("https://api.example.com/users")

print(response.status_code)
print(response.json())
```

`response.json()` converts the JSON response into Python data.

A POST request:

```python
import requests

data = {
    "name": "Shubham",
    "age": 25
}

response = requests.post(
    "https://api.example.com/users",
    json=data
)

print(response.json())
```

## 9. API Parameters

APIs commonly receive data in three ways.

### Path Parameter

The value is part of the URL.

```text
/users/101
```

Here `101` is the user ID.

### Query Parameter

The value comes after `?`.

```text
/users?age=25
```

Here:

```text
age=25
```

is a query parameter.

Multiple parameters:

```text
/users?age=25&city=Dehradun
```

### Request Body

Data is sent inside the request body.

Example:

```json
{
    "name": "Shubham",
    "age": 25
}
```

POST requests commonly use request bodies.

## 10. Exception Handling

Errors can happen while a program is running.

Python provides:

```python
try
except
else
finally
```

Example:

```python
try:
    number = int(input("Enter number: "))
    print(10 / number)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

If the user enters:

```text
abc
```

Python raises `ValueError`.

If the user enters:

```text
0
```

Python raises `ZeroDivisionError`.

## 11. `else` and `finally`

`else` runs when no exception occurs.

```python
try:
    number = int("10")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")
```

Output:

```text
Conversion successful
```

`finally` runs whether an error occurs or not.

```python
try:
    print("Processing")

except Exception:
    print("Error")

finally:
    print("Finished")
```

Output:

```text
Processing
Finished
```

## 12. Custom Exceptions

We can create our own exceptions.

```python
class InsufficientBalanceError(Exception):
    pass
```

Use it:

```python
balance = 500

if balance < 1000:
    raise InsufficientBalanceError("Insufficient balance")
```

Custom exceptions make application errors easier to understand.

## API Error Handling

When calling an API, we should handle possible failures.

```python
import requests

try:
    response = requests.get(
        "https://api.example.com/users"
    )

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.RequestException:
    print("API request failed")
```

`raise_for_status()` raises an exception when the API returns an error status.

## JSON + API Example

Suppose an AI application sends a question to an API.

Request:

```json
{
    "question": "What is RAG?",
    "user_id": 101
}
```

API response:

```json
{
    "answer": "RAG combines retrieval with generation.",
    "source": "knowledge_base"
}
```

Python can process it:

```python
import json

response = '''
{
    "answer": "RAG combines retrieval with generation.",
    "source": "knowledge_base"
}
'''

data = json.loads(response)

print(data["answer"])
print(data["source"])
```

## JSON + Pydantic

Pydantic can also be used to structure API data.

```python
from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    user_id: int
```

Example data:

```python
request = ChatRequest(
    question="What is RAG?",
    user_id=101
)

print(request.question)
print(request.user_id)
```

This connects the concepts from Day 5 and Day 6:

```text
JSON
  ↓
API Request
  ↓
Pydantic Validation
  ↓
Python Application
  ↓
AI Agent / RAG
  ↓
API Response
  ↓
JSON
```

## Error Handling in AI Applications

AI applications can fail for many reasons:

```text
API unavailable
Invalid user input
LLM timeout
Invalid JSON
Database error
Vector database error
Authentication failure
```

Instead of letting the application crash, handle these errors properly.

Example:

```python
try:
    result = ask_agent("Explain RAG")

except Exception as error:
    print(f"Agent failed: {error}")
```

For production applications, specific exceptions should generally be handled instead of catching every error with a broad `Exception`.

## Quick Revision

| Concept        | Meaning                            |
| -------------- | ---------------------------------- |
| JSON           | Data exchange format               |
| `json.dumps()` | Python → JSON                      |
| `json.loads()` | JSON → Python                      |
| API            | Allows applications to communicate |
| GET            | Retrieve data                      |
| POST           | Create data                        |
| PUT            | Replace data                       |
| PATCH          | Partially update data              |
| DELETE         | Delete data                        |
| 200            | Successful request                 |
| 404            | Resource not found                 |
| 500            | Server error                       |
| `try`          | Code that may cause an error       |
| `except`       | Handles an error                   |
| `else`         | Runs when no error occurs          |
| `finally`      | Always runs                        |
| `raise`        | Manually raises an exception       |

## Practice

### 1. JSON

Create a JSON object containing:

```text
name
age
skills
city
```

Convert it between Python and JSON.

### 2. API

Write Python code to:

* Send a GET request
* Print the status code
* Print the JSON response

### 3. Exception Handling

Create a calculator that handles:

* Invalid input
* Division by zero

### 4. Custom Exception

Create:

```python
InvalidAgeError
```

Raise it when age is less than `18`.

### 5. AI API Structure

Create a Pydantic model:

```text
ChatRequest
    question
    user_id
```

Create another model:

```text
ChatResponse
    answer
    source
```

## Day 6 Goal

By the end of Day 6, you should understand:

```text
JSON
  ↓
Python JSON Handling
  ↓
APIs
  ↓
HTTP Methods
  ↓
HTTP Status Codes
  ↓
API Requests
  ↓
Exception Handling
  ↓
Custom Exceptions
  ↓
FastAPI + AI Applications
```

These concepts form the foundation for building Python APIs and connecting AI applications to external services.