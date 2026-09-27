from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.course import CourseCreate, CourseResponse
from app.services.course_service import (
    create_course,
    get_courses,
    get_course,
    update_course,
    delete_course
)


router = APIRouter()


@router.post("/", response_model=CourseResponse)
def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return create_course(db, course)


@router.get("/", response_model=list[CourseResponse])
def get_all_courses(
    db: Session = Depends(get_db)
):
    return get_courses(db)


@router.get("/{course_id}", response_model=CourseResponse)
def get_single_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = get_course(db, course_id)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course




@router.put("/{course_id}", response_model = CourseResponse)
def update_existing_course(
    course_id: int,
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    course = update_course(
        db,
        course_id,
        course_data
    )

    if not course:
        raise HTTPException(
            status_code= 404,
            detail="Course not found"
        )
    return course

@router.delete("/{courss_id}")
def delete_existing_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = delete_course(db, course_id)

    if not course:
        raise HTTPException(
            status_code = 404,
            detials = "Course not found"
        )

    return {
        "message": "Course deleted seccessfully"
    }