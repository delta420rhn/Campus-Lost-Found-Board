# Campus Lost & Found Board

A web app where university students post lost or found items, browse and search the board, contact a poster, and mark items as resolved once returned.

- **Frontend:** React 18 + Vite + React Router + Axios
- **Backend:** FastAPI in an MVC style (Router -> Controller -> Service -> Repository)
- **Database:** SQLAlchemy. SQLite for local dev, Postgres in production via `DATABASE_URL`
- **Auth:** JWT tokens, passwords hashed with bcrypt

---

## Project layout

```
Campus-Lost-Found-Board/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app, CORS, router wiring
│   │   ├── config.py            # settings from env
│   │   ├── database.py          # engine, session, Base
│   │   ├── models/              # SQLAlchemy models (User, Listing, Message)
│   │   ├── schemas/             # Pydantic request/response models
│   │   ├── routers/             # Router layer  (URLs, methods, status codes)
│   │   ├── controllers/         # Controller layer (thin, calls services)
│   │   ├── services/            # Service layer (business logic)
│   │   ├── repositories/        # Repository layer (database access only)
│   │   └── core/                # security (jwt, bcrypt) + auth dependency
│   ├── seed.py                  # sample users and listings
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── api/                 # axios client + one file per resource
    │   ├── context/             # AuthContext (login state)
    │   ├── components/          # Navbar, ListingCard, ProtectedRoute
    │   └── pages/               # Board, ListingDetail, PostListing, Login, Register, Profile, Inbox
    └── package.json
```

---

## Run it locally

You need two terminals, one for the API and one for the frontend.

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python seed.py                  # creates the database with sample data
uvicorn app.main:app --reload   # runs on http://127.0.0.1:8000
```

Interactive API docs are at `http://127.0.0.1:8000/docs`.

Seeded logins (password is `password123` for both):
- `amir@university.edu`
- `fatima@university.edu`

### 2. Frontend

```bash
cd frontend
npm install
echo "VITE_API_URL=http://127.0.0.1:8000" > .env
npm run dev                     # runs on http://127.0.0.1:5173
```

Open `http://127.0.0.1:5173` in the browser.

---

## Hosting on free services

The app is set up so deployment is only a few clicks. You will need your own free accounts because accounts cannot be created for you.

### Frontend on Vercel
1. Push this repo to your GitHub.
2. On Vercel, import the repo and set the **Root Directory** to `frontend`.
3. Add an environment variable `VITE_API_URL` pointing to your deployed backend URL.
4. Deploy. `frontend/vercel.json` already handles React Router routes.

### Backend on Render (recommended for FastAPI)
1. On Render, create a new **Web Service** from this repo and set the root to `backend`.
2. Render reads `backend/render.yaml`. It sets the build and start commands for you.
3. Set `CORS_ORIGINS` to your Vercel frontend URL.
4. For data that survives restarts, add a free Postgres database and set `DATABASE_URL` to its connection string. Without it the app uses SQLite, which resets when the free service sleeps.

The backend can also run on Vercel through `backend/vercel.json`, but Render keeps a normal always on process which suits FastAPI better on the free tier.

---

## API summary

Base URL: `/api`

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| POST | `/api/auth/register` | no | create an account |
| POST | `/api/auth/login` | no | log in, get a token |
| GET | `/api/listings` | no | list active listings, supports `?search=&category=&location=` |
| GET | `/api/listings/{id}` | no | one listing |
| GET | `/api/listings/mine` | yes | my listings, including resolved |
| POST | `/api/listings` | yes | create a listing |
| PUT | `/api/listings/{id}` | yes, owner | edit a listing |
| DELETE | `/api/listings/{id}` | yes, owner | delete a listing |
| PATCH | `/api/listings/{id}/resolve` | yes, owner | mark resolved |
| POST | `/api/messages` | yes | contact a poster |
| GET | `/api/messages/inbox` | yes | messages on my listings |

See `VIVA-GUIDE.md` for the full walk through used to answer the viva questions.
