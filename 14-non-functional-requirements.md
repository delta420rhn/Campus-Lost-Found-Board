# Non-Functional Requirements

## NFR-01: Performance
The main board must load within 3 seconds on a standard mobile connection. Search results must appear within 2 seconds of submitting a query.

## NFR-02: Usability
The interface must be simple enough for any student to use without instructions. The key actions (post, search, contact) must be reachable within 2 clicks from the home page. The layout must be mobile-friendly and work on small screens.

## NFR-03: Reliability
The system must be available at least 95% of the time. Data must not be lost during normal use. If a listing submission fails, the user must be notified and the form data must be preserved so they do not have to retype it.

## NFR-04: Security
User passwords must be stored using a secure hashing method (e.g., bcrypt). Sessions must expire after a reasonable period of inactivity. Only the listing owner must be able to edit or delete their own listings. Contact messages must be routed through the system without exposing user email addresses.

## NFR-05: Scalability
The system must handle at least 500 concurrent users without degradation in performance. The database must support growth in listings over time without requiring major changes.

## NFR-06: Maintainability
The codebase must be organized in a clear folder structure. Functions and components must be kept small and focused. Code must include comments where the logic is not obvious.

## NFR-07: Compatibility
The platform must work correctly on modern browsers including Chrome, Firefox, Safari, and Edge. It must be usable on both desktop and mobile screen sizes without a separate mobile app.

## NFR-08: Privacy
The platform must not expose personal user data such as email addresses or phone numbers to other users. Contact between users must happen only through the in-app messaging system.
