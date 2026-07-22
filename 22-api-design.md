# API Design

## Base URL
`/api`

All responses are in JSON format. Protected routes require a valid JWT in the `Authorization: Bearer <token>` header.

---

## Authentication

### POST /api/auth/register
Register a new user.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@university.edu",
  "password": "securepassword"
}
```

**Response (201):**
```json
{
  "message": "Account created successfully"
}
```

---

### POST /api/auth/login
Log in with email and password.

**Request Body:**
```json
{
  "email": "john@university.edu",
  "password": "securepassword"
}
```

**Response (200):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": { "id": 1, "name": "John Doe" }
}
```

---

## Listings

### GET /api/listings
Get all active listings. Supports optional query parameters.

**Query Params:** `?search=keys&category=accessories&location=gym`

**Response (200):**
```json
[
  {
    "id": 5,
    "type": "found",
    "title": "Black keys",
    "category": "accessories",
    "location": "gym",
    "photo_url": "/uploads/keys.jpg",
    "created_at": "2026-06-15T10:00:00Z"
  }
]
```

---

### GET /api/listings/:id
Get a single listing by ID.

**Response (200):**
```json
{
  "id": 5,
  "type": "found",
  "title": "Black keys",
  "description": "Found near the gym entrance.",
  "category": "accessories",
  "location": "gym",
  "photo_url": "/uploads/keys.jpg",
  "status": "active",
  "created_at": "2026-06-15T10:00:00Z"
}
```

---

### POST /api/listings
Create a new listing. **Protected.**

**Request Body (multipart/form-data):**
- type, title, description, category, location, photo (optional)

**Response (201):**
```json
{
  "id": 6,
  "message": "Listing created"
}
```

---

### PUT /api/listings/:id
Edit an existing listing. **Protected. Owner only.**

**Request Body:** Any fields to update

**Response (200):**
```json
{
  "message": "Listing updated"
}
```

---

### DELETE /api/listings/:id
Delete a listing. **Protected. Owner only.**

**Response (200):**
```json
{
  "message": "Listing deleted"
}
```

---

### PATCH /api/listings/:id/resolve
Mark a listing as resolved. **Protected. Owner only.**

**Response (200):**
```json
{
  "message": "Listing marked as resolved"
}
```

---

## Messages

### POST /api/messages
Send a message to a listing's poster. **Protected.**

**Request Body:**
```json
{
  "listing_id": 5,
  "body": "Hi, I think I lost those keys. Can we meet?"
}
```

**Response (201):**
```json
{
  "message": "Message sent"
}
```

---

### GET /api/messages/inbox
Get all messages received by the logged-in user. **Protected.**

**Response (200):**
```json
[
  {
    "id": 1,
    "listing_id": 5,
    "listing_title": "Black keys",
    "sender_name": "Amir",
    "body": "Hi, I think I lost those keys.",
    "sent_at": "2026-06-15T11:00:00Z"
  }
]
```
