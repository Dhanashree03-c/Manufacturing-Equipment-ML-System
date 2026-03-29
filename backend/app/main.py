from fastapi import FastAPI
from .schema import MachineInput
from .predict import predict_output

app = FastAPI(
    title="Manufacturing Output Prediction API",
    description="Predict hourly machine production output",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Manufacturing ML API Running"}

@app.post("/predict")
def predict(data: MachineInput):

    result = predict_output(data)

    return {
        "predicted_parts_per_hour": result
    }