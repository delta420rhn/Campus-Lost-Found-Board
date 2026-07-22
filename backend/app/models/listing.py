"""Listing SQLAlchemy model. Maps to the `listings` table."""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    type = Column(String(10), nullable=False)          # 'lost' or 'found'
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=False, index=True)
    location = Column(String(100), nullable=False, index=True)
    photo_url = Column(String(255), nullable=True)
    status = Column(String(10), nullable=False, default="active", index=True)  # 'active' or 'resolved'
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="listings")
    messages = relationship("Message", back_populates="listing", cascade="all, delete-orphan")
