"""Repository layer for listings. All listing database access lives here."""
from sqlalchemy.orm import Session

from app.models.listing import Listing


class ListingRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_active(self, search=None, category=None, location=None):
        """Return active listings, optionally filtered by keyword/category/location."""
        query = self.db.query(Listing).filter(Listing.status == "active")

        if search:
            like = f"%{search}%"
            query = query.filter(
                (Listing.title.ilike(like)) | (Listing.description.ilike(like))
            )
        if category:
            query = query.filter(Listing.category == category)
        if location:
            query = query.filter(Listing.location == location)

        return query.order_by(Listing.created_at.desc()).all()

    def get_by_id(self, listing_id: int) -> Listing | None:
        return self.db.query(Listing).filter(Listing.id == listing_id).first()

    def get_by_user(self, user_id: int):
        return (
            self.db.query(Listing)
            .filter(Listing.user_id == user_id)
            .order_by(Listing.created_at.desc())
            .all()
        )

    def create(self, user_id: int, data: dict) -> Listing:
        listing = Listing(user_id=user_id, **data)
        self.db.add(listing)
        self.db.commit()
        self.db.refresh(listing)
        return listing

    def update(self, listing: Listing, data: dict) -> Listing:
        for key, value in data.items():
            setattr(listing, key, value)
        self.db.commit()
        self.db.refresh(listing)
        return listing

    def delete(self, listing: Listing) -> None:
        self.db.delete(listing)
        self.db.commit()
