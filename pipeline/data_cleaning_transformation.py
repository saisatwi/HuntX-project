

import pandas as pd

# Sample data for illustration (assuming you have your own dataset loaded here)
master_data = pd.DataFrame({
    'danger_level_x': ['High', 'Low', 'Medium', 'High', None, 'Low', 'Medium', 'High', None]
})

# Create a dictionary to map 'High', 'Medium', 'Low' to numeric values
danger_level_mapping = {
    'High': 3,
    'Medium': 2,
    'Low': 1
}

# Map the danger levels to numeric values
master_data['danger_level_x'] = master_data['danger_level_x'].map(danger_level_mapping)

# Fill NaN values with the median (using numeric values now)
master_data['danger_level_x'].fillna(master_data['danger_level_x'].median(), inplace=True)

# If you want to map it back to the original string values, you can reverse the mapping
reverse_danger_level_mapping = {v: k for k, v in danger_level_mapping.items()}
master_data['danger_level_x'] = master_data['danger_level_x'].map(reverse_danger_level_mapping)

print(master_data)
