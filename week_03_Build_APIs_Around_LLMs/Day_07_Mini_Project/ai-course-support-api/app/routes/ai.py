from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.course import Course

from app.schemas.ai import AIQuestion, AIResponse
from app.security.auth import get_current_user

from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)

from app.services.ai_services import (
    recommend_courses,
    ask_course_question    
)

router = APIRouter()

@router.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend(
    request: RecommendationRequest
):
    result = recommend_courses(
        goal=request.goal,
        current_skills=request.current_skills,
        experience=request.experience
    )

    return {
        "goal": request.goal,
        **result
    }


@router.post(
    "/ask",
    response_model=AIResponse
)
def ask_course(
    request: AIQuestion,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    course = db.query(Course).filter(
        Course.id == request.course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    answer = ask_course_question(
        course_name=course.name,
        course_level=course.level,
        course_description=course.description,
        question=request.question
    )

    return {
        "answer": answer
    }