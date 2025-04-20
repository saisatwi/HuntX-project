import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/raw/hunting_logs.csv")

# Add new column: hunt_result
def get_result(row):
    if row["event_type"] == "hunt_success":
        return "Success"
    elif row["event_type"] == "hunt_failed":
        return "Failed"
    else:
        return "None"

df["hunt_result"] = df.apply(get_result, axis=1)

# Add is_danger column
df["is_danger"] = df["damage"] > 50

# Add energy_category column
def get_energy(cat):
    if cat < 200:
        return "Low"
    elif cat < 600:
        return "Medium"
    else:
        return "High"

df["energy_category"] = df["calories_burned"].apply(get_energy)

# Save to processed
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/hunting_logs_transformed.csv", index=False)
print("✅ Transformed hunting logs saved to data/processed/hunting_logs_transformed.csv")
