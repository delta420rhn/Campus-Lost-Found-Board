"""Pydantic schemas for message requests and responses."""
from datetime import datetime
from pydantic import BaseModel, Field


class MessageCreate(BaseModel):
    listing_id: int
    body: str = Field(..., min_length=1)


class MessageOut(BaseModel):
    id: int
    listing_id: int
    listing_title: str
    sender_name: str
    body: str
    sent_at: datetime

    class Config:
        from_attributes = True
