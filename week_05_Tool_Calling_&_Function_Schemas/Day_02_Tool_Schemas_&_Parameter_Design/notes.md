# Week 05 — Day 02: Tool Schemas & Parameter Design

## Points Covered

* What is a Tool Schema?
* Why Tool Schemas are Important
* Tool Name
* Tool Description
* Parameters
* Parameter Types
* Required vs Optional Parameters
* Parameter Descriptions
* Object Parameters
* Enum Parameters
* Default Values
* Nested Parameters
* Designing Good Tool Schemas
* Tool Schema Example
* Tool Schema with Python
* Tool Schema Validation
---

# 1. What is a Tool Schema?

A **tool schema** is a structured description of a tool that tells the LLM:

* What the tool is called
* What the tool does
* What inputs it accepts
* What type of inputs it expects
* Which inputs are required
* Which inputs are optional

Example:

```text
Tool:
search_courses

Description:
Search courses based on technology and level.

Parameters:
technology → string
level → string
```

The schema acts like a **contract between the LLM and your application**.

```text
Tool Schema
     ↓
LLM understands the tool
     ↓
LLM generates arguments
     ↓
Application validates arguments
     ↓
Tool executes
```

---

# 2. Why are Tool Schemas Important?

An LLM cannot automatically understand every function in your application.

Suppose your Python application has:

```python
def search_courses(technology, level):
    ...
```

The LLM needs to know:

```text
What does search_courses do?

What is technology?

What is level?

What type should they be?

Are they required?
```

The schema provides this information.

A good schema helps with:

* Tool selection
* Argument generation
* Input validation
* Consistent tool usage
* Maintainability

---

# 3. Tool Schema as a Contract

Think of a schema as an **API contract**.

For example:

```text
search_courses(
    technology: string,
    level: string
)
```

This means:

```text
The tool expects:

technology → string
level      → string
```

The LLM should generate arguments that follow this structure.

```text
LLM
 ↓
Tool Arguments
 ↓
Schema
 ↓
Application
```

However, the schema is **not a security boundary by itself**.

Your backend must still validate and authorize the request.

---

# 4. Main Parts of a Tool Schema

A typical tool schema contains:

```text
Tool
│
├── Name
├── Description
└── Parameters
     │
     ├── Type
     ├── Properties
     ├── Description
     └── Required
```

Example:

```json
{
    "name": "get_course",
    "description": "Get course details by course ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "course_id": {
                "type": "integer",
                "description": "Unique ID of the course."
            }
        },
        "required": ["course_id"]
    }
}
```

---

# 5. Tool Name

The tool name identifies the tool.

Example:

```text
get_course
```

Other examples:

```text
search_courses
get_course_price
get_weather
create_support_ticket
calculate_total
```

Use clear and meaningful names.

### Good

```text
search_courses
```

### Bad

```text
do_task
```

A tool name should communicate its purpose.

---

# 6. Tool Description

The description tells the LLM what the tool does.

Example:

```text
Search available courses based on technology,
learning level, and goal.
```

A good description should answer:

```text
What does this tool do?
When should it be used?
What kind of result does it provide?
```

Clear descriptions help the model decide when a tool should be used.

---

# 7. Parameters

Parameters are the inputs that a tool needs.

Example:

```text
get_course(course_id)
```

Here:

```text
course_id
```

is a parameter.

Another example:

```text
search_courses(
    technology,
    level,
    max_duration
)
```

Parameters:

```text
technology
level
max_duration
```

---

# 8. Parameter Types

Every parameter should have an appropriate type.

Common types include:

```text
string
integer
number
boolean
array
object
```

Example:

```text
course_id → integer
course_name → string
price → number
is_active → boolean
topics → array
filters → object
```

Example schema:

```json
{
    "course_id": {
        "type": "integer"
    }
}
```

The type tells the LLM what kind of value should be generated.

---

# 9. String Parameters

A string represents text.

Example:

```text
technology → string
```

Tool:

```text
search_courses(
    technology="Python"
)
```

Schema:

```json
{
    "technology": {
        "type": "string"
    }
}
```

---

# 10. Integer Parameters

An integer represents a whole number.

Example:

```text
course_id → integer
```

Valid:

```json
{
    "course_id": 10
}
```

If the schema specifically expects an integer, this is different from:

