"""FastAPI application entry point.

Wires together CORS, the database tables, and all routers. This file is the
composition root: it does not contain business logic, only setup.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import Base, engine
from app.routers import auth_router, listing_router, message_router

# Import models so SQLAlchemy registers all tables before create_all runs.
from app import models  # noqa: F401


def init_db():
    """Create tables and, if the database is empty, load sample data.

    Auto seeding matters on Vercel because the SQLite file lives in /tmp and is
    wiped on every cold start, so without this the board would show up empty.
    """
    Base.metadata.create_all(bind=engine)
    from app.database import SessionLocal
    from app.models import User, Listing, Message
    from app.core.security import hash_password

    db = SessionLocal()
    try:
        if db.query(User).count() > 0:
            return  # already has data, nothing to do

        amir = User(name="Amir Khan", email="amir@university.edu",
                    password_hash=hash_password("password123"))
        fatima = User(name="Fatima Noor", email="fatima@university.edu",
                      password_hash=hash_password("password123"))
        db.add_all([amir, fatima])
        db.commit()
        db.refresh(amir)
        db.refresh(fatima)

        db.add_all([
            Listing(user_id=fatima.id, type="found", title="Black car keys",
                    description="Found near the gym entrance on Monday evening. Has a red keychain.",
                    category="accessories", location="gym",
                    photo_url="https://images.unsplash.com/photo-1622560481979-f5b0174242a0?w=600"),
            Listing(user_id=amir.id, type="lost", title="Student ID card",
                    description="Lost my university ID card somewhere between the library and cafeteria.",
                    category="documents", location="library", photo_url=None),
            Listing(user_id=fatima.id, type="found", title="Blue water bottle",
                    description="Left in lecture hall B. Stainless steel, a few stickers on it.",
                    category="other", location="lecture-hall",
                    photo_url="https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600"),
            Listing(user_id=amir.id, type="lost", title="Wireless earbuds",
                    description="White earbuds in a small case, lost near the parking lot.",
                    category="electronics", location="parking",
                    photo_url="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600"),
        ])
        db.commit()
    finally:
        db.close()


# Build the schema and sample data. Wrapped so a transient error does not stop
# the whole function from booting.
try:
    init_db()
except Exception as exc:  # pragma: no cover
    print(f"init_db skipped: {exc}")

app = FastAPI(
    title="Campus Lost & Found Board API",
    description="REST API for reporting and recovering lost items on campus.",
    version="1.0.0",
)

# CORS. When CORS_ORIGINS is "*" we allow any origin. The frontend authenticates
# with a Bearer token in a header, not cookies, so credentials are not needed.
_origins = [o.strip() for o in settings.CORS_ORIGINS.split(",")]
_allow_all = _origins == ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if _allow_all else _origins,
    allow_credentials=not _allow_all,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(listing_router.router)
app.include_router(message_router.router)


@app.get("/")
def root():
    return {"status": "ok", "service": "Campus Lost & Found Board API"}


@app.get("/api/health")
def health():
    return {"status": "healthy"}
