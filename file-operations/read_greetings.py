file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/greetings.txt"

fr = open(file_path,"r")

st = {line.rstrip("\n") for line in fr}


print(st)