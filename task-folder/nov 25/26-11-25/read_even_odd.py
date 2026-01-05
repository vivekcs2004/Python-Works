file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/task-folder/26-11-25/numbers.txt"

fr = open(file_path,"r")
odd = []
even = []

for line in fr:
    
    n = int(line.rstrip("/n"))

    if n%2 == 0:
        even.append(n)

    else:
        odd.append(n)
        
print(even)
print(odd)


