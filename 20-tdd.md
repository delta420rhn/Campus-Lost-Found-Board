# Technical Design Document (TDD)

## 1. Overview
This document describes the technical decisions and design choices made for the Campus Lost & Found Board. It covers the tech stack, folder structure, data models, and key implementation details.

---

## 2. Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript (or React) |
| Backend | Node.js + Express (or Django) |
| Database | MySQL or PostgreSQL |
| File Storage | Local file system or Cloudinary |
| Authentication | JWT (JSON Web Tokens) |
| Password Hashing | bcrypt |
| Hosting | Render / Railway / VPS |

---

## 3. Folder Structure (Node.js Example)

```
campus-lost-found/
├── client/                  # Frontend code
│   ├── index.html
│   ├── css/
│   └── js/
├── server/                  # Backend code
│   ├── index.js             # Entry point
│   ├── routes/
│   │   ├── auth.js
│   │   ├── listings.js
│   │   └── messages.js
│   ├── controllers/
│   ├── models/
│   ├── middleware/
│   │   └── auth.js          # JWT verification
│   └── uploads/             # Uploaded photos
├── .env                     # Environment variables
└── package.json
```

---

## 4. Authentication Flow

1. User registers with name, email, password
2. Server hashes password using bcrypt and stores in database
3. User logs in; server verifies credentials and issues a JWT
4. JWT is stored in the browser (localStorage or cookie)
5. All protected routes require the JWT in the Authorization header
6. Server verifies JWT on each request using middleware

---

## 5. Listing Flow

1. Logged-in user submits post form (type, title, description, category, location, photo)
2. Server validates inputs and uploads photo to storage
3. Server saves listing record to database with user_id from JWT
4. Response returns new listing ID
5. Listing appears on main board immediately

---

## 6. Messaging Flow

1. User clicks "Contact Poster" on a listing
2. User types a message and submits
3. Server saves message to messages table with sender_id and listing_id
4. Poster can view received messages in their profile/inbox
5. Poster's email is never exposed to the sender

---

## 7. Key Design Decisions

**Why JWT over server sessions?**  
JWT allows the backend to be stateless, which is simpler to deploy and scale without needing a session store.

**Why a relational database?**  
The data has clear relationships (users own listings, listings receive messages) so a relational structure is a natural fit and easier to query.

**Why not a full mobile app?**  
A responsive web app covers the same audience without the overhead of building and distributing a native app. Students can access it from their phone browser.
