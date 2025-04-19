import pandas as pd

# Read raw terrain data
df = pd.read_csv("data/raw/terrain.csv")

# Optional: Clean or check for missing values
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("data/processed/cleaned_terrain.csv", index=False)

print("Terrain data ingested and cleaned successfully.")
