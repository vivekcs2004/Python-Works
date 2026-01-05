arr = [3,4,12,13,14,20,22]

even_arr = []
odd_arr = []

for i in arr:
    if i % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)

print("even numbers are :", even_arr)
print("odd numbers are :", odd_arr)