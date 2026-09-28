"""
Week 04 — Day 01: LLM Application Architecture
Practice + Interview Questions
Uncomment one question/task at a time and solve it.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is an LLM application?
Answer:
An LLM application is a software application that uses an LLM
as one of its components to perform language-based tasks.

Q2. Is an LLM application the same as an LLM?
Answer:
No.
An LLM is the model, while an LLM application includes the
model along with application logic, APIs, data, prompts,
validation, and other components.

Q3. What is the role of the backend in an LLM application?
Answer:
The backend handles request validation, authentication,
context retrieval, prompt construction, LLM calls,
response processing, and database operations.

Q4. Why do we need a backend between the frontend and LLM?
Answer:
The backend protects API keys, handles business logic,
validates requests, retrieves data, and controls communication
with the LLM.

Q5. What is context in an LLM application?
Answer:
Context is relevant information provided to the LLM along
with the user's request so it can generate a more useful response.

Q6. Why should LLM responses be validated?
Answer:
LLM output is generated rather than deterministically produced
by traditional application logic. Validation helps ensure that
the output follows the expected structure and rules.

Q7. What is the difference between a traditional application and an LLM application?
Answer:
A traditional application primarily follows explicitly programmed
rules, while an LLM application also uses a language model to
generate or understand information.

Q8. What are the main layers of a basic LLM application?
Answer:
Frontend/UI
Backend/API
Prompt + Context
LLM
Response Processing

Q9. What can the backend do in an LLM application?
Answer:
It can validate requests, authenticate users, retrieve data,
build prompts, call the LLM, process responses, and return
API responses.

Q10. Why should API keys not be placed in the frontend?
Answer:
Because sensitive API keys could be exposed to users.
The backend should communicate with the LLM provider.

Q11. What is the purpose of the context/data layer?
Answer:
It provides relevant information such as database records,
user profiles, and previous conversations to the LLM.

Q12. What are common LLM application patterns?
Answer:
Question answering
Summarization
Classification
Information extraction
Recommendation
Conversational AI

Q13. What is the difference between an LLM and an LLM API?
Answer:
An LLM is the language model itself.
An LLM API is the interface through which an application
communicates with the model.

Q14. Why is architecture important in LLM applications?
Answer:
A reliable application needs more than an LLM API call.
It also needs validation, authentication, data retrieval,
prompt management, error handling, security, logging,
database integration, and monitoring.

Q15. Where do tools and agents fit into an LLM application?
Answer:
An agent can use an LLM to decide what action to take,
call a tool, receive the tool result, and then generate
a final answer.
"""

# ============================================================
# CODING PRACTICE
# ============================================================

# Q16. Create a simple FastAPI endpoint /chat that accepts
# a user message and returns a response.
# Expected flow:
# User -> /chat -> Build prompt -> Call LLM -> Return response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    prompt = f"You are an AI assistant.\nUser: {request.message}"
    # Replace this with an actual LLM API call.
    response = f"Generated response for: {request.message}"
    return {"answer": response}


# Q17. Create a function that builds a prompt using
# system instructions, user input, and context.

def build_prompt_q17(system_instruction, user_message, context):
    return f"""
System:
{system_instruction}
Context:
{context}
User:
{user_message}
"""

# prompt_demo = build_prompt_q17(
#     "You are an AI course assistant.",
#     "What should I learn for backend development?",
#     "Available courses: Python, FastAPI, Java, Spring Boot"
# )
# print(prompt_demo)


# Q18. Create a Pydantic response model for an LLM recommendation.
# Expected fields: recommendation, reason

class RecommendationResponseQ18(BaseModel):
    recommendation: str
    reason: str


# Q19. Validate an LLM response using the Pydantic model.

# response_raw = {
#     "recommendation": "FastAPI",
#     "reason": "Useful for building Python backend APIs."
# }
# validated_response = RecommendationResponseQ18(**response_raw)
# print(validated_response)
# print(validated_response.model_dump())


# Q20. Create a simple course retrieval function.
# The function should receive a list of courses and return
# courses related to the user's query.

courses_list = [
    "Python Fundamentals",
    "FastAPI",
    "Machine Learning",
    "Deep Learning",
    "Java Spring Boot"
]

def find_courses(query, courses):
    query = query.lower()
    return [course for course in courses if query in course.lower()]

# result_courses = find_courses("python", courses_list)
# print(result_courses)


# Q21. Build a simple LLM application flow using functions.
# Required functions:
# - validate_request()
# - retrieve_context()
# - build_prompt()
# - call_llm()
# - process_response()

def validate_request(message):
    if not message.strip():
        raise ValueError("Message cannot be empty")
    return message

