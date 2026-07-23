"""Service layer for listings. Holds ownership checks and the rules
for creating, editing, deleting and resolving listings.
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.listing_repository import ListingRepository
from app.schemas.listing import ListingCreate, ListingUpdate


class ListingService:
    def __init__(self, db: Session):
        self.repo = ListingRepository(db)

    def _to_out(self, listing):
        """Attach the owner's name for the response model."""
        data = {c.name: getattr(listing, c.name) for c in listing.__table__.columns}
        data["owner_name"] = listing.owner.name if listing.owner else None
        return data

    def list_active(self, search=None, category=None, location=None):
        listings = self.repo.get_active(search, category, location)
        return [self._to_out(l) for l in listings]

    def get(self, listing_id: int):
        listing = self.repo.get_by_id(listing_id)
        if not listing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
        return self._to_out(listing)

    def list_for_user(self, user_id: int):
        return [self._to_out(l) for l in self.repo.get_by_user(user_id)]

    def create(self, user_id: int, data: ListingCreate):
        listing = self.repo.create(user_id, data.model_dump())
        return self._to_out(listing)

    def _get_owned(self, listing_id: int, user_id: int):
        """Fetch a listing and enforce that the caller owns it."""
        listing = self.repo.get_by_id(listing_id)
        if not listing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
        if listing.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only modify your own listings",
            )
        return listing

    def update(self, listing_id: int, user_id: int, data: ListingUpdate):
        listing = self._get_owned(listing_id, user_id)
        changes = {k: v for k, v in data.model_dump().items() if v is not None}
        self.repo.update(listing, changes)
        return {"message": "Listing updated"}

    def delete(self, listing_id: int, user_id: int):
        listing = self._get_owned(listing_id, user_id)
        self.repo.delete(listing)
        return {"message": "Listing deleted"}

    def resolve(self, listing_id: int, user_id: int):
        listing = self._get_owned(listing_id, user_id)
        self.repo.update(listing, {"status": "resolved"})
        return {"message": "Listing marked as resolved"}
