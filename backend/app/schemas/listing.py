"""Pydantic schemas for listing requests and responses."""
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field


class ListingCreate(BaseModel):
    type: Literal["lost", "found"]
    title: str = Field(..., min_length=2, max_length=150)
    description: str = Field(..., min_length=2)
    category: str = Field(..., min_length=1, max_length=50)
    location: str = Field(..., min_length=1, max_length=100)
    photo_url: Optional[str] = Field(None, max_length=255)


class ListingUpdate(BaseModel):
    type: Optional[Literal["lost", "found"]] = None
    title: Optional[str] = Field(None, min_length=2, max_length=150)
    description: Optional[str] = Field(None, min_length=2)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    location: Optional[str] = Field(None, min_length=1, max_length=100)
    photo_url: Optional[str] = Field(None, max_length=255)


class ListingOut(BaseModel):
    id: int
    user_id: int
    type: str
    title: str
    description: str
    category: str
    location: str
    photo_url: Optional[str]
    status: str
    created_at: datetime
    owner_name: Optional[str] = None

    class Config:
        from_attributes = True
