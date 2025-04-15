from pydantic import BaseModel
from datetime import datetime

class BuchungRequest(BaseModel):
    user_id: int
    vehicle_id: int
    start: datetime
    end: datetime

class BuchungResponse(BaseModel):
    success: bool
    message: str
