import sys
import os
from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to ATCars your booking page for our company vehicles"}

#hier hinzufügen


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
