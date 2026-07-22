# System Design

## Architecture Overview
The Campus Lost & Found Board follows a standard three-tier web architecture: a frontend client, a backend server, and a database.

```
[Browser / Client]
       |
       | HTTP/HTTPS
       |
[Web Server / Backend API]
       |
       |
[Database]
```

---

## Frontend
The frontend is a web interface served to the browser. It handles all user interaction including the listing board, forms, search, and messaging UI.

- Technology: HTML, CSS, JavaScript (or React)
- Communicates with the backend via REST API calls
- Responsive design to support both desktop and mobile browsers

**Key Pages:**
- Home / Listing Board
- Listing Detail
- Post a Listing Form
- Login / Register
- User Profile / My Listings

---

## Backend
The backend is a REST API server that handles business logic, authentication, and database operations.

- Technology: Node.js with Express (or Django/Python)
- Handles routing, input validation, session management, and file uploads
- Returns JSON responses to the frontend

**Key API Routes (see 22-api-design.md for full details):**
- Auth: register, login, logout
- Listings: create, read, update, delete, resolve
- Messages: send message to poster

---

## Database
A relational database stores all persistent data.

- Technology: MySQL or PostgreSQL
- Three main tables: users, listings, messages
- See 21-database-design.md for schema details

---

## File Storage
Uploaded photos are stored either on the server's local file system or on a cloud storage service (e.g., Cloudinary or AWS S3). The database stores only the URL of the uploaded photo, not the file itself.

---

## Security
- Passwords are hashed using bcrypt before storage
- Sessions are managed using JWT tokens or server-side sessions with cookies
- All routes that modify data (post, edit, delete, message) require authentication
- Only the listing owner can edit, delete, or resolve their own listing

---

## Deployment (Planned)
- The app can be hosted on a platform like Render, Railway, or a VPS
- The database runs on the same server or a managed database service
- HTTPS is enforced using a TLS certificate
