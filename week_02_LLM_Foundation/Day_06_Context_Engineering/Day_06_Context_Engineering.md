# Week 02 — Day 06: Context Engineering

- What is Context?
- What is Context Engineering?
- Prompt Engineering vs Context Engineering
- Why is Context Important?
- Components of Context
- System Instructions
- User Request
- Conversation History
- Retrieved Context
- Tool Results
- Memory as Context
- Context Selection
- Context Relevance
- Context Ordering
- Context Formatting
- Context Window
- Token Usage
- Context Compression
- Context and RAG
- Context and Agents
- Static Context
- Dynamic Context
- Context Quality
- Context Engineering in Agentic AI
- Context Pipeline
- Context Engineering and Embeddings
- Context Engineering and Memory
- Context Engineering and Tool Calling
- Context Engineering vs Sending Everything

## 1. What is Context?

Context is the information provided to an LLM along with the user's request.

It can include:

* System instructions
* User request
* Conversation history
* Retrieved documents
* Tool results
* Memory
* Examples
* Structured data

Example:

```text
Instructions
+
User Request
+
Conversation History
+
Retrieved Information
+
Tool Results
+
Memory
        ↓
       LLM
```

---

## 2. What is Context Engineering?

Context engineering is the process of deciding:

* What information should be given to the LLM
* What information should not be given
* What information should be retrieved
* How information should be organized
* How much information should be included
* When information should be added or removed

Simple idea:

```text
Raw Information
      ↓
Select Relevant Information
      ↓
Organize Context
      ↓
LLM
      ↓
Response
```

---

## 3. Prompt Engineering vs Context Engineering

### Prompt Engineering

Focuses mainly on writing better instructions.

```text
Instruction
    ↓
LLM
```

Example:

```text
Explain dependency injection in simple English.
```

### Context Engineering

Focuses on the complete information available to the model.

```text
Instructions
+
User Information
+
Conversation History
+
Retrieved Data
+
Tool Results
+
Memory
      ↓
LLM
```

Prompt engineering focuses on **what the model should do**.

Context engineering focuses on **what information the model has available to do it**.

---

## 4. Why is Context Important?

LLMs generate responses using the information available in their context.

Poor context can cause:

* Irrelevant answers
* Missing information
* Confusion
* Incorrect assumptions
* Higher token usage

Good context provides:

* Relevant information
* Clear instructions
* Required history
* Useful tool results
* Correct structure

---

## 5. Components of Context

A context can contain:

```text
Context
├── System Instructions
├── User Request
├── Conversation History
├── Retrieved Documents
├── Tool Results
├── Memory
├── Examples
└── Structured Data
```

Not every application needs all of these.

The goal is to provide the information required for the current task.

---

## 6. System Instructions

System instructions define how the model should behave.

Example:

```text
You are a Java backend development assistant.
Explain concepts using simple examples.
```

They provide general rules and behavior for the model.

---

## 7. User Request

The user request is the main task that the model needs to solve.

Example:

```text
Explain dependency injection in Spring Boot.
```

A clear user request makes it easier to build useful context.

---

## 8. Conversation History

Previous messages can provide useful context.

Example:

```text
User:
I am learning Spring Boot.

Assistant:
Start with dependency injection.

User:
Explain dependency injection with an example.
```

History helps the model understand:

* What the user already knows
* What has already been discussed
* What the current request means

However, keeping too much history increases context size.

---

## 9. Retrieved Context

Applications can retrieve relevant information before calling the LLM.

Example:

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Relevant Chunks
      ↓
Context
      ↓
LLM
```

This connects context engineering with:

* Embeddings
* Semantic search
* Vector databases
* RAG

---

## 10. Tool Results

Agents can use tools to obtain information.

Example:

```text
User
 ↓
Agent
 ↓
Tool
 ↓
Tool Result
 ↓
Context
 ↓
LLM
```

Example tool result:

```text
Temperature = 25°C
City = Dehradun
```

The agent can add this information to the context before generating a response.

---

## 11. Memory as Context

Agents can retrieve relevant information from memory.

Example:

```text
Memory:
User is learning Java and Spring Boot.
```

Current question:

```text
What should I learn next?
```

The relevant memory can be added to the context.

```text
Current Question
+
Relevant Memory
      ↓
LLM
```

Only relevant memories should normally be included.

---

## 12. Context Selection

More context does not always mean better context.

Suppose an application has:

```text
10,000 documents
```

Sending all of them to the LLM is unnecessary.

Instead:

```text
10,000 Documents
       ↓
Retrieval
       ↓
Relevant Documents
       ↓
Context
       ↓
LLM
```

The goal is:

> Give the model the information it needs, not everything available.

---

## 13. Context Relevance

Context should be relevant to the task.

Question:

```text
How do I create a Spring Boot REST API?
```

Relevant information:

```text
Spring Boot
REST Controller
@GetMapping
@PostMapping
Request Mapping
```

Unnecessary information:

```text
Python syntax
Machine learning theory
Unrelated documentation
```

---

## 14. Context Ordering

The order of information can also be important.

A common structure is:

```text
Instructions
      ↓
