"""Controller layer for messages."""
from sqlalchemy.orm import Session

from app.services.message_service import MessageService
from app.schemas.message import MessageCreate


class MessageController:
    def __init__(self, db: Session):
        self.service = MessageService(db)

    def send(self, sender_id: int, data: MessageCreate):
        return self.service.send(sender_id, data)

    def inbox(self, user_id: int):
        return self.service.inbox(user_id)
