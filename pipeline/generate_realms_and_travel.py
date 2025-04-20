import pandas as pd
import random
from datetime import datetime

# Create Realms Data (if not already created)
realms_data = [
    {'realm_id': 1, 'realm_name': 'Forest', 'difficulty_level': 10, 'climate': 'Tropical', 'special_features': 'Hidden Lakes'},
    {'realm_id': 2, 'realm_name': 'Desert', 'difficulty_level': 40, 'climate': 'Arid', 'special_features': 'Mirages'},
    {'realm_id': 3, 'realm_name': 'Arctic', 'difficulty_level': 50, 'climate': 'Polar', 'special_features': 'Blizzards'},
    {'realm_id': 4, 'realm_name': 'Mountain', 'difficulty_level': 30, 'climate': 'Temperate', 'special_features': 'Rock Slides'},
    {'realm_id': 5, 'realm_name': 'Jungle', 'difficulty_level': 20, 'climate': 'Tropical', 'special_features': 'Dense Foliage'},
]

# Convert to DataFrame
realms_df = pd.DataFrame(realms_data)

# Save Realms Data to CSV (processed folder)
realms_df.to_csv('data/processed/realms.csv', index=False)

# Example Function to Create Travel Log
def create_travel_log(hunter_id, start_realm_id, destination_realm_id):
    distance_traveled = random.randint(50, 200)  # Random distance between realms
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    travel_log = {
        'hunter_id': hunter_id,
        'start_realm_id': start_realm_id,
        'destination_realm_id': destination_realm_id,
        'distance_traveled': distance_traveled,
        'timestamp': timestamp
    }
    
    return travel_log

# Simulate travel log entries (for 3 hunters)
travel_logs = []
for hunter_id in range(1, 4):
    start_realm_id = random.choice([1, 2, 3, 4, 5])
    destination_realm_id = random.choice([1, 2, 3, 4, 5])
    travel_log = create_travel_log(hunter_id, start_realm_id, destination_realm_id)
    travel_logs.append(travel_log)

# Convert travel logs to DataFrame and Save
travel_logs_df = pd.DataFrame(travel_logs)
travel_logs_df.to_csv('data/processed/travel_logs.csv', index=False)

print("Realms and Travel Logs have been successfully generated and saved.")
