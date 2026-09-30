# Week 04 — Day 03: Prompt Templates & Dynamic Prompts

## Points Covered

* What is a Prompt Template?
* Static vs Dynamic Prompts
* Why Prompt Templates are Needed
* Variables in Prompts
* Dynamic Prompt Construction
* System and User Prompt Templates
* Multiple Variables
* Reusable Prompts
* Prompt Templates with LLM APIs
* Prompt Templates with FastAPI
* Separating Prompts from Application Logic
* Prompt Templates with Context
* Prompt Templates and RAG
* Prompt Templates and Conversation History
* Prompt Template vs Hardcoded Prompt
* Prompt Template vs Prompt Engineering
* Dynamic Prompt Example
* Common Mistakes
* Interview Questions

---

# 1. What is a Prompt Template?

A **prompt template** is a reusable prompt containing placeholders for values that can change.

Example:

```text
You are a helpful {role}.

Explain {topic} in simple English.
```

Here:

```text
{role}  → variable
{topic} → variable
```

If:

```text
role = Python tutor
topic = FastAPI
```

The final prompt becomes:

```text
You are a helpful Python tutor.

Explain FastAPI in simple English.
```

---

# 2. Static vs Dynamic Prompts

## Static Prompt

A static prompt does not change.

```text
You are a helpful Python tutor.

Explain concepts using simple English.
```

Every request receives the same instructions.

## Dynamic Prompt

A dynamic prompt contains values that change based on the user's request.

```text
You are a helpful {role}.

Explain {topic} in simple English.
```

For example:

```text
role = Java tutor
topic = Spring Boot
```

The generated prompt becomes:

```text
You are a helpful Java tutor.

Explain Spring Boot in simple English.
```

---

# 3. Why Use Prompt Templates?

Prompt templates make LLM applications:

* Reusable
* Easier to maintain
* Easier to modify
* More consistent
* Easier to test

Without templates, prompts may be repeated throughout the application.

With a template:

```text
One Template
     ↓
Different Inputs
     ↓
Different Prompts
```

---

# 4. Variables in Prompts

A variable represents information that will be inserted into the prompt.

Example:

```text
Explain {topic} for a {level} learner.
```

Variables:

```text
topic
level
```

Input:

```text
topic = FastAPI
level = beginner
```

Final prompt:

```text
Explain FastAPI for a beginner learner.
```

---

# 5. Creating a Simple Prompt Template

In Python, an f-string can be used to create a simple dynamic prompt.

```python
topic = "FastAPI"
level = "beginner"

prompt = f"""
Explain {topic} for a {level} learner.

Use simple English.
"""
```

The final prompt becomes:

```text
Explain FastAPI for a beginner learner.

Use simple English.
```

This is a basic form of dynamic prompting.

---

# 6. Multiple Variables

A prompt can contain multiple variables.

```python
name = "Shubham"
skill = "Python"
experience = "beginner"

prompt = f"""
Create a learning recommendation for {name}.

Skill:
{skill}

Experience:
{experience}
"""
```

The final prompt contains the actual values:

```text
Create a learning recommendation for Shubham.

Skill:
Python

Experience:
beginner
```

---

# 7. Dynamic Prompts in an LLM Application

Consider an AI course recommendation application.

The user provides:

```text
Goal:
Learn backend development

Experience:
Beginner

Preferred language:
Python
```

The application can create:

```text
You are an AI course advisor.

User goal:
Learn backend development

Experience:
Beginner

Preferred language:
Python

Recommend a suitable learning path.
```

The flow is:

```text
User Input
    ↓
Application Data
    ↓
Prompt Template
    ↓
Final Prompt
    ↓
LLM
    ↓
Response
```

---

# 8. System Prompt Template

A system prompt can also contain variables.

Example:

```text
You are a {role}.

Your answers should be:

- {style}
- {language}
- {detail_level}
```

Example values:

```text
role = Python tutor
style = beginner-friendly
language = English
detail_level = concise
```

Final system prompt:

```text
You are a Python tutor.

Your answers should be:

- beginner-friendly
- English
- concise
```

