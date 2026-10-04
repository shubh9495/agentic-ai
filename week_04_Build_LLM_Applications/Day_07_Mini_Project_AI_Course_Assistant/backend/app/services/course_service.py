from sqlalchemy.orm import Session

from app.models.course import Course


def get_all_courses(db: Session) -> list[Course]:
    return db.query(Course).order_by(Course.id).all()


def get_course_by_id(db: Session, course_id: int) -> Course | None:
    return db.query(Course).filter(Course.id == course_id).first()


def find_matching_courses(db: Session, level: str, technology: str) -> list[Course]:
    """Send only RELEVANT courses to the LLM, not the whole table."""
    matches = (
        db.query(Course)
        .filter(Course.level.ilike(level), Course.technology.ilike(technology))
        .all()
    )
    if matches:
        return matches

    # Fallback: match on technology only
    matches = db.query(Course).filter(Course.technology.ilike(technology)).all()
    if matches:
        return matches

    # Last fallback: all courses (the table is small in this project)
    return get_all_courses(db)