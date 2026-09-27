from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.schemas.user import UserCreate
from app.security.auth import hash_password
from fastapi import HTTPException

from app.schemas.user import UserLogin
from app.security.auth import (
    create_access_token,
    verify_password
)


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
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )
    return user


def get_user_by_email(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()


def authenticate_user(
    db: Session,
    user_data: UserLogin
):
    user = get_user_by_email(
        db,
        user_data.email
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub": str(user.id)
    })

    return token