# Entity Relationship Diagram (ERD)

## Entities and Attributes

### User
| Field | Type | Notes |
|-------|------|-------|
| id | INT | Primary Key, auto increment |
| name | VARCHAR(100) | Required |
| email | VARCHAR(150) | Required, unique |
| password_hash | VARCHAR(255) | Required |
| created_at | DATETIME | Auto set on creation |

### Listing
| Field | Type | Notes |
|-------|------|-------|
| id | INT | Primary Key, auto increment |
| user_id | INT | Foreign Key → User.id |
| type | ENUM('lost', 'found') | Required |
| title | VARCHAR(150) | Required |
| description | TEXT | Required |
| category | VARCHAR(50) | Required |
| location | VARCHAR(100) | Required |
| photo_url | VARCHAR(255) | Optional |
| status | ENUM('active', 'resolved') | Default: active |
| created_at | DATETIME | Auto set on creation |

### Message
| Field | Type | Notes |
|-------|------|-------|
| id | INT | Primary Key, auto increment |
| sender_id | INT | Foreign Key → User.id |
| listing_id | INT | Foreign Key → Listing.id |
| body | TEXT | Required |
| sent_at | DATETIME | Auto set on creation |

---

## Relationships

- A **User** can create many **Listings** (one-to-many)
- A **Listing** belongs to one **User**
- A **User** can send many **Messages** (one-to-many)
- A **Message** belongs to one **Listing** and one sender **User**
- A **Listing** can have many **Messages**

---

## ERD Diagram (Text Representation)

```
User (1) ──────────< Listing (many)
User (1) ──────────< Message (many)
Listing (1) ───────< Message (many)
```
