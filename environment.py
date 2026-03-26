from models import State, Action, StepResponse
import random

restaurants = [
    {"name": "Veg Delight", "type": "veg", "rating": 4.5, "base_cost": 200},
    {"name": "Spicy Hub", "type": "non-veg", "rating": 4.2, "base_cost": 250},
    {"name": "Healthy Bites", "type": "veg", "rating": 4.8, "base_cost": 300}
]

current_state = None
step_count = 0

def reset():
    global current_state, step_count
    step_count = 0

    current_state = State(
        customer_budget=random.randint(200, 500),
        preferences=random.choice([["veg"], ["non-veg"], ["low_spicy"]]),
        location=random.choice(["urban", "semi-urban"])
    )
    return current_state


def state():
    return current_state


def dynamic_pricing(base_cost):
    surge = random.uniform(0.8, 1.5)
    return int(base_cost * surge)


def step(action: Action):
    global current_state, step_count

    step_count += 1
    reward = 0

    selected_restaurant = next(
        (r for r in restaurants if r["name"] == action.restaurant), None
    )

    if not selected_restaurant:
        return StepResponse(state=current_state, reward=0, done=True, info={"error": "Invalid restaurant"})

    cost = dynamic_pricing(selected_restaurant["base_cost"])
    delivery_time = random.randint(15, 45)

    if cost <= current_state.customer_budget:
        reward += 0.3
    else:
        reward -= 0.2

    if selected_restaurant["type"] in current_state.preferences:
        reward += 0.3

    if delivery_time < 30:
        reward += 0.2

    if selected_restaurant["rating"] > 4.5:
        reward += 0.2

    reward = max(0, min(reward, 1))
    done = step_count >= 3

    return StepResponse(
        state=current_state,
        reward=round(reward, 2),
        done=done,
        info={
            "restaurant": selected_restaurant["name"],
            "cost": cost,
            "delivery_time": delivery_time
        }
    )