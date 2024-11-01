from flask import Blueprint, request
from app import db
from app.models.task import Task

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")  # Note: task_bp not taks_bp

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()
    
    new_task = Task(
        title=request_body["title"],
        description=request_body["description"],
        completed_at=request_body["completed_at"]
        
        
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return {"task":new_task.to_dict()}, 201 
    
    

    