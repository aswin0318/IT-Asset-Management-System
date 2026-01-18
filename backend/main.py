from fastapi import FastAPI

from backend.database import engine
from backend import models
from backend.routes import assets, employees, assignments, reports

app = FastAPI(title="IT Asset Management System")

models.Base.metadata.create_all(bind=engine)

app.include_router(assets.router)
app.include_router(employees.router)
app.include_router(assignments.router)
app.include_router(reports.router)


@app.get("/")
def root():
    return {"message": "IT Asset Management API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
