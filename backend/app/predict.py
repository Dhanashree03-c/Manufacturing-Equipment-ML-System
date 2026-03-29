import joblib
import pandas as pd
import os

# Load model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "manufacturing_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_output(data):

    # Convert incoming JSON to dataframe
    df = pd.DataFrame([{
        "Temperature": data.Temperature,
        "Pressure": data.Pressure,
        "Cycle_Time": data.Cycle_Time,
        "Material_Viscosity": data.Material_Viscosity,
        "Ambient_Temperature": data.Ambient_Temperature,
        "Operator_Experience": data.Operator_Experience,
        "Machine_Type": data.Machine_Type,
        "Shift": data.Shift,
        "Material_Grade": data.Material_Grade,
        "Day_of_Week": data.Day_of_Week,
        "Humidity": data.Humidity,
        "Cooling_Time": data.Cooling_Time,
        "Injection_Speed": data.Injection_Speed,
        "Machine_Age": data.Machine_Age,
        "Maintenance_Score": data.Maintenance_Score,
        "Vibration_Level": data.Vibration_Level,
        "Energy_Consumption": data.Energy_Consumption,

        # Missing features required by model
        "Injection_Pressure": data.Injection_Pressure,
        "Injection_Temperature": data.Injection_Temperature,
        "Maintenance_Hours": data.Maintenance_Hours,
        "Efficiency_Score": data.Efficiency_Score,
        "Machine_Utilization": data.Machine_Utilization,
        "Total_Cycle_Time": data.Total_Cycle_Time,
        "Temperature_Pressure_Ratio": data.Temperature_Pressure_Ratio
    }])

    prediction = model.predict(df)

    return float(prediction[0])