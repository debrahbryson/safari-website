# Serengeti Trails — Safari Website

Full-stack safari booking site: **FastAPI** backend, **PostgreSQL** database, **React + Vite** frontend.

## Project Structure
```
safari-website/
├── docker-compose.yml        # PostgreSQL + API
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py           # FastAPI entrypoint
│       ├── config.py         # Settings (env-driven)
│       ├── database.py       # SQLAlchemy engine/session
│       ├── models.py         # Tour, Booking
│       ├── schemas.py        # Pydantic v2 schemas
│       ├── seed.py           # 6 seeded safari tours
│       └── routers/
│           ├── tours.py      # GET /api/tours, GET /api/tours/{slug}
│           └── bookings.py   # POST/GET /api/bookings, PATCH cancel
└── frontend/
    ├── package.json
    ├── vite.config.js        # proxies /api -> localhost:8000
    └── src/
        ├── App.jsx, main.jsx, api.js, index.css
        ├── components/ (Navbar, Hero, TourCard, BookingForm, Footer)
        └── pages/ (Home, Tours, TourDetail)
```

## Quick Start (Docker)

```bash
cd safari-website
docker compose up --build
```
- API: http://localhost:8000  (docs at /docs)
- Database auto-seeds with 6 tours on first start

## Frontend (dev mode)

```bash
cd frontend
npm install
npm run dev        # http://localhost:5173, /api proxied to :8000
```

## Run backend without Docker

```bash
# 1. Start PostgreSQL and create the DB, then:
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # adjust DATABASE_URL if needed
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | /api/tours | List tours (filters: `park`, `max_price`, `min_days`) |
| GET | /api/tours/{slug} | Tour detail |
| POST | /api/bookings | Create booking request |
| GET | /api/bookings/{id} | Booking status |
| PATCH | /api/bookings/{id}/cancel | Cancel booking |
| GET | /api/health | Health check |

## Next Steps
- Auth (JWT) for an admin panel to confirm/cancel bookings
- Alembic migrations
- Email/WhatsApp confirmation on booking (Twilio / SendGrid)
- Payment deposit via Stripe or Flutterwave (works well in TZ)
