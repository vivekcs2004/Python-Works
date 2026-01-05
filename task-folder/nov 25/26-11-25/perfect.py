file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/task-folder/26-11-25/perf_num.txt"

fr = open(file_path, "r")

perfect_num = []

for num in fr:
    number = int(num.rstrip("/n"))
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i

    if sum == number:
        perfect_num.append(number)

print(perfect_num)
