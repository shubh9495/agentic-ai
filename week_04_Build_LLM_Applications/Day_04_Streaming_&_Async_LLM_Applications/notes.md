# Week 04 — Day 04: Streaming & Async LLM Applications

## Points Covered

* What is Streaming?
* Normal LLM Response vs Streaming
* Why Streaming is Useful
* Streaming in Chat Applications
* Tokens and Streaming
* What is Async Programming?
* Sync vs Async LLM Calls
* `async` and `await`
* Async API Endpoints
* Streaming + Async
* Basic LLM Streaming Flow
* Streaming in FastAPI
* When to Use Streaming
* Common Mistakes
* Interview Questions
* Final Mental Model

---

# 1. What is Streaming?

**Streaming** means sending the LLM response to the user gradually as it is generated instead of waiting for the complete response.

Without streaming:

```text
User
 ↓
LLM
 ↓
Generate complete response
 ↓
Send complete response
 ↓
User
```

With streaming:

```text
User
 ↓
LLM
 ↓
First part → User
Second part → User
Third part → User
...
Final part → User
```

This makes the application feel faster and more interactive.

---

# 2. Normal LLM Response vs Streaming

Suppose the LLM needs several seconds to generate:

```text
"FastAPI is a modern Python framework for building APIs..."
```

### Without Streaming

The user sees nothing until the complete response is ready.

```text
Request
   ↓
Wait
   ↓
Wait
   ↓
Complete Response
```

### With Streaming

The user may see:

```text
FastAPI
```

then:

```text
FastAPI is
```

then:

```text
FastAPI is a modern
```

then:

```text
FastAPI is a modern Python framework...
```

The exact chunks depend on the model and API.

---

# 3. Why is Streaming Useful?

Streaming is especially useful for applications where the model generates longer responses.

Examples:

* Chatbots
* AI coding assistants
* AI writing tools
* AI tutors
* Customer support assistants
* Content generation applications

The main benefit is **lower perceived waiting time**.

The model may still take the same amount of time to finish generating the complete answer, but the user starts seeing output earlier.

---

# 4. Streaming and Tokens

LLMs generate text incrementally.

The API can expose these generated pieces as they become available.

Conceptually:

```text
LLM
 ↓
Token / Chunk
 ↓
Token / Chunk
 ↓
Token / Chunk
 ↓
...
 ↓
Complete Response
```

For example:

```text
"The"
" answer"
" is"
" FastAPI..."
```

The exact chunks are not necessarily individual tokens. An API may group multiple tokens into a chunk.

So:

```text
Streaming ≠ Always One Token at a Time
```

It means the response is delivered incrementally.

---

# 5. Streaming in a Chat Application

A normal chatbot might work like:

```text
User
 ↓
Send Question
 ↓
Wait
 ↓
Complete AI Response
 ↓
Display
```

A streaming chatbot works like:

```text
User
 ↓
Send Question
 ↓
LLM starts generating
 ↓
Stream chunks
 ↓
Display chunks immediately
 ↓
Continue receiving chunks
 ↓
Complete
```

This creates the familiar "AI is typing" experience.

---

# 6. What is Async Programming?

**Asynchronous programming** allows a program to start an operation and handle other work while waiting for that operation to complete.

This is especially useful for operations that spend time waiting for external resources.

Examples:

* LLM API calls
* Database queries
* HTTP requests
* File operations
* External APIs

---

# 7. Synchronous vs Asynchronous

## Synchronous

In synchronous code, the program waits for the operation to finish.

```text
Task A
 ↓
Wait
 ↓
Task A Complete
 ↓
Task B
```

For example:

```python
response = call_llm()
print(response)
```

The program waits for `call_llm()` to finish.

---

## Asynchronous

In asynchronous code, the program can handle other work while waiting for an I/O operation.

```text
Task A
 ↓
Waiting for API
 ↓
Other work can continue
 ↓
API response arrives
 ↓
Continue Task A
```

Example:

```python
response = await call_llm()
print(response)
```

The `await` indicates that the program is waiting for an asynchronous operation.

---

# 8. `async` and `await`

