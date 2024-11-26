def generate_training_plan(weight, height, experience, focus, days_per_week):
    if experience == "beginner":
        if days_per_week == 3:
            return ["Day 1: Full Body", "Day 2: Rest", "Day 3: Full Body", "Day 4: Rest", "Day 5: Full Body"]
        elif days_per_week == 4:
            return ["Day 1: Upper Body", "Day 2: Lower Body", "Day 3: Rest", "Day 4: Upper Body", "Day 5: Lower Body"]
    elif experience == "intermediate":
        return ["Custom split based on your inputs..."]
    elif experience == "advanced":
        return ["Push/Pull/Legs, 6 days a week"]
    else:
        return ["Default: 3 days full body workout"]

    return ["Example plan based on inputs"]
