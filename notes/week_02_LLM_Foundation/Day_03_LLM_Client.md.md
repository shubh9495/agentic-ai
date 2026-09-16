# Week 2 — Day 3: LLM APIs

## Topics Covered

1. **What is an LLM API?** — Understanding how applications communicate with LLMs
2. **API Keys** — Authenticating requests
3. **SDKs** — Using provider libraries from Python
4. **Client Objects** — Creating an LLM client
5. **Model Selection** — Choosing an appropriate model
6. **Messages** — Sending system and user instructions
7. **API Requests** — Sending data to the model
8. **API Responses** — Understanding returned data
9. **Input & Output Tokens** — Understanding token usage
10. **Temperature & Generation Settings** — Controlling model behavior
11. **Error Handling** — Handling API failures
12. **Environment Variables** — Safely storing API keys
13. **Practical Usage** — Building a basic Python LLM client

---

## 1. What is an LLM API?

An LLM API allows your application to communicate with an LLM hosted by a provider.

Instead of running a large model yourself, your application sends a request to the provider.

For example:

```text
Your Python Application
        ↓
      Request
        ↓
   LLM Provider
        ↓
       Model
        ↓
     Response
        ↓
Your Python Application
```

Your application can then use the generated response.

---

## 2. Why Use an API?

Running a large language model locally can require significant:

* Compute
* GPU memory
* Storage
* Setup
* Maintenance

With an API, the model runs on the provider's infrastructure.

Your application only needs to send requests and process responses.

For example:

```text
Your App
   ↓
Internet
   ↓
LLM API
   ↓
Model
```

This makes it easier to build AI applications.

---

## 3. API Key

Most LLM APIs require authentication.

An API key identifies and authorizes your application.

Conceptually:

```text
Python Application
       ↓
API Key + Request
       ↓
LLM Provider
       ↓
Response
```

Never put an API key directly into source code that you plan to publish.

Bad:

```python
api_key = "my-secret-key"
```

If this code is pushed to GitHub, the key may become exposed.

---

## 4. Environment Variables

A better approach is to store the API key in an environment variable.

For example:

```text
OPENAI_API_KEY=your_key_here
```

Then Python can read it:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

This keeps the secret outside your source code.

A common project structure is:

```text
project/
│
├── main.py
├── .env
├── .gitignore
└── requirements.txt
```

The `.env` file should not be committed to GitHub.

Add it to `.gitignore`:

```text
.env
```

---

## 5. SDK

An SDK is a software development kit provided to make API usage easier.

Instead of manually constructing HTTP requests, you can use a Python library.

Conceptually:

```text
Without SDK:

Python
 ↓
HTTP Request
 ↓
API
```

With an SDK:

```text
Python
 ↓
SDK
 ↓
API
```

The SDK handles many details for you.

Different providers have different SDKs and APIs.

---

## 6. Client Object

Many LLM SDKs provide a client object.

The client is responsible for communicating with the provider's API.

Conceptually:

```python
client = SomeLLMClient(api_key=api_key)
```

Then you use the client to send requests.

For example:

```python
response = client.generate(...)
```

The exact syntax depends on the provider and SDK.

---

## 7. Choosing a Model

LLM providers usually offer multiple models.

Different models may differ in:

* Speed
* Cost
* Context window
* Reasoning ability
* Output quality
* Tool-calling capabilities
* Multimodal capabilities

You should select a model based on the task.

For example:

```text
Simple task
    ↓
Smaller/faster model
```

while:

```text
Complex reasoning task
    ↓
More capable model
```

There is no single model that is always the correct choice for every application.

---

## 8. Messages

LLM APIs commonly work with messages.

The main roles are:

```text
system
user
assistant
```

For example:

```text
System:
You are a helpful Python tutor.

User:
Explain decorators.

Assistant:
A decorator is...
```

When using an API, these messages are sent as part of the request.

---

## 9. Basic API Request

A simplified request looks like:

```python
response = client.generate(
    model="model-name",
    prompt="Explain Python decorators."
)
```

The actual syntax varies between providers.

The important concept is:

```text
model
+
input
+
settings
      ↓
API Request
```

---

## 10. Chat-Based API Request

A chat-style request may look conceptually like:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor."
    },
    {
        "role": "user",
        "content": "Explain decorators."
    }
]
```

Then the messages are sent to the model.

```text
System Message
       +
User Message
       ↓
      LLM
       ↓
Assistant Response
```

---

## 11. API Response

The API usually returns structured data.

Conceptually:

```python
response = client.generate(...)

print(response)
```

The response may contain information such as:

```text
Generated text
Model information
Token usage
Finish information
Request metadata
```

The exact structure depends on the API.

Your application usually extracts the generated text from the response.

For example:

```python
answer = response.text

print(answer)
```

The exact property depends on the SDK.

---

## 12. Input and Output Tokens

Remember from Day 1:

LLMs process text using tokens.

When using an API, there are generally:

```text
Input Tokens
     +
