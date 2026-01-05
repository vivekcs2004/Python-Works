file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/task-folder/26-11-25/perf_num.txt"

fr = open(file_path, "r")

last_dig = {int(num):int(num)%10 for num in fr}
print(last_dig)