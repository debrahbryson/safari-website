from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from ..database import get_db
from ..models import Tour
from ..schemas import TourOut

router = APIRouter(prefix="/api/tours", tags=["tours"])

@router.get("", response_model=list[TourOut])
def list_tours(park: Optional[str] = None, max_price: Optional[float] = None,
               min_days: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(Tour)
    if park:
        q = q.filter(Tour.park.ilike(f"%{park}%"))
    if max_price is not None:
        q = q.filter(Tour.price_usd <= max_price)
    if min_days is not None:
        q = q.filter(Tour.duration_days >= min_days)
    return q.order_by(Tour.price_usd).all()

@router.get("/{slug}", response_model=TourOut)
def get_tour(slug: str, db: Session = Depends(get_db)):
    tour = db.query(Tour).filter(Tour.slug == slug).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    return tour