User Request
      ↓
Relevant Context
      ↓
Tool Results
      ↓
Output Requirements
```

The exact structure depends on the application.

---

## 15. Context Formatting

Context should be clearly structured.

Instead of putting everything into one large block:

```text
Here is some information and here is the question...
```

use clear sections.

Example:

```text
SYSTEM:
You are a Java tutor.

CONTEXT:
Spring Boot uses dependency injection.

QUESTION:
What is dependency injection?

OUTPUT:
Explain using a simple example.
```

Structured context is easier to understand and manage.

---

## 16. Context Window

A context window is the maximum amount of information a model can process as context for a request.

Conceptually:

```text
Context Window
-------------------------
Instructions
Conversation
Retrieved Context
Tool Results
User Question
-------------------------
```

If too much information is included, the application can exceed the model's context limit.

---

## 17. Token Usage

Context consumes input tokens.

Larger context means:

* More input tokens
* Higher processing requirements
* Potentially higher cost
* Potentially higher latency

Therefore, applications should avoid unnecessary context.

---

## 18. Context Compression

Context compression means reducing the amount of context while keeping the important information.

Common techniques include:

* Summarization
* Filtering
* Removing duplicates
* Selecting relevant sections
* Retrieving only required chunks

Example:

```text
100 Messages
     ↓
Summary
     ↓
Important Information
     ↓
LLM
```

---

## 19. Context and RAG

RAG is an important application of context engineering.

Indexing:

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
```

Retrieval:

```text
User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Context
      ↓
LLM
      ↓
Answer
```

The retrieval step determines what information becomes context.

---

## 20. Context and Agents

Agents can dynamically build context while solving a task.

Example:

```text
User
 ↓
Agent
 ↓
Understand Task
 ↓
Retrieve Information
 ↓
Use Tool
 ↓
Receive Tool Result
 ↓
Update Context
 ↓
LLM
 ↓
Next Decision
```

The context can change during agent execution.

---

## 21. Static Context

Static context is information that normally remains fixed.

Examples:

* System instructions
* Agent rules
* Output format
* General behavior instructions

Example:

```text
You are a Java backend assistant.
Always explain using simple examples.
```

---

## 22. Dynamic Context

Dynamic context changes depending on the current task.

Examples:

* Retrieved documents
* Tool results
* Current user request
* Relevant memory
* API data

Example:

```text
User Question
      ↓
Retrieve Documents
      ↓
Get Tool Result
      ↓
Build Dynamic Context
      ↓
LLM
```

Agentic systems commonly use dynamic context.

---

## 23. Context Quality

Good context should be:

* Relevant
* Accurate
* Clear
* Sufficient
* Up-to-date
* Well structured

Bad context may contain:

* Irrelevant information
* Duplicate information
* Outdated information
* Conflicting information
* Too much information

---

## 24. Context Engineering in Agentic AI

Agents may interact with:

* Users
* Tools
* APIs
* Databases
* Memory
* Documents
* Other agents

All of these can produce information.

The agent needs to decide:

```text
What should enter the context?
What should be removed?
What should be summarized?
What should be retrieved?
What should be kept for later?
```

---

## 25. Context Pipeline

A practical context pipeline can look like:

```text
User Request
      ↓
Understand Task
      ↓
Retrieve Relevant Information
      ↓
Select Useful Memory
      ↓
Call Required Tools
      ↓
Filter Results
      ↓
Build Context
      ↓
LLM
      ↓
Response
```

---

## 26. Context Engineering and Embeddings

Embeddings help retrieve relevant information.

Example:

```text
User Query
    ↓
Embedding
    ↓
Similarity Search
    ↓
Relevant Information
    ↓
Context
    ↓
LLM
```

Therefore, embeddings can be one part of a context engineering pipeline.

---

## 27. Context Engineering and Memory

Memory can provide information from previous interactions.

Example:

```text
Stored Memories
      ↓
Retrieve Relevant Memory
      ↓
Add to Context
      ↓
LLM
```

The important part is selecting relevant memories instead of blindly adding everything.

---

## 28. Context Engineering and Tool Calling

Tools can provide new information during execution.

```text
Agent
  ↓
Tool Call
  ↓
Tool Result
  ↓
Filter Result
  ↓
Context
  ↓
LLM
```

Tool results should be relevant to the current task.

---

## 29. Context Engineering vs Sending Everything

Bad approach:

```text
All Documents
+
All History
+
All Memories
+
All Tool Results
      ↓
LLM
```

Better approach:

```text
Relevant Documents
+
Relevant History
+
Relevant Memory
+
Required Tool Results
      ↓
LLM
```

The goal is not maximum context.

The goal is **useful context**.

---

## Key Takeaway

Context engineering is about providing the **right information, in the right structure, at the right time** so that an LLM or agent can perform a task effectively.
