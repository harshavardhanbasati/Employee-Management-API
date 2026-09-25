from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .crud import (
    create_employee,
    delete_employee,
    get_employee,
    get_employees,
    update_employee,
)
from .database import Base, engine, get_db
from .models import Employee
from .schemas import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Employee Management API",
    description="REST API for managing employee records",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }


# CREATE
@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=201
)
def add_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee(
        db,
        employee_data
    )


# READ ALL
@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_all_employees(
    db: Session = Depends(get_db)
):
    return get_employees(db)


# READ ONE
@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = get_employee(
        db,
        employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# UPDATE
@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee_by_id(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    employee = update_employee(
        db,
        employee_id,
        employee_data
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# DELETE
@app.delete("/employees/{employee_id}")
def delete_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = delete_employee(
        db,
        employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }