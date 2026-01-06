from typing import List
from fastapi import FastAPI, Depends, HTTPException
from . import models
from .database import engine, get_db
from .schemas import AssetCreate, AssetResponse, EmployeeCreate, EmployeeResponse, AssignmentCreate, AssignmentResponse
from sqlalchemy.orm import Session
from datetime import datetime, timezone

app = FastAPI(title="IT Asset Management System")
models.Base.metadata.create_all(bind=engine)

@app.post("/assets", response_model=AssetResponse)
def create_asset(asset: AssetCreate, db:Session = Depends(get_db)):
    new_asset = models.Asset(
        asset_name = asset.asset_name,
        asset_type = asset.asset_type,
        serial_number = asset.serial_number
    )
    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)
    return new_asset

@app.get("/assets", response_model=List[AssetResponse])
def get_assets(db: Session = Depends(get_db)):
    assets = db.query(models.Asset).all()
    return assets

@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employee(
        name=employee.name,
        department=employee.department,
        email=employee.email
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@app.get("/employees", response_model=List[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

@app.post("/assignments", response_model=AssignmentResponse)
def assign_asset(data: AssignmentCreate, db: Session = Depends(get_db)):

    asset = db.query(models.Asset).filter(models.Asset.id == data.asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    employee = db.query(models.Employee).filter(models.Employee.id == data.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if asset.status == "Assigned":
        raise HTTPException(status_code=400, detail="Asset already assigned")

    assignment = models.Assignment(
        asset_id=data.asset_id,
        employee_id=data.employee_id
    )

    asset.status = "Assigned"

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return assignment

@app.get("/assignments", response_model=List[AssignmentResponse])
def list_assignments(db: Session = Depends(get_db)):
    return db.query(models.Assignment).all()

@app.put("/assignments/{assignment_id}/return", response_model=AssignmentResponse)
def return_asset(assignment_id: int, db: Session = Depends(get_db)):

    assignment = db.query(models.Assignment).filter(
        models.Assignment.id == assignment_id
    ).first()

    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    if assignment.returned_date is not None:
        raise HTTPException(status_code=400, detail="Asset already returned")

    assignment.returned_date = datetime.now(timezone.utc)

    asset = db.query(models.Asset).filter(
        models.Asset.id == assignment.asset_id
    ).first()

    asset.status = "Available"

    db.commit()
    db.refresh(assignment)

    return assignment



@app.get("/")
def root():
    return {"message": "IT Asset Management API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

