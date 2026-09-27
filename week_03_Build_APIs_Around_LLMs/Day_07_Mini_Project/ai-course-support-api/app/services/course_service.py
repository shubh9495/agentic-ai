from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate

def get_courses(db: Session):
    return db.query(Course).all()


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(
        Course.id == course_id
    ).first()


def create_course(db: Session, course_data: CourseCreate):
    course = Course(
        name=course_data.name,
        level=course_data.level,
        description=course_data.description
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course

def update_course(
        db:Session,
        course_id: int,
        course_data: CourseCreate
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        return None
    
    course_name = course_data.name
    course.level = course_data.level
    course.description = course_data.description

    db.commit()
    db.refresh(course)

    return course

def delete_course(db:Session, course_id:int):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        return None

    db.delete(course)
    db.commit()

    return course