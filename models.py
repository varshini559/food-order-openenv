from pydantic import BaseModel
from typing import List

class State(BaseModel):
    customer_budget: int
    preferences: List[str]
    location: str

class Action(BaseModel):
    restaurant: str

class StepResponse(BaseModel):
    state: State
    reward: float
    done: bool
    info: dict