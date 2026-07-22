# Use Cases

## UC-01: Register Account

**Actor:** Guest (unauthenticated user)  
**Precondition:** User does not have an account  
**Main Flow:**
1. User opens the registration page
2. User enters name, email, and password
3. User submits the form
4. System validates the input and checks that email is not already registered
5. System creates the account and redirects the user to the main board

**Alternative Flow:**  
- If the email is already registered, the system shows an error and asks the user to log in instead

---

## UC-02: Post a Listing

**Actor:** Logged-in student  
**Precondition:** User is authenticated  
**Main Flow:**
1. User clicks "Post a Listing"
2. User selects type: Lost or Found
3. User fills in title, description, category, and location
4. User optionally uploads a photo
5. User submits the form
6. System saves the listing and displays it on the main board

**Alternative Flow:**  
- If required fields are missing, the system shows validation errors and does not submit

---

## UC-03: Search and Filter Listings

**Actor:** Any user (guest or logged-in)  
**Precondition:** At least one active listing exists  
**Main Flow:**
1. User opens the main board
2. User types a keyword in the search bar
3. User optionally selects a category or location filter
4. System returns matching listings

**Alternative Flow:**  
- If no listings match the criteria, the system displays a "No results found" message

---

## UC-04: Contact a Poster

**Actor:** Logged-in student  
**Precondition:** User is logged in and a relevant listing exists  
**Main Flow:**
1. User opens a listing
2. User clicks "Contact Poster"
3. User writes and submits a message
4. System delivers the message to the poster's inbox or email

**Alternative Flow:**  
- If the user is not logged in, the system redirects them to the login page before allowing contact

---

## UC-05: Mark Listing as Resolved

**Actor:** Listing owner  
**Precondition:** User is logged in and owns the listing  
**Main Flow:**
1. User opens their listing
2. User clicks "Mark as Resolved"
3. System asks for confirmation
4. User confirms
5. System sets the listing status to resolved and removes it from the active board
