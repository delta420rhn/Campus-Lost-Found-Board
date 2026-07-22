# Data Flow Diagram (DFD)

## Level 0 – Context Diagram

At the highest level, the system has two types of users: Students and the System itself. Students send data into the system (listings, messages, searches) and receive data back (listings, search results, messages).

```
[Student] ----> [Campus Lost & Found System] ----> [Student]
```

External entities: Student (poster), Student (searcher/claimer)  
The system stores data in a database and handles all communication between users.

---

## Level 1 – Main Processes

### Process 1: User Management
- Input: Registration details (name, email, password), login credentials
- Output: Session token, error messages
- Data store: Users table

### Process 2: Listing Management
- Input: Listing data (type, title, description, category, location, photo)
- Output: Listing ID, updated board
- Data store: Listings table, Photos storage

### Process 3: Search and Filter
- Input: Keyword, category filter, location filter
- Output: Filtered list of matching listings
- Data store: Listings table

### Process 4: Messaging
- Input: Message text, sender ID, listing ID
- Output: Message delivered to poster
- Data store: Messages table

### Process 5: Resolve Listing
- Input: Listing ID, user confirmation
- Output: Listing status updated to resolved
- Data store: Listings table

---

## Data Stores
- **Users** – stores user accounts (id, name, email, hashed password, created_at)
- **Listings** – stores all listings (id, user_id, type, title, description, category, location, photo_url, status, created_at)
- **Messages** – stores contact messages (id, sender_id, listing_id, message_body, sent_at)

---

## Data Flows Summary

| Flow | From | To | Data |
|------|------|----|------|
| Registration | Student | Process 1 | Name, email, password |
| Login | Student | Process 1 | Email, password |
| Post listing | Student | Process 2 | Listing data + photo |
| View board | Student | Process 3 | (query) |
| Search | Student | Process 3 | Keyword, filters |
| Send message | Student | Process 4 | Message text |
| Mark resolved | Student | Process 5 | Listing ID |
