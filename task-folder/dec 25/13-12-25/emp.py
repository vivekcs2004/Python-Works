import csv

file_path = "task-folder/dec 25/13-12-25/employee_salary_dataset.csv"   

fr = open(file_path, "r", encoding="utf-8")
reader = csv.DictReader(fr)
data = list(reader)
fr.close()

# Q1 Print first 5 employee names
# for e in data[:5]:
    # print(e["Name"])

# # Q2 Count total employees
# print("Total employees =", len(data))

# # Q3 List unique departments
# departments = list({e["Department"] for e in data})
# print(departments)

# # Q4 Employees with more than 10 years of experience
# exp_10 = [e["Name"] for e in data if int(e["Experience_Years"]) > 10]
# print(exp_10)

# # Q5 Count employees with Master's degree
# masters = [e for e in data if e["Education_Level"] == "Master"]
# print("Master's Degree Count =", len(masters))

# # Q6 Employees older than 45
# older_45 = [e["Name"] for e in data if int(e["Age"]) > 45]
# print(older_45)

# # Q7 Average monthly salary
# salaries = [int(e["Monthly_Salary"]) for e in data]
# avg_salary = sum(salaries) / len(salaries)
# print(avg_salary)

# # Q8 All employees from Bangalore
# blr = [e["Name"] for e in data if e["City"] == "Bangalore"]
# print(blr)

# # Q9 Highest salary employee
# top_salary = max(data, key=lambda x: int(x["Monthly_Salary"]))
# print(top_salary["Name"], top_salary["Monthly_Salary"])

# # Q10 Count employees by gender
gender_count = {}
for e in data:
    g = e["Gender"]
    gender_count[g] = gender_count.get(g, 0) + 1
print(gender_count)
