lst = ["10","20","hello","300","hai","4 00"]

#error handling
#sum,min,max,sort


num_list = []

for i in lst:

    try:
        num = int(i)

        num_list.append(num)

    except Exception as e:

        continue

max_element = max(num_list)
min_element = min(num_list)
srt_numbers = sorted(num_list)
total       = sum(num_list)

print(max_element)
print(min_element)
print(srt_numbers)
print(total)


    
