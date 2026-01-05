students = {
    "101": {"name": "Rahul", "age": 14, "grade": "B"},
    "102": {"name": "Anita", "age": 15, "grade": "A"}
}

for k, v in students.items():
    if k == "102":
        pass
        print(v.get("name"))

# update rahul's grade
for v in students.values():
    if v.get("name") == "Rahul":
        v["grade"] = "A+"

# students.update()
students.update({"103": {"name": "Vikram", "age": 16, "grade": "B+"}})

# id with names
for k, v in students.items():
    print(f"{k} : {v.get('name')}")
