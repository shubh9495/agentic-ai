from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User
from app.models.course import Course
from app.routes import courses, auth


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Course Support API"
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(
    courses.router,
    prefix="/courses",
    tags=["Course"]
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)