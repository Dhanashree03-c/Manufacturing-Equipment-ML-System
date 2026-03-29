import joblib
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../models/manufacturing_model.pkl"
)

model = joblib.load(MODEL_PATH)

def get_model():
    return model