```json
{
    "course_id": "10"
}
```

---

# 11. Number Parameters

A number can represent values such as prices or measurements.

Example:

```text
price → number
```

Tool:

```text
calculate_discount(
    price=5000,
    discount=10
)
```

Possible schema:

```json
{
    "price": {
        "type": "number"
    },
    "discount": {
        "type": "number"
    }
}
```

---

# 12. Boolean Parameters

A boolean represents:

```text
true
false
```

Example:

```text
get_courses(
    include_inactive=false
)
```

Schema:

```json
{
    "include_inactive": {
        "type": "boolean"
    }
}
```

---

# 13. Array Parameters

An array contains multiple values.

Example:

```text
topics → array
```

A tool could accept:

```json
{
    "topics": [
        "Python",
        "FastAPI",
        "PostgreSQL"
    ]
}
```

Arrays are useful when a tool needs multiple values.

---

# 14. Object Parameters

An object contains multiple related fields.

For example:

```text
user_preferences
```

could contain:

```json
{
    "level": "beginner",
    "technology": "Python",
    "goal": "backend development"
}
```

Conceptually:

```text
user_preferences
 ├── level
 ├── technology
 └── goal
```

Objects are useful for grouping related information.

---

# 15. Required Parameters

A required parameter must be provided.

Example:

```text
get_course(course_id)
```

The tool cannot work without `course_id`.

Therefore:

```text
required:
course_id
```

Schema:

```json
{
    "required": ["course_id"]
}
```

---

# 16. Optional Parameters

An optional parameter is not always required.

Example:

```text
search_courses(
    technology,
    level=None
)
```

The user might say:

```text
"Find Python courses."
```

Here:

```text
technology = Python
level = not provided
```

The tool can still execute if `level` is optional.

---

# 17. Required vs Optional

Example:

```text
search_courses(
    technology,
    level,
    max_duration
)
```

Suppose:

```text
technology → required
level → optional
max_duration → optional
```

Then this can be valid:

```json
{
    "technology": "Python"
}
```

But:

```json
{}
```

would not be valid if `technology` is required.

---

# 18. Parameter Descriptions

Parameter descriptions are important.

Instead of:

```json
{
    "course_id": {
        "type": "integer"
    }
}
```

Prefer:

```json
{
    "course_id": {
        "type": "integer",
        "description": "Unique ID of the course."
    }
}
```

The description gives the LLM more context.

Another example:

```json
{
    "level": {
        "type": "string",
        "description": "Learner level such as beginner, intermediate, or advanced."
    }
}
```

Good descriptions reduce ambiguity.

---

# 19. Enum Parameters

Sometimes a parameter should accept only specific values.

For example:

```text
level:
beginner
intermediate
advanced
```

This can be represented using an enum.

```json
{
    "level": {
        "type": "string",
        "enum": [
            "beginner",
            "intermediate",
            "advanced"
        ]
    }
}
```

This is useful for:

* User roles
* Status values
* Categories
* Difficulty levels
* Sorting options

---

# 20. Why Use Enums?

Without an enum, the model might generate:

```text
beginner
```

or:

```text
basic
```

or:

```text
entry-level
```

If your backend expects only:

```text
beginner
intermediate
advanced
```

an enum communicates the allowed values.

```text
Allowed Values
      ↓
LLM
      ↓
More Predictable Arguments
```

The backend should still validate the actual value.

---

# 21. Default Values

Optional parameters can have default values.

Example:

```text
search_courses(
    technology,
    level="beginner"
)
```

If the user does not provide `level`, the application can use:

```text
beginner
```

Conceptually:

```text
level
default = beginner
```

Defaults should be used carefully.

They should represent sensible application behavior rather than silently changing user intent.

---

# 22. Nested Parameters

Some tools need more complex input.

Example:

```text
search_courses(
    filters
)
```

Where:

```text
filters:
    technology
    level
    duration
```

Conceptually:

```json
{
    "filters": {
        "technology": "Python",
        "level": "beginner",
        "duration": 30
    }
}
```

Nested objects are useful when several related parameters belong together.

---

# 23. Complete Tool Schema Example

Suppose we create:

```text
search_courses
```

The tool searches courses based on:

```text
technology
level
max_duration
```

A conceptual schema:

