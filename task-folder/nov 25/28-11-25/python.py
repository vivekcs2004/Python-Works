file_path = "task-folder/nov 25/28-11-25/python_basics_report.csv"
import csv


fr = open(file_path, "r", encoding="utf-8")

reader = csv.DictReader(fr)
data = list(reader)

# Q1 Read & Print File
for s in data:
    print(s)

# Q2 Count students
total_students = len(data)
print("Total students =", total_students)

# Q3 Only Names
names = [s.get("NAME") for s in data]
print(names)

# Q4 Students in Python batch
python_batch = [s.get("NAME") for s in data if s.get("BATCH") == "Python"]
print(python_batch)

# Q5 Students with 100% attendance
perfect_attendance = [s.get("NAME") for s in data if s.get("PRESENT_%") == "100"]
print(perfect_attendance)

# Q6 Name + MCQ1
name_mcq1 = [(s.get("NAME"), s.get("MCQ1")) for s in data]
print(name_mcq1)

# Q7 Convert to list → already done (data)
print(data)

# Medium Q1 Highest overall  (FIXED: ignore "-" entries)
clean_overall = [s for s in data if s["OVERALL"] not in ("", "-")]
top_student = max(clean_overall, key=lambda s: float(s["OVERALL"]))
print("Top performer =", top_student["NAME"], top_student["OVERALL"])

# Medium Q2 Low performers < 30  (FIXED: ignore "-" entries)
low_performers = [
    (s["NAME"], s["OVERALL"])
    for s in clean_overall
    if float(s["OVERALL"]) < 30
]
print(low_performers)

# Medium Q3 Contains missing values "-"
missing_values = [s["NAME"] for s in data if any("-" in v for v in s.values())]
print(missing_values)
