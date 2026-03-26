from fastapi import FastAPI
from environment import reset, step, state
from baseline import run_baseline
from tasks import tasks_list
from grader import grade
from models import Action

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Food Ordering OpenEnv Running"}

@app.get("/reset")
def reset_api():
    return reset()

@app.get("/state")
def state_api():
    return state()

@app.post("/step")
def step_api(action: Action):
    return step(action)

@app.get("/tasks")
def tasks_api():
    return tasks_list

@app.get("/baseline")
def baseline_api():
    return {"score": run_baseline()}

@app.post("/grader")
def grader_api(data: dict):
    return {"score": grade(data)}