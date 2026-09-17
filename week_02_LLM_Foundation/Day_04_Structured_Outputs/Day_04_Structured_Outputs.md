# Day 4: Structured Outputs

Structured output means asking an LLM to return data in a predefined format instead of normal free-form text.

## 1. Structured Output

Example:

```json
{
    "name": "Rahul",
    "experience": 2,
    "skills": ["Python", "FastAPI"]
}
```

This makes LLM responses easier for programs to process.

## 2. Free-Form vs Structured Output

Free-form:

* Human-friendly
* Flexible
* Harder to parse
* Can vary between responses

Structured:

* Machine-friendly
* Predictable
* Easier to parse
* Follows a defined structure

## 3. JSON

JSON is commonly used for structured data.

It contains:

* Objects
* Key-value pairs
* Lists
* Strings
* Numbers
* Booleans

Example:

```json
{
    "name": "Shubham",
    "age": 25,
    "skills": ["Python", "Java"]
}
```

## 4. JSON Schema

JSON Schema defines what the expected JSON structure should look like.

Example:

```text
Person
├── name → string
├── age → integer
└── skills → list of strings
```

## 5. Pydantic

Pydantic is used to define and validate structured data in Python.

```python
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    skills: list[str]
```

## 6. Validation

Pydantic checks whether data matches the expected structure.

```text
LLM Response
     ↓
Pydantic
     ↓
Validation
     ↓
Application
```

If the data is invalid, Pydantic raises a validation error.

## 7. Required Fields

Fields without default values are required.

```python
class Job(BaseModel):
    title: str
    company: str
    experience: int
```

All three fields are required.

## 8. Optional Fields

A field can be optional by providing a default value.

```python
class Job(BaseModel):
    title: str
    company: str
    salary: float | None = None
```

If salary is not provided, its value is `None`.

## 9. Nested Models

Pydantic supports nested structures.

```python
class Experience(BaseModel):
    years: int
    role: str


class Candidate(BaseModel):
    name: str
    experience: Experience
    skills: list[str]
```

One model can contain another model.

## 10. Lists of Objects

A model can also contain a list of other models.

```python
class Job(BaseModel):
    title: str
    company: str


class JobList(BaseModel):
    jobs: list[Job]
```

## 11. Parsing Structured Data

LLM/API responses can be converted into Python data.

```python
person = Person(**response)
```

Now the application can access:

```python
person.name
person.age
```

## 12. JSON Mode vs Structured Output

JSON mode focuses on getting JSON.

Structured output focuses on getting data that follows a defined structure or schema.

The exact guarantees depend on the model and API.

## 13. Validation vs Generation

Pydantic does not generate the LLM response.

The LLM generates the data.

Pydantic checks the generated data.

```text
LLM
 ↓
Generate Data
 ↓
Pydantic
 ↓
Validate
```

## 14. Structured Output Does Not Mean Correct Information

Valid structure does not guarantee correct information.

```text
Valid Structure
≠
Factually Correct Information
```

For factual correctness, applications may need:

* Retrieval
* Tools
* External data
* Validation
* Human review

## 15. Structured Output in Tool Calling

Agents can use structured data as tool arguments.

Example:

```json
{
    "instance_type": "t3.micro",
    "region": "us-east-1",
    "count": 1
}
```

Flow:

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Structured Tool Arguments
 ↓
Validation
 ↓
Tool
 ↓
Result
```

## 16. Structured Output in RAG

RAG applications can return structured information such as:

```json
{
    "answer": "The refund period is 30 days.",
    "sources": ["refund_policy.pdf"],
    "confidence": "high"
}
```

The application can process each field separately.

## 17. Structured Output in FastAPI

FastAPI uses Pydantic for defined request and response structures.

```python
class Question(BaseModel):
    question: str


class Answer(BaseModel):
    answer: str
    sources: list[str]
```

This gives APIs predictable input and output.

## 18. Structured Output in Agentic AI

A common agent flow is:

```text
User
 ↓
LLM
 ↓
Decision
 ↓
Structured Tool Arguments
 ↓
Validation
 ↓
Tool
 ↓
Tool Result
 ↓
LLM
 ↓
Structured Final Response
```

## Key Concepts

* **Structured Output** → LLM response following a defined structure
* **JSON** → Common format for structured data
* **JSON Schema** → Defines expected JSON structure
* **Pydantic** → Defines and validates Python data
* **Validation** → Checks whether data matches the expected structure
* **Nested Model** → A model containing another model
* **Optional Field** → Field that can be missing or `None`
* **Structured Tool Arguments** → Structured data passed from an LLM to a tool