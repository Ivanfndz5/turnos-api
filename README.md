# Shifts API

This is a simple API for managing doctor and patient shifts.  
Built with **FastAPI**, **Pydantic**, and **SQLAlchemy**.

## What it does

- Create and list doctors
- Create and list patients
- Create and list doctor availabilities
- Link shifts to doctors and patients

## Main Endpoints

| Method | Endpoint           | Description                          |
|--------|------------------|--------------------------------------|
| POST   | /doctors          | Create a doctor                      |
| GET    | /doctors          | List all doctors                     |
| POST   | /patients         | Create a patient                     |
| GET    | /patients         | List all patients                     |
| POST   | /availabilities   | Create a doctor availability         |
| GET    | /availabilities   | List doctor availabilities           |

## How to run

1. Clone the repository  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run the API: `uvicorn main:app --reload`  
4. Open Swagger at: `http://localhost:8000/docs`

## Notes

- Some dependencies and endpoints are still incomplete.
- This project is a **work-in-progress prototype**, ideal for testing backend concepts and basic entity relationships.
