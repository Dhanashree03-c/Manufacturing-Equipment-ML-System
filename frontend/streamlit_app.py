import streamlit as st
import requests

API_URL = "https://manufacturing-equipment-ml-system-2.onrender.com/predict"

st.title("Manufacturing Equipment Output Prediction")

st.write("Enter machine parameters to predict hourly production output.")

st.subheader("Machine Operating Parameters")

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    Temperature = st.number_input("Temperature (°C)", min_value=150.0, max_value=350.0, value=220.0)

with col2:
    Pressure = st.number_input("Pressure (bar)", min_value=50.0, max_value=200.0, value=120.0)

with col3:
    Cycle_Time = st.number_input("Cycle Time (sec)", min_value=5.0, max_value=120.0, value=30.0)


# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    Material_Viscosity = st.number_input("Material Viscosity", min_value=0.1, max_value=10.0, value=3.0)

with col5:
    Ambient_Temperature = st.number_input("Ambient Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0)

with col6:
    Operator_Experience = st.number_input("Operator Experience (years)", min_value=0, max_value=30, value=5)


# Row 3
col7, col8, col9 = st.columns(3)

with col7:
    Humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=50.0)

with col8:
    Cooling_Time = st.number_input("Cooling Time (sec)", min_value=1.0, max_value=60.0, value=10.0)

with col9:
    Injection_Speed = st.number_input("Injection Speed (mm/s)", min_value=10.0, max_value=300.0, value=100.0)


# Row 4
col10, col11, col12 = st.columns(3)

with col10:
    Machine_Age = st.number_input("Machine Age (years)", min_value=0, max_value=30, value=5)

with col11:
    Maintenance_Score = st.number_input("Maintenance Score (0-100)", min_value=0, max_value=100, value=80)

with col12:
    Vibration_Level = st.number_input("Vibration Level (mm/s)", min_value=0.0, max_value=10.0, value=2.0)


# Row 5
col13, col14 = st.columns(2)

with col13:
    Energy_Consumption = st.number_input("Energy Consumption (kWh)", min_value=1.0, max_value=100.0, value=20.0)

with col14:
    Injection_Pressure = st.number_input("Injection Pressure (bar)", min_value=50.0, max_value=200.0, value=120.0)

# Row 6
col15, col16, col17 = st.columns(3)

with col15:
    Injection_Temperature = st.number_input("Injection Temperature (°C)", min_value=150.0, max_value=350.0, value=230.0)

with col16:
    Maintenance_Hours = st.number_input("Maintenance Hours", min_value=0.0, max_value=50.0, value=5.0)

with col17:
    Efficiency_Score = st.number_input("Efficiency Score (0-100)", min_value=0, max_value=100, value=85)


# Row 7
col18, col19, col20 = st.columns(3)

with col18:
    Machine_Utilization = st.number_input("Machine Utilization (%)", min_value=0.0, max_value=100.0, value=75.0)

with col19:
    Total_Cycle_Time = st.number_input("Total Cycle Time (sec)", min_value=5.0, max_value=150.0, value=40.0)

with col20:
    Temperature_Pressure_Ratio = st.number_input("Temperature / Pressure Ratio", min_value=0.5, max_value=5.0, value=1.8)


st.divider()

st.subheader("Machine Configuration")

# Categorical Inputs

col21, col22 = st.columns(2)

with col21:
    Machine_Type = st.selectbox("Machine Type", ["TypeA", "TypeB", "TypeC"])

with col22:
    Shift = st.selectbox("Shift", ["Day", "Night"])


col23, col24 = st.columns(2)

with col23:
    Material_Grade = st.selectbox("Material Grade", ["A", "B", "C"])

with col24:
    Day_of_Week = st.selectbox(
        "Day of Week",
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    )


st.divider()

# Prediction Button

if st.button("Predict Production Output"):

    payload = {
        "Temperature": Temperature,
        "Pressure": Pressure,
        "Cycle_Time": Cycle_Time,
        "Material_Viscosity": Material_Viscosity,
        "Ambient_Temperature": Ambient_Temperature,
        "Operator_Experience": Operator_Experience,
        "Machine_Type": Machine_Type,
        "Shift": Shift,
        "Material_Grade": Material_Grade,
        "Day_of_Week": Day_of_Week,
        "Humidity": Humidity,
        "Cooling_Time": Cooling_Time,
        "Injection_Speed": Injection_Speed,
        "Machine_Age": Machine_Age,
        "Maintenance_Score": Maintenance_Score,
        "Vibration_Level": Vibration_Level,
        "Energy_Consumption": Energy_Consumption,

        "Injection_Pressure": Injection_Pressure,
        "Injection_Temperature": Injection_Temperature,
        "Maintenance_Hours": Maintenance_Hours,
        "Efficiency_Score": Efficiency_Score,
        "Machine_Utilization": Machine_Utilization,
        "Total_Cycle_Time": Total_Cycle_Time,
        "Temperature_Pressure_Ratio": Temperature_Pressure_Ratio
    }

    response = requests.post(API_URL, json=payload, headers={"Content-Type": "application/json"}, timeout=30)

    if response.status_code == 200:
        result = response.json()["predicted_parts_per_hour"]
        st.success(f"Predicted Parts Per Hour: {result:.2f}")

    else:
        st.error(f"Prediction failed: {response.status_code} - {response.text}")