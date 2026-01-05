numbers_path = "error-handling/numbers.txt"

try:
    fr = open(numbers_path,"r")

    num_lst = []

    for line in fr:

        line = line.rstrip("\n")

        try:
            num_lst.append(int(line))

        except Exception as e:
            continue
except Exception as e:
    print(e)      


print("max : ",max(num_lst))
print("min : ",min(num_lst))
print("sum : ",sum(num_lst))

num_count = { num : num_lst.count(num) for num in num_lst}

max_value = max(num_count.values())

frequent_numbers = [k for k,v in num_count.items() if v == max_value]

print("frequent number: ",frequent_numbers)



    

