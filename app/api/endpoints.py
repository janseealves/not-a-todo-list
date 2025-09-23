from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.schemas import Task, TaskCreate, TaskUpdate
from services.crud import create_task, read_task,  read_tasks, delete_task, update_task

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
def get_tasks(db: Session=Depends(get_db)):
    return read_tasks(db)

@router.post("/task", response_model=Task)
def create_new_task(task_in: TaskCreate=Depends(TaskCreate), db: Session=Depends(get_db)):
    return create_task(db, task_in)

@router.get("/task/{id}", response_model=Task)
def get_task(task_id: int, db: Session=Depends(get_db)):
    task = read_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.put("/task/{id}", response_model=Task)
def edit_task(id: int, task_update: TaskUpdate=Depends(TaskUpdate), db: Session=Depends(get_db)):
    return update_task(db, id, task_update)

@router.delete("/task/{id}")
def delete_single_task(id: int, db: Session=Depends(get_db)):
    return delete_task(db, id)
