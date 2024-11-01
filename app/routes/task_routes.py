from flask import Blueprint, request, abort, make_response, Response
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
    
 
@tasks_bp.get("/<task_id>")
def get_one_task(task_id):
    task = valiadate_one_task(task_id)
   
    return {
            "task":{
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "is_complete": task.completed_at
            }
    }
       
@tasks_bp.get("/tasks")
def get_all_task():
    query = db.select(Task)
    tasks = db.session.scalars(query).all()
    tasks_response = [task.to_dict() for task in tasks]
    return tasks_response



@tasks_bp.get("")
def get_zero_task():
    tasks = []
    return tasks, 200

@tasks_bp.put("/<task_id>")
def update_task(task_id):
    tasks = Task.query.all()
    task = validate_task(task_id,tasks)
    db.session.commit()
    return {
        "task": {
            "id":  task.id,
            "title": task.title,
            "description" : task.description,
            "is_complete": task.is_complete
            }
     }
    
@tasks_bp.delete("/<task_id>")
def delete_taks(task_id):
    task = valiadate_one_task(task_id)
    title = task.title
    db.session.delete(task)
    db.session.commit()
    
    return {
          "details": f'Task {task_id} {title} successfully deleted'
    }, 200
    

def valiadate_one_task(task_id):
    try:
        task_id = int(task_id)
    except:
        response = {"message": f"task {task_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Task).where(Task.id == task_id)
    task = db.session.scalar(query)

    if not task:
        response = {"message": f"{task_id} not found"}
        abort(make_response(response, 404))

    return task

def validate_task(task_id, tasks):

    try:
       task_id = int(task_id)
    except:
        abort(make_response({"message": f"Task id {task_id} invalid"}, 400))

    for task in tasks:
        if task.id == task_id:
            return task

    abort(make_response({"message": f"Task {task_id} not found"}, 404))
    
def validate_task_data(request_body):
    if not request_body or "task" not in request_body:
        abort(make_response({"details": "Invalid data"}, 400))
    
    task_data = request_body["task"]
    
    required_fields =["title", "description"]
    for field in required_fields:
        if field not in task_data or not task_data[field]:
            abort(make_response({"details": "Invaild data"}, 400))
    return task_data