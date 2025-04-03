import sys
import os
from fastapi import FastAPI
import uvicorn
from enum import Enum

class ModelName(str, Enum):
    test1 = "beispiel1"
    test2 = "beispiel2"
    test3 = "beispiel3"


app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


@app.get("/")
async def root():
    return {"message": "Welcome to ATCars your booking page for our company vehicles"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return{"Item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.test1:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name is ModelName.test3:
        return {"model_name": model_name, "message": "test3 war erfolgreich"}
    return {"model_name": model_name, "message": "Bitte versuchen sie es erneut"}
