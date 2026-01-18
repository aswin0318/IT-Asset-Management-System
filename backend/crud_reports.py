from sqlalchemy.orm import Session
from datetime import datetime, timezone

from backend import models


def assignment_audit_report(db: Session):
    rows = (
        db.query(
            models.Assignment.id.label("assignment_id"),
            models.Asset.asset_name,
            models.Asset.serial_number,
            models.Employee.name.label("employee_name"),
            models.Assignment.assigned_date,
            models.Assignment.returned_date,
        )
        .join(models.Asset, models.Assignment.asset_id == models.Asset.id)
        .join(models.Employee, models.Assignment.employee_id == models.Employee.id)
        .order_by(models.Assignment.assigned_date.desc())
        .all()
    )

    results = [
        {
            "assignment_id": row.assignment_id,
            "asset_name": row.asset_name,
            "serial_number": row.serial_number,
            "employee_name": row.employee_name,
            "assigned_date": row.assigned_date,
            "returned_date": row.returned_date,
        }
        for row in rows
    ]

    return results


def currently_assigned_assets(db: Session):
    rows = (
        db.query(
            models.Asset.asset_name,
            models.Asset.serial_number,
            models.Employee.name.label("employee_name"),
            models.Assignment.assigned_date,
        )
        .join(models.Assignment, models.Assignment.asset_id == models.Asset.id)
        .join(models.Employee, models.Assignment.employee_id == models.Employee.id)
        .filter(models.Assignment.returned_date.is_(None))
        .order_by(models.Assignment.assigned_date.desc())
        .all()
    )

    return [
        {
            "asset_name": row.asset_name,
            "serial_number": row.serial_number,
            "employee_name": row.employee_name,
            "assigned_date": row.assigned_date,
        }
        for row in rows
    ]


def expired_assets_report(db: Session):
    now = datetime.now(timezone.utc)

    rows = (
        db.query(
            models.Asset.asset_name,
            models.Asset.serial_number,
            models.Asset.expiry_date,
            models.Asset.status,
        )
        .filter(models.Asset.expiry_date < now)
        .order_by(models.Asset.expiry_date)
        .all()
    )

    return [
        {
            "asset_name": row.asset_name,
            "serial_number": row.serial_number,
            "expiry_date": row.expiry_date,
            "status": row.status,
        }
        for row in rows
    ]
