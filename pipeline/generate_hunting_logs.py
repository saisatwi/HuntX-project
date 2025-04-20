import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()

# Load hunter data
hunter_df = pd.read_csv("data/processed/hunter_data.csv")

# List of event types
event_types = ["encounter", "hunt_success", "hunt_failed", "injured", "bike_travel"]

# Voice assistant messages
voice_msgs = [
    "Stay alert!",
    "Nice shot!",
    "Be careful!",
    "Scan complete.",
    "Enemy nearby!",
    "Mission success.",
    "Low health warning!"
]

# Generate event logs
events = []
start_time = datetime(2025, 4, 1)

for i in range(10000):
    event_id = f"E-{10000 + i}"
    timestamp = (start_time + timedelta(minutes=random.randint(0, 100000))).strftime("%Y-%m-%d %H:%M:%S")
    
    hunter = hunter_df.sample(1).iloc[0]
    hunter_id = hunter["hunter_id"]
    terrain_type = hunter["terrain_type"]

    event_type = random.choice(event_types)
    animal_id = f"A-{random.randint(100, 999)}" if event_type in ["encounter", "hunt_success", "hunt_failed"] else None
    damage = random.randint(10, 100) if event_type == "injured" else 0
    calories_burned = random.randint(50, 1000)
    voice_msg = random.choice(voice_msgs)

    events.append({
        "event_id": event_id,
        "timestamp": timestamp,
        "hunter_id": hunter_id,
        "terrain_type": terrain_type,
        "event_type": event_type,
        "animal_id": animal_id,
        "damage": damage,
        "calories_burned": calories_burned,
        "voice_msg": voice_msg
    })

# Create DataFrame
df_events = pd.DataFrame(events)

# Ensure folder exists
os.makedirs("data/raw", exist_ok=True)

# Save
df_events.to_csv("data/raw/hunting_logs.csv", index=False)
print("✅ 10,000+ hunting events saved to data/raw/hunting_logs.csv")
