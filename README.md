# KPA Wheel Specification API

## 📌 Overview
A FastAPI-based backend implementing the Wheel Specification Form APIs from the KPA Form Data documentation.

## 🚀 Features
- Create a new Wheel Specification (POST)
- Get all or filtered Wheel Specifications (GET)
- Stores data in PostgreSQL
- Fully tested with Postman

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd kpa_wheel_spec_project
2. Create and Activate Virtual Environment
bash
Copy code
python -m venv env
env\Scripts\activate  # On Windows
# or
source env/bin/activate  # On Mac/Linux
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up PostgreSQL Database
Create a database named kpa_db and update the .env file like:

bash
Copy code
DATABASE_URL=postgresql://postgres:your_password@localhost/kpa_db
5. Run the Server
bash
Copy code
uvicorn app.main:app --reload
6. Visit the API Docs
Open browser: http://127.0.0.1:8000/docs

📮 API Endpoints
✅ POST /api/forms/wheel-specifications
Creates a new wheel specification record.

✅ GET /api/forms/wheel-specifications
Fetches all records or filtered by query parameters:

formNumber

submittedBy

submittedDate

📦 Postman Collection
Import kpa_form.postman_collection.json in Postman to test both endpoints.

🙋 Author
NEERAJ D SHET

📁 Submission Format
Source Code: (GitHub or zipped folder)

Postman Collection: kpa_form.postman_collection.json

README.md