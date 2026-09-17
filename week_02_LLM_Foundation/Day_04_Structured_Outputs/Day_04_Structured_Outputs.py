# Week 2 Day 4: Structured Outputs

# Coding Practice
# ==================================================
# PRACTICE QUESTIONS
# ==================================================

# 1. What is structured output?
# 2. Why is structured output useful?
# 3. What is JSON?
# 4. What is JSON Schema?
# 5. What is Pydantic?
# 6. What is validation?
# 7. What is a nested Pydantic model?
# 8. What is the difference between required and optional fields?
# 9. Why does structured output not guarantee factual correctness?
# 10. How is structured output useful in tool calling?
# 11. How is structured output useful in RAG?
# 12. How can FastAPI and Pydantic work together?

# ==================================================
# PRACTICE 1: BASIC PYDANTIC MODEL
# ==================================================

# Create a Candidate model with:

# name: str
# experience: int
# skills: list[str]

# Create an object and print its values.

# ==================================================
# PRACTICE 2: VALIDATE DATA
# ==================================================

# Create a Candidate model.

# Validate this data:

# data = {
# "name": "Rahul",
# "experience": 2,
# "skills": ["Python", "FastAPI"]
# }

# Print the validated object.

# ==================================================
# PRACTICE 3: HANDLE INVALID DATA
# ==================================================

# Use the Candidate model.

# Test it with:
# data = {
# "name": "Rahul",
# "experience": "hello",
# "skills": ["Python"]
# }

# Catch the Pydantic validation error.

# ==================================================
# PRACTICE 4: OPTIONAL FIELD
# ==================================================

# Create a Job model with:
# title: str
# company: str
# experience: int
# salary: float | None = None

# Create one Job without salary.

# Print the salary.

# ==================================================
# PRACTICE 5: NESTED MODEL
# ==================================================

# Create:

# Experience:
# years: int
# role: str

# Candidate:
# name: str
# experience: Experience
# skills: list[str]


# Create a Candidate object with nested experience.

# Print the nested values.

# ==================================================
# PRACTICE 6: LIST OF OBJECTS
# ==================================================

# Create:
# Job:
# title: str
# company: str

# JobList:

# jobs: list[Job]

# Validate a list containing two jobs.

# ==================================================
# PRACTICE 7: STRUCTURED RAG RESPONSE
# ==================================================

# Create a Pydantic model:

# class RAGResponse(BaseModel):
# answer: str
# sources: list[str]
# confidence: str

# Validate:

# response = {
# "answer": "The refund period is 30 days.",
# "sources": ["refund_policy.pdf"],
# "confidence": "high"
# }


# Print answer and sources.

# ==================================================
# PRACTICE 8: STRUCTURED TOOL ARGUMENTS
# ==================================================

# Create an EC2Request model with:

# instance_type: str
# region: str
# count: int

#

# Validate:
# tool_arguments = {
# "instance_type": "t3.micro",
# "region": "us-east-1",
# "count": 1
# }
#

# Print the validated values.