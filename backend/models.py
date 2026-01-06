from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    status = Column(String, default="Available")

    assignments = relationship("Assignment", back_populates="asset")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    assignments = relationship("Assignment", back_populates="employee")

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    assigned_date = Column(Date, default=date.today)
    returned_date = Column(Date, nullable=True)

    asset = relationship("Asset", back_populates="assignments")
    employee = relationship("Employee", back_populates="assignments")
