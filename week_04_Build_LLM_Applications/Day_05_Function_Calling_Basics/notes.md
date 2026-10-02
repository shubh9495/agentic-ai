# Week 04 — Day 05: Function Calling Basics

## Points Covered

* What is Function Calling?
* Why LLMs Need Function Calling
* LLM vs Application Functions
* Basic Function Calling Flow
* Tools and Functions
* Function Schema
* Tool Call
* Function Execution
* Returning Tool Results to the LLM
* Function Calling with FastAPI
* Real-World Examples
* Function Calling vs Normal LLM Response
* Common Mistakes
* Interview Questions
---

# 1. What is Function Calling?

**Function calling** allows an LLM to request that a specific function in your application be executed.

The LLM does not directly execute your Python function.

Instead:

```text
User
 ↓
LLM
 ↓
Requests a Function Call
 ↓
Your Application
 ↓
Executes the Function
 ↓
Function Result
 ↓
LLM
 ↓
Final Response
```

For example, a user asks:

```text
"What is the weather in Dehradun?"
```

The LLM itself may not have access to live weather data.

Your application can provide a function:

```python
get_weather(city)
```

The LLM can decide:

```text
Call get_weather
city = "Dehradun"
```

Your backend executes the function and sends the result back to the LLM.

---

# 2. Why Do LLMs Need Function Calling?

An LLM mainly generates text based on its available context.

It cannot automatically:

* Query your database
* Call your APIs
* Read live weather
* Send an email
* Search your application data
* Execute your business logic

Function calling allows the LLM to interact with external systems through your application.

For example:

```text
LLM
 ↓
Function Call
 ↓
Database
 ↓
Result
 ↓
LLM
```

This makes LLM applications more useful and interactive.

---

# 3. LLM vs Application Functions

It is important to understand who does what.

### LLM

The LLM decides **which function may be useful and what arguments to provide**.

### Application

Your application actually **executes the function**.

Example:

```text
User:
"What is the price of course 101?"
```

The LLM may decide:

```text
Function:
get_course_price

Arguments:
course_id = 101
```

Your backend executes:

```python
get_course_price(101)
```

The database returns:

```text
₹4,999
```

The result is sent back to the LLM.

The LLM then generates:

```text
"The course costs ₹4,999."
```

---

# 4. Basic Function Calling Flow

The complete flow is:

```text
User
 ↓
Application
 ↓
LLM
 ↓
LLM decides a function is needed
 ↓
Tool / Function Call
 ↓
Application executes function
 ↓
Function Result
 ↓
LLM
 ↓
Final Answer
 ↓
User
```

This is the basic foundation of tool-using agents.

---

# 5. What is a Tool?

A **tool** is an operation that an LLM can request through your application.

A tool can be backed by a normal Python function.

For example:

```python
def get_course(course_id: int):
    ...
```

This function can be exposed to the LLM as a tool.

Conceptually:

```text
Python Function
      ↓
Tool Definition
      ↓
LLM
```

Common tools include:

```text
get_weather()
search_courses()
get_user()
calculate_price()
send_email()
search_database()
```

---

# 6. What is a Function Schema?

The LLM needs to know:

* Function name
* What the function does
* What arguments it accepts
* The type of each argument

This information is represented using a **function schema**.

Example:

```text
Function:
get_weather

Description:
Get the current weather for a city.

Arguments:
city → string
```

Conceptually:

```json
{
  "name": "get_weather",
  "description": "Get the current weather for a city.",
  "parameters": {
    "city": {
      "type": "string"
    }
  }
}
```

The exact schema format depends on the LLM provider.

---

# 7. Why is the Schema Important?

The LLM needs information about the function before it can request it.

For example:

```text
Function: get_course

Description:
Get course information using a course ID.

Arguments:
course_id → integer
```

Now if the user asks:

```text
"Tell me about course 10."
```

The model can determine:

