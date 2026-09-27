from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate,UserLogin, UserResponse
from app.services.auth_services import create_user, authenticate_user
from app.security.auth import get_current_user

router = APIRouter()


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    access_token = authenticate_user(
        db,
        user
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user = Depends(get_current_user)
):
    return current_user