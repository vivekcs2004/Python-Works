import csv

file_path = "indian_food.csv"   

fr = open(file_path, "r", encoding="utf-8")
reader = csv.DictReader(fr)
data = list(reader)
fr.close()

# # Q1 Print first 5 sweet names
# for s in data[:5]:
#     print(s["name"])

# # Q2 Count total sweets
# print("Total sweets =", len(data))

# # Q3 List all unique states
# states = list({s["state"] for s in data})
# print(states)

# # Q4 List all unique regions
# regions = list({s["region"] for s in data})
# print(regions)

# # Q5 List all vegetarian sweets
# veg_sweets = [s["name"] for s in data if s["diet"] == "vegetarian"]
# print(veg_sweets)

# # Q6 List all desserts (course = dessert)
# desserts = [s["name"] for s in data if s["course"] == "dessert"]
# print(desserts)

# # Q7 List sweets from West Bengal
# wb_sweets = [s["name"] for s in data if s["state"] == "West Bengal"]
# print(wb_sweets)

# # Q8 List sweets from Odisha
# odisha_sweets = [s["name"] for s in data if s["state"] == "Odisha"]
# print(odisha_sweets)

# # Q9 List sweets with sweet flavor profile
# sweet_flavor = [s["name"] for s in data if s["flavor_profile"] == "sweet"]
# print(sweet_flavor)

# # Q10 Print sweets with prep_time <= 15
# quick_prep = [s["name"] for s in data if s["prep_time"] != "-1" and int(s["prep_time"]) <= 15]
# print(quick_prep)

# # Q11 Print sweets with cook_time <= 30
# quick_cook = [s["name"] for s in data if s["cook_time"] != "-1" and int(s["cook_time"]) <= 30]
# print(quick_cook)

# # Q12 Count sweets from East region
# east_count = len([s for s in data if s["region"] == "East"])
# print("East region count =", east_count)

# # Q13 Count sweets from North region
# north_count = len([s for s in data if s["region"] == "North"])
# print("North region count =", north_count)

# # Q14 Print all sweets that use sugar
# with_sugar = [s["name"] for s in data if "sugar" in s["ingredients"].lower()]
# print(with_sugar)

# # Q15 Print all sweets that use milk
# with_milk = [s["name"] for s in data if "milk" in s["ingredients"].lower()]
# print(with_milk)

# # Q16 Print all sweets from Rajasthan
# rajasthan_sweets = [s["name"] for s in data if s["state"] == "Rajasthan"]
# print(rajasthan_sweets)

# # Q17 Print all sweets from Uttar Pradesh
# up_sweets = [s["name"] for s in data if s["state"] == "Uttar Pradesh"]
# print(up_sweets)

# # Q18 Print sweets with prep_time = -1
# unknown_prep = [s["name"] for s in data if s["prep_time"] == "-1"]
# print(unknown_prep)

# # Q19 Print sweets with cook_time >= 60
# long_cook = [s["name"] for s in data if s["cook_time"] != "-1" and int(s["cook_time"]) >= 60]
# print(long_cook)

# # Q20 Print sweet name and state
name_state = [(s["name"], s["state"]) for s in data]
print(name_state)
