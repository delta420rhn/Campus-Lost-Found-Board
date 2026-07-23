"""Controller layer for listings."""
from sqlalchemy.orm import Session

from app.services.listing_service import ListingService
from app.schemas.listing import ListingCreate, ListingUpdate


class ListingController:
    def __init__(self, db: Session):
        self.service = ListingService(db)

    def list_active(self, search=None, category=None, location=None):
        return self.service.list_active(search, category, location)

    def get(self, listing_id: int):
        return self.service.get(listing_id)

    def mine(self, user_id: int):
        return self.service.list_for_user(user_id)

    def create(self, user_id: int, data: ListingCreate):
        return self.service.create(user_id, data)

    def update(self, listing_id: int, user_id: int, data: ListingUpdate):
        return self.service.update(listing_id, user_id, data)

    def delete(self, listing_id: int, user_id: int):
        return self.service.delete(listing_id, user_id)

    def resolve(self, listing_id: int, user_id: int):
        return self.service.resolve(listing_id, user_id)
