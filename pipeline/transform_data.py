import pandas as pd
import os

input_path = os.path.join("data", "processed", "cleaned_animals.csv")
output_path = os.path.join("data", "processed", "transformed_animals.csv")

df = pd.read_csv(input_path)

def get_species(animal_type):
    if animal_type.lower() == "predator":
        return "Carnivora"
    elif animal_type.lower() == "herbivore":
        return "Herbivora"
    else:
        return "Unknown"

df["species"] = df["type"].apply(get_species)

df.to_csv(output_path, index=False)

print("✅ Transformed data saved to:", output_path)
print(df.head())
