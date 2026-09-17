# Day 5 — Type Hints + Pydantic

Type hints help us clearly define what type of data a variable, parameter, or function should use.

Pydantic is a Python library used to validate and structure data.

These concepts are especially useful when working with APIs, FastAPI, LLM applications, and Agentic AI systems.

## Topics Covered

1. Type Hints
2. Basic Type Hints
3. Type Hints in Functions
4. Lists and Dictionaries
5. Optional Values
6. Union Types
7. Type Aliases
8. Pydantic
9. Pydantic Models
10. Field Validation
11. Nested Models
12. Pydantic with FastAPI
13. Pydantic in Agentic AI
14. Type Hints vs Pydantic
15. Practical Usage

## 1. Type Hints

Type hints tell us what type of value is expected.

Example:

```text
name: str
age: int
price: float
is_active: bool
```

Type hints:

* Make code easier to understand.
* Improve code readability.
* Help development tools detect possible type mistakes.
* Describe what type of data is expected.

Important:

Type hints do not automatically prevent the wrong type from being assigned.

For example:

```text
age: int = "twenty"
```

Python may still run this, but a type checker can identify the problem.

## 2. Basic Type Hints

Common Python type hints are:

| Type    | Meaning        |
| ------- | -------------- |
| `str`   | String         |
| `int`   | Integer        |
| `float` | Decimal number |
| `bool`  | True or False  |

Basic syntax:

```text
variable: type = value
```

Example:

```text
name: str = "Shubham"
age: int = 25
rating: float = 4.5
is_logged_in: bool = True
```

## 3. Type Hints in Functions

Type hints can be used for:

* Function parameters
* Function return values

Example:

```text
def add(a: int, b: int) -> int:
    return a + b
```

Here:

* `a: int` → `a` is expected to be an integer.
* `b: int` → `b` is expected to be an integer.
* `-> int` → the function is expected to return an integer.

Another example:

```text
def greet(name: str) -> str:
    return f"Hello {name}"
```

## 4. Lists and Dictionaries

We can specify the types of values stored inside collections.

### List

```text
names: list[str]
```

This means the list contains strings.

Example:

```text
numbers: list[int] = [1, 2, 3, 4]
```

### Dictionary

```text
scores: dict[str, int]
```

This means:

* Keys are strings.
* Values are integers.

Example:

```text
scores: dict[str, int]
```

This is useful when working with structured data such as API responses and JSON data.

## 5. Optional Values

Sometimes a value may or may not exist.

We can use:

```text
str | None
```

Example:

```text
name: str | None = None
```

This means `name` can contain:

* A string
* `None`

Example:

```text
def find_user(user_id: int) -> str | None:
```

The function can return either a string or `None`.

This is useful when working with:

* Databases
* APIs
* Search results
* Optional user information

## 6. Union Types

A Union Type means a value can have more than one possible type.

Example:

```text
user_id: int | str
```

This means `user_id` can be either:

* `int`
* `str`

For example:

```text
user_id: int | str = 101

user_id = "user_101"
```

Both values are allowed by the type hint.

A simple way to understand it:

```text
int | str

   ↓

Either int OR str
```

## 7. Type Aliases

If we use the same complex type multiple times, we can give that type a name.

Example:

```text
UserData = dict[str, str]
```

Now we can use:

```text
user: UserData
```

Instead of repeatedly writing:

```text
dict[str, str]
```

Type aliases:

* Make complex types easier to understand.
* Make types reusable.
* Improve code readability.

## 8. Pydantic

Pydantic is a Python library used to:

* Validate data.
* Structure data.
* Create data models.

Install Pydantic using:

```text
pip install pydantic
```

Pydantic uses `BaseModel` to create structured models.

Basic structure:

```text
class User(BaseModel):
    name: str
    age: int
```

When data is provided to this model, Pydantic checks the data according to the model.

## 9. Pydantic Models

A Pydantic model defines the structure of data.

Example structure:

```text
User

├── name
├── age
└── email
```

The model tells us what fields are expected and what types they should have.

For example:

```text
name  → string
age   → integer
email → string
```

Pydantic models are useful when receiving data from:

* Users
* APIs
* Databases
* AI systems

## 10. Field Validation

Pydantic allows us to add validation rules to model fields.

For example:

