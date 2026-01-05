file_path = "error-handling\\nums.txt"

fr = open(file_path,"r")

num_list = []

for line in fr:
    line = line.rstrip("\n")

    try:
        num = int(line)
        num_list.append(num)

    except Exception as e:
        continue
# print(num_list)

even_numbers = []

even = [num for num in num_list if num%2==0]

# even_numbers.append(even)

# print(even_numbers)

even_count = {num : even.count(num) for num in even}

max_count = max(even_count.values())

frequent_numbers = [k for k,v in even_count.items() if v == max_count]

print(frequent_numbers)


