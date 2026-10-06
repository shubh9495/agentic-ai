# Week 05 — Day 01: Tool Calling Fundamentals

## Points Covered

* What is Tool Calling?
* Why LLMs Need Tools
* LLM vs Tool vs Application
* Function Calling vs Tool Calling
* What is a Tool?
* Tool Definition
* Tool Schema
* Tool Name
* Tool Description
* Tool Parameters
* Parameter Types
* Required Parameters
* How an LLM Chooses a Tool
* Tool Call Lifecycle
* Tool Execution
* Tool Result
* Multiple Tools
* Tool Calling vs Normal LLM Response
* Basic Tool Calling Architecture
* Tool Registry
* Tool Calling and Security
* Tool Calling and Validation
* Tool Calling and Agents

---

# 1. What is Tool Calling?

**Tool calling** allows an LLM to request an external capability from an application.

The tool can perform an action or retrieve information that the LLM cannot reliably do by itself.

Example:

```text
User:
"What is the weather in Dehradun?"

        ↓

LLM
        ↓
Tool Call
        ↓
Application
        ↓
get_weather("Dehradun")
        ↓
Tool Result
        ↓
LLM
        ↓
Final Answer
```

The important idea is:

```text
LLM requests
Application executes
```

---

# 2. Why Do LLMs Need Tools?

An LLM is good at understanding and generating language, but an application may need to interact with external systems.

Examples:

```text
LLM alone
→ Explain Python

Tool
→ Query PostgreSQL

Tool
→ Call Weather API

Tool
→ Search Courses

Tool
→ Calculate Price

Tool
→ Send Email
```

Tools connect the LLM to the outside world.

```text
LLM
 ↓
Tools
 ↓
External Systems
```

---

# 3. LLM vs Tool vs Application

These three responsibilities should be clear.

## LLM

The LLM understands the user's request and can decide whether a tool is needed.

## Tool

A tool represents a capability that the application makes available to the LLM.

## Application

The application actually executes the tool.

Example:

```text
User:
"What is course 10's price?"

        ↓

LLM:
"I need course price information."

        ↓

Tool Call:
get_course_price(course_id=10)

        ↓

Application:
Executes the function.

        ↓

Database:
Returns ₹4,999.

        ↓

LLM:
Generates final response.
```

Remember:

```text
LLM → Decides
Application → Executes
```

---

# 4. Function Calling vs Tool Calling

You learned basic function calling in Week 04.

The concepts are closely related.

## Function Calling

The model requests a specific function.

```text
get_course(course_id=10)
```

## Tool Calling

A broader concept where the model requests an available tool.

```text
search_courses()
get_course()
get_weather()
calculate_price()
```

Modern LLM APIs commonly use **tool calling** as the broader terminology.

For this week:

```text
Tool
 ↓
Name
Description
Parameters
 ↓
LLM
```

---

# 5. What is a Tool?

A **tool** is an external capability exposed to an LLM.

A tool can be backed by:

* Python function
* Database operation
* External API
* Search system
* Business logic
* Another service

Example:

```python
def get_course(course_id: int):
    ...
```

The function itself is application code.

The tool definition tells the LLM how it can request that capability.

```text
Python Function
      ↓
Tool Definition
      ↓
LLM
```

---

# 6. Tool Definition

A tool definition generally contains:

```text
Tool Name
Tool Description
Input Parameters
Parameter Types
Required Parameters
```

Example:

```text
Name:
get_course

Description:
Get course information using a course ID.

Parameters:
course_id → integer

Required:
course_id
```

The model uses this information to understand when and how to use the tool.

---

# 7. Tool Name

The tool name identifies the capability.

Example:

```text
get_course
```

Other examples:

```text
search_courses
get_weather
calculate_total
get_user
create_ticket
```

Use clear names.

Good:

```text
search_courses
```

Bad:

```text
do_task
```

The name should communicate what the tool does.

---

# 8. Tool Description

The description tells the LLM what the tool is used for.

Example:

```text
Search available courses using the user's
technology and experience level.
```

A good description helps the model decide when to use the tool.

Compare:

```text
search_courses
```

with:

