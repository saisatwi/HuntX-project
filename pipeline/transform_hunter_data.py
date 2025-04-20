import pandas as pd

# Load the original hunter data
df_hunters = pd.read_csv('../data/Processed/hunter.csv')

# Example transformation: Convert rewards to a percentage of max rewards (as an example transformation)
max_rewards = df_hunters['total_rewards'].max()
df_hunters['reward_percentage'] = df_hunters['total_rewards'] / max_rewards * 100

# Save the transformed data
df_hunters.to_csv('../data/Processed/transformed_hunter_data.csv', index=False)

print("Transformed data saved successfully.")
