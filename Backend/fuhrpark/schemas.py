from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BuchungRequest(BaseModel):
    user_id: int
    vehicle_id: int
    start: datetime
    end: datetime

class BuchungResponse(BaseModel):
    success: bool
    message: str

#so soll die buchung am ende im JSON schema aussehen
class BuchungInfo(BaseModel):
    booking_id: int
    user_id: int
    vehicle_id: int
    bookingstart: datetime
    bookingend: datetime
    passenger: int
    destination: str
    reason: str

    class Config:
        from_attributes = True

class BuchungsUpdate(BaseModel):
    bookingstart: Optional[datetime] = None
    bookingend: Optional[datetime] = None
    passenger: Optional[int] = None
    destination: Optional[str] = None
    reason: Optional[str] = None