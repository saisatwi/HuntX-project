# pipeline/generate_main_terrain.py

import pandas as pd
import random
import os

# Load the base terrain types
terrain_df = pd.read_csv("data/raw/terrain.csv")  # base file with 10 terrain types

# Generate 1000 terrain entries by randomly assigning terrain types and difficulty
terrain_types = terrain_df['terrain_name'].tolist()
data = []

for i in range(1000):
    terrain_type = random.choice(terrain_types)
    difficulty = random.randint(1, 50)
    data.append({
        'terrain_id': f"T{i+1:04}",
        'terrain_type': terrain_type,
        'difficulty': difficulty
    })

# Create DataFrame
main_terrain_df = pd.DataFrame(data)

# Save to processed folder
os.makedirs("data/processed", exist_ok=True)
main_terrain_df.to_csv("data/processed/terrain_main.csv", index=False)

print("✅ terrain_main.csv created with 1000 terrains!")
