import pandas as pd
import random

# Predefined terrain options
terrains = [
    'Jungle', 'Desert', 'Arctic', 'Savanna', 'Rainforest',
    'Volcanic', 'Swamp', 'Mountain', 'Urban Ruins', 'Tundra'
]

# List to store all hunter stats
data = []

# Generate stats for 1000 hunters
for hunter in range(1, 1001):  # Loop through 1000 hunters
    hunter_id = f"H{hunter:04d}"  # Format as H0001, H0002, ..., H1000
    fame = 0
    xp = 0

    # Generate stats for 100 days
    for day in range(1, 101):  # Loop through 100 days
        animals_hunted = random.randint(0, 5)
        money_earned = animals_hunted * random.randint(100, 1000)
        fame += animals_hunted * random.randint(5, 15)
        xp += animals_hunted * 10

        # Hunter's daily entry
        entry = {
            "hunter_id": hunter_id,
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

# Create DataFrame from the generated data
df = pd.DataFrame(data)

# Save the data to CSV
df.to_csv("data/raw/hunter_stats_1000.csv", index=False)
print("Hunter stats for 1000 hunters over 100 days generated and saved.")
