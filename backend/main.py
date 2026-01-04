from fastapi import FastAPI, Depends
from . import models
from .database import engine, get_db
from .schemas import AssetCreate, AssetResponse
from sqlalchemy.orm import Session

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

@app.get("/")
def root():
    return {"message": "IT Asset Management API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

