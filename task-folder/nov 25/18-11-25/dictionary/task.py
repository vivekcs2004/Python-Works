# 1. Create a Dictionary
student = {"name": "Rahul", "age": 14, "grade": "B"}

# a. Access Value by Key
print(student["name"])

# b. Add a New Key-Value Pair
student["school"] = "City High School"
print(student)

# c. Update a Value
student["grade"] = "A+"
print(student)

# d. Delete a Key
student.pop("age")
print(student)

# e. Check if Key Exists
print("name exists:", "name" in student)

# f. Length of Dictionary
print("Total items:", len(student))

# g. Loop through Keys
print("Keys:", ", ".join(student.keys()))

# h. Loop through Values
print("Values:", ", ".join(student.values()))

# i. Loop through Items
print("Key -> Value:")
for key, value in student.items():
    print(f"{key} -> {value}")
