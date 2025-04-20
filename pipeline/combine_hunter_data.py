import pandas as pd

# Load the hunter stats and event data
hunter_stats_df = pd.read_csv('data/raw/hunter_stats.csv')  # Hunter stats is in 'raw' folder
events_df = pd.read_csv('data/processed/hunter_events.csv')  # Hunter events is in 'processed' folder

# Merge the two DataFrames based on 'hunter_id'
combined_df = pd.merge(hunter_stats_df, events_df, on='hunter_id', how='inner')

# Save the combined dataset to CSV in the 'processed' folder
combined_df.to_csv('data/processed/combined_hunter_data.csv', index=False)

print("Combined hunter stats and events data generated successfully!")
