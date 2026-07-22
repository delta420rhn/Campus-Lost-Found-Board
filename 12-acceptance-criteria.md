# Acceptance Criteria

## US-01 – Register an account
- User can enter their name, email, and password on the registration page
- If the email is already registered, an error message is shown
- After successful registration, the user is redirected to the main board

## US-02 – Log in
- User can enter their email and password to log in
- If credentials are wrong, an error message is shown
- After successful login, the user sees the main board and their name in the header

## US-03 – Log out
- A logout button is visible when the user is logged in
- Clicking logout ends the session and redirects to the home page

## US-04 – Post a Lost listing
- The post form includes fields for: title, description, category (dropdown), campus location, and photo upload
- All fields except photo are required; if a required field is missing, an error is shown
- After submission, the listing appears on the main board marked as "Lost"

## US-05 – Post a Found listing
- Same form fields as US-04
- After submission, the listing appears on the main board marked as "Found"

## US-06 – Edit a listing
- The poster can click Edit on their own listing
- Changes are saved and reflected immediately on the board
- Other users cannot edit listings they did not create

## US-07 – Delete a listing
- The poster can delete their own listing
- A confirmation prompt appears before deletion
- After deletion, the listing is removed from the board

## US-08 – Browse listings without login
- The main board is visible to guests (not logged in)
- Guests can view all active listings but cannot post or send messages

## US-09 – Search by keyword
- A search bar is visible on the main board
- Entering a keyword filters listings by title and description in real time or on submit

## US-10 – Filter by category and location
- Dropdown filters for category and campus location are available
- Selecting a filter narrows the listings shown without clearing the search keyword

## US-11 – Contact poster
- A "Contact Poster" button appears on each listing for logged-in users
- Clicking it opens a message form
- The message is sent to the poster; the poster's email or phone is not shown publicly

## US-12 – Mark as resolved
- The poster sees a "Mark as Resolved" button on their own listing
- Clicking it changes the listing status to resolved and hides it from the active board
- The listing can still be viewed by the poster in their profile history
