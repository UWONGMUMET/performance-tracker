from sqlalchemy.orm import Session
from models.user import User
from sqlalchemy import func
from datetime import datetime, date, timedelta

def get_dashboard_stats(db: Session):
    total_users = db.query(func.count(User.id)).scalar()
    active_users = db.query(func.count(User.id)).filter(User.is_active == True).scalar()
    inactive_users = db.query(func.count(User.id)).filter(User.is_active == False).scalar()

    today = date.today()
    new_users_today = db.query(func.count(User.id)).filter(func.date(User.created_at) == today).scalar()

    recent_users = db.query(User).order_by(User.created_at.desc()).limit(5).all()
    
    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": inactive_users,
        "new_users_today": new_users_today,
        "recent_users": [
            {
                "id": user.id,
                "email": user.email,
                "created_at": user.created_at
            } for user in recent_users
        ]
    }

def users_per_day(db: Session):
    last_7_days = datetime.now() - timedelta(days=7)

    data = db.query(
        func.date(User.created_at),
        func.count(User.id)
    ).filter(
        User.created_at >= last_7_days
    ).group_by(
        func.date(User.created_at)
    ).all()

    return [
        {
            "date": record[0],
            "count": record[1]
        } for record in data
    ]