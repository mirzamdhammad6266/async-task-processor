from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import Dict
import asyncio

app = FastAPI(
    title="Async Task Processor",
    description="Small FastAPI service that demonstrates async background task processing.",
)

# ----- Pydantic models ----- #

class TaskRequest(BaseModel):
    task_type: str
    payload: dict

class TaskStatus(BaseModel):
    task_id: str
    status: str


# ----- In-memory task store (demo only) ----- #

tasks: Dict[str, str] = {}


async def process_task(task_id: str, task: TaskRequest) -> None:
    """
    Simulated long-running task.
    In a real system this could be sending emails, calling external APIs, etc.
    """
    tasks[task_id] = "processing"

    # Fake work
    await asyncio.sleep(2)

    tasks[task_id] = "completed"


# ----- API endpoints ----- #

@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/tasks", response_model=TaskStatus)
async def enqueue_task(request: TaskRequest, background_tasks: BackgroundTasks):
    """
    Enqueue a task for background processing.
    """
    task_id = f"task_{len(tasks) + 1}"
    tasks[task_id] = "queued"

    # Run async processing in the background
    background_tasks.add_task(process_task, task_id, request)

    return TaskStatus(task_id=task_id, status=tasks[task_id])


@app.get("/tasks/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str):
    """
    Check the status of a previously enqueued task.
    """
    status = tasks.get(task_id, "not_found")
    return TaskStatus(task_id=task_id, status=status)
