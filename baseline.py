from environment import reset, step
from models import Action

def run_baseline():
    state = reset()

    if "veg" in state.preferences:
        restaurant = "Veg Delight"
    else:
        restaurant = "Spicy Hub"

    total_reward = 0

    for _ in range(3):
        action = Action(restaurant=restaurant)
        result = step(action)
        total_reward += result.reward

    return round(total_reward / 3, 2)