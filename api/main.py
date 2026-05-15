from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WasteInput(BaseModel):
    data: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(input: WasteInput):
    prediction = f"Prediction for: {input.data}"
    return {"prediction": prediction}