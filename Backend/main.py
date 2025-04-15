import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from fastapi import FastAPI
import uvicorn
from enum import Enum
from fuhrpark.routes import buchung
from fuhrpark.schemas import BuchungRequest, BuchungResponse


app = FastAPI(
    title="ATCars Fuhrpark",
    description="REST-API für intere Fahrzeugbuchung",
    version="1.0.0"
)
app.include_router(buchung.router)


@app.get("/")
async def root():
    return {"Welcome to ATCars your booking page for our company vehicles"}

#hier hinzufügen


#nur bei lokales starten
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
