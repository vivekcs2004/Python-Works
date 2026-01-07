from json import load

file_path = "JSON_WORKS\\jobs.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

for j in data:

    print(j.get("title"))