from app.database import Base, engine, SessionLocal
from app.models.course import Course

COURSES = [
    {
        "name": "FastAPI Backend Development",
        "level": "Beginner",
        "technology": "Python",
        "duration": 30,
        "topics": "HTTP, REST APIs, FastAPI, Pydantic, SQLAlchemy, PostgreSQL",
        "description": "Build production-style REST APIs with FastAPI, validate data with Pydantic and store it with SQLAlchemy and PostgreSQL.",
    },
    {
        "name": "Python Fundamentals",
        "level": "Beginner",
        "technology": "Python",
        "duration": 25,
        "topics": "Syntax, Data Types, Functions, OOP, File Handling, Error Handling",
        "description": "Learn core Python from scratch, including functions, object-oriented programming and file handling.",
    },
    {
        "name": "React Frontend Development",
        "level": "Beginner",
        "technology": "JavaScript",
        "duration": 28,
        "topics": "JSX, Components, Props, State, Hooks, Fetching Data",
        "description": "Build interactive user interfaces with React using components, hooks and API calls.",
    },
    {
        "name": "Advanced Backend Architecture",
        "level": "Advanced",
        "technology": "Python",
        "duration": 40,
        "topics": "Async Python, Caching, Message Queues, Docker, Microservices",
        "description": "Design scalable backend systems with async programming, caching, queues and containers.",
    },
    {
        "name": "Building LLM Applications",
        "level": "Intermediate",
        "technology": "Python",
        "duration": 35,
        "topics": "LLM SDKs, Prompt Templates, Streaming, Function Calling, RAG Basics",
        "description": "Integrate LLMs into backend applications using prompts, streaming and function calling.",
    },
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Course).count() == 0:
            db.add_all([Course(**c) for c in COURSES])
            db.commit()
            print(f"Seeded {len(COURSES)} courses.")
        else:
            print("Courses already exist. Skipping seed.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()