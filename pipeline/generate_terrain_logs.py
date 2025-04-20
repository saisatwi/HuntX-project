import random
import pandas as pd

# List of terrain types
terrain_types = ['Jungle', 'Desert', 'Arctic', 'Mountain', 'Forest', 'Swamp', 'Cave', 'Plains', 'Savannah', 'Tundra']

# Generate data for 1000 hunters (hunter IDs)
hunter_ids = range(1, 1001)  # 1000 hunters

# Generate random terrain type, difficulty level, and hunter action for each hunter
terrain_type = [random.choice(terrain_types) for _ in hunter_ids]
difficulty = [random.randint(1, 50) for _ in hunter_ids]
action = [random.choice(['Hunted Animal', 'Rested', 'Lost in Terrain', 'Found Shelter']) for _ in hunter_ids]

# Create a DataFrame to store the terrain log data
terrain_logs = pd.DataFrame({
    'Hunter_ID': hunter_ids,
    'Terrain_Type': terrain_type,
    'Difficulty': difficulty,
    'Action': action
})

# Save the terrain log data to CSV in the 'processed' folder
terrain_logs.to_csv('data/processed/terrain_logs.csv', index=False)

print("Terrain log data generated and saved.")
