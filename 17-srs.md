# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
This document specifies the software requirements for the Campus Lost & Found Board, a web application that helps university students report, search for, and recover lost items on campus.

### 1.2 Scope
The system is a web-based platform accessible from any modern browser. It allows students to post lost or found item listings, search and filter the board, contact posters, and mark items as resolved.

### 1.3 Definitions
- **Listing:** A post created by a user describing a lost or found item
- **Poster:** The user who created a listing
- **Guest:** A user who is not logged in
- **Resolved:** A listing status indicating the item has been returned

---

## 2. Overall Description

### 2.1 Product Perspective
The system is a standalone web application. It does not integrate with any external university systems in this version. It uses its own user database and does not rely on university SSO.

### 2.2 User Classes
- **Students:** The main users. They register, post listings, search the board, and contact each other.
- **Guests:** Users who browse without logging in. They can view and search listings but cannot post or send messages.

### 2.3 Assumptions and Dependencies
- Users have access to a modern web browser and internet connection
- Image uploads are stored on the server or a cloud file storage service
- There is no admin panel in this version

---

## 3. Functional Requirements

See 13-functional-requirements.md for the full list (FR-01 through FR-12).

---

## 4. Non-Functional Requirements

See 14-non-functional-requirements.md for the full list (NFR-01 through NFR-08).

---

## 5. System Constraints
- The platform must be accessible on mobile browsers without a native app
- No payment or shipping functionality will be included
- All item exchanges happen in person on campus
- The system will not expose user email addresses or phone numbers to other users

---

## 6. External Interface Requirements

### 6.1 User Interface
- Web-based, responsive layout
- Main board page, listing detail page, post form, login/register pages, and profile page

### 6.2 Communication Interfaces
- HTTPS for all traffic
- Email notifications for new messages (optional in first version)
