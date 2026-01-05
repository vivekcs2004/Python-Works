import csv

file_path = "task-folder/dec 25/18-12-25/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, "r", encoding="utf-8-sig")

reader = csv.DictReader(fr)
data = list(reader)
fr.close()

# Q1 Print first 5 rows
# for r in data[:5]:
#     print(r)

# # Q2 Count total rows
# print("Total rows =", len(data))

# # Q3 List all unique Report_Section values
# sections = list({r["Report_Section"] for r in data})
# print(sections)

# # Q4 Count how many rows belong to CATEGORY_PERFORMANCE
# category_perf = [r for r in data if r["Report_Section"] == "CATEGORY_PERFORMANCE"]
# print("CATEGORY_PERFORMANCE count =", len(category_perf))

# # Q5 Print all Dimensions under TOP_SELLING_PRODUCTS
# top_products = [r["Dimension"] for r in data if r["Report_Section"] == "TOP_SELLING_PRODUCTS"]
# print(top_products)


# # Q6 Print all STATE_WISE_SALES dimensions (state names)
# for r in data:
#     if r["Report_Section"] == "STATE_WISE_SALES":
#         print(r["Dimension"])

# # Q7 Print Metric1 values for PAYMENT_METHOD_PREFERENCES
# for r in data:
#     if r["Report_Section"] == "PAYMENT_METHOD_PREFERENCES":
#         print(r["Metric1"])

# # Q8 Count MONTHLY_SALES_TRENDS rows
# count = 0
# for r in data:
#     if r["Report_Section"] == "MONTHLY_SALES_TRENDS":
#         count += 1
# print("MONTHLY_SALES_TRENDS count =", count)

# # Q9 Print all TOP_SELLING_PRODUCTS names
# for r in data:
#     if r["Report_Section"] == "TOP_SELLING_PRODUCTS":
#         print(r["Dimension"])

# # Q10 Print Dimension for HIGH_VALUE_ORDERS
for r in data:
    if r["Report_Section"] == "HIGH_VALUE_ORDERS":
        print(r["Dimension"])
