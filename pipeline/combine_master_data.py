import pandas as pd
import random

# Step 1: Load CSVs
terrain_data = pd.read_csv('data/raw/terrain.csv')
animal_data = pd.read_csv('data/raw/animals.csv')
hunter_data = pd.read_csv('data/processed/hunter.csv')

# Step 2: Clean column names
terrain_data.columns = terrain_data.columns.str.strip().str.lower()
animal_data.columns = animal_data.columns.str.strip().str.lower()
hunter_data.columns = hunter_data.columns.str.strip().str.lower()

# Step 3: Add mock hunter_id and terrain_id to animal_data to allow merging
# Simulate random assignments from hunter_data and terrain_data
animal_data['hunter_id'] = random.choices(hunter_data['hunter_id'].astype(str).tolist(), k=len(animal_data))
animal_data['terrain_name'] = random.choices(terrain_data['terrain_name'].astype(str).tolist(), k=len(animal_data))

# Convert data types for merge
animal_data['hunter_id'] = animal_data['hunter_id'].astype(str)
hunter_data['hunter_id'] = hunter_data['hunter_id'].astype(str)

# Merge with hunter_data
merged_1 = pd.merge(animal_data, hunter_data, on='hunter_id', how='left')

# Merge with terrain_data on terrain_name
terrain_data['terrain_name'] = terrain_data['terrain_name'].astype(str)
merged_final = pd.merge(merged_1, terrain_data, on='terrain_name', how='left')

# Save final master dataset
merged_final.to_csv('data/processed/master_data.csv', index=False)

print("✅ Merged data saved to: data/processed/master_data.csv")
print("📊 Null values in merged data:\n", merged_final.isnull().sum())
