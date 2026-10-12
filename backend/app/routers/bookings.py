from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Booking, Tour, BookingStatus
from ..schemas import BookingCreate, BookingOut

router = APIRouter(prefix="/api/bookings", tags=["bookings"])

@router.post("", response_model=BookingOut, status_code=201)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    tour = db.get(Tour, payload.tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    if payload.guests > tour.max_group_size:
        raise HTTPException(status_code=400,
                            detail=f"Max group size for this tour is {tour.max_group_size}")
    booking = Booking(**payload.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.get("/{booking_id}", response_model=BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    b = db.get(Booking, booking_id)
    if not b:
        raise HTTPException(status_code=404, detail="Booking not found")
    return b

@router.patch("/{booking_id}/cancel", response_model=BookingOut)
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    b = db.get(Booking, booking_id)
    if not b:
        raise HTTPException(status_code=404, detail="Booking not found")
    b.status = BookingStatus.cancelled
    db.commit()
    db.refresh(b)
    return b
