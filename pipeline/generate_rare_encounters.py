import pandas as pd
import random
from faker import Faker

fake = Faker()

# Load hunter IDs from hunter stats
hunter_stats_path = 'data/raw/hunter_stats.csv'
hunter_df = pd.read_csv(hunter_stats_path)

# Ensure 'hunter_id' exists in hunter_df
if 'hunter_id' not in hunter_df.columns:
    raise ValueError("❌ hunter_id column not found in hunter_stats.csv")

hunter_ids = hunter_df['hunter_id'].tolist()

# Generate rare encounters
rare_encounters = []

rare_animals = ['Shadow Panther', 'Crystal Tiger', 'Storm Eagle', 'Ghost Serpent', 'Titan Wolf']

for _ in range(100):
    encounter = {
        'encounter_id': fake.uuid4(),
        'hunter_id': random.choice(hunter_ids),
        'animal': random.choice(rare_animals),
        'location': fake.city(),
        'date': fake.date_this_year(),
        'rarity_score': round(random.uniform(8.5, 10.0), 2)
    }
    rare_encounters.append(encounter)

df = pd.DataFrame(rare_encounters)
df.to_csv('data/processed/rare_encounters.csv', index=False)

print("✅ Fixed rare_encounters.csv generated with 'hunter_id'")
