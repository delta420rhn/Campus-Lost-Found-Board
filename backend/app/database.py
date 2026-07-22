"""Database engine, session factory and declarative base.

This is the single place where the SQLAlchemy connection is configured.
The repository layer is the only layer that talks to the session.
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

# Work out the real database URL. On Vercel the filesystem is read only except
# for /tmp, so a SQLite file has to live there or the function crashes on boot.
DATABASE_URL = settings.DATABASE_URL
if DATABASE_URL.startswith("sqlite") and os.environ.get("VERCEL"):
    DATABASE_URL = "sqlite:////tmp/campus_lost_found.db"

# SQLite needs a special flag when used with a threaded server like uvicorn.
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a DB session and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
