import random
import pandas as pd
from faker import Faker

# Initialize Faker for random data generation
fake = Faker()

# Load the animals and terrain data
animals = pd.read_csv('data/raw/animals.csv')
terrains = pd.read_csv('data/raw/terrain.csv')

# Function to generate a game event
def generate_game_event():
    event = {
        'event_id': fake.uuid4(),  # Generate unique event ID
        'event_type': random.choice(['encounter', 'boss_battle', 'danger']),  # Randomly pick event type
        'animal_id': random.choice(animals['id']),  # Use 'id' as animal ID
        'terrain_name': random.choice(terrains['terrain_name']),  # Use 'terrain_name' from terrain.csv
        'event_time': fake.date_time_this_year(),  # Generate event time within the current year
        'result': random.choice(['hunter_defeated', 'hunter_escaped', 'animal_fled']),  # Random event result
        'reward': random.randint(10, 100)  # Random reward points for the event
    }
    return event

# Generate a list of game events
events = [generate_game_event() for _ in range(1000)]  # Adjust number of events as needed

# Convert list of events to a DataFrame and save to CSV
events_df = pd.DataFrame(events)
events_df.to_csv('data/processed/game_events.csv', index=False)

print("Game events generated and saved to 'data/processed/game_events.csv'.")
