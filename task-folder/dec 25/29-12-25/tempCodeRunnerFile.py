long_cook = [s["name"] for s in data if s["cook_time"] != "-1" and int(s["cook_time"]) >= 60]
print(long_cook)