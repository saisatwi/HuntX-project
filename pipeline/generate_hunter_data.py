import pandas as pd
import random
from faker import Faker
import os

# Initialize Faker
fake = Faker()

# Load terrain data from processed folder
terrain_df = pd.read_csv('data/processed/terrain_main.csv')

# Generate 1000 hunters aligned to terrains
hunter_data = []
for i in range(1000):
    hunter_id = f"H-{1000 + i}"
    name = fake.name()
    age = random.randint(18, 50)
    experience = random.randint(1, 20)

    # Assign terrain (rotating through available terrains)
    assigned_terrain = terrain_df.iloc[i % len(terrain_df)]
    terrain_type = assigned_terrain["terrain_type"]
    terrain_difficulty = assigned_terrain["difficulty"]  # ✅ fixed here

    hunter_data.append({
        "hunter_id": hunter_id,
        "name": name,
        "age": age,
        "experience": experience,
        "terrain_type": terrain_type,
        "terrain_difficulty": terrain_difficulty
    })

# Create DataFrame and save it
df_hunters = pd.DataFrame(hunter_data)

# Make sure the output folder exists
os.makedirs("data/processed", exist_ok=True)

# Save the CSV
df_hunters.to_csv("data/processed/hunter_data.csv", index=False)
print("✅ 1000 hunters saved to data/processed/hunter_data.csv")