```text
Function:
get_course

Arguments:
course_id = 10
```

Without a clear schema, the model has less information about how the function should be used.

---

# 8. Tool Call

A **tool call** is the LLM's structured request to execute a specific tool.

For example:

```text
Tool:
get_course

Arguments:
{
    "course_id": 10
}
```

The LLM is not executing the function.

It is saying:

```text
"I want the application to execute get_course with course_id = 10."
```

---

# 9. Function Execution

After receiving the tool call, your backend executes the actual function.

Example:

```python
def get_course(course_id: int):
    return {
        "id": course_id,
        "name": "FastAPI",
        "level": "Beginner"
    }
```

The application receives:

```text
course_id = 10
```

and executes:

```python
result = get_course(10)
```

Result:

```python
{
    "id": 10,
    "name": "FastAPI",
    "level": "Beginner"
}
```

---

# 10. Returning the Result to the LLM

The function result is then sent back to the LLM.

Flow:

```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Python Function
 ↓
Function Result
 ↓
LLM
 ↓
Final Answer
```

For example:

```text
Function Result:

{
    "id": 10,
    "name": "FastAPI",
    "level": "Beginner"
}
```

The LLM can convert this into a natural-language response:

```text
"Course 10 is FastAPI and it is suitable for beginners."
```

---

# 11. Simple Example

Suppose we have:

```python
def calculate_total(price: float, quantity: int):
    return price * quantity
```

User:

```text
"I want 3 courses that cost ₹1000 each."
```

The LLM can request:

```text
Function:
calculate_total

Arguments:
price = 1000
quantity = 3
```

Your application executes:

```python
calculate_total(1000, 3)
```

Result:

```text
3000
```

The LLM receives the result and responds:

```text
"The total price is ₹3,000."
```

---

# 12. Function Calling with FastAPI

Function calling can be integrated into a FastAPI application.

Example structure:

```text
Frontend
   ↓
FastAPI
   ↓
LLM
   ↓
Tool Call
   ↓
Python Function
   ↓
Database / API
   ↓
Tool Result
   ↓
LLM
   ↓
FastAPI
   ↓
Frontend
```

Example endpoint:

```python
@app.post("/course-info")
async def course_info(request: CourseRequest):

    response = await call_llm(
        request.question,
        tools=[get_course]
    )

    return response
```

The exact implementation depends on the LLM SDK.

---

# 13. Example: Course Support Application

Suppose your AI Course Support API has a database containing courses.

User:

```text
"What is the duration of the FastAPI course?"
```

Your application provides:

```python
def get_course_details(course_name: str):
    # Query database
    ...
```

The LLM can request:

```text
get_course_details(
    course_name="FastAPI"
)
```

Your application queries PostgreSQL.

Database result:

```text
Course:
FastAPI

Duration:
30 hours
```

The result goes back to the LLM.

Final response:

```text
"The FastAPI course has a duration of 30 hours."
```

---

# 14. Function Calling vs Normal LLM Response

### Normal LLM

```text
User
 ↓
LLM
 ↓
Text Response
```

Example:

```text
User:
"What is Python?"

LLM:
"Python is a programming language..."
```

---

### Function Calling

```text
User
 ↓
LLM
 ↓
Tool Call
 ↓
Application
 ↓
Function
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
"What is the current price of course 101?"

LLM
 ↓
get_course_price(101)
 ↓
Database
 ↓
₹4,999
 ↓
LLM
 ↓
"Course 101 costs ₹4,999."
```

---

# 15. Function Calling Does Not Mean the LLM Executes Code

This is an important concept.

The LLM generates a structured tool request.

Your application controls execution.

```text
LLM
 ↓
"Call get_course(10)"
 ↓
Application
 ↓
Actually executes get_course(10)
```

Therefore:

```text
LLM = Decides what tool to request

Application = Executes the tool
```

This separation is important for security and control.

---

# 16. Multiple Functions

An application can provide multiple tools.

