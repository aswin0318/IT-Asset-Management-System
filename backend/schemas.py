from pydantic import BaseModel, EmailStr
from datetime import date

class AssetCreate(BaseModel):
    asset_name: str
    asset_type: str
    serial_number: str

class AssetResponse(BaseModel):
    id: int
    asset_name: str
    asset_type: str
    serial_number: str
    status: str

    class Config:
        orm_mode = True

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
        orm_mode = True 

class AssignmentCreate(BaseModel):
    asset_id: int
    employee_id: int


class AssignmentResponse(BaseModel):
    id: int
    asset_id: int
    employee_id: int
    assigned_date: date
    returned_date: date | None

    class Config:
        orm_mode = True