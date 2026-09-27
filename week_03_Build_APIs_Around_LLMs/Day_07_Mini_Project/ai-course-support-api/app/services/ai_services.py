from google import genai
from google.genai import types

from app.config import settings

import json

client = genai.Client(
    api_key=settings.LLM_API_KEY
)

def ask_llm(question: str):

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=question
        )
        return response.text
    except Exception:
        raise Exception(
            "Failed to get response from LLM"
        )


def recommend_courses(
    goal:str,
    current_skills: list[str],
    experience: str
):
    prompt = f"""
You are a course recommendation assistant.

User goal:
{goal}

Current skills:
{", ".join(current_skills)}

Experience:
{experience}

Recommend suitable courses for this learner.

Return ONLY valid JSON.

The JSON must have exactly this structure:

{{
    "recommendations": [
        {{
            "course": "course name",
            "reason": "why this course is suitable"
        }}
    ],
    "next_steps": [
        "step 1",
        "step 2",
        "step 3"
    ]
}}

Important:
- "next_steps" must be outside "recommendations".
- Each recommendation must contain only "course" and "reason".
- "next_steps" must be a list of strings.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )

        return json.loads(response.text)
    except Exception:
            raise Exception(
                "Failed to get response from LLM"
            )


def ask_course_question(
    course_name: str,
    course_level: str,
    course_description: str,
    question: str
):
    prompt = f"""
You are an AI course support assistant.

Course:
{course_name}

Level:
{course_level}

Description:
{course_description}

Student question:
{question}

Answer the student's question using the course information provided above.

If the information is not enough to answer the question,
say that the information is not available in the course description.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text