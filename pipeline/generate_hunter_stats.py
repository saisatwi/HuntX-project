import pandas as pd
import random

terrains = [
    'Jungle', 'Desert', 'Arctic', 'Savanna', 'Rainforest',
    'Volcanic', 'Swamp', 'Mountain', 'Urban Ruins', 'Tundra'
]

data = []

fame = 0
xp = 0

for day in range(1, 101):
    animals_hunted = random.randint(0, 5)
    money_earned = animals_hunted * random.randint(100, 1000)
    fame += animals_hunted * random.randint(5, 15)
    xp += animals_hunted * 10

    entry = {
        "hunter_id": "H001",
        "day": day,
        "terrain_visited": random.choice(terrains),
        "animals_hunted": animals_hunted,
        "health": random.randint(50, 100),
        "stamina": random.randint(30, 100),
        "fame": fame,
        "money_earned": money_earned,
        "experience_points": xp
    }
    data.append(entry)

df = pd.DataFrame(data)
df.to_csv("data/raw/hunter_stats.csv", index=False)
print("Hunter stats generated and saved.")
