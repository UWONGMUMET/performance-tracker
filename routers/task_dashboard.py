from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from core.dependencies import admin_required
from services.task_dashboard_service import get_task_dashboard_stats, get_tasks_per_day

router = APIRouter(prefix="/task-dashboard", tags=["task-dashboard"])
@router.get("/stats", dependencies=[Depends(admin_required)])
def task_stats(
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return get_task_dashboard_stats(db)

@router.get("/tasks-per-day", dependencies=[Depends(admin_required)])
def tasks_per_day(
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return get_tasks_per_day(db)