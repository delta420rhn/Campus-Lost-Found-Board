# Database Design

## Database: MySQL / PostgreSQL

---

## Table: users

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## Table: listings

```sql
CREATE TABLE listings (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  type ENUM('lost', 'found') NOT NULL,
  title VARCHAR(150) NOT NULL,
  description TEXT NOT NULL,
  category VARCHAR(50) NOT NULL,
  location VARCHAR(100) NOT NULL,
  photo_url VARCHAR(255),
  status ENUM('active', 'resolved') DEFAULT 'active',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

---

## Table: messages

```sql
CREATE TABLE messages (
  id INT PRIMARY KEY AUTO_INCREMENT,
  sender_id INT NOT NULL,
  listing_id INT NOT NULL,
  body TEXT NOT NULL,
  sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE
);
```

---

## Indexes

```sql
-- Speed up search by listing status
CREATE INDEX idx_listings_status ON listings(status);

-- Speed up filtering by category
CREATE INDEX idx_listings_category ON listings(category);

-- Speed up filtering by location
CREATE INDEX idx_listings_location ON listings(location);

-- Speed up message lookup by listing
CREATE INDEX idx_messages_listing ON messages(listing_id);
```

---

## Notes
- Passwords are never stored in plain text. Only the bcrypt hash is saved.
- Photo URLs point to the file storage location, not the raw file.
- Deleting a user cascades and removes their listings and messages.
- Deleting a listing cascades and removes associated messages.
