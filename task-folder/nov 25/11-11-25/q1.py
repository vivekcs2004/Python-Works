# TASK 1 
# arr = [1, 5, 7, 9, 12, 15, 16, 19, 20].
# a. Print all Even Numbers
# b. Print all Odd numbers.
# c. Count odd numbers
# d. Count even numbers.

arr = [1, 5, 7, 9, 12, 15, 16, 19, 20]

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even numbers are :", *even)
print("odd numbers are :", *odd)


odd_count = 0
even_count = 0
for c in arr:
    if c%2 == 0:
        even_count+=1
    else:
        odd_count+=1
print("total even numbers : ",even_count)
print("total odd numbers : ",odd_count)

       