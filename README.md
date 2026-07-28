# Task API

A simple RESTful Task Management API built with **FastAPI**. It allows users to create, retrieve, update, and delete tasks stored in an in-memory dictionary.

> **Note:** This project uses an in-memory database (`task_DB`), so all data is lost when the server restarts.

---

## Features

- View API information
- Health check endpoint
- Get all tasks
- Get a task by ID
- Create a new task
- Update an existing task
- Delete a task
- Automatic interactive API documentation with Swagger UI

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

---

## Installation & Run

### 1. Install dependencies

pip install fastapi uvicorn


### 2. Run the application


uvicorn main:app --reload



The API will be available at:


http://127.0.0.1:8000


Swagger UI:


http://127.0.0.1:8000/docs



# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---



# Example Responses

### GET `/tasks`

json
{
  "1": {
    "title": "Set up Git",
    "completed": false
  },
  "2": {
    "title": "Watch a vedio",
    "completed": false
  },
  "3": {
    "title": "push the project",
    "completed": true
  }
}


---

### GET `/health`

json
{
  "status": "ok"
}


---

# Swagger UI Screenshot

<img width="2848" height="1348" alt="لقطة شاشة 2026-07-29 010838" src="https://github.com/user-attachments/assets/fe997bc8-0f29-46e0-9887-e2b597fa6b0c" />
<img width="2820" height="1302" alt="لقطة شاشة 2026-07-29 010855" src="https://github.com/user-attachments/assets/4639b32a-17ca-4bd9-a6f0-1b1d75e46a3f" />
<img width="2816" height="1566" alt="لقطة شاشة 2026-07-29 010916" src="https://github.com/user-attachments/assets/47fb2395-9571-4333-80ca-98bb31e590fb" />
<img width="2106" height="1686" alt="لقطة شاشة 2026-07-29 011049" src="https://github.com/user-attachments/assets/5ffe10d1-0fb4-4bca-a5f9-0580b31c978b" />
<img width="2834" height="1560" alt="لقطة شاشة 2026-07-29 011110" src="https://github.com/user-attachments/assets/05d09c6f-b166-4efc-9d3e-d45d1e839b89" />
<img width="2828" height="1508" alt="لقطة شاشة 2026-07-29 010946" src="https://github.com/user-attachments/assets/b964ac4d-13f6-4ebf-86e7-209da62a9dfa" />




---


---

# Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

---

# Notes

- Data is stored in memory only.
- Restarting the server resets all tasks.
- FastAPI automatically generates OpenAPI documentation.