---

# 9. User Prompt Template

The user's message can also be combined with application data.

Example:

```text
User question:

{question}

Relevant course:

{course}

Answer the question using the course information.
```

If:

```text
question = "What is FastAPI?"
course = "Backend Development with Python"
```

The final prompt becomes:

```text
User question:

What is FastAPI?

Relevant course:

Backend Development with Python

Answer the question using the course information.
```

---

# 10. System Prompt + User Prompt

An LLM application can use both system and user prompts.

Example:

```text
System:

You are an AI course advisor.
Give beginner-friendly recommendations.

User:

I want to learn backend development.

My experience is beginner level.
```

The application can dynamically generate both messages.

Conceptually:

```text
System Template
       +
User Template
       ↓
    Messages
       ↓
      LLM
       ↓
    Response
```

---

# 11. Prompt Template Function

Instead of creating prompts directly inside API routes, create a function.

```python
def build_course_prompt(goal, level):

    return f"""
    You are an AI course advisor.

    User goal:
    {goal}

    User level:
    {level}

    Recommend a suitable learning path.
    """
```

Then:

```python
prompt = build_course_prompt(
    goal="Learn backend development",
    level="beginner"
)
```

This keeps prompt logic separate from the rest of the application.

---

# 12. Why Separate Prompts from Application Logic?

A prompt can be placed directly inside an API route:

```python
@app.post("/recommend")
def recommend(request):

    prompt = f"""
    You are an AI course advisor.

    Goal:
    {request.goal}

    Level:
    {request.level}
    """

    response = call_llm(prompt)

    return response
```

This works, but prompts can become large as the application grows.

A better structure is:

```text
app/
│
├── routes/
│   └── recommendation.py
│
├── services/
│   └── llm_service.py
│
└── prompts/
    └── recommendation.py
```

Responsibilities:

```text
Route
  ↓
Service
  ↓
Prompt
  ↓
LLM
```

This makes the application easier to maintain.

---

# 13. Prompt Template with FastAPI

Create a request model:

```python
from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    goal: str
    level: str
```

Create a prompt function:

```python
def build_prompt(goal: str, level: str) -> str:

    return f"""
    You are an AI course advisor.

    User goal:
    {goal}

    User level:
    {level}

    Recommend a suitable learning path.
    """
```

Use it in the API:

```python
@app.post("/recommend")
def recommend(request: RecommendationRequest):

    prompt = build_prompt(
        request.goal,
        request.level
    )

    response = call_llm(prompt)

    return {
        "answer": response
    }
```

Flow:

```text
POST /recommend
      ↓
Pydantic Validation
      ↓
Prompt Template
      ↓
LLM
      ↓
Response
```

---

# 14. Reusable Prompt Templates

One template can be reused for many requests.

```python
def build_explanation_prompt(topic: str, level: str) -> str:

    return f"""
    Explain {topic} to a {level} learner.

    Use simple English.

    Give a practical example.
    """
```

For:

```python
build_explanation_prompt("FastAPI", "beginner")
```

The result is:

```text
Explain FastAPI to a beginner learner.

Use simple English.

Give a practical example.
```

The same function can be used for:

```python
build_explanation_prompt("LangGraph", "intermediate")
```

Result:

```text
Explain LangGraph to an intermediate learner.

Use simple English.

Give a practical example.
```

---

# 15. Prompt Templates with Context

Prompt templates become more useful when application data is added.

Example:

```text
You are an AI customer support assistant.

Customer question:
{question}

Customer information:
{customer_info}

Relevant documentation:
{documentation}

Answer the customer's question using the provided information.
```

The application can dynamically provide:

```text
question
customer_info
documentation
```

This creates a context-aware prompt.

---

# 16. Prompt Templates and RAG

Prompt templates become important when building RAG applications.

A RAG application may first retrieve relevant documents.

Flow:

```text
User Question
      ↓
Retrieve Relevant Documents
      ↓
Prompt Template
      ↓
Question + Retrieved Context
      ↓
LLM
      ↓
Answer
```

Example:

