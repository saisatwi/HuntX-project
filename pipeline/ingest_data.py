import pandas as pd

# Load the raw data
raw_data_path = 'data/raw/animals.csv'
raw_data = pd.read_csv(raw_data_path)

# Display a preview of the raw data
print("Raw data preview:")
print(raw_data.head())

# Clean the data (for example, removing empty values or cleaning columns)
cleaned_data = raw_data.dropna()

# Save cleaned data
cleaned_data_path = 'data/processed/cleaned_animals.csv'
cleaned_data.to_csv(cleaned_data_path, index=False)

print(f"Cleaned data saved at {cleaned_data_path}")