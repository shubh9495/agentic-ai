# Week 04 — Day 06: LLM Application Patterns

## Points Covered

* What are LLM Application Patterns?
* Why Application Patterns are Useful
* Text Generation
* Summarization
* Classification
* Information Extraction
* Question Answering
* Recommendation
* Translation
* Sentiment Analysis
* Content Generation
* Structured Output in LLM Applications
* Combining Multiple Patterns
* Choosing the Right Pattern
* LLM Pattern vs Traditional Programming
* Combining LLMs with Application Logic
* Common Mistakes
---

# 1. What are LLM Application Patterns?

An **LLM application pattern** is a common way of using an LLM to solve a specific type of problem.

For example:

```text
User Text
    ↓
   LLM
    ↓
  Summary
```

This is a **summarization pattern**.

Another example:

```text
User Text
    ↓
   LLM
    ↓
 Category
```

This is a **classification pattern**.

Common LLM application patterns include:

```text
Summarization
Classification
Information Extraction
Question Answering
Recommendation
Translation
Content Generation
Sentiment Analysis
```

---

# 2. Why are Application Patterns Useful?

Instead of treating every LLM application as completely different, we can recognize common patterns.

For example:

```text
AI Resume Analyzer
AI Customer Support
AI Course Assistant
AI News Summarizer
AI Email Assistant
```

These applications may look different, but internally they can use similar LLM patterns.

For example:

```text
Resume Analyzer
→ Information Extraction
→ Classification
→ Recommendation

Customer Support
→ Question Answering
→ Classification

News App
→ Summarization
→ Classification
```

Understanding these patterns helps you design LLM applications faster.

---

# 3. Text Generation

The simplest LLM application pattern is **text generation**.

The user provides an instruction and the LLM generates new text.

Example:

```text
User:
Write a short introduction about Python.

        ↓

LLM

        ↓

Generated Text
```

Common uses:

* Blog writing
* Email generation
* Product descriptions
* Documentation
* Social media content
* Code generation

---

# 4. Summarization

**Summarization** means converting a large amount of information into a shorter version while preserving important points.

Example:

```text
Long Article
     ↓
    LLM
     ↓
 Short Summary
```

Example prompt:

```text
Summarize this article in 5 bullet points.
```

A simple implementation can look like:

```python
def summarize(text: str):
    prompt = f"""
    Summarize the following text in 5 bullet points:

    {text}
    """

    return call_llm(prompt)
```

Common uses:

* News summarization
* Meeting summaries
* Document summaries
* Research paper summaries
* Email summaries

---

# 5. Classification

**Classification** means assigning input to one or more predefined categories.

Example:

```text
User Message
     ↓
    LLM
     ↓
  Category
```

Suppose a customer sends:

```text
"My payment failed."
```

The LLM can classify it as:

```text
payment_issue
```

Other categories could be:

```text
technical_issue
billing_issue
account_issue
general_question
```

Example:

```python
def classify_message(message: str):
    prompt = f"""
    Classify this customer message.

    Categories:
    - billing
    - technical
    - account
    - general

    Message:
    {message}
    """

    return call_llm(prompt)
```

Classification is useful for routing user requests to the correct part of an application.

---

# 6. Information Extraction

**Information extraction** means extracting specific information from unstructured text.

Example:

```text
Input:
"John has 5 years of Python experience
and currently works at ABC Technologies."
```

Extract:

```text
Name: John
Experience: 5 years
Skill: Python
Company: ABC Technologies
```

Flow:

```text
Unstructured Text
       ↓
      LLM
       ↓
Structured Information
```

Common uses:

* Resume parsing
* Invoice processing
* Contract analysis
* Document processing
* Entity extraction

Example:

```python
def extract_resume_info(resume: str):
    prompt = f"""
    Extract the following information:

    - Name
    - Skills
    - Experience
    - Education

    Resume:
    {resume}
    """

    return call_llm(prompt)
```

For production applications, structured output or schema validation should be used instead of relying only on plain text formatting.

---

# 7. Question Answering

**Question answering** means using an LLM to answer a user's question based on provided information or knowledge.

Basic flow:

```text
Question
   ↓
  LLM
   ↓
 Answer
```

Example:

```text
User:
What is FastAPI?

LLM:
FastAPI is a Python framework for building APIs.
```

Real applications often need answers based on specific data.

For example:

```text
User Question
      ↓
Relevant Context
      ↓
     LLM
      ↓
    Answer
```

This becomes especially important in **RAG applications**.

---

# 8. Recommendation

A recommendation application uses an LLM to suggest something based on user requirements.

Example:

```text
User:
"I am a beginner and want to learn backend development using Python."

        ↓

       LLM

        ↓

Recommendation:
FastAPI
PostgreSQL
SQLAlchemy
REST APIs
```

Flow:

```text
User Preferences
      ↓
     LLM
      ↓
Recommendation
```

Recommendations can be based on:

* User goals
* Experience
* Preferences
* Available options
* Context

Example:

```python
def recommend_course(goal: str, level: str):
    prompt = f"""
    Recommend a suitable course.

    Goal:
    {goal}

    Level:
    {level}
    """

    return call_llm(prompt)
```

For high-quality recommendations, applications often combine LLM reasoning with actual databases, retrieval, or ranking logic rather than relying only on the model's internal knowledge.

---

# 9. Translation

LLMs can translate text between languages.

Example:

