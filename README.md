# Finance Data Processing & Access Control Backend

**Backend Developer Intern – Internship Assignment**  

A fully functional backend system for managing financial records with **role-based access control**, **authentication**, and **dashboard analytics**. Built with **FastAPI**, **SQLite**, and **SQLAlchemy**.

---

## 🛠 Tech Stack

- **Language:** Python 3.13  
- **Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT tokens  

Optional tools for development: Uvicorn, Pydantic, Passlib.

---

## 📂 Project Structure
FinanceBackend/
│
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── database.py # SQLite & SQLAlchemy setup
│ ├── models/ # Database models (User, Record)
│ ├── schemas/ # Pydantic schemas for validation
│ ├── core/ # Security utils (JWT, hashing)
│ └── routes/ # API routers (auth, users, records)
│
├── .gitignore
├── README.md
├── finance.db # SQLite database
└── requirements.txt

---

## ⚡ Features

1. **Authentication (JWT)**  
   - Register & login endpoints  
   - Token-based authentication  

2. **Role-Based Access Control**  
   - `Admin` – full access (create/update/delete users & records)  
   - `Analyst` – read records & dashboard summary  
   - `Viewer` – view dashboard only  

3. **CRUD Operations for Financial Records**  
   - Create, read, update, delete  
   - Filter by `type` (income/expense)  

4. **Dashboard Analytics**  
   - Total income, total expenses, net balance  

5. **Data Validation & Error Handling**  
   - Input validation via Pydantic  
   - Proper HTTP status codes  

---
## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Deeksha7-wa/Finance-Data-Processing-Access-Control-Backend.git
cd Finance-Data-Processing-Access-Control-Backend
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate Virtual Environment

```bash
source .venv/bin/activate   # Mac/Linux
# .venv\\Scripts\\activate    # Windows
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Server

```bash
uvicorn app.main:app --reload --port 8000
```

### 📄 Access Swagger UI

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📸 API Endpoints Overview

### 🔐 Auth
- **POST** `/auth/register` → Register
- **POST** `/auth/login` → Login

### 👥 Users
- **GET** `/users/admin-only` → Admin Data  
- **GET** `/users/analytics` → Analytics Data  
- **GET** `/users/dashboard` → Dashboard  

### 💰 Records
- **POST** `/records/` → Create Record  
- **GET** `/records/` → Get Records  
- **PUT** `/records/{record_id}` → Update Record  
- **DELETE** `/records/{record_id}` → Delete Record  
- **GET** `/records/summary` → Summary  

### 🌐 Default
- **GET** `/` → Root
---

## 👥 Roles & Permissions

| Role    | Allowed Endpoints                                                         |
| ------- | ------------------------------------------------------------------------- |
| Admin   | `/users/admin-only`, `/users/analytics`, `/users/dashboard`, `/records/*` |
| Analyst | `/users/analytics`, `/users/dashboard`, `/records/*` *(read-only)*        |
| Viewer  | `/users/dashboard`                                                        |

---

## 🧪 Example API Requests

### 1. Register User

```bash
POST /auth/register
```

```json
{
  "username": "admin",
  "password": "1234",
  "role": "admin"
}
```

### 2. Login

```bash
POST /auth/login
```

```json
{
  "username": "admin",
  "password": "1234"
}
```

#### Response

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### 3. Create Record (Admin)

```bash
POST /records/
```

```json
{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "date": "2026-04-02",
  "notes": "April salary"
}
```

### 4. Get Records

```bash
GET /records?type=income
```

#### Response

```json
[
  {
    "id": 1,
    "amount": 5000,
    "type": "income",
    "category": "salary",
    "date": "2026-04-02",
    "notes": "April salary"
  }
]
```

### 5. Dashboard Summary

```bash
GET /records/summary
```

#### Response

```json
{
  "total_income": 5000,
  "total_expense": 0,
  "net_balance": 5000
}
```

---

## 🔒 Swagger Authorization

1. Login using `/auth/login` to get JWT token
2. Click **Authorize** in Swagger UI
3. Enter token in this format:

```
Bearer <JWT_TOKEN>
```

---

## ✅ Key Highlights

* Clean project structure with modular routes
* Role-based authorization with decorators
* JWT authentication & password hashing
* SQLite database for lightweight setup
* FastAPI Swagger docs for easy testing

---

## 🔧 Optional Improvements

* Pagination for records
* Search / filter by notes & categories
* Soft delete instead of permanent delete
* Unit tests / integration tests
* Docker setup for easy deployment

---

## 📌 Notes

* Ensure `.env` or secret tokens are kept secure if deployed
* Use a `.gitignore` to avoid pushing `finance.db` or virtual environments







    




