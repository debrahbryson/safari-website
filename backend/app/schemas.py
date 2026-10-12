from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional

class TourBase(BaseModel):
    title: str
    park: str
    duration_days: int
    price_usd: float
    rating: float = 4.8
    image_url: str = ""
    description: str = ""
    highlights: str = ""
    max_group_size: int = 6

class TourCreate(TourBase):
    slug: str

class TourOut(TourBase):
    id: int
    slug: str
    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    tour_id: int
    full_name: str = Field(min_length=2, max_length=150)
    email: EmailStr
    phone: str = Field(min_length=5, max_length=30)
    travel_date: date
    guests: int = Field(ge=1, le=20)
    notes: Optional[str] = ""

class BookingOut(BookingCreate):
    id: int
    status: str
    created_at: datetime
    class Config:
        from_attributes = True
