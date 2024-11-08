from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from datetime import datetime
from app import db
from typing import List
from .task import Task

class Goal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
    tasks: Mapped[List["Task"]] = relationship(back_populates="goal")
    
    
    def to_dict(self):
            
        return {
            "id": self.id,
            "title": self.title
        }
    
    @classmethod
    def from_dict(cls, goal_data):
        new_goal = cls(
            title=goal_data["title"]
        )
        return new_goal