from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import crud_reports
from fastapi.responses import FileResponse
from pathlib import Path
from backend.pdf_utils import render_pdf


router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/assignment-audit")
def assignment_audit(db: Session = Depends(get_db)):
    return crud_reports.assignment_audit_report(db)

@router.get("/currently-assigned")
def currently_assigned(db: Session = Depends(get_db)):
    return crud_reports.currently_assigned_assets(db)

@router.get("/expired-assets")
def expired_assets(db: Session = Depends(get_db)):
    return crud_reports.expired_assets_report(db)

@router.get("/assignment-audit/pdf")
def assignment_audit_pdf(db: Session = Depends(get_db)):
    data = crud_reports.assignment_audit_report(db)

    output_file = Path("backend/reports/assignment_audit_report.pdf")

    render_pdf(
        template_name="assignment_audit.html",
        context={"rows": data},
        output_path=str(output_file)
    )

    return FileResponse(
        path=output_file,
        media_type="application/pdf",
        filename="assignment_audit_report.pdf"
    )

@router.get("/currently-assigned/pdf")
def currently_assigned_pdf(db: Session = Depends(get_db)):
    data = crud_reports.currently_assigned_assets(db)

    output_file = Path("backend/reports/currently_assigned_assets.pdf")

    render_pdf(
        template_name="currently_assigned.html",
        context={"rows": data},
        output_path=str(output_file)
    )

    return FileResponse(
        path=output_file,
        media_type="application/pdf",
        filename="currently_assigned_assets.pdf"
    )

@router.get("/expired-assets/pdf")
def expired_assets_pdf(db: Session = Depends(get_db)):
    data = crud_reports.expired_assets_report(db)

    output_file = Path("backend/reports/expired_assets_report.pdf")

    render_pdf(
        template_name="expired_assets.html",
        context={"rows": data},
        output_path=str(output_file)
    )

    return FileResponse(
        path=output_file,
        media_type="application/pdf",
        filename="expired_assets_report.pdf"
    )
