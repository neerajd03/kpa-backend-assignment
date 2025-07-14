# KPA Wheel Specification API

This is a FastAPI-based backend project that implements one of the APIs from the KPA Form Data Postman collection.  
It allows users to submit and retrieve wheel specification form data and stores it in a PostgreSQL database.

---

## 🚀 Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/kpa_wheel_spec_project.git
cd kpa_wheel_spec_project
```
### 2. Create a virtual environment and activate it
```
python -m venv env
env\Scripts\activate   # For Windows
```
### 3. Install the requirements
```
pip install -r requirements.txt
```
### 4. Configure .env
```
Create a .env file in the root directory with:
DATABASE_URL=postgresql://postgres:yourpassword@localhost/kpa_db
```
### 5. Run the application
```
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000/docs for Swagger UI.
```

# 🧩 Tech Stack Used
    Python 3
    FastAPI
    PostgreSQL
    SQLAlchemy
    Pydantic

# ✅ Implemented API Endpoints

### 1. POST /api/forms/wheel-specifications
Creates a new wheel specification form in the database.

### 2. GET /api/forms/wheel-specifications
Retrieves all wheel specification forms, with optional filters for:
          formNumber
          submittedBy
          submittedDate

# 📦 Files/Folders to Include in Submission
app/ (your FastAPI code: main.py, routes/, models.py, schemas.py, etc.)
.gitignore
requirements.txt
README.md
neeraj_postman_collection.json (your working Postman collection)

# 📹 Video Links
project-demo: [your_drive_link_to_demo_video]
