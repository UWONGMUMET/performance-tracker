from sqlalchemy.orm import Session
from sqlalchemy import func
from models.task import Task
from datetime import datetime, timedelta

def get_task_dashboard_stats(db: Session):
    total_task = db.query(func.count(Task.id)).scalar()

    pending_tasks = db.query(func.count(Task.id)).filter(
        Task.status == "PENDING"
    ).scalar()

    done_tasks = db.query(func.count(Task.id)).filter(
        Task.status == "DONE"
    ).scalar()

    overdue_tasks = db.query(func.count(Task.id)).filter(
        Task.due_date < datetime.utcnow(),
        Task.status != "DONE"
    ).scalar()

    return {
        "total_tasks": total_task,
        "pending_tasks": pending_tasks,
        "done_tasks": done_tasks,
        "overdue_tasks": overdue_tasks
    }

def get_tasks_per_day(db: Session):
    last_7_days = datetime.utcnow() - timedelta(days=7)

    data = db.query(
        func.date(Task.created_at),
        func.count(Task.id)
    ).filter(
        Task.created_at >= last_7_days
    ).group_by(
        func.date(Task.created_at)
    ).all()

    return [
        {
            "date": record[0],
            "count": record[1]
        } for record in data
    ]