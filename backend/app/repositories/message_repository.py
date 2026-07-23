"""Repository layer for messages. All message database access lives here."""
from sqlalchemy.orm import Session

from app.models.message import Message


class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, sender_id: int, listing_id: int, body: str) -> Message:
        message = Message(sender_id=sender_id, listing_id=listing_id, body=body)
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_inbox_for_user(self, user_id: int):
        """Return messages sent to listings owned by the given user."""
        from app.models.listing import Listing
        return (
            self.db.query(Message)
            .join(Listing, Message.listing_id == Listing.id)
            .filter(Listing.user_id == user_id)
            .order_by(Message.sent_at.desc())
            .all()
        )