def retrieve_context():
    return [
        "Python Fundamentals",
        "FastAPI",
        "Machine Learning"
    ]

def build_prompt_flow(message, context):
    return f"""
You are an AI course advisor.
User:
{message}
Available courses:
{context}
Recommend a suitable course.
"""

def call_llm(prompt):
    # Replace this with an actual LLM API call.
    return "Start with Python Fundamentals."

def process_response(response):
    return {"recommendation": response}

# message_input = "I want to learn Python for AI."
# message_validated = validate_request(message_input)
# ctx = retrieve_context()
# prmt = build_prompt_flow(message_validated, ctx)
# llm_res = call_llm(prmt)
# final_output = process_response(llm_res)
# print(final_output)


# Q22. Create a FastAPI endpoint for an AI course assistant.
# Expected architecture:
# Frontend -> FastAPI -> Retrieve Context -> Build Prompt -> LLM -> Validate Response -> Return JSON

class CourseRequest(BaseModel):
    message: str

class CourseResponse(BaseModel):
    recommendation: str

def retrieve_courses_q22():
    return [
        "Python Fundamentals",
        "Machine Learning",
        "Deep Learning",
        "FastAPI"
    ]

def build_prompt_q22(message, courses):
    return f"""
You are an AI course advisor.
User:
{message}
Available courses:
{courses}
Recommend a suitable learning path.
"""

def call_llm_q22(prompt):
    # Replace this with an actual LLM API call.
    return "Start with Python Fundamentals, then Machine Learning."

@app.post("/recommend", response_model=CourseResponse)
def recommend(request: CourseRequest):
    courses = retrieve_courses_q22()
    prompt = build_prompt_q22(request.message, courses)
    response = call_llm_q22(prompt)
    return CourseResponse(recommendation=response)


# Q23. Design the architecture of an AI Course Assistant.
"""
Answer:
User -> React Frontend -> FastAPI Backend -> Authentication -> Course Retrieval -> Prompt Construction -> LLM -> Response Validation -> React Frontend
"""

# Q24. Separate the following responsibilities into appropriate application layers:
"""
Answer:
Frontend:
- User interaction
Backend / API:
- Request validation
Service layer:
- Prompt construction
- LLM call
- Business logic
Database layer:
- Database access
Response processing:
- Response validation
"""

# Q25. Write the complete conceptual flow of a production-style LLM application.
"""
Answer:
User -> Frontend -> Backend API -> Authentication -> Request Validation -> Context Retrieval -> Prompt Construction -> LLM -> Response Validation -> Business Logic -> API Response -> Frontend -> User
"""

# ============================================================
# MINI PRACTICE PROJECT
# ============================================================

# Q26. Build a simple AI Course Assistant.
# Requirements:
# 1. Create a FastAPI application.
# 2. Create a POST /recommend endpoint.
# 3. Accept a user message.
# 4. Store a small list of courses.
# 5. Retrieve the available courses.
# 6. Build a prompt.
# 7. Create a placeholder LLM function.
# 8. Return a structured response.

project_app = FastAPI()

stored_courses = [
    "Python Fundamentals",
    "FastAPI",
    "Machine Learning",
    "Deep Learning",
    "Java Spring Boot"
]

class RecommendationRequest(BaseModel):
    message: str

class RecommendationResponse(BaseModel):
    recommendation: str

def build_project_prompt(message, courses):
    return f"""
You are an AI course advisor.
User wants:
{message}
Available courses:
{courses}
Recommend a suitable learning path.
"""

def call_project_llm(prompt):
    # Replace this placeholder with a real LLM API call.
    return "Start with Python Fundamentals, then Machine Learning."

@project_app.post("/recommend-project", response_model=RecommendationResponse)
def recommend_project(request: RecommendationRequest):
    prompt = build_project_prompt(request.message, stored_courses)
    response = call_project_llm(prompt)
    return RecommendationResponse(recommendation=response)

# ============================================================
# FINAL REVISION QUESTIONS
# ============================================================

"""
Q27. Complete the architecture:
User -> Frontend -> Backend -> Prompt + Context -> LLM -> Response Processing -> User

Q28. Complete the mental model:
LLM = Brain
Backend = Application Logic
Database = Persistent Data
Prompt = Instructions + Context
Frontend = User Interaction

Q29. What should happen before returning an LLM response when a specific output structure is expected?
Answer:
The response should be validated and processed before returning it to the client.

Q30. Why should an LLM application provide only relevant context to the model?
Answer:
Only relevant context should be provided because unnecessary context can increase cost and reduce useful context.
"""