# Async Task Processor

An asynchronous task processing microservice built with **FastAPI**.  
This project demonstrates how to accept incoming work, dispatch it to background
tasks, and expose simple HTTP endpoints for checking task status.

It is intentionally small and easy to read so it can be used as a teaching /
portfolio project for backend + async patterns in Python.

---

## ✨ Features

- `/tasks` endpoint to enqueue work using FastAPI `BackgroundTasks`
- In-memory task store for demo purposes (no external queue required)
- `/tasks/{task_id}` endpoint to check the task status
- `/health` endpoint for simple health checking
- Clean separation between **request models**, **task processor**, and **status store**

---

## 🧱 Project Structure

```text
async-task-processor/
├─ app/
│  └─ main.py        # FastAPI app + background task processing
├─ requirements.txt  # Python dependencies
└─ README.md         # Project documentation
```

---

## ▶️ Run Locally
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/async-task-processor.git
cd async-task-processor

# 2. Create a virtual environment (optional, but recommended)
python3 -m venv venv
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the FastAPI server
uvicorn app.main:app --reload
```

---

## 🔌 API Endpoints

---

### **1. POST /tasks – Enqueue a task**

#### Request  
```json
{
  "task_type": "send_email",
  "payload": {
    "to": "user@example.com",
    "subject": "Welcome",
    "body": "Thanks for signing up!"
  }
}
```

#### Example Response  
```json
{
  "task_id": "task_1",
  "status": "queued"
}
```

---

### **2. GET /tasks/{task_id} – Check status

#### Example  
```http
GET /tasks/task_1
```

#### Example Response  
```json
{
  "task_id": "task_1",
  "status": "processing"
}
```

---

### **3. GET /health – Health check
```json
{ "status": "ok" }
```

---

## 🧩 Extending With a Real Queue

To make it production-ready you could integrate:
- **Redis + RQ / Celery workers**
- **A message broker like RabbitMQ or Kafka**
- **A database table to persist task status**

The API contract can stay the same while the internal implementation improves underneath.

---

## 🛠 Tech Stack

- Python 3.10+  
- FastAPI  
- Pydantic  
- Uvicorn(ASGI server)
