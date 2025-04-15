from faker import Faker
import pandas as pd
import random

# Initialize Faker and create an instance
fake = Faker()

# Define lists for the new fields
species_list = ['Lion', 'Elephant', 'Wolf', 'Tiger', 'Giraffe', 'Zebra', 'Cheetah', 'Bear', 'Leopard', 'Rhino']
breeds = ['African', 'Asian', 'Siberian', 'Bengal', 'Indochinese', 'Sumatran', 'Indian', 'Mountain', 'Snow', 'Arctic']
danger_levels = ['High', 'Medium', 'Low']
varieties = ['Common', 'Uncommon', 'Rare']

# Function to generate random data for animals
def generate_animal_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        animal = {
            'id': i,  # Sequential IDs from 1 to num_records
            'name': fake.first_name(),  # Random animal name
            'species': random.choice(species_list),  # Random species
            'breed': random.choice(breeds),  # Random breed
            'type': random.choice(['Predator', 'Herbivore', 'Omnivore']),  # Random type
            'danger_level': random.choice(danger_levels),  # Random danger level
            'variety': random.choice(varieties)  # Random variety (e.g. Common, Rare)
        }
        data.append(animal)
    return data

# Generate 1000 records
num_records = 1000
animal_data = generate_animal_data(num_records)

# Convert to DataFrame
df = pd.DataFrame(animal_data)

# Save the data to 'animals.csv' in raw folder
df.to_csv('data/raw/animals.csv', index=False)

print(f"{num_records} records of animal data have been generated and saved to 'data/raw/animals.csv'")
