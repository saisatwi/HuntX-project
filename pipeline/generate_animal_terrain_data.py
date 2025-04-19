import pandas as pd
import random

# Predefined terrain options
terrains = [
    'Jungle', 'Desert', 'Arctic', 'Savanna', 'Rainforest',
    'Volcanic', 'Swamp', 'Mountain', 'Urban Ruins', 'Tundra'
]

# List of animal species and types (you can expand this)
species = ['Lion', 'Elephant', 'Wolf', 'Tiger', 'Bear', 'Giraffe', 'Zebra', 'Cheetah', 'Rhino', 'Fox']
types = ['Predator', 'Herbivore', 'Omnivore']

# Create the DataFrame
data = []

# Generate 1000 animals, assign to terrains
for animal_id in range(1, 1001):
    animal_name = random.choice(species)
    animal_type = random.choice(types)
    terrain = random.choice(terrains)
    rarity = random.choice(['Common', 'Uncommon', 'Rare', 'Epic'])
    
    # Randomly assigning a difficulty level for terrain
    difficulty_level = random.randint(1, 50)

    # Animal entry
    entry = {
        "id": animal_id,
        "name": animal_name,
        "type": animal_type,
        "terrain": terrain,
        "rarity": rarity,
        "difficulty_level": difficulty_level
    }
    data.append(entry)

# Create DataFrame from the generated data
df = pd.DataFrame(data)

# Save the data to CSV
df.to_csv("data/raw/animals_with_terrain.csv", index=False)
print("Animal data with terrain generated and saved.")
