SYSTEM_PROMPT = (
    "You are an AI course assistant. Answer only using the course information "
    "provided. If the information is not in the provided data, say you do not "
    "have that information. Keep answers clear and concise."
)


def format_course(course) -> str:
    return (
        f"Course: {course.name}\n"
        f"Level: {course.level}\n"
        f"Technology: {course.technology}\n"
        f"Duration: {course.duration} hours\n"
        f"Topics: {course.topics}\n"
        f"Description: {course.description}"
    )


def build_course_prompt(course_context: str, question: str) -> str:
    return f"""Course information:
    {course_context}

    User question:
    {question}

    Answer using the provided course information."""


def build_recommendation_prompt(
    goal: str, 
    level: str, 
    technology: str, 
    courses_context: str
    ) -> str:
    return f"""User profile:
    Goal: {goal}
    Experience level: {level}
    Preferred technology: {technology}

    Available courses:
    {courses_context}

    Recommend the most suitable course from the available courses.
    Explain briefly why it fits the user. Do not recommend courses that are not listed."""

def build_summary_prompt(course_context: str) -> str:
    return f"""Course information:
    {course_context}

    Write a short summary (3-4 sentences) of this course. Mention who it is for
    and the main skills the learner will gain."""