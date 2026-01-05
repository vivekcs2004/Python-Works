file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/task-folder/26-11-25/perf_num.txt"

fr = open(file_path, "r")

for n in fr:
    n = n.rstrip("\n")
    print(n[-1])