```text
English:
"How are you?"

      ↓
     LLM
      ↓

Hindi:
"आप कैसे हैं?"
```

Example:

```python
def translate(text: str, language: str):
    prompt = f"""
    Translate the following text into {language}.

    Text:
    {text}
    """

    return call_llm(prompt)
```

Applications include:

* Multilingual chatbots
* Localization
* Document translation
* Customer support

---

# 10. Sentiment Analysis

**Sentiment analysis** determines the emotional or opinion-based tone of text.

Example:

```text
"I really liked this product."

        ↓

     Positive
```

Another example:

```text
"The application keeps crashing."

        ↓

      Negative
```

A simple classification could be:

```text
positive
negative
neutral
```

Flow:

```text
Text
 ↓
LLM
 ↓
Sentiment
```

Applications:

* Product reviews
* Customer feedback
* Social media analysis
* Customer support monitoring

---

# 11. Content Generation

Content generation uses an LLM to create new content based on instructions.

Examples:

```text
Generate an email
Generate a blog post
Generate product description
Generate code
Generate documentation
Generate interview questions
```

Example:

```python
def generate_email(topic: str):
    prompt = f"""
    Write a professional email about:

    {topic}
    """

    return call_llm(prompt)
```

Flow:

```text
Instruction
    ↓
   LLM
    ↓
Generated Content
```

---

# 12. Structured Output in LLM Applications

LLMs normally generate text.

But applications often need structured data.

For example:

```text
User:
"John has 5 years of Python experience."
```

The application may need:

```json
{
    "name": "John",
    "experience": 5,
    "skill": "Python"
}
```

Structured output is useful for:

* Databases
* APIs
* Application logic
* Validation
* Automation

General flow:

```text
User Input
    ↓
   LLM
    ↓
Structured Output
    ↓
Validation
    ↓
Application
```

This connects directly with the **Structured Outputs** topic from Week 02.

---

# 13. Combining Multiple Patterns

Real-world LLM applications often use multiple patterns together.

For example, an **AI Resume Analyzer** might use:

```text
Resume
  ↓
Information Extraction
  ↓
Classification
  ↓
Skill Comparison
  ↓
Recommendation
  ↓
Final Report
```

An AI customer support system might use:

```text
Customer Message
      ↓
Classification
      ↓
Question Answering
      ↓
Recommendation / Action
      ↓
Final Response
```

This is how simple LLM capabilities become complete applications.

---

# 14. Example: AI Course Assistant

Your Week 03 project and Week 04 capstone direction can use several patterns.

User:

```text
"I am a beginner and want to learn backend
development with Python."
```

The application can perform:

```text
User Request
      ↓
Classification
      ↓
Understand User Goal
      ↓
Course Retrieval
      ↓
Recommendation
      ↓
LLM
      ↓
Final Answer
```

For course questions:

```text
User Question
      ↓
Question Answering
      ↓
Course Context
      ↓
LLM
      ↓
Answer
```

For course summaries:

```text
Course Content
      ↓
Summarization
      ↓
Short Summary
```

One application can therefore contain multiple LLM patterns.

---

# 15. Choosing the Right Pattern

Start with the actual problem.

| Problem                             | Suitable Pattern       |
| ----------------------------------- | ---------------------- |
| Make a short version of a document  | Summarization          |
| Determine message category          | Classification         |
| Extract information from a resume   | Information Extraction |
| Answer a question                   | Question Answering     |
| Suggest a course                    | Recommendation         |
| Convert text to another language    | Translation            |
| Determine positive/negative opinion | Sentiment Analysis     |
| Create an email                     | Content Generation     |

The important question is:

```text
"What does my application need the LLM to do?"
```

Then choose the appropriate pattern.

---

# 16. LLM Pattern vs Traditional Programming

Some tasks are better handled using normal application logic.

For example:

```text
Calculate:
100 + 200
```

You do not necessarily need an LLM.

Python can do it directly:

```python
result = 100 + 200
```

But:

```text
"Explain why the price increased
and summarize the customer's complaint."
```

An LLM can be useful because the task involves natural language understanding and generation.

A good application uses:

```text
LLM
+
Traditional Code
```

rather than using an LLM for everything.

---

# 17. Combining LLMs with Application Logic

A strong LLM application usually separates responsibilities.

Example:

```text
User
 ↓
FastAPI
 ↓
Validate Input
 ↓
Application Logic
 ↓
LLM
 ↓
Process Result
 ↓
Database / API
 ↓
Response
```

For example:

```text
LLM
→ Understand user request

Python
→ Calculate price

Database
→ Store course information

LLM
→ Explain result to user
```

Each component performs the task it is best suited for.

---

# 18. Common Mistakes

## Mistake 1: Using an LLM for everything

Not every task requires an LLM.

Use normal code for deterministic operations when possible.

---

## Mistake 2: Treating generated text as automatically reliable

LLM output can contain errors.

Validate important outputs before using them.

---

## Mistake 3: Ignoring structured output

If your application needs predictable data, use structured outputs and validation instead of parsing arbitrary text.

---

## Mistake 4: Sending unnecessary context

Only send information relevant to the task.

This can reduce:

* Token usage
* Cost
* Latency
* Noise

---

## Mistake 5: Building everything as one large prompt

Large applications should separate:

```text
Prompt Logic
Application Logic
Database Logic
API Logic
```

This makes the system easier to maintain.

---