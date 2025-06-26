import sys
import os
from fastapi import APIRouter, HTTPException, Path
from fuhrpark.schemas import BuchungRequest, BuchungResponse, BuchungInfo, BuchungsUpdate
from fuhrpark.crud import buche_fahrzeug, get_all_buchungen, get_filtered_buchungen, update_buchung, delete_buchung
from typing import List
from fastapi import Query
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

# from fuhrpark.crud import get_all_buchungen

router = APIRouter(
    prefix="/buchung",
    tags=["Buchung"]
)



@router.post("/", response_model=BuchungResponse)
def buchung_absenden(buchung: BuchungRequest):
    success, message = buche_fahrzeug(
        user_id=buchung.user_id,
        vehicle_id=buchung.vehicle_id,
        start=buchung.start,
        end=buchung.end,
        destination=buchung.destination,
        reason=buchung.reason
    )

    # Wenn es kein Erfolg war, wirf eine HTTP-Fehlermeldung mit dem Text
    if not success:
        raise HTTPException(status_code=400, detail=message)

    # Wenn alles gut dann gib ein valides Response zurück
    return BuchungResponse(success=True, message=message)


@router.get("/", response_model=List[BuchungInfo])
def alle_buchungen_anzeigen():
    return get_all_buchungen()


@router.get("/filter", response_model=List[BuchungInfo])
def gefilterte_buchungen_anzeigen(
        user_id: int = Query(default=None, description="Filtere nach Benutzer-ID"),
        vehicle_id: int = Query(default=None, description="Filtere nach Fahrzeug-ID"),
        start: datetime = Query(default=None, description="Zeitraum: Startzeit (Standard = heute)"),
        end: datetime = Query(default=None, description="Zeitraum: Ende"),
        limit: int = Query(default=10, description="Begrenze die Anzahl an Ergebnissen"),
        offset: int = Query(default=0, description="Überspringe eine Anzahl von Ergebnissen"),
        sort_by: str = Query(default="bookingstart", description="Sortiere nach bookingstart, bookingend, user_id, vehicles_id"),
        order: str = Query(default="asc", description="Sortierreihenfolge: asc oder desc")
):
    if start is None:
        start = datetime.now()
    return get_filtered_buchungen(
        user_id=user_id,
        vehicle_id=vehicle_id,
        start=start,
        end=end,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        order=order
    )

@router.patch("/{booking_id}")
def buchung_aktualisieren(
    buchung: BuchungsUpdate,
    booking_id: int = Path(..., description="Die ID der zu ändernden Buchung")):
    success, message = update_buchung(booking_id, buchung.dict(exclude_unset=True))
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"success": True, "message": message}

@router.delete("/{booking_id}")
def buchung_loeschen(booking_id: int):
    success, message = delete_buchung(booking_id)
    if not success:
        raise HTTPException(status_code=404, detail=message)
    return {"success": True, "message": message}
