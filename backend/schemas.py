from pydantic import BaseModel

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
    email: str

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    email: str
    class Config:
        orm_mode = True 