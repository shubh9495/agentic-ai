from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.prompts import course_prompts as prompts
from app.schemas.ai import (
    AIResponse,
    CourseQuestion,
    RecommendationRequest,
    SummarizeRequest,
)
from app.services import course_service
from app.services.llm_service import LLMServiceError, ask_llm, stream_llm

router = APIRouter(prefix="/ai", tags=["AI"])


def _get_course_or_404(db: Session, course_id: int):
    course = course_service.get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("/ask", response_model=AIResponse)
async def ask(request: CourseQuestion, db: Session = Depends(get_db)):
    course = _get_course_or_404(db, request.course_id)
    prompt = prompts.build_course_prompt(
        prompts.format_course(course), request.question
    )
    try:
        answer = await ask_llm(prompt)
    except LLMServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    return {"answer": answer}


@router.post("/ask/stream")
async def ask_stream(request: CourseQuestion, db: Session = Depends(get_db)):
    # Validate BEFORE streaming starts, so we can still return a proper 404
    course = _get_course_or_404(db, request.course_id)
    prompt = prompts.build_course_prompt(
        prompts.format_course(course), request.question
    )
    return StreamingResponse(stream_llm(prompt), media_type="text/plain")


@router.post("/recommend", response_model=AIResponse)
async def recommend(request: RecommendationRequest, db: Session = Depends(get_db)):
    courses = course_service.find_matching_courses(
        db, request.level, request.technology
    )
    if not courses:
        raise HTTPException(status_code=404, detail="No courses available")

    courses_context = "\n\n".join(prompts.format_course(c) for c in courses)
    prompt = prompts.build_recommendation_prompt(
        request.goal, request.level, request.technology, courses_context
    )
    try:
        answer = await ask_llm(prompt)
    except LLMServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    return {"answer": answer}


@router.post("/summarize", response_model=AIResponse)
async def summarize(request: SummarizeRequest, db: Session = Depends(get_db)):
    course = _get_course_or_404(db, request.course_id)
    prompt = prompts.build_summary_prompt(prompts.format_course(course))
    try:
        answer = await ask_llm(prompt)
    except LLMServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    return {"answer": answer}