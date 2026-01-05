file_path = "task-folder/dec 25/4-12-25/Food_Nutrition_Dataset.csv"

import csv

with open(file_path, "r", encoding="utf-8") as fr:
    reader = csv.DictReader(fr)
    data = list(reader)


#total number of foods
total_foods = len(data)
# print(total_foods)


# # which category has more food
# all_category_list = [food.get("category") for food in data]
# category_wise_food_count = {category : all_category_list.count(category) for category in set(all_category_list)}
# category_with_most_food_count = [cat for cat,count in category_wise_food_count.items() if count == max(category_wise_food_count.values())]
# print(f"category_with_most_food_count : {category_with_most_food_count}")


# # # foods with high protein
highest_protein = max(float(food.get("protein")) for food in data)
high_protein_foods = [food.get("food_name") for food in data if float(food.get("protein")) == highest_protein]
# print(f"high_protein_foods : {high_protein_foods}")


# # # foods with low protein
lowest_protein = min(float(food.get("protein")) for food in data if food.get("protein"))
low_protein_foods = [food.get("food_name") for food in data if float(food.get("protein")) == lowest_protein]
print(f"low_protein_foods : {low_protein_foods}")