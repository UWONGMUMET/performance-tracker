from sqlalchemy.orm import Session
from models.task import Task
from fastapi import HTTPException

def create_task(db: Session, user, data):
    task = Task(
        title=data.title,
        description=data.description,
        due_date=data.due_date,
        user_id=user.get("sub")
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_all_tasks(db: Session, user):
    if user.get("role") == "ADMIN":
        return db.query(Task).all()
    return db.query(Task).filter(Task.user_id == user.get("sub")).all()

def get_task_by_id(db: Session, task_id: str, user):
    query = db.query(Task).filter(Task.id == task_id)
    if user.get("role") != "ADMIN!":
        query = query.filter(Task.user_id == user.get("sub"))
    
    task = query.first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


def update_task(db: Session, task_id: str, user, data):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if user.get("role") != "ADMIN" and task.user_id != user.get("sub"):
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: str, user):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if user.get("role") != "ADMIN" and task.user_id != user.get("sub"):
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")

    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}