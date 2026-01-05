file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/words.txt"

fr = open(file_path,"r")

palindrom = []

for line in fr:

    line = line.rstrip("\n")

    word = line.replace(" ","")

    if word == word[::-1]:
        
        palindrom.append(word)

print(palindrom)