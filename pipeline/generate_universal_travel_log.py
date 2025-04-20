import pandas as pd
import random
from datetime import datetime, timedelta

# Load existing realms
realms = ['Jungle', 'Desert', 'Arctic', 'Forest', 'Mountain']

# Load existing hunters (assuming hunter data is in hunter_data.csv)
hunter_df = pd.read_csv('data/processed/hunter_data.csv')

# Initialize list to store travel log events
travel_log = []

# Function to generate random travel log
def generate_travel_log(num_entries=100):
    for i in range(num_entries):
        hunter_id = random.choice(hunter_df['hunter_id'])  # Randomly pick a hunter
        from_realm = random.choice(realms)
        to_realm = random.choice([realm for realm in realms if realm != from_realm])  # Ensure it's a different realm
        timestamp = datetime.now() + timedelta(hours=random.randint(1, 1000))  # Random time in future
        travel_id = f"T{1000 + i}"  # Unique travel_id

        travel_log.append([hunter_id, travel_id, from_realm, to_realm, timestamp])

# Generate 1000 random travel log entries
generate_travel_log(1000)

# Convert to DataFrame and save as CSV
travel_log_df = pd.DataFrame(travel_log, columns=['hunter_id', 'travel_id', 'from_realm', 'to_realm', 'timestamp'])
travel_log_df.to_csv('data/processed/universal_travel_log.csv', index=False)

print("Universal travel log generated successfully!")
