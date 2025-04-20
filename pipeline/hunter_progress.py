import pandas as pd
import random
from faker import Faker

# Initialize Faker for random data generation
fake = Faker()

# Load data
animals = pd.read_csv('data/raw/animals.csv')
terrains = pd.read_csv('data/raw/terrain.csv')

# Initialize hunter stats (you can expand this based on more attributes you want to track)
hunter_stats = {
    'hunter_id': [],
    'terrain_explored': [],
    'animals_hunted': [],
    'xp_earned': [],
    'money_earned': [],
    'fame': [],
}

# Function to simulate a hunter's journey and update stats
def simulate_hunters_progress():
    for hunter_id in range(1, 101):  # Simulate for 100 hunters (you can increase the number as needed)
        terrain_explored = random.choice(terrains['terrain_name'])  # Random terrain from terrain.csv
        animals_hunted = random.choice(animals['id'])  # Random animal ID from animals.csv
        xp_earned = random.randint(50, 150)  # Random XP earned from event (adjust as per game rules)
        money_earned = random.randint(100, 500)  # Random money earned (you can use a better system)
        fame = random.choice(['Low', 'Medium', 'High'])  # Fame based on performance

        hunter_stats['hunter_id'].append(hunter_id)
        hunter_stats['terrain_explored'].append(terrain_explored)
        hunter_stats['animals_hunted'].append(animals_hunted)
        hunter_stats['xp_earned'].append(xp_earned)
        hunter_stats['money_earned'].append(money_earned)
        hunter_stats['fame'].append(fame)

# Simulate for 100 hunters
simulate_hunters_progress()

# Convert to DataFrame and save as CSV
hunter_progress_df = pd.DataFrame(hunter_stats)
hunter_progress_df.to_csv('data/processed/hunter_progress.csv', index=False)

print("Hunter progress data generated and saved to 'data/processed/hunter_progress.csv'.")
