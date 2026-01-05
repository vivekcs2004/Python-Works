file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/task-folder/26-11-25/names.txt"

fr = open(file_path,"r")

for name in fr:
    name = name.rstrip("\n")
    print(f"name :{name},first char : {name[0]},last char : {name[-1]}")