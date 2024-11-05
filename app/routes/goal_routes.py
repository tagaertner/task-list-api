from flask import Blueprint
from app import db
from app.models.goal import Goal
from flask import request

goals_bp = Blueprint("goals_bp", __name__, url_prefix="/goals")

@goals_bp.post("")
def create_goal():
    request_body = request.get_json()
    
    new_goal = Goal.from_dict(request_body)
    db.session.add(new_goal)
    db.session.commit()
    
    return {
        "goal": new_goal.to_dict()
    }, 201
    

@goals_bp.get("")
def get_goals():
    goals = Goal.query.all()
    goals_list = [goal.to_dict() for goal in goals]
    return goals_list, 200

@goals_bp.get("/<goal_id>")
def get_goal(goal_id):
    goal = Goal.query.get(goal_id)
    
    return {
        "goal": goal.to_dict()
        }, 200
    

