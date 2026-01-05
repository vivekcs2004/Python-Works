file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/words.txt"

fr = open(file_path,"r")

result = []

for line in fr:
    
    line = line.rstrip("\n")

    word = line.replace(" ","")

    result.append(word)

print(result)