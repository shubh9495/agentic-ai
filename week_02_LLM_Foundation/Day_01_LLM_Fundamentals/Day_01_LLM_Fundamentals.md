# Day 1: LLM Fundamentals

Day 1 introduces the basic concepts behind Large Language Models (LLMs).

The goal is to understand how LLMs work at a practical level before using them through APIs.

## Topics Covered

1. **LLM** — Understanding Large Language Models
2. **Generative AI** — Understanding how AI generates content
3. **Tokens** — Understanding how text is processed
4. **Context Window** — Understanding how much information an LLM can process
5. **Training vs Inference** — Understanding how models learn and generate responses
6. **Parameters** — Understanding what model parameters represent
7. **Temperature** — Controlling response randomness
8. **System, User & Assistant Messages** — Understanding conversation structure
9. **Prompt** — Giving instructions to an LLM
10. **LLM Input & Output** — Understanding the basic LLM workflow
11. **Hallucination** — Understanding why LLMs can generate incorrect information
12. **Practical Usage** — Connecting LLM concepts with Agentic AI

---

## 1. What is an LLM?

LLM stands for:

**Large Language Model**

An LLM is an AI model trained on a large amount of text data to understand and generate human-like text.

Examples include:

* GPT
* Claude
* Gemini
* Llama
* Mistral

A simple workflow is:

```text
User Input
    ↓
LLM
    ↓
Generated Output
```

Example:

```text
Input:
What is Python?

Output:
Python is a high-level programming language...
```

---

## 2. What is Generative AI?

Generative AI refers to AI systems that can generate new content.

The content can include:

* Text
* Images
* Audio
* Video
* Code

LLMs are mainly used for generating and understanding text and code.

Example:

```text
Prompt
  ↓
Generative AI
  ↓
New Content
```

For example:

```text
Prompt:
Write a Python function to calculate factorial.

Generated:
def factorial(n):
    ...
```

---

## 3. How Does an LLM Generate Text?

At a simplified level, an LLM predicts what token should come next based on the previous context.

Example:

```text
The capital of India is
```

The model may predict:

```text
New
```

Then:

```text
Delhi
```

The process continues until the model generates the response.

Simplified:

```text
Input
 ↓
Understand Context
 ↓
Predict Next Token
 ↓
Predict Next Token
 ↓
Predict Next Token
 ↓
Final Response
```

LLMs do not simply retrieve a fixed answer from a database.

They generate a response based on patterns learned during training and the context provided at inference time.

---

## 4. What is a Token?

LLMs generally process text as **tokens**, not directly as complete words.

A token can be:

* A complete word
* Part of a word
* A punctuation mark
* A special token

For example:

```text
I love Python!
```

may be split into tokens approximately like:

```text
I
love
Python
!
```

The exact tokenization depends on the model and tokenizer.

### Why are tokens important?

Tokens are important because:

* Models have token limits.
* API usage is often measured using tokens.
* Input consumes tokens.
* Output consumes tokens.

For example:

```text
Input tokens
      +
Output tokens
      =
Total tokens
```

---

## 5. Context Window

The **context window** is the amount of information a model can consider within a single request/conversation context.

It is generally measured in tokens.

Example:

```text
Context Window
-------------------------
System instructions
User messages
Conversation history
Documents
Tool results
Current question
-------------------------
```

If the context becomes too large, older information may need to be removed, summarized, or otherwise managed.

### Why is this important for Agentic AI?

Agents may work with:

* Conversation history
* Tool results
* Documents
* API responses
* Previous actions
* Instructions

All of these can become part of the agent's context.

Therefore, **context management** becomes very important when building agents.

---

## 6. Training vs Inference

These are two different stages.

### Training

During training, the model learns patterns from large amounts of data.

```text
Training Data
     ↓
Model Training
     ↓
Trained Model
```

Training is computationally expensive and is normally performed by the model provider.

### Inference

Inference happens when you actually use the trained model.

```text
Your Prompt
     ↓
Trained Model
     ↓
Response
```

When you send a request to an LLM API, you are performing inference.

### Simple Difference

| Training               | Inference                      |
| ---------------------- | ------------------------------ |
| Model learns           | Model generates                |
| Uses training data     | Uses current input/context     |
| Expensive              | Usually much cheaper           |
| Done before deployment | Happens when you use the model |

---

## 7. What are Model Parameters?

Parameters are values learned by the neural network during training.

You can think of them as part of the model's learned internal representation.

For example:

```text
Training
   ↓
Millions/Billions of learned parameters
   ↓
Model
```

A model with more parameters is not automatically better.

Model quality also depends on:

* Architecture
* Training data
* Training methods
* Reasoning capabilities
* Post-training
* Context handling
* Tool use
* Model design

You do not normally modify these parameters when simply calling an LLM API.

---

## 8. Temperature

Temperature controls how random or varied the model's output can be.

A lower temperature generally produces more predictable output.

