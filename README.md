# Manufacturing Output Prediction

ML system predicting injection molding machine output.

## Run Locally

1. clone repo
2. open folder

Backend:
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend:
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py

Backend runs:
http://localhost:8000

Frontend:
http://localhost:8501