file_path = "task-folder\\dec 25\\9-12-25\\mental_health_social_media_dataset.csv"

import csv

fr = open(file_path,"r",encoding="utf-8")

reader = csv.DictReader(fr)
data = list(reader)

# # 1. How many total people are in the dataset?
# total_people = len(data)
# print(total_people)

# # 2. How many users are Male?
# male_count = sum(1 for row in data if row.get("gender") == "Male")
# print(male_count)



# # 4. What is the average daily screen time?
# avg_screen = sum(int(row.get("daily_screen_time_min")) for row in data) / len(data)
# print(avg_screen)

# # 5. Who has the highest social media usage?
# max_social = max(int(row.get("social_media_time_min")) for row in data)
# highest_user = [row.get("person_name") for row in data if int(row.get("social_media_time_min")) == max_social]
# print(highest_user)

# # 6. Count how many users are 'Stressed'.
# stressed_count = sum(1 for row in data if row.get("mental_state") == "Stressed")
# print(stressed_count)

# # 7. Get the person with the lowest sleep hours.
# min_sleep = min(float(row.get("sleep_hours")) for row in data)
# low_sleep_person = [row.get("person_name") for row in data if float(row.get("sleep_hours")) == min_sleep]
# print(low_sleep_person)

# # 8. Average negative interactions per user.
# avg_negative = sum(int(row.get("negative_interactions_count")) for row in data) / len(data)
# print(avg_negative)

# # 9. Who has the highest anxiety level?
# max_anxiety = max(float(row.get("anxiety_level")) for row in data)
# anxious_person = [row.get("person_name") for row in data if float(row.get("anxiety_level")) == max_anxiety]
# print(anxious_person)

# 10. How many users are marked Healthy?
healthy_count = sum(1 for row in data if row.get("mental_state") == "Healthy")
print(healthy_count)
