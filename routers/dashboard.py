from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services.dashboard_service import get_dashboard_stats, users_per_day
from core.dependencies import admin_required

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/stats", dependencies=[Depends(admin_required)])
def dashboard_stats(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)

@router.get("/users-chart", dependencies=[Depends(admin_required)])
def chart(db: Session = Depends(get_db)):
    return users_per_day(db)