A higher temperature generally allows more variation.

Conceptually:

```text
Low Temperature
      ↓
More predictable
More consistent
```

```text
High Temperature
      ↓
More varied
More creative
```

Example:

```text
Prompt:
Give me a name for an AI startup.
```

Lower temperature may repeatedly produce similar types of names.

Higher temperature may produce more diverse names.

### Important

Temperature does **not** make the model smarter.

It mainly affects how the model selects among possible outputs.

---

## 9. System, User and Assistant Messages

LLM applications commonly organize conversations using different message roles.

### System

Contains high-level instructions for the model.

Example:

```text
You are a helpful Python tutor.
Explain concepts using simple examples.
```

### User

Contains the user's request.

Example:

```text
Explain decorators in Python.
```

### Assistant

Represents the model's response.

Example:

```text
A decorator is a function that...
```

The basic structure is:

```text
System
   ↓
User
   ↓
Assistant
   ↓
User
   ↓
Assistant
```

This structure becomes very important when working with LLM APIs.

---

## 10. What is a Prompt?

A prompt is the input or instruction provided to an AI model.

Simple example:

```text
Explain Python decorators.
```

A better prompt provides more context.

```text
Explain Python decorators to a beginner.

Requirements:
- Use simple English.
- Give one practical example.
- Explain the code step by step.
```

The second prompt provides clearer instructions.

---

## 11. LLM Input and Output

The basic LLM workflow is:

```text
Input
  ↓
LLM
  ↓
Output
```

For example:

```text
Input:
Explain REST APIs.

LLM:
A REST API is an interface that allows
applications to communicate over HTTP...
```

In an application, the input can contain much more than a simple question.

For example:

```text
System Instructions
+
User Question
+
Conversation History
+
Retrieved Documents
+
Tool Results
        ↓
       LLM
        ↓
     Response
```

This is the foundation of more advanced AI applications.

---

## 12. Hallucination

An LLM can sometimes generate information that sounds correct but is actually incorrect.

This is commonly called a **hallucination**.

Example:

```text
User:
Who invented a fictional programming language called XYZ?

LLM:
XYZ was invented by John Smith in 1998.
```

The answer may sound confident even though the information is not real.

### Why does this happen?

An LLM generates text based on learned patterns and the available context.

It does not automatically guarantee that every generated statement is factually correct.

### How can we reduce hallucinations?

Common techniques include:

* Better prompts
* Providing reliable context
* Retrieval-Augmented Generation (RAG)
* Tool calling
* Structured outputs
* Validation
* Human verification

Later in our roadmap, these concepts will become very important.

---

## 13. LLM vs Traditional Program

A traditional program usually follows explicitly defined logic.

```text
Input
 ↓
Rules
 ↓
Output
```

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

The result is deterministic for the same input.

An LLM works differently:

```text
Input
 ↓
Model
 ↓
Generated Output
```

The output is generated based on the model's learned behavior and configuration.

---

## 14. LLM API

Instead of running a large model locally, an application can communicate with a model through an API.

Basic architecture:

```text
Python Application
       ↓
    API Request
       ↓
   LLM Provider
       ↓
      Model
       ↓
   API Response
       ↓
Python Application
```

For example:

```python
response = client.generate(
    "Explain RAG"
)

print(response)
```

The exact API syntax depends on the provider and SDK.

You will work with actual LLM APIs on Day 10.

---

## 15. LLM in Agentic AI

An LLM is often the reasoning and language component inside an AI agent.

A simplified agent can look like:

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Decide What To Do
 ↓
Tool
 ↓
Tool Result
 ↓
LLM
 ↓
Final Response
```

For example:

```text
User:
What is the weather in Dehradun?

Agent
 ↓
LLM decides that weather information is required
 ↓
Weather Tool
 ↓
Weather Result
 ↓
LLM
 ↓
Final Answer
```

This is different from simply asking an LLM a question.

The agent can interact with external tools and data.

---

## 16. Important Concepts to Remember

```text
LLM
→ Large Language Model

Token
→ Unit of text processed by the model

Context Window
→ Amount of context the model can handle

Training
→ Learning from training data

Inference
→ Using the trained model to generate output

Temperature
→ Controls output variation/randomness

Prompt
→ Instructions/input given to the model

Hallucination
→ Incorrect information generated by the model

LLM API
→ Interface for communicating with an LLM

Agent
→ System that can use an LLM with tools, context and actions
```

## 17. Connection to our Agentic AI Roadmap

Your Week 1 Python knowledge now connects to LLMs:

```text
Python
   ↓
Functions
   ↓
Classes
   ↓
Type Hints
   ↓
Pydantic
   ↓
JSON
   ↓
APIs
   ↓
LLM APIs
   ↓
Structured Outputs
   ↓
Tool Calling
   ↓
Agents
   ↓
RAG
   ↓
LangGraph
   ↓
MCP
```