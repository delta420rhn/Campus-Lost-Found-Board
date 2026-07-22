# Functional Requirements

## FR-01: User Registration
The system must allow new users to register using a name, email address, and password. Email addresses must be unique. A success message or redirect must follow successful registration.

## FR-02: User Login
The system must authenticate users using their email and password. The system must reject invalid credentials with an appropriate error message.

## FR-03: User Logout
The system must allow logged-in users to end their session at any time.

## FR-04: Create a Listing
The system must allow logged-in users to create a listing by selecting the type (Lost or Found), entering a title, description, category, and campus location, and optionally uploading a photo. All fields except photo must be required.

## FR-05: View Listings
The system must display all active (unresolved) listings on the main board. Each listing must show the type, title, photo (if provided), category, location, and date posted. This page must be accessible to guests (users who are not logged in).

## FR-06: Search Listings
The system must allow users to search listings by keyword. The search must match against the listing title and description.

## FR-07: Filter Listings
The system must allow users to filter listings by category and by campus location. Filters can be combined with a keyword search.

## FR-08: Edit a Listing
The system must allow the creator of a listing to edit any field of their listing. Other users must not be able to edit listings they did not create.

## FR-09: Delete a Listing
The system must allow the creator of a listing to delete it. The system must ask for confirmation before deletion.

## FR-10: Contact Poster
The system must allow logged-in users to send a message to the poster of a listing. The message must be delivered to the poster without exposing the poster's contact details publicly.

## FR-11: Mark as Resolved
The system must allow the creator of a listing to mark it as resolved. Resolved listings must be hidden from the main board but remain accessible in the user's posting history.

## FR-12: View Own Listings
The system must allow logged-in users to view all listings they have created, including resolved ones, through a profile or dashboard page.
