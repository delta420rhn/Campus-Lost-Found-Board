"""Service layer for messages. Enforces that a listing exists before a
message can be sent and shapes the inbox response.
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.message_repository import MessageRepository
from app.repositories.listing_repository import ListingRepository
from app.schemas.message import MessageCreate


class MessageService:
    def __init__(self, db: Session):
        self.messages = MessageRepository(db)
        self.listings = ListingRepository(db)

    def send(self, sender_id: int, data: MessageCreate):
        listing = self.listings.get_by_id(data.listing_id)
        if not listing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
        # Business rule: no point messaging yourself about your own listing.
        if listing.user_id == sender_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You cannot contact yourself on your own listing",
            )
        self.messages.create(sender_id, data.listing_id, data.body)
        return {"message": "Message sent"}

    def inbox(self, user_id: int):
        rows = self.messages.get_inbox_for_user(user_id)
        return [
            {
                "id": m.id,
                "listing_id": m.listing_id,
                "listing_title": m.listing.title,
                "sender_name": m.sender.name,
                "body": m.body,
                "sent_at": m.sent_at,
            }
            for m in rows
        ]
