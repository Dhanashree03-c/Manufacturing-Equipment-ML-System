# Manufacturing Equipment Output Prediction System

An end-to-end **Machine Learning web application** that predicts hourly production output of manufacturing equipment using operational parameters.
The system uses a **Linear Regression model**, a **FastAPI backend**, and a **Streamlit frontend**, containerized with **Docker** and deployed on **Render**.

# Key Features

* Predict hourly machine production output
* Interactive web interface using Streamlit
* FastAPI REST API for ML inference
* Docker containerization
* Cloud deployment using Render
* Supports multiple operational parameters and machine configurations

# Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* Pandas
* NumPy

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Deployment

* Docker
* Render Cloud Platform

# Machine Learning Model

The model predicts **parts produced per hour** using machine operational parameters.

Algorithm used:

Linear Regression

The model was trained on a dataset containing **1000 simulated manufacturing records** with features such as:

* Temperature
* Pressure
* Cycle Time
* Material Viscosity
* Ambient Temperature
* Operator Experience
* Humidity
* Cooling Time
* Injection Speed
* Machine Age
* Maintenance Score
* Energy Consumption
* Machine Utilization
* Efficiency Score

Target Variable:

Parts Produced Per Hour

# System Architecture

User Interface (Streamlit)
↓
REST API (FastAPI Backend)
↓
Machine Learning Model (Linear Regression)
↓
Prediction Output

# Running the Project Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/Manufacturing-Equipment-ML-System.git
```

```
cd Manufacturing-Equipment-ML-System
```

### 2. Run using Docker Compose

```
docker compose up --build
```

### 3. Access the application

Frontend (Streamlit):

```
http://localhost:8501
```

Backend API:

```
http://localhost:8000
```

# Deployment

The project is deployed on **Render** using two web services.

### Frontend

Streamlit Web App

```
https://manufacturing-equipment-ml-system-1.onrender.com
```

### Backend

FastAPI ML API

```
https://manufacturing-equipment-ml-system-2.onrender.com
```

# Input Parameters

The model accepts the following machine parameters:

* Temperature
* Pressure
* Cycle Time
* Material Viscosity
* Ambient Temperature
* Operator Experience
* Humidity
* Cooling Time
* Injection Speed
* Machine Age
* Maintenance Score
* Vibration Level
* Energy Consumption
* Injection Pressure
* Injection Temperature
* Maintenance Hours
* Efficiency Score
* Machine Utilization
* Total Cycle Time
* Temperature Pressure Ratio

Categorical inputs:

* Machine Type
* Shift
* Material Grade
* Day of Week

# Future Improvements

* Use real industrial datasets
* Add advanced models such as Random Forest or XGBoost
* Add model monitoring and logging
* Deploy using Kubernetes
* Add dashboard analytics

# Author

**Dhanashree Tankar**

**Sujal Yewale**

**Maheshree Katla**

**Anchal Pandey**

**Haady**