from pydantic import BaseModel

class MachineInput(BaseModel):

    Temperature: float
    Pressure: float
    Cycle_Time: float
    Material_Viscosity: float
    Ambient_Temperature: float
    Operator_Experience: float
    Machine_Type: str
    Shift: str
    Material_Grade: str
    Day_of_Week: str
    Humidity: float
    Cooling_Time: float
    Injection_Speed: float
    Machine_Age: float
    Maintenance_Score: float
    Vibration_Level: float
    Energy_Consumption: float

    Injection_Pressure: float
    Injection_Temperature: float
    Maintenance_Hours: float
    Efficiency_Score: float
    Machine_Utilization: float
    Total_Cycle_Time: float
    Temperature_Pressure_Ratio: float