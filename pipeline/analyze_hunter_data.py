import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the transformed hunter data (make sure the path is correct)
df_hunters = pd.read_csv('../data/processed/transformed_hunter_data.csv')

# Check the first few rows of the data to confirm it is loaded correctly
print(df_hunters.head())

# Calculate basic statistics
average_rewards = df_hunters['total_rewards'].mean()
average_health = df_hunters['health'].mean()
terrain_counts = df_hunters['terrain_id'].value_counts()

# Print the results
print(f"Average Rewards: {average_rewards}")
print(f"Average Health: {average_health}")
print(f"Terrain Counts:\n{terrain_counts}")


# Plotting Distribution of Rewards
plt.figure(figsize=(10, 6))
sns.histplot(df_hunters['total_rewards'], bins=20, kde=True)
plt.title("Distribution of Rewards")
plt.xlabel("Total Rewards")
plt.ylabel("Frequency")
plt.show()



# Plotting Health vs. Progress
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_hunters, x='health', y='progress', hue='terrain_id', palette='Set2')
plt.title("Hunter Health vs. Progress")
plt.xlabel("Health")
plt.ylabel("Progress (%)")
plt.show()


# Saving Analysis Data to CSV (for future reporting)
analysis_df = df_hunters[['id', 'name', 'terrain_id', 'total_rewards', 'health', 'experience']]
analysis_df.to_csv('../data/processed/hunter_analysis_data.csv', index=False)

print("Hunter analysis data saved successfully.")
