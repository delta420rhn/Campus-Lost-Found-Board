"""Pydantic schemas for user requests and responses."""
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    token: str
    user: UserPublic
