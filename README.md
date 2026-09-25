# Employee Management API

A RESTful Employee Management API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy ORM**.

The application provides complete CRUD operations for managing employee records with request validation using **Pydantic** and automatic interactive API documentation using **Swagger/OpenAPI**.

---

## 🚀 Features

- Create employee records
- Retrieve all employees
- Retrieve an employee by ID
- Update employee information
- Delete employee records
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request and response validation
- Automatic Swagger/OpenAPI documentation
- Environment variable configuration
- HTTP error handling
- Clean project structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| Swagger/OpenAPI | API documentation |
| Git/GitHub | Version control |

---

## 📁 Project Structure

```text
employee-management-api/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── app/
    ├── __init__.py
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    └── crud.py
```

### File Responsibilities

- `main.py` — FastAPI application and API endpoints
- `database.py` — PostgreSQL connection and SQLAlchemy session
- `models.py` — SQLAlchemy database models
- `schemas.py` — Pydantic request/response schemas
- `crud.py` — Create, Read, Update, Delete database operations
- `.env` — Environment-specific configuration

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-management-api.git
cd employee-management-api
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ PostgreSQL Setup

Create a PostgreSQL database named:

```text
employee_db
```

Example configuration:

```text
Host: localhost
Port: 5432
Database: employee_db
Username: postgres
Password: YOUR_PASSWORD
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/employee_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

> **Do not commit the `.env` file to GitHub.**

---

# ▶️ Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/employees` | Create an employee |
| GET | `/employees` | Get all employees |
| GET | `/employees/{id}` | Get employee by ID |
| PUT | `/employees/{id}` | Update an employee |
| DELETE | `/employees/{id}` | Delete an employee |

---

# 📝 API Usage

## Create Employee

### Request

```http
POST /employees
```

### JSON Body

```json
{
  "name": "Harsha",
  "email": "harsha@gmail.com",
  "department": "IT",
  "salary": 45000
}
```

### Response

```json
{
  "id": 1,
  "name": "Harsha",
  "email": "harsha@gmail.com",
  "department": "IT",
  "salary": 45000
}
```

---

## Get All Employees

```http
GET /employees
```

### Response

```json
[
  {
    "id": 1,
    "name": "Harsha",
    "email": "harsha@gmail.com",
    "department": "IT",
    "salary": 45000
  },
  {
    "id": 2,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "department": "HR",
    "salary": 50000
  }
]
```

---

## Get Employee by ID

```http
GET /employees/1
```

### Response

```json
{
  "id": 1,
  "name": "Harsha",
  "email": "harsha@gmail.com",
  "department": "IT",
  "salary": 45000
}
```

If the employee doesn't exist:

```json
{
  "detail": "Employee not found"
}
```

Status code:

```text
404 Not Found
```

---

## Update Employee

```http
PUT /employees/1
```

### JSON Body

```json
{
  "name": "Harsha Vardhan",
  "email": "harsha.vardhan@gmail.com",
  "department": "Development",
  "salary": 60000
}
```

### Response

```json
{
  "id": 1,
  "name": "Harsha Vardhan",
  "email": "harsha.vardhan@gmail.com",
  "department": "Development",
  "salary": 60000
}
```

---

## Delete Employee

```http
DELETE /employees/1
```

### Response

```json
{
  "message": "Employee deleted successfully",
  "employee_id": 1
}
```

---

# ✅ Validation

The API validates incoming employee data using Pydantic.

Example invalid request:

```json
{
  "name": "A",
  "email": "invalid-email",
  "department": "",
  "salary": -500
}
```

The API rejects invalid data and returns a validation error.

Validation rules include:

- Employee name: 2–100 characters
- Valid email format
- Department: 2–50 characters
- Salary must be greater than 0

---

# 🏗️ Application Architecture

```text
                Client
                  │
                  ▼
             FastAPI API
                  │
                  ▼
          Pydantic Validation
                  │
                  ▼
            CRUD Functions
                  │
                  ▼
           SQLAlchemy ORM
                  │
                  ▼
             PostgreSQL
```

---

# 🔄 CRUD Operations

```text
CREATE
POST /employees
       ↓
  PostgreSQL

READ
GET /employees
       ↓
  PostgreSQL

READ ONE
GET /employees/{id}
       ↓
  PostgreSQL

UPDATE
PUT /employees/{id}
       ↓
  PostgreSQL

DELETE
DELETE /employees/{id}
       ↓
  PostgreSQL
```

---

# 🧪 Testing

The API can be tested using:

- Swagger UI
- Postman
- Browser for GET endpoints

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🚀 Future Improvements

Possible improvements include:

- JWT authentication
- User roles and authorization
- Pagination
- Search and filtering
- Sorting
- Automated tests with Pytest
- Alembic database migrations
- Docker support
- API logging
- Improved exception handling
- CI/CD with GitHub Actions

---

# 📌 Learning Objectives

This project was developed to practice:

- REST API development
- FastAPI
- Python backend development
- PostgreSQL
- SQLAlchemy ORM
- Pydantic validation
- CRUD operations
- API documentation
- Database integration
- Git and GitHub

---

# 👨‍💻 Author

**Harsha Vardhan Basati**

B.Tech Computer Science & Engineering

---

## 📄 License

This project is intended for learning and portfolio purposes.
