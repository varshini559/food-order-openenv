def grade(data):
    score = 0

    if data["cost"] <= data["budget"]:
        score += 0.3

    if data["preference_match"]:
        score += 0.3

    if data["delivery_time"] < 30:
        score += 0.2

    if data["rating"] > 4.5:
        score += 0.2

    return round(min(score, 1.0), 2)