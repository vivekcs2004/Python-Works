file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/numbers.txt"

fr = open(file_path,"r")

result = []

for line in fr:

    line = line.rstrip("\n")

    rev = line[::-1]

    result.append(rev)

print("reversed list",result)
    

