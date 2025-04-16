import sys
import os
from fastapi import APIRouter, HTTPException
from fuhrpark.schemas import BuchungRequest, BuchungResponse
from fuhrpark.crud import buche_fahrzeug

router = APIRouter(
    prefix="/buchung",
    tags=["Buchung"]
)



@router.post("/", response_model=BuchungResponse)
def buchung_absenden(buchung: BuchungRequest):
    # Tuple entpacken
    success, message = buche_fahrzeug(
        user_id=buchung.user_id,
        vehicle_id=buchung.vehicle_id,
        start=buchung.start,
        end=buchung.end
    )

    # Wenn es kein Erfolg war, wirf eine HTTP-Fehlermeldung mit dem Text
    if not success:
        raise HTTPException(status_code=400, detail=message)

    # Wenn alles gut dann gib ein valides Response zurück
    return BuchungResponse(success=True, message=message)
