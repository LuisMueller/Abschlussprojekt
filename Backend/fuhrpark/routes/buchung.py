import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "Backend"))
from fastapi import APIRouter, HTTPException
from schemas import BuchungRequest, BuchungResponse
#from fuhrpark.crud import buche_fahrzeug

router = APIRouter(
    prefix="/buchung",
    tags=["Buchung"]
)



@router.post("/", response_model=BuchungResponse)
def buchung_absenden(buchung: BuchungRequest):
    result = buche_fahrzeug(
        user_id=buchung.user_id,
        vehicle_id=buchung.vehicle_id,
        start=buchung.start,
        end=buchung.end
    )

    if "Fehler" in result or "nicht verfügbar" in result:
        raise HTTPException(status_code=400, detail=result)

    return BuchungResponse(message=result)