```text
age: int = Field(gt=0)
```

`gt=0` means:

```text
age > 0
```

So an age of `25` is valid, while an age of `-5` fails validation.

### Important `Field()` Parameters

| Parameter     | Meaning               |
| ------------- | --------------------- |
| `gt`          | Greater than          |
| `ge`          | Greater than or equal |
| `lt`          | Less than             |
| `le`          | Less than or equal    |
| `min_length`  | Minimum string length |
| `max_length`  | Maximum string length |
| `min`         | Minimum value/items   |
| `max`         | Maximum value/items   |
| `description` | Describes the field   |
| `default`     | Default value         |

Examples:

```text
Field(gt=0)
Field(ge=18)
Field(lt=100)
Field(le=100)
Field(min_length=3)
Field(max_length=20)
```

Field validation is especially useful when we need to make sure incoming data follows specific rules.

## 11. Nested Models

One Pydantic model can contain another Pydantic model.

For example:

```text
User

├── name
└── address
      ├── city
      └── country
```

Here, `Address` is a model inside the `User` model.

Nested models are useful for complex data structures.

They are commonly used when API data contains objects inside other objects.

## 12. Pydantic with FastAPI

Pydantic is heavily used with FastAPI.

A Pydantic model can define the structure of an API request.

For example, an API may expect:

```text
Question

└── question: string
```

A client can send JSON such as:

```text
{
    "question": "What is RAG?"
}
```

FastAPI uses the Pydantic model to:

* Understand the expected request structure.
* Validate incoming data.
* Make API code easier to understand.

This is one of the most important practical uses of Pydantic.

## 13. Pydantic in Agentic AI

Pydantic is also useful when building AI agents.

Suppose an AI agent should return:

```text
answer
confidence
source
```

We can define this expected structure using a Pydantic model.

Conceptually:

```text
AgentResponse

├── answer
├── confidence
└── source
```

This gives the AI application a predictable output structure.

Pydantic can be useful for:

* LLM structured outputs
* Tool calling
* API requests and responses
* Agent state
* RAG responses
* FastAPI endpoints

## 14. Type Hints vs Pydantic

| Type Hints                        | Pydantic                         |
| --------------------------------- | -------------------------------- |
| Describe expected types           | Validate and structure data      |
| Mainly help developers and tools  | Used for runtime validation      |
| Improve code readability          | Checks incoming data             |
| Used with variables and functions | Used to create data models       |
| Example: `age: int`               | Example: `class User(BaseModel)` |

Simple way to remember:

```text
Type Hints
    ↓
Tell us what type of data we expect

Pydantic
    ↓
Checks and structures the actual data
```

## 15. Practical Usage in an AI Chatbot

Imagine an AI chatbot API receives:

```text
{
    "question": "Explain RAG",
    "user_id": 101
}
```

We can define the expected structure:

```text
ChatRequest

├── question: str
└── user_id: int
```

FastAPI can then use this model to validate the incoming request.

The flow is:

```text
Client
   ↓
JSON Request
   ↓
Pydantic Model
   ↓
Validation
   ↓
FastAPI Endpoint
   ↓
AI / Agent Logic
   ↓
Response
```

This pattern is very common in AI applications.

## Quick Revision

| Concept          | Meaning                        |
| ---------------- | ------------------------------ |
| Type Hint        | Specifies the expected type    |
| `str`            | String                         |
| `int`            | Integer                        |
| `float`          | Decimal number                 |
| `bool`           | True/False                     |
| `list[str]`      | List of strings                |
| `dict[str, int]` | String keys and integer values |
| `str \| None`    | String or None                 |
| Pydantic         | Data validation and structure  |
| `BaseModel`      | Base class for Pydantic models |
| `Field()`        | Adds validation rules          |
| Nested Model     | Model inside another model     |

## Practice

1. Create a `Product` Pydantic model with:

   * `name`
   * `price`
   * `quantity`

2. Add validation so `price` must be greater than `0`.

3. Create a `User` model with:

   * `name`
   * `age`
   * `email`

4. Create a nested `Address` model inside `User`.

5. Create an `AgentResponse` model with:

   * `answer`
   * `confidence`
   * `source`

## Day 5 Goal

Understand how Python can work with **typed, structured, and validated data**, especially for APIs, FastAPI, and Agentic AI systems.