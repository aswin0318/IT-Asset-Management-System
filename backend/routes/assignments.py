from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.database import get_db
from backend.schemas import AssignmentCreate, AssignmentResponse
from backend import crud

router = APIRouter(prefix="/assignments", tags=["Assignments"])

@router.post("/", response_model=AssignmentResponse)
def assign_asset(data: AssignmentCreate, db: Session = Depends(get_db)):
    assignment, error = crud.create_assignment(db, data)

    if error == "asset_not_found":
        raise HTTPException(404, "Asset not found")
    if error == "employee_not_found":
        raise HTTPException(404, "Employee not found")
    if error == "asset_already_assigned":
        raise HTTPException(400, "Asset already assigned")

    return assignment

@router.get("/", response_model=List[AssignmentResponse])
def list_assignments(db: Session = Depends(get_db)):
    return crud.get_assignments(db)

@router.put("/{assignment_id}/return", response_model=AssignmentResponse)
def return_asset(assignment_id: int, db: Session = Depends(get_db)):
    assignment, error = crud.return_assignment(db, assignment_id)

    if error == "assignment_not_found":
        raise HTTPException(404, "Assignment not found")
    if error == "already_returned":
        raise HTTPException(400, "Asset already returned")

    return assignment
