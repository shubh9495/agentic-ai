# Day 7 — Mini Project + Revision

Day 7 is about applying the concepts learned during Days 1–6.

The goal is not to learn many new concepts, but to combine Python fundamentals, OOP, type hints, Pydantic, JSON, APIs, and error handling into one small project.

## Topics Covered

1. **Project Structure** — Organizing a Python project
2. **Revision** — Reviewing Days 1–6
3. **Project Planning** — Breaking a project into smaller parts
4. **OOP in Project** — Using classes and objects
5. **Type Hints** — Adding type information
6. **Pydantic Models** — Validating input data
7. **JSON** — Working with structured data
8. **API Requests** — Communicating with an API
9. **Error Handling** — Handling API and application errors
10. **Testing** — Checking whether the project works correctly
11. **Code Cleanup** — Improving readability and structure
12. **Agentic AI Connection** — Understanding how these concepts are used in AI applications

## 1. Project

Build a simple **AI Question Client**.

The project will take a question from the user, send it to an API, and display the response.

Basic flow:

```text
User
 ↓
Enter Question
 ↓
Pydantic Validation
 ↓
API Request
 ↓
Process Response
 ↓
Display Answer
```

## 2. Project Structure

A simple project can look like:

```text
day7_project/
│
├── main.py
├── models.py
├── api.py
└── README.md
```

### `models.py`

Contains Pydantic models.

### `api.py`

Contains API-related functions.

### `main.py`

Contains the main application logic.

## 3. Create the Pydantic Model

```python id="q7zj4x"
from pydantic import BaseModel


class Question(BaseModel):
    question: str
```

This defines the structure of the user's input.

Example:

```python id="xqk4j1"
data = Question(
    question="What is RAG?"
)

print(data.question)
```

## 4. Create an API Function

```python id="4z5j2p"
import requests


def call_api(question: str) -> dict:

    response = requests.post(
        "https://api.example.com/ask",
        json={
            "question": question
        }
    )

    response.raise_for_status()

    return response.json()
```

The function:

1. Accepts a question.
2. Sends it to an API.
3. Checks for an error.
4. Returns the JSON response.

## 5. Add Error Handling

API calls can fail.

```python id="g3z8wp"
import requests


def call_api(question: str) -> dict:

    try:

        response = requests.post(
            "https://api.example.com/ask",
            json={
                "question": question
            }
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:
        print("API request failed")
        return {}
```

Now an API failure will not immediately crash the application.

## 6. Use OOP

We can organize the API logic using a class.

```python id="7m1v4c"
import requests


class AIClient:

    def __init__(self, api_url: str):
        self.api_url = api_url

    def ask(self, question: str) -> dict:

        response = requests.post(
            self.api_url,
            json={
                "question": question
            }
        )

        response.raise_for_status()

        return response.json()
```

Create an object:

```python id="s4x9kp"
client = AIClient(
    "https://api.example.com/ask"
)

result = client.ask("What is RAG?")

print(result)
```

Here we are using:

```text
Class
Object
__init__()
self
Method
Type Hints
API
JSON
```

## 7. Complete Basic Example

```python id="f1w9zk"
import requests

from pydantic import BaseModel


class Question(BaseModel):
    question: str


class AIClient:

    def __init__(self, api_url: str):
        self.api_url = api_url

    def ask(self, question: str) -> dict:

        response = requests.post(
            self.api_url,
            json={
                "question": question
            }
        )

        response.raise_for_status()

        return response.json()


def main():

    user_input = input("Ask a question: ")

    question = Question(
        question=user_input
    )

    client = AIClient(
        "https://api.example.com/ask"
    )

    try:

        result = client.ask(
            question.question
        )

        print(result)

    except requests.RequestException:
        print("Something went wrong while calling the API.")


if __name__ == "__main__":
    main()
```

The URL above is only an example. Replace it with a real API endpoint when building the project.

## Week 1 Final Goal

After completing Days 1–7, you should be able to:

* Write basic Python programs.
* Work with collections and loops.
* Create reusable functions.
* Understand decorators.
* Build classes and objects.
* Use inheritance and composition.
* Add type hints.
* Create Pydantic models.
* Validate data.
* Read and create JSON.
* Call APIs from Python.
* Handle common errors.
* Organize a small Python project.

The next step is to move from Python fundamentals toward **LLM APIs, structured outputs, tool calling, and Agentic AI development**.
