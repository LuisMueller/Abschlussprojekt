from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, index=True)
    model = Column(String(100), nullable=False)
    location = Column(String(100))
    seats = Column(Integer)
    vehiclestatus = Column(String(20), default="verfügbar")

    bookings = relationship("Booking", back_populates="vehicle")


class Booking(Base):
    __tablename__ = "buchung"

    booking_id = Column(Integer, primary_key=True, index=True)
    bookingstart = Column(DateTime, nullable=False)
    bookingend = Column(DateTime, nullable=False)
    passenger = Column(Integer)
    destination = Column(String(100))
    reason = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    vehicles_id = Column(Integer, ForeignKey("vehicles.vehicle_id"), nullable=False)

    vehicle = relationship("Vehicle", back_populates="bookings")
