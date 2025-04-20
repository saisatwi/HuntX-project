import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate a random interaction
def generate_interaction(hunter_id):
    interaction_types = ["Vital Check", "Location Update", "Advice"]
    interaction_time = datetime.now() - timedelta(days=random.randint(0, 30))  # Random time in past month
    interaction_details = f"Check: Heart Rate - {random.choice(['Normal', 'High', 'Low'])}" if random.choice([True, False]) else "Location Update: Jungle"
    interaction_type = random.choice(interaction_types)
    
    return {
        "interaction_id": f"INT{hunter_id}{random.randint(1000, 9999)}",
        "hunter_id": hunter_id,
        "interaction_type": interaction_type,
        "interaction_time": interaction_time,
        "interaction_details": interaction_details
    }

# Generate AI interactions for 1000 hunters
data = [generate_interaction(hunter_id) for hunter_id in range(1, 1001)]

# Create a DataFrame
ai_interactions_df = pd.DataFrame(data)

# Save it as CSV in processed folder
ai_interactions_df.to_csv('data/processed/ai_interactions.csv', index=False)

print("AI interactions data generated successfully!")
