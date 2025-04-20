import random
import pandas as pd
from datetime import datetime

# Define some sample rare encounters
rare_animals = pd.read_csv("data/processed/rare_animals.csv")
terrain_types = ["Jungle", "Desert", "Arctic", "Forest"]

# Generate random encounters
def generate_rare_encounters(num_encounters=10):
    encounters = []
    for _ in range(num_encounters):
        animal = rare_animals.sample(1).iloc[0]
        encounter = {
            "encounter_id": random.randint(1000, 9999),
            "animal_id": animal["rare_animal_id"],
            "terrain_type": random.choice(terrain_types),
            "event_type": random.choice(["Ambush", "Boss Battle", "Loot Drop"]),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        encounters.append(encounter)

    return pd.DataFrame(encounters)

# Generate and save encounters
encounters = generate_rare_encounters()
encounters.to_csv("data/processed/rare_encounters.csv", index=False)
print("Generated rare encounters and saved to CSV.")
