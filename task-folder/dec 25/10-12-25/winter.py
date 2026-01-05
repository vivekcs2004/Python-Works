import csv

file_path = "task-folder/dec 25/10-12-25/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, "r", encoding="utf-8")
reader = csv.DictReader(fr)
data = list(reader)

# Q1 Print num of rows
# print(len(data))

# Q2 Count total products
# total_products = len(data)
# print("Total products =", total_products)

# Q3 Show only Brand names
# brands = [i.get("Brand") for i in data]
# print(brands)

# Q4 Items priced above $300
# expensive_items = [i.get("Brand") for i in data if float(i["Price(USD)"]) > 300]
# print(expensive_items)

# # Q5 Items with Customer Rating >= 4.5
# high_rated = [i.get("Brand") for i in data if float(i["Customer_Rating"]) >= 4.5]
# print(high_rated)

# # Q6 Filter all Winter 2025 products
# winter_2025 = [i for i in data if i["Season"] == "Winter 2025"]
# print(winter_2025)

# # Q7 Show Brand + Popularity Score
# brand_popularity = [(i["Brand"], i["Popularity_Score"]) for i in data]
# print(brand_popularity)

# # Q8 Find highest priced item
# max_price_item = max(data, key=lambda x: float(x["Price(USD)"]))
# print("Highest priced item =", max_price_item["Brand"], max_price_item["Price(USD)"])

# # Q9 All products marked Trending
# trending_items = [i["Brand"] for i in data if i["Trend_Status"] == "Trending"]
# print(trending_items)

# # Q10 Items made of Cashmere
cashmere_items = [i["Brand"] for i in data if i["Material"] == "Cashmere"]
print(cashmere_items)
