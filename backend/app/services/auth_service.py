"""Service layer for authentication. Holds the business rules for
registering and logging in: uniqueness checks, hashing, token creation.
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserRegister, UserLogin


class AuthService:
    def __init__(self, db: Session):
        self.users = UserRepository(db)

    def register(self, data: UserRegister):
        # Business rule: email must be unique.
        if self.users.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists",
            )
        password_hash = hash_password(data.password)
        self.users.create(name=data.name, email=data.email, password_hash=password_hash)
        return {"message": "Account created successfully"}

    def login(self, data: UserLogin):
        user = self.users.get_by_email(data.email)
        # Business rule: reject unknown email or wrong password with the same error.
        if not user or not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        token = create_access_token(user.id)
        return {"token": token, "user": {"id": user.id, "name": user.name}}
