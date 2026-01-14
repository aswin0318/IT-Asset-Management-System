from pydantic import BaseModel, EmailStr
from datetime import datetime

class AssetCreate(BaseModel):
    asset_name: str
    asset_type: str
    serial_number: str
    purchase_date : datetime
    expiry_date : datetime

class AssetResponse(BaseModel):
    id: int
    asset_name: str
    asset_type: str
    serial_number: str
    status: str
    purchase_date : datetime
    expiry_date : datetime

    class Config:
        from_attributes = True   #earlier orm_mode = True

class EmployeeCreate(BaseModel):
    name: str
    department: str
    email: EmailStr

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    email: EmailStr
    class Config:
        from_attributes = True

class AssignmentCreate(BaseModel):
    asset_id: int
    employee_id: int


class AssignmentResponse(BaseModel):
    id: int
    asset_id: int
    employee_id: int
    assigned_date: datetime
    returned_date: datetime | None

    class Config:
        from_attributes = True