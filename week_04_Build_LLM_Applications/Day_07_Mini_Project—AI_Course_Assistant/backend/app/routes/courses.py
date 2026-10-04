from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.course import CourseOut
from app.services import course_service

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("", response_model=list[CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return course_service.get_all_courses(db)


@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = course_service.get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course