For example:

```text
get_course()
search_courses()
get_user()
calculate_price()
```

The LLM can select the appropriate function based on the user's request.

Example:

```text
User:
"Find Python courses for beginners."

        ↓

LLM

        ↓

search_courses(
    language="Python",
    level="beginner"
)
```

Another request:

```text
"What is the price of course 10?"

        ↓

get_course_price(
    course_id=10
)
```

The application can expose multiple tools to the model.

---

# 17. Function Calling and External APIs

Tools do not have to access only databases.

A function can call an external API.

Example:

```python
def get_weather(city: str):

    # Call weather API
    response = requests.get(...)

    return response.json()
```

The LLM requests:

```text
get_weather("Dehradun")
```

Your backend calls the weather API.

```text
LLM
 ↓
get_weather()
 ↓
Weather API
 ↓
Weather Data
 ↓
LLM
 ↓
Final Answer
```

---

# 18. Function Calling and AI Agents

Function calling is one of the foundations of AI agents.

An agent can:

```text
Understand Goal
     ↓
Choose Tool
     ↓
Call Tool
     ↓
Observe Result
     ↓
Decide Next Action
     ↓
Call Another Tool
     ↓
Final Answer
```

For example:

```text
User:
"Find a suitable Python course and tell me its price."
```

The agent may:

```text
search_courses()
      ↓
get_course_price()
      ↓
Final Answer
```

You will study the complete agent loop in **Week 06**.

---

# 19. Function Calling vs Tool Calling

These terms are closely related.

### Function Calling

Usually refers to allowing an LLM to request a specific function with structured arguments.

### Tool Calling

A broader term for allowing an LLM to interact with external capabilities.

```text
Tool
 ├── Function
 ├── Database Operation
 ├── API
 └── Other External Capability
```

Modern LLM APIs often use the term **tool calling**.

For now, remember:

```text
Function Calling
        ↓
LLM requests a function

Tool Calling
        ↓
LLM requests an external capability
```

The exact terminology varies between providers.

---

# 20. Common Mistakes

## Mistake 1: Thinking the LLM executes the function

The LLM only requests the function.

Your application executes it.

---

## Mistake 2: Poor function descriptions

Bad:

```text
get_data()
```

Better:

```text
Get course details using the course ID.
```

Clear descriptions help the model understand when the function should be used.

---

## Mistake 3: Poor argument definitions

Clearly define:

```text
name
type
description
```

For example:

```text
course_id:
Type → integer
Description → Unique ID of the course
```

---

## Mistake 4: Trusting tool arguments blindly

Tool arguments should still be validated by your application.

```text
LLM Tool Call
      ↓
Validate Arguments
      ↓
Execute Function
```

Do not assume model-generated input is always correct.

---

## Mistake 5: Giving the LLM unnecessary tools

Only expose tools that the application actually needs.

Too many unrelated tools can make tool selection more difficult.

---

# 21. Interview Questions

### Q1. What is function calling?

Function calling allows an LLM to request that a specific function in the application be executed using structured arguments.

---

### Q2. Does the LLM execute the function?

No.

The LLM generates a tool/function request, while the application executes the actual function.

---

### Q3. Why is function calling useful?

It allows LLM applications to interact with databases, APIs, external services, and application logic.

---

### Q4. What is a function schema?

A function schema describes the function's name, purpose, arguments, and argument types so the LLM knows how the function can be used.

---

### Q5. What is a tool call?

A tool call is the structured request generated by the LLM asking the application to execute a particular tool with specific arguments.

---

### Q6. What happens after a function is executed?

The application sends the function result back to the LLM, which can use that result to generate the final response.

---

### Q7. Can an LLM use multiple functions?

Yes. An application can provide multiple tools, and the model can request the tool that is appropriate for the user's request.

---

### Q8. How is function calling related to AI agents?

Function calling provides the mechanism through which agents interact with external tools and systems.

---