```text
Search available courses based on technology,
level, and learning goal.
```

The second provides much more useful information.

---

# 9. Tool Parameters

Parameters are the inputs required by the tool.

Example:

```text
search_courses(
    technology,
    level
)
```

Parameters:

```text
technology → string
level → string
```

Example tool call:

```json
{
    "technology": "Python",
    "level": "beginner"
}
```

The parameters provide the information required for execution.

---

# 10. Parameter Types

Tool parameters should have clear types.

For example:

```text
course_id → integer
course_name → string
price → number
is_active → boolean
```

Example:

```text
get_course(course_id: integer)
```

The LLM should know that:

```text
course_id = 10
```

is valid, while:

```text
course_id = "abc"
```

is not the expected type.

The application should still validate the actual arguments before execution.

---

# 11. Required Parameters

Some parameters are necessary for a tool to work.

Example:

```text
get_course(course_id)
```

`course_id` is required.

A search tool might have:

```text
technology → required
level → optional
```

Conceptually:

```text
search_courses(
    technology: string,
    level: string = optional
)
```

Required parameters help define what the tool needs before execution.

---

# 12. Tool Schema

A **tool schema** describes the tool in a machine-readable format.

A simplified schema can look like:

```json
{
    "name": "get_course",
    "description": "Get course information by course ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "course_id": {
                "type": "integer",
                "description": "The unique ID of the course."
            }
        },
        "required": ["course_id"]
    }
}
```

The exact schema format depends on the LLM provider.

The important concept is:

```text
Tool Schema
    ↓
Describes what the tool does
    ↓
Describes what input it needs
```

---

# 13. Why is the Schema Important?

The model cannot automatically know how every application function works.

Suppose your application has:

```python
def search_courses(
    technology: str,
    level: str
):
    ...
```

The LLM needs to know:

```text
Tool:
search_courses

Purpose:
Search courses.

Input:
technology → string
level → string
```

The schema provides this information.

Therefore:

```text
Good Schema
     ↓
Better Tool Understanding
     ↓
Better Tool Selection
     ↓
Better Tool Arguments
```

A schema does not guarantee that the model will always make the correct choice, so application-side validation is still required.

---

# 14. How Does the LLM Choose a Tool?

Suppose the application provides three tools:

```text
get_course()
search_courses()
get_weather()
```

User:

```text
"Find beginner Python courses."
```

The LLM analyzes the request.

```text
User Request
     ↓
Available Tools
     ↓
Choose Relevant Tool
     ↓
search_courses()
```

It may generate:

```json
{
    "technology": "Python",
    "level": "beginner"
}
```

The application then executes the tool.

---

# 15. Tool Call Lifecycle

The complete lifecycle is:

```text
1. User sends request
        ↓
2. Application sends request + tool definitions to LLM
        ↓
3. LLM decides whether a tool is needed
        ↓
4. LLM generates tool call
        ↓
5. Application receives tool call
        ↓
6. Application validates arguments
        ↓
7. Application executes tool
        ↓
8. Tool returns result
        ↓
9. Result is sent back to LLM
        ↓
10. LLM generates final response
```

This lifecycle is one of the most important concepts in tool calling.

---

# 16. Normal LLM Response vs Tool Call

## Normal Response

```text
User
 ↓
LLM
 ↓
Text
 ↓
User
```

Example:

```text
User:
"What is FastAPI?"

LLM:
"FastAPI is a Python framework..."
```

## Tool Call

```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Application
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Final Response
```

Example:

```text
User:
"What is the price of course 10?"

LLM
 ↓
get_course_price(10)
 ↓
Database
 ↓
₹4,999
 ↓
LLM
 ↓
"Course 10 costs ₹4,999."
```

---

# 17. Tool Execution

The LLM does not normally execute your Python code directly.

Suppose the model generates:

```text
get_course(course_id=10)
```

Your application receives the tool call and maps it to the actual function:

```python
result = get_course(10)
```

Then:

```text
Tool Call
    ↓
Python Function
    ↓
Database/API
    ↓
Result
```

The application remains responsible for execution.

---

# 18. Tool Result

