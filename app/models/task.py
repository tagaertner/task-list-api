from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime
from app import db

class Task(db.Model):
    __tablename__ = "task_list_api_development"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[datetime] = mapped_column(nullable=True, default=None)
    is_complete: Mapped[bool] = mapped_column(nullable=True) 
    # (nullable=False, default=False)
    

    
    def to_dict(self):
    # Return only the fields expected by the test
        is_complete_value = False if self.completed_at is None else True
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": is_complete_value
    }
    
 
       