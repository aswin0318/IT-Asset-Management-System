from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.database import get_db
from backend.schemas import AssetCreate, AssetResponse
from backend import crud

router = APIRouter(prefix="/assets", tags=["Assets"])

@router.post("/", response_model=AssetResponse)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    return crud.create_asset(db, asset)

@router.get("/", response_model=List[AssetResponse])
def list_assets(db: Session = Depends(get_db)):
    return crud.get_assets(db)