```json
{
    "name": "search_courses",
    "description": "Search courses based on technology, learner level, and maximum duration.",
    "parameters": {
        "type": "object",
        "properties": {
            "technology": {
                "type": "string",
                "description": "Technology the learner wants to study."
            },
            "level": {
                "type": "string",
                "enum": [
                    "beginner",
                    "intermediate",
                    "advanced"
                ],
                "description": "Learner's current experience level."
            },
            "max_duration": {
                "type": "integer",
                "description": "Maximum course duration in hours."
            }
        },
        "required": ["technology"]
    }
}
```

Here:

```text
technology
→ required

level
→ optional

max_duration
→ optional
```

---

# 24. Schema and Python Function

Suppose the actual Python function is:

```python
def search_courses(
    technology: str,
    level: str | None = None,
    max_duration: int | None = None
):
    ...
```

The schema should represent the same contract.

```text
Python Function
       ↕
Tool Schema
```

The two should not contradict each other.

For example, if Python expects:

```python
course_id: int
```

the schema should also describe it as an integer.

---

# 25. Tool Schema Validation

There are two important validation layers.

## Layer 1: Schema Guidance

The schema tells the LLM what arguments are expected.

```text
LLM
 ↓
Schema
 ↓
Tool Arguments
```

## Layer 2: Application Validation

Your backend validates the actual tool call before execution.

```text
Tool Arguments
 ↓
Backend Validation
 ↓
Execute
```

This is important because LLM output is not automatically trustworthy.

---

# 26. Example of Validation

Suppose:

```python
def get_course(course_id: int):
    ...
```

The model requests:

```json
{
    "course_id": "abc"
}
```

Your application should reject the invalid value.

Better flow:

```text
LLM
 ↓
Tool Call
 ↓
Validate course_id
 ↓
Invalid
 ↓
Return Error
```

The tool should not blindly execute invalid input.

---

# 27. Designing Good Tool Schemas

Follow these principles.

### 1. Use clear names

```text
search_courses
```

instead of:

```text
search
```

### 2. Write useful descriptions

Explain what the tool does and when it should be used.

### 3. Use correct parameter types

```text
course_id → integer
```

not:

```text
course_id → string
```

unless the application actually expects a string.

### 4. Keep parameters minimal

Only request information the tool actually needs.

### 5. Use enums when values are limited

```text
beginner
intermediate
advanced
```

### 6. Clearly mark required fields

Do not make every parameter required unnecessarily.

---

# 28. Bad vs Good Tool Schema

## Bad

```text
Name:
search

Description:
Search stuff.

Parameters:
data
```

The LLM has very little information.

## Good

```text
Name:
search_courses

Description:
Search available courses based on technology,
learner level, and maximum duration.

Parameters:
technology → string → required
level → enum → optional
max_duration → integer → optional
```

The second schema provides much clearer guidance.

---

# 29. Tool Schema and Tool Selection

Good schemas help the LLM distinguish between tools.

Suppose we have:

```text
search_courses
get_course
get_course_price
```

Descriptions:

```text
search_courses
→ Find courses matching user requirements.

get_course
→ Get details of a specific course.

get_course_price
→ Get the price of a specific course.
```

User:

```text
"Find beginner Python courses."
```

The model can identify:

```text
search_courses
```

User:

```text
"How much does course 10 cost?"
```

The model can identify:

```text
get_course_price
```

Clear schemas make the available capabilities easier for the model to distinguish.

---

# 30. Common Mistakes

## Mistake 1: Vague tool names

Avoid:

```text
do_task
```

Prefer:

```text
search_courses
```

## Mistake 2: Vague descriptions

Avoid:

```text
Get data.
```

Prefer:

```text
Get course details using the unique course ID.
```

## Mistake 3: Too many parameters

Do not add parameters that the tool does not need.

Bad:

```text
get_course(
    course_id,
    user_name,
    email,
    age,
    location
)
```

if the tool only needs:

```text
course_id
```

## Mistake 4: Incorrect parameter types

If the backend expects:

```text
course_id → integer
```

the schema should communicate that.

## Mistake 5: Making everything required

Only required inputs should be required.

## Mistake 6: Relying only on the schema for security

A schema helps guide tool calls, but it does not replace:

* Backend validation
* Authentication
* Authorization
* Business rules

---