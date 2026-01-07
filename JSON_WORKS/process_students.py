from json import load

file_path ="JSON_WORKS/students.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

# for st in data:

#     print(st.get("name") )


# 