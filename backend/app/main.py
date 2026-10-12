from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .seed import seed_if_empty
from .routers import tours, bookings

app = FastAPI(title="Safari Adventures API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tours.router)
app.include_router(bookings.router)

@app.on_event("startup")
def startup():
    seed_if_empty()

@app.get("/api/health")
def health():
    return {"status": "ok"}
