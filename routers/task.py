from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.task import TaskCreate, TaskUpdate, TaskResponse
from services.task_service import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from core.dependencies import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_task(db, user, task)

@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_all_tasks(db, user)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_task_by_id(db, task_id, user)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: str, task: TaskUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return update_task(db, task_id, user, task)

@router.delete("/{task_id}", response_model=dict)
def delete_task_endpoint(task_id: str, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return delete_task(db, task_id, user)