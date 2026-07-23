"""Router layer for message endpoints."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.deps import get_current_user
from app.controllers.message_controller import MessageController
from app.schemas.message import MessageCreate, MessageOut
from app.models.user import User

router = APIRouter(prefix="/api/messages", tags=["messages"])


@router.post("", status_code=status.HTTP_201_CREATED)
def send_message(
    data: MessageCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return MessageController(db).send(user.id, data)


@router.get("/inbox", response_model=list[MessageOut])
def get_inbox(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return MessageController(db).inbox(user.id)