Output Tokens
     =
Total Token Usage
```

For example:

```text
Prompt
 ↓
500 input tokens

Response
 ↓
200 output tokens

Total
 ↓
700 tokens
```

Token usage can affect:

* Cost
* Context limits
* Application performance

---

## 13. Temperature

Temperature can be passed as a generation setting when supported by the model/API.

Conceptually:

```python
response = client.generate(
    model="model-name",
    prompt="Write a creative story.",
    temperature=0.8
)
```

Lower values generally produce more predictable output.

Higher values generally allow more variation.

Remember:

```text
Temperature
≠
Model intelligence
```

It controls output variation rather than making the model smarter.

---

## 14. API Parameters

An LLM request can contain different parameters.

Conceptually:

```text
Request
│
├── Model
├── Messages / Prompt
├── Temperature
├── Maximum output tokens
├── Tools
└── Other model-specific settings
```

Not every model supports every parameter.

Always check the documentation for the specific model/API you are using.

---

## 15. Error Handling

API requests can fail.

Common reasons include:

* Invalid API key
* Invalid request
* Rate limit
* Network failure
* Server error
* Model unavailable
* Invalid parameters

Your application should handle these errors.

Example:

```python
try:

    response = client.generate(
        model="model-name",
        prompt="Explain APIs."
    )

    print(response.text)

except Exception as error:

    print(f"API request failed: {error}")
```

In production applications, you should catch specific exceptions when the SDK provides them rather than relying only on `Exception`.

---

## 16. Rate Limits

API providers may limit how many requests your application can make.

For example:

```text
Application
   ↓
Request 1
Request 2
Request 3
Request 4
...
   ↓
Rate Limit
```

If you exceed a limit, the API may return an error.

A production application may need:

* Retries
* Exponential backoff
* Request limits
* Caching
* Queues
* Monitoring

You will encounter these concepts later when learning production AI systems.

---

## 17. Environment Variables with Python

You can use Python's `os` module:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

You can also use a `.env` file with a package such as `python-dotenv`.

Example `.env`:

```text
OPENAI_API_KEY=your_key_here
```

Python:

```python
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```

Now the API key can be accessed without putting it directly into the source code.

---

## 18. Basic LLM Client Structure

A simple application can be organized like this:

```text
llm_app/
│
├── main.py
├── client.py
├── .env
├── .gitignore
└── requirements.txt
```

### `client.py`

Contains LLM communication logic.

### `main.py`

Contains application logic.

### `.env`

Contains local secrets.

### `.gitignore`

Prevents secrets from being committed.

### `requirements.txt`

Contains project dependencies.

---

## 19. Simple LLM Client

A provider-specific SDK should be used according to its current documentation.

The general structure is:

```python
import os


class LLMClient:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def ask(self, question: str) -> str:

        # Send question to LLM API
        # Receive response
        # Extract generated text

        return "LLM response"
```

Then:

```python
api_key = os.getenv("LLM_API_KEY")

client = LLMClient(api_key)

answer = client.ask(
    "What is RAG?"
)

print(answer)
```

This is the same OOP pattern you learned in Week 1.

---

## 20. Connecting Week 1 with Week 2

You already learned how to create API clients in Python.

Week 1:

```text
Python
 ↓
Class
 ↓
Method
 ↓
HTTP Request
 ↓
JSON Response
```

Now:

```text
Python
 ↓
LLM Client
 ↓
LLM API
 ↓
Model
 ↓
Generated Response
```

The underlying software concepts are similar.

---

## 21. LLM API vs Normal API

A normal API might return data from a database or service.

Example:

```text
Python
 ↓
Weather API
 ↓
Weather Data
```

An LLM API generates model output:

```text
Python
 ↓
LLM API
 ↓
Language Model
 ↓
Generated Response
```

An Agentic AI application can combine both:

```text
                 ┌── Weather API
                 │
User → Agent → LLM
                 │
                 ├── Database
                 │
                 └── Search Tool
```

This is one of the foundations of tool-using agents.

---

## 22. LLM API in an Agent

An agent can use an LLM to decide what action to take.

For example:

```text
User:
Find my order status.
        ↓
      Agent
        ↓
       LLM
        ↓
Decides to use order-status tool
        ↓
Order API
        ↓
Tool Result
        ↓
       LLM
        ↓
Final Response
```

The LLM itself may not know the current order status.

The agent gives it access to a tool that can retrieve the information.

This distinction is very important:

```text
LLM
→ Generates and reasons over language/context

Tool
→ Performs an external action or retrieves external data

Agent
→ Coordinates the LLM and tools
```

---

## 23. Security Basics

Never expose your API key.

Avoid:

```python
api_key = "secret-key"
```

Avoid committing:

```text
.env
```

to GitHub.

Use:

```text
Environment Variables
+
.gitignore
+
Secret Management
```

For production applications, use a proper secrets-management system rather than relying only on a local `.env` file.

---