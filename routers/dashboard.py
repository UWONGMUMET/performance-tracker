from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services.dashboard_service import get_dashboard_stats

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/stats")
def dashboard_stats(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)