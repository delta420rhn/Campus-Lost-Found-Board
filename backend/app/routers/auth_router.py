"""Router layer for authentication endpoints. The router defines the URL,
HTTP method and status code, then delegates to the controller.
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.controllers.auth_controller import AuthController
from app.schemas.user import UserRegister, UserLogin, TokenResponse

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db)):
    return AuthController(db).register(data)


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    return AuthController(db).login(data)
