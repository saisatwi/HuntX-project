import pandas as pd
import random

# Define possible event types and outcomes
event_types = ['Animal Encounter', 'Dangerous Challenge', 'Treasure Found']
event_outcomes = ['Success', 'Failure']

# Number of events (we will generate 1000 events)
num_events = 1000

# Generate event data
events_data = {
    'event_id': [f'Event_{i}' for i in range(1, num_events + 1)],
    'hunter_id': [f'Hunter_{random.randint(1, 1000)}' for _ in range(num_events)],
    'event_type': [random.choice(event_types) for _ in range(num_events)],
    'event_description': [
        f'Encountered a {random.choice(["rare animal", "dangerous obstacle", "hidden treasure"])}.' 
        for _ in range(num_events)
    ],
    'event_outcome': [random.choice(event_outcomes) for _ in range(num_events)]
}

# Create DataFrame
events_df = pd.DataFrame(events_data)

# Save to CSV
events_df.to_csv('data/processed/hunter_events.csv', index=False)

print("Hunter events data generated successfully!")
