# IT Asset Management System

This project is a full-stack **IT Asset Management System** built to manage assets, employees, assignments, lifecycle tracking, and audit reporting.  
It is designed with a **clean backend-first architecture**, where the frontend consumes APIs without embedding business logic.

The system supports asset lifecycle management, assignment tracking, audit reports, expiry monitoring, and PDF report generation.

---

## Key Features

- Add and manage IT assets with lifecycle dates
- Add and manage employees
- Assign assets to employees
- Return assets and maintain assignment history
- Track asset availability and lifecycle status
- Generate audit, assignment, and expiry reports
- Download reports as PDF files
- Streamlit-based UI consuming FastAPI APIs

---

## Project Architecture (Conceptual)

- **Backend**  
  Handles all business logic, database access, reporting, and PDF generation.

- **Frontend (Streamlit)**  
  Acts as a thin client:
  - Collects user input
  - Displays data
  - Triggers API calls
  - Downloads PDFs

No database logic or report generation exists in the UI.

---

## How to Run the Project

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd it-asset-management

# 2. Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the FastAPI backend
uvicorn backend.main:app --reload

# Backend will be available at:
# http://127.0.0.1:8000
# Swagger Docs:
# http://127.0.0.1:8000/docs

# 5. Open a NEW terminal (keep backend running)
cd streamlit_ui
..\venv\Scripts\activate

# 6. Start the Streamlit frontend
streamlit run app.py