After execution, the tool returns data.

For example:

```json
{
    "id": 10,
    "name": "FastAPI",
    "level": "Beginner",
    "duration": 30
}
```

This result is sent back to the LLM.

The LLM can then turn the raw data into a natural-language response:

```text
"Course 10 is FastAPI. It is a beginner-level
course with a duration of 30 hours."
```

So:

```text
Tool Result
    ↓
LLM
    ↓
User-Friendly Response
```

---

# 19. Multiple Tools

An application can expose multiple tools.

Example:

```text
search_courses()
get_course()
get_course_price()
get_weather()
```

The LLM can choose the appropriate tool based on the user's request.

Examples:

```text
"Find beginner Python courses."
        ↓
search_courses()
```

```text
"Tell me about course 10."
        ↓
get_course()
```

```text
"What is the price of course 10?"
        ↓
get_course_price()
```

This is the foundation for more advanced agent behavior.

---

# 20. Tool Calling Example

Suppose we have:

```python
def get_course(course_id: int):
    return {
        "id": course_id,
        "name": "FastAPI",
        "level": "Beginner"
    }
```

The corresponding tool information could conceptually be:

```json
{
    "name": "get_course",
    "description": "Get course details using a course ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "course_id": {
                "type": "integer"
            }
        },
        "required": ["course_id"]
    }
}
```

User:

```text
"Tell me about course 10."
```

Model requests:

```text
get_course(course_id=10)
```

Application executes:

```python
result = get_course(10)
```

Result:

```json
{
    "id": 10,
    "name": "FastAPI",
    "level": "Beginner"
}
```

Then the model generates the final response.

---

# 21. Tool Calling with FastAPI

A typical architecture can look like:

```text
Frontend
   ↓
FastAPI
   ↓
LLM Service
   ↓
LLM
   ↓
Tool Call
   ↓
Tool Executor
   ↓
Database / External API
   ↓
Tool Result
   ↓
LLM
   ↓
FastAPI
   ↓
Frontend
```

The route should not contain all tool implementation logic.

A better structure is:

```text
routes/
    ↓
services/
    ↓
tools/
```

Example:

```text
app/
├── routes/
│   └── chat.py
│
├── services/
│   └── llm_service.py
│
└── tools/
    ├── course_tools.py
    └── weather_tools.py
```

---

# 22. Tool Registry

As the number of tools grows, you can keep them organized in a central registry.

Conceptually:

```python
tools = [
    get_course,
    search_courses,
    get_course_price
]
```

The LLM receives the definitions of the available tools.

The application can maintain a mapping:

```text
Tool Name
    ↓
Python Function
```

For example:

```text
"get_course"
      ↓
get_course()

"search_courses"
      ↓
search_courses()
```

This becomes useful when building larger agent systems.

---

# 23. Tool Calling and Security

Tool calling introduces an important security consideration.

The LLM can request tools, but not every tool should be freely executable.

For example:

```text
get_course()
```

may be low risk.

But:

```text
delete_user()
send_payment()
send_email()
```

can have real-world consequences.

Therefore:

```text
LLM Tool Request
       ↓
Validate
       ↓
Check Permissions
       ↓
Execute
```

Never treat an LLM-generated tool call as automatically trusted.

---

# 24. Tool Calling and Validation

Tool arguments should be validated before execution.

For example:

```python
def get_course(course_id: int):
    ...
```

If the model provides:

```text
course_id = "hello"
```

the application should reject or correct the input rather than blindly executing it.

A safer flow is:

```text
LLM
 ↓
Tool Call
 ↓
Validate Arguments
 ↓
Permission Check
 ↓
Execute Tool
 ↓
Result
```

---

# 25. Tool Calling and Agents

Tool calling is an important building block for agents.

A simple tool call:

```text
User
 ↓
LLM
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Answer
```

An agent can go further:

```text
User
 ↓
LLM
 ↓
Tool A
 ↓
Result
 ↓
LLM
 ↓
Tool B
 ↓
Result
 ↓
LLM
 ↓
Final Answer
```

The repeated decision process is called an **agent loop**.

You will study agent loops in **Week 06**.

---