Python provides two important keywords for asynchronous programming.

### `async`

Used to define an asynchronous function.

```python
async def get_response():
    ...
```

### `await`

Used to wait for an asynchronous operation inside an async function.

```python
response = await call_llm()
```

Basic structure:

```python
async def get_response():
    response = await call_llm()
    return response
```

---

# 9. Why Async is Useful for LLM Applications

LLM APIs are external network services.

A request may take time because:

```text
Your Application
      ↓
Internet
      ↓
LLM Provider
      ↓
Model Processing
      ↓
Response
      ↓
Internet
      ↓
Your Application
```

During this time, the application is mostly waiting for I/O.

Async programming can help your backend handle other work efficiently while those requests are waiting.

---

# 10. Sync LLM Application

Conceptually:

```python
def chat():
    response = call_llm()
    return response
```

Flow:

```text
Request
  ↓
LLM API Call
  ↓
Wait
  ↓
Response
  ↓
Return
```

---

# 11. Async LLM Application

Conceptually:

```python
async def chat():
    response = await call_llm()
    return response
```

Flow:

```text
Request
  ↓
Async LLM API Call
  ↓
Wait without blocking the async event loop
  ↓
Response
  ↓
Return
```

The exact behavior also depends on the SDK and whether the operation is truly asynchronous.

---

# 12. Async FastAPI Endpoint

FastAPI supports asynchronous endpoints.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
async def chat():
    response = await call_llm()

    return {
        "answer": response
    }
```

The important parts are:

```text
async def
   ↓
await
   ↓
Async LLM Operation
```

---

# 13. Streaming + Async

Streaming and async can be combined.

Conceptually:

```text
User
 ↓
FastAPI
 ↓
Async LLM Request
 ↓
LLM starts generating
 ↓
Stream chunk
 ↓
User
 ↓
Stream chunk
 ↓
User
 ↓
...
```

This is a common architecture for modern AI chat applications.

---

# 14. Basic Streaming Flow

The complete process can be represented as:

```text
User Message
      ↓
FastAPI Endpoint
      ↓
Build Prompt
      ↓
Async LLM Request
      ↓
LLM Starts Generating
      ↓
Receive Chunk
      ↓
Send Chunk to Client
      ↓
Receive Next Chunk
      ↓
Send Chunk to Client
      ↓
...
      ↓
Generation Complete
```

---

# 15. Conceptual Streaming Code

The exact implementation depends on the LLM provider.

Conceptually:

```python
async def stream_response():
    stream = await call_llm_stream()

    async for chunk in stream:
        yield chunk
```

Here:

```text
async def
```

defines an async function.

```text
await
```

waits for the async operation.

```text
async for
```

iterates over data arriving asynchronously.

```text
yield
```

sends each chunk incrementally.

---

# 16. `yield` in Streaming

`yield` allows a function to produce values one at a time instead of returning everything at once.

Normal function:

```python
def get_data():
    return "complete data"
```

Streaming-style function:

```python
def get_data():
    yield "first"
    yield "second"
    yield "third"
```

The consumer can receive the values incrementally.

For LLM streaming:

```text
LLM
 ↓
Chunk 1 → yield
Chunk 2 → yield
Chunk 3 → yield
...
```

---

# 17. Streaming Response in FastAPI

FastAPI provides `StreamingResponse` for streaming data.

Conceptually:

```python
from fastapi.responses import StreamingResponse

@app.get("/chat")
async def chat():

    return StreamingResponse(
        stream_response(),
        media_type="text/plain"
    )
```

The client can receive the response progressively.

The exact implementation may differ depending on the LLM SDK and transport being used.

---

# 18. Streaming with a Frontend

The backend streams chunks to the frontend.

Architecture:

```text
                 LLM
                  ↓
             Stream Chunks
                  ↓
              FastAPI
                  ↓
              HTTP Stream
                  ↓
               React
                  ↓
          Display Incrementally
```

The frontend can append each received chunk to the existing answer.

Example:

```text
Chunk 1:
"FastAPI"

Chunk 2:
" is a"

Chunk 3:
" Python"

