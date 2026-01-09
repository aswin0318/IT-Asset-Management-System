from sqlalchemy.orm import Session
from datetime import datetime, timezone

from backend import models

# Asset CRUD operations

def create_asset(db: Session, asset_data):
    asset = models.Asset(
        asset_name=asset_data.asset_name,
        asset_type=asset_data.asset_type,
        serial_number=asset_data.serial_number
    )
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset



def get_assets(db: Session):
    return db.query(models.Asset).all()


# Employee CRUD operations

def create_employee(db: Session, employee_data):
    new_employee = models.Employee(
        name=employee_data.name,
        department=employee_data.department,
        email=employee_data.email
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


def get_employees(db: Session):
    return db.query(models.Employee).all()

# Assignment CRUD operations

def create_assignment(db: Session, data):
    asset = db.query(models.Asset).filter(
        models.Asset.id == data.asset_id
    ).first()

    if not asset:
        return None, "asset_not_found"

    employee = db.query(models.Employee).filter(
        models.Employee.id == data.employee_id
    ).first()

    if not employee:
        return None, "employee_not_found"

    if asset.status == "Assigned":
        return None, "asset_already_assigned"

    assignment = models.Assignment(
        asset_id=data.asset_id,
        employee_id=data.employee_id
    )

    asset.status = "Assigned"

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return assignment, None

def get_assignments(db: Session):
    return db.query(models.Assignment).all()

def return_assignment(db: Session, assignment_id: int):
    assignment = db.query(models.Assignment).filter(
        models.Assignment.id == assignment_id
    ).first()

    if not assignment:
        return None, "assignment_not_found"

    if assignment.returned_date is not None:
        return None, "already_returned"

    assignment.returned_date = datetime.now(timezone.utc)

    asset = db.query(models.Asset).filter(
        models.Asset.id == assignment.asset_id
    ).first()

    asset.status = "Available"

    db.commit()
    db.refresh(assignment)

    return assignment, None