```text
Context:

FastAPI is a Python framework for building APIs.

Question:

What is FastAPI?

Instruction:

Answer using the provided context.
```

The retrieved context is dynamically inserted into the prompt.

---

# 17. Prompt Templates and Conversation History

A chatbot can dynamically include conversation history.

Example:

```text
System:

You are a helpful AI tutor.

Conversation:

User: What is Python?

Assistant: Python is a programming language.

User:

What can I build with it?
```

The application dynamically creates the input using:

```text
System Instructions
        +
Conversation History
        +
Current User Message
```

This is an important foundation for memory later in the roadmap.

---

# 18. Prompt Template vs Hardcoded Prompt

## Hardcoded Prompt

```python
prompt = "Explain FastAPI."
```

This works for one specific input.

## Prompt Template

```python
prompt = f"Explain {topic}."
```

This can work for many topics.

Therefore:

```text
Hardcoded Prompt
      ↓
Specific Use Case

Prompt Template
      ↓
Reusable Use Case
```

---

# 19. Prompt Template vs Prompt Engineering

These concepts are related but different.

## Prompt Engineering

Prompt engineering focuses on designing effective instructions for an LLM.

Example:

```text
Explain the concept using:

1. Definition
2. Example
3. Common mistake
```

## Prompt Template

A prompt template creates a reusable structure with variables.

Example:

```text
Explain {topic} for a {level} learner.
```

Together:

```text
Prompt Engineering
       +
Prompt Templates
       ↓
Reusable Effective Prompts
```

---

# 20. Dynamic Prompt Example

Consider an AI resume analyzer.

Input:

```text
Candidate:
Shubham

Target Role:
Backend Developer

Skills:
Python, FastAPI, SQL
```

Template:

```text
You are a technical recruiter.

Candidate:
{name}

Target Role:
{role}

Skills:
{skills}

Analyze the candidate's skills against the target role.

Identify missing skills and suggest improvements.
```

The application replaces the variables.

Final prompt:

```text
You are a technical recruiter.

Candidate:
Shubham

Target Role:
Backend Developer

Skills:
Python, FastAPI, SQL

Analyze the candidate's skills against the target role.

Identify missing skills and suggest improvements.
```

---

# 21. Common Mistakes

## Mistake 1: Hardcoding Dynamic Data

Avoid writing separate prompts for every possible input.

Use variables instead.

## Mistake 2: Mixing Too Much Logic Inside Prompts

Application logic should remain in the backend.

The prompt should primarily provide instructions and relevant context.

```text
Backend Logic
      +
Prompt
      ↓
LLM
```

## Mistake 3: Poor Variable Names

Prefer clear names:

```python
user_question
course_context
user_level
```

Instead of:

```python
x
data
value
```

Clear names make prompts easier to maintain.

## Mistake 4: Sending Irrelevant Context

Do not add every piece of application data to the prompt.

Only provide information relevant to the task.

## Mistake 5: Forgetting Input Validation

Dynamic values can come from users or external systems.

Validate them before using them in your application.

FastAPI + Pydantic helps with this.

---

# 22. Interview Questions

### Q1. What is a prompt template?

A prompt template is a reusable prompt structure containing variables that can be replaced with dynamic values.

### Q2. What is the difference between a static and dynamic prompt?

A static prompt remains the same, while a dynamic prompt changes based on application or user input.

### Q3. Why are prompt templates useful?

They make prompts reusable, maintainable, consistent, and easier to modify.

### Q4. What is a variable in a prompt template?

A variable is a placeholder whose value is provided dynamically when the prompt is created.

Example:

```text
Explain {topic}.
```

Here, `{topic}` is a variable.

### Q5. What is the difference between prompt engineering and prompt templates?

Prompt engineering focuses on designing effective instructions, while prompt templates provide a reusable structure for those instructions and dynamic data.

### Q6. How can prompt templates be used with FastAPI?

FastAPI can receive validated user input, pass it to a prompt-building function, and use the generated prompt to call an LLM.

### Q7. Why should prompts be separated from API routes?

Separating prompts from routes keeps application responsibilities organized and makes prompts easier to modify and reuse.
