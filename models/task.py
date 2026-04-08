from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
import uuid
from db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    status = Column(String, default="PENDING")
    user_id = Column(String, ForeignKey("users.id"))

    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)