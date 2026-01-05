import csv

file_path = "task-folder/dec 25/15-12-25/dog_breeds.csv"   

fr = open(file_path, "r", encoding="utf-8")
reader = csv.DictReader(fr)
data = list(reader)
fr.close()

# Q1 Print first 5 dog breeds
# for d in data[:5]:
#     print(d["Breed"])

# # Q2 Count total dog breeds
# print("Total breeds =", len(data))

# # Q3 List unique countries of origin
# countries = list({d["Country of Origin"] for d in data})
# print(countries)

# # Q4 List all breeds from Germany
# german_breeds = [d["Breed"] for d in data if d["Country of Origin"] == "Germany"]
# print(german_breeds)

# # Q5 List all breeds with Brown eye color
# brown_eyes = [d["Breed"] for d in data if "Brown" in d["Color of Eyes"]]
# print(brown_eyes)

# # Q6 List breeds with longevity more than 12 years
# long_life = [
#     d["Breed"]
#     for d in data
#     if int(d["Longevity (yrs)"].split("-")[1]) > 12
# ]
# print(long_life)

# # Q7 List breeds that mention 'energetic' in character traits
# energetic_dogs = [
#     d["Breed"]
#     for d in data
#     if "energetic" in d["Character Traits"].lower()
# ]
# print(energetic_dogs)

# # Q8 Count breeds that have hip dysplasia listed
# hip_dysplasia = [
#     d["Breed"]
#     for d in data
#     if "hip dysplasia" in d["Common Health Problems"].lower()
# ]
# print("Hip dysplasia count =", len(hip_dysplasia))

# # Q9 List all breeds from France
# french_breeds = [d["Breed"] for d in data if d["Country of Origin"] == "France"]
# print(french_breeds)

# # Q10 Print breed name and longevity
# breed_longevity = [(d["Breed"], d["Longevity (yrs)"]) for d in data]
# print(breed_longevity)
