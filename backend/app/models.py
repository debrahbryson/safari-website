from sqlalchemy import Column, Integer, String, Text, Float, Date, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .database import Base

class BookingStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class Tour(Base):
    __tablename__ = "tours"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(220), unique=True, index=True, nullable=False)
    park = Column(String(120), nullable=False)
    duration_days = Column(Integer, nullable=False)
    price_usd = Column(Float, nullable=False)
    rating = Column(Float, default=4.8)
    image_url = Column(String(500), default="")
    description = Column(Text, default="")
    highlights = Column(Text, default="")  # comma-separated
    max_group_size = Column(Integer, default=6)
    created_at = Column(DateTime, default=datetime.utcnow)
    bookings = relationship("Booking", back_populates="tour")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    tour_id = Column(Integer, ForeignKey("tours.id"), nullable=False)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(30), nullable=False)
    travel_date = Column(Date, nullable=False)
    guests = Column(Integer, nullable=False)
    notes = Column(Text, default="")
    status = Column(Enum(BookingStatus), default=BookingStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)
    tour = relationship("Tour", back_populates="bookings")
