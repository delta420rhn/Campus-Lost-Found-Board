"""Router layer for listing endpoints."""
from typing import Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.deps import get_current_user
from app.controllers.listing_controller import ListingController
from app.schemas.listing import ListingCreate, ListingUpdate, ListingOut
from app.models.user import User

router = APIRouter(prefix="/api/listings", tags=["listings"])


@router.get("", response_model=list[ListingOut])
def get_listings(
    search: Optional[str] = None,
    category: Optional[str] = None,
    location: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return ListingController(db).list_active(search, category, location)


@router.get("/mine", response_model=list[ListingOut])
def get_my_listings(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return ListingController(db).mine(user.id)


@router.get("/{listing_id}", response_model=ListingOut)
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    return ListingController(db).get(listing_id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ListingOut)
def create_listing(
    data: ListingCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ListingController(db).create(user.id, data)


@router.put("/{listing_id}")
def update_listing(
    listing_id: int,
    data: ListingUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ListingController(db).update(listing_id, user.id, data)


@router.delete("/{listing_id}")
def delete_listing(
    listing_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ListingController(db).delete(listing_id, user.id)


@router.patch("/{listing_id}/resolve")
def resolve_listing(
    listing_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ListingController(db).resolve(listing_id, user.id)
