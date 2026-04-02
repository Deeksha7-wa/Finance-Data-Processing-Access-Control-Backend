# Finance Data Processing & Access Control Backend

## 📌 Overview

This project is a backend system built for managing financial records with role-based access control. It allows different types of users to interact with financial data based on their permissions and provides summary analytics for a dashboard.

The system is designed with a focus on clean architecture, proper data handling, and secure access control.

---

## 🚀 Tech Stack

* **Framework:** FastAPI (Python)
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens)
* **API Docs:** Swagger UI (auto-generated)

---

## 🎯 Features

### 🔐 Authentication & Authorization

* User registration and login
* JWT-based authentication
* Role-based access control (RBAC)

### 👤 User Roles

* **Admin**

  * Full access (create, update, delete records & manage users)
* **Analyst**

  * View records and access analytics
* **Viewer**

  * Read-only access to dashboard data

---

### 💰 Financial Records Management

* Create financial records (Admin)
* View records (All users)
* Update records (Admin)
* Delete records (Admin)

Each record includes:

* Amount
* Type (Income / Expense)
* Category
* Date
* Notes

---

### 🔍 Filtering Support

* Filter by:

  * Type (income / expense)
  * Category
  * Date range

---

### 📊 Dashboard Analytics

* Total Income
* Total Expenses
* Net Balance

---

## 📡 API Endpoints

### 🔐 Auth

* `POST /auth/register` → Register new user
* `POST /auth/login` → Login & get JWT token

---

### 👤 Users (Role-Based Access)

* `GET /users/admin-only` → Admin only
* `GET /users/analytics` → Admin & Analyst
* `GET /users/dashboard` → All roles

---

### 💰 Records

* `POST /records/` → Create record (Admin)
* `GET /records/` → Get records (All users)
* `PUT /records/{record_id}` → Update record (Admin)
* `DELETE /records/{record_id}` → Delete record (Admin)

---

### 📊 Dashboard

* `GET /records/summary` → Financial summary (Admin, Analyst)

---

## 🧪 Test Users

You can use these sample users:

```
Admin:
username: admin
password: 1234

Analyst:
username: analyst
password: 1234

Viewer:
username: viewer
password: 1234
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd finance-backend
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the server

```
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Once the server is running, open:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Design Decisions

* Used FastAPI for its performance and clean API design
* Implemented JWT for stateless authentication
* Used role-based access control for realistic permission handling
* Designed modular structure (routes, models, schemas, core)

---

## 🚀 Future Improvements

* Pagination for records
* Search functionality
* Soft delete support
* Deployment (Render / Railway)
* Unit & integration testing

---

## 🏆 Conclusion

This project demonstrates backend development skills including API design, authentication, access control, and data processing. The system is structured to be scalable, maintainable, and aligned with real-world backend practices.

---
