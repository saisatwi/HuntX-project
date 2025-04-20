import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate a random economy record
def generate_economy_record(hunter_id):
    items_list = ["Health Potion", "Weapon", "Armor", "Map", "Boots"]
    money = random.randint(500, 5000)  # Random money earned
    fame = random.randint(1, 100)  # Random fame points earned
    items_collected = random.sample(items_list, k=random.randint(1, 3))  # Random items collected
    transaction_date = datetime.now() - timedelta(days=random.randint(0, 30))  # Random time in past month
    
    return {
        "economy_id": f"ECON{hunter_id}{random.randint(1000, 9999)}",
        "hunter_id": hunter_id,
        "money": money,
        "fame": fame,
        "items_collected": ", ".join(items_collected),
        "transaction_date": transaction_date
    }

# Generate economy records for 1000 hunters
data = [generate_economy_record(hunter_id) for hunter_id in range(1, 1001)]

# Create a DataFrame
economy_df = pd.DataFrame(data)

# Save it as CSV in processed folder
economy_df.to_csv('data/processed/economy_data.csv', index=False)

print("Economy data generated successfully!")
