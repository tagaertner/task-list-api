from flask import Blueprint, request, abort, make_response, Response, json
from app import db
from app.models.task import Task
from datetime import datetime

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")  # Note: task_bp not taks_bp

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()
    
    if "title" not in request_body or "description" not in request_body:
        return{"details": "Invalid data"}, 400
 
    new_task = Task(
        title=request_body["title"],
        description=request_body["description"],
        completed_at=None,  
        is_complete=False   
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return {"task": new_task.to_dict()}, 201

@tasks_bp.get("")
def get_tasks():
    tasks = Task.query.all()
    sort_param = request.args.get("sort")
    
    sort_options ={
        "asc": Task.title.asc(),
        "desc": Task.title.desc()
    }
    
    query = db.select(Task)
    if sort_param in sort_options:
        query= query.order_by(sort_options[sort_param])
        
    tasks = db.session.scalars(query).all()
    return [task.to_dict() for task in tasks], 200

@tasks_bp.get("/<task_id>")
def get_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return {"message": f"task {task_id} not found"}, 404

    return {"task": task.to_dict()}, 200  


@tasks_bp.patch("/<task_id>/mark_complete")
def mark_complete(task_id):
    task = Task.query.get(int(task_id))
    
    if not task:
        return {"message": f"Task {task_id} not found"}, 404
    
    task.completed_at = datetime.now()
    task.is_complete = True
    db.session.commit()
    
    return {"task": task.to_dict()}, 200

@tasks_bp.patch("/<task_id>/mark_incomplete")
def mark_incomplete(task_id):
    task = Task.query.get(int(task_id))
    
    if not task:
        return {"message": f"Task {task_id} not found"}, 404
    
    task.completed_at = None
    task.is_complete = False
    db.session.commit()
    
    return {"task": task.to_dict()}, 200
    
@tasks_bp.put("/<task_id>")
def update_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return {"message": f"Task {task_id} not found"}, 404
    
    request_body = request.get_json()
    task.title = request_body["title"]
    task.description = request_body["description"]
    
    db.session.commit()
  
    return {"task": task.to_dict()}, 200

@tasks_bp.delete("/<task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return {"message": f"Task {task_id} not found"}, 404
    
    task_title = task.title
    db.session.delete(task)
    db.session.commit()
    
    return {
          "details": f'Task {task_id} "{task_title}" successfully deleted'
    }, 200
    