Chunk 4:
" framework."
```

Frontend displays:

```text
FastAPI is a Python framework.
```

---

# 19. Streaming vs Async

These concepts are related but not the same.

### Streaming

Defines **how data is delivered**.

```text
Data → Incrementally
```

### Async

Defines **how the application handles waiting operations**.

```text
Wait → Without blocking the async workflow
```

Therefore:

```text
Streaming ≠ Async
```

But they can be used together:

```text
Async LLM Call
      +
Streaming Response
      ↓
Responsive LLM Application
```

---

# 20. When Should You Use Streaming?

Streaming is useful when:

* Responses are long
* Users expect a chatbot experience
* First output should appear quickly
* The application generates content interactively
* You want an AI typing effect

Streaming may be unnecessary when:

* The response is very short
* The application needs the complete result before processing
* The output is primarily structured data that must be validated as a whole

For example:

```text
Classification:
"positive"
```

does not usually need streaming.

But:

```text
Long AI explanation
```

can benefit from streaming.

---

# 21. When Should You Use Async?

Async is useful when your application performs many I/O-bound operations.

For example:

```text
FastAPI
  ↓
LLM API
  ↓
Database
  ↓
External API
```

Async can be useful when these operations involve waiting on network or other I/O.

A key point:

```text
Async is not automatically faster.
```

It is mainly useful for handling I/O efficiently and improving concurrency.

---

# 22. Async vs Threading

These are different approaches.

### Async

Usually useful for I/O-bound operations that support asynchronous APIs.

```text
Network I/O
API Calls
Database I/O
```

### Threading

Can be useful for certain blocking I/O operations.

```text
Blocking API
File I/O
Legacy libraries
```

For CPU-heavy work, other approaches such as multiprocessing or separate workers may be more appropriate.

The important point for today's topic is:

```text
LLM API calls → Mostly I/O-bound
```

So async APIs can be useful when the SDK supports them.

---

# 23. Async LLM Application Architecture

A more complete architecture looks like:

```text
                         User
                           ↓
                        React
                           ↓
                        FastAPI
                           ↓
                    Async Endpoint
                           ↓
                  Prompt Construction
                           ↓
                    Async LLM SDK
                           ↓
                         LLM
                           ↓
                  Streamed Chunks
                           ↓
                    FastAPI Stream
                           ↓
                         React
                           ↓
                          User
```

---

# 24. Example: AI Course Assistant

Suppose the user asks:

```text
"Explain SQLAlchemy."
```

The application can work like:

```text
User
 ↓
POST /chat
 ↓
FastAPI
 ↓
Build Prompt
 ↓
Async LLM Request
 ↓
LLM generates response
 ↓
"SQLAlchemy"
 ↓
"is an"
 ↓
"ORM..."
 ↓
Frontend displays progressively
```

The user does not have to wait for the complete explanation before seeing the first part.

---

# 25. Error Handling with Streaming

Streaming introduces additional cases that should be handled.

For example:

```text
Request
 ↓
Stream starts
 ↓
Some chunks received
 ↓
LLM/API error
```

The application should handle the failure gracefully.

Possible issues:

* Network interruption
* Provider error
* Timeout
* Rate limit
* Client disconnect
* Invalid request

Do not assume that a stream will always complete successfully.

---

# 26. Common Mistakes

## Mistake 1: Thinking streaming makes the model generate faster

Streaming mainly reduces **perceived waiting time**.

It does not necessarily reduce the total generation time.

---

## Mistake 2: Thinking async and streaming are the same

They solve different problems.

```text
Async → How waiting is handled

Streaming → How results are delivered
```

---

## Mistake 3: Using async without an async API

If the underlying SDK operation is blocking, simply writing `async def` does not automatically make the operation asynchronous.

The library or operation must support async behavior, or blocking work needs to be handled appropriately.

---

## Mistake 4: Streaming everything

Not every response needs streaming.

For small structured outputs, a normal response may be simpler.

---

## Mistake 5: Ignoring client disconnects

In a real streaming application, users can close the page or cancel the request.

The backend should handle disconnected clients and clean up resources appropriately.

---