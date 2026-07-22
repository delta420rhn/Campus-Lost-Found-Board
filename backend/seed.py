"""Seed the database with sample users and listings for demos and the viva.

Run:  python seed.py
Login for either seeded user with password: password123
"""
from app.database import Base, engine, SessionLocal
from app.models import User, Listing, Message
from app.core.security import hash_password

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Start clean so re-seeding is idempotent.
db.query(Message).delete()
db.query(Listing).delete()
db.query(User).delete()
db.commit()

amir = User(name="Amir Khan", email="amir@university.edu", password_hash=hash_password("password123"))
fatima = User(name="Fatima Noor", email="fatima@university.edu", password_hash=hash_password("password123"))
db.add_all([amir, fatima])
db.commit()
db.refresh(amir)
db.refresh(fatima)

listings = [
    Listing(user_id=fatima.id, type="found", title="Black car keys",
            description="Found near the gym entrance on Monday evening. Has a red keychain.",
            category="accessories", location="gym",
            photo_url="https://images.unsplash.com/photo-1622560481979-f5b0174242a0?w=600"),
    Listing(user_id=amir.id, type="lost", title="Student ID card",
            description="Lost my university ID card somewhere between the library and cafeteria.",
            category="documents", location="library",
            photo_url=None),
    Listing(user_id=fatima.id, type="found", title="Blue water bottle",
            description="Left in lecture hall B. Stainless steel, a few stickers on it.",
            category="other", location="lecture-hall",
            photo_url="https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600"),
    Listing(user_id=amir.id, type="lost", title="Wireless earbuds",
            description="White earbuds in a small case, lost near the parking lot.",
            category="electronics", location="parking",
            photo_url="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600"),
]
db.add_all(listings)
db.commit()

# A sample message so the inbox demo has data.
db.refresh(listings[0])
db.add(Message(sender_id=amir.id, listing_id=listings[0].id,
               body="Hi, those might be my keys! Can we meet at the gym tomorrow?"))
db.commit()

print("Seeded:")
print(f"  users:    {db.query(User).count()}")
print(f"  listings: {db.query(Listing).count()}")
print(f"  messages: {db.query(Message).count()}")
print("Login with amir@university.edu / password123  (or fatima@university.edu)")
db.close()
