from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import FRONTEND_ORIGIN
from app.database import Base, engine
from app.models import course as course_model 
from app.routes import ai, courses

Base.metadata.create_all(bind=engine)
from app.seed import seed
seed()

app = FastAPI(title="AI Course Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(courses.router)
app.include_router(ai.router)


@app.get("/health")
def health():
    return {"status": "ok"}