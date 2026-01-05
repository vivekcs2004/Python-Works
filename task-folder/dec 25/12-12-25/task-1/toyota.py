import csv

file_path = "task-folder/dec 25/12-12-25/task-1/toyota.csv"

fr = open(file_path, "r", encoding="utf-8")
reader = csv.DictReader(fr)
data = list(reader)


# Q1 Print first 5 models
# for r in data[:5]:
#     print(r["model"])

# Q2 Count total cars
# print("Total cars =", len(data))

# Q3 List unique years
years = list({r["year"] for r in data})
# print(years)

# Q4 List all Manual car models
manual_cars = [r["model"] for r in data if r["transmission"] == "Manual"]
# print(manual_cars)

# Q5 Cars priced above 20,000
expensive = [r["model"] for r in data if float(r["price"]) > 20000]
# print(expensive)

# Q6 Car models with MPG above 35
good_mpg = [r["model"] for r in data if float(r["mpg"]) > 35]
# print(good_mpg)

# Q7 All Petrol cars
petrol = [r["model"] for r in data if r["fuelType"] == "Petrol"]
# print(petrol)
                                                                                                                                                                                                        

# Q8 Cheapest car
cheapest = min(data, key=lambda x: float(x["price"]))
# print(cheapest["model"], cheapest["price"])

# Q9 Car with highest mileage
highest_mileage = max(data, key=lambda x: float(x["mileage"]))
# print(highest_mileage["model"], highest_mileage["mileage"])

# Q10 Count cars by transmission type
tr_count = {}
for r in data:
    t = r["transmission"]
    tr_count[t] = tr_count.get(t, 0) + 1
print(tr_count)
