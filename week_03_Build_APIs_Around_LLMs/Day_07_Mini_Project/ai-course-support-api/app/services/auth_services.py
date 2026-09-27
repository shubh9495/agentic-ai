from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.security.auth import hash_password

def create_user(
        db: Session,
        user_data: UserCreate
):
    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        email = user_data.email,
        hashed_password = hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user