n1 = int(input("enter num 1 : "))
n2 = int(input("enter num 2 : "))

largest = n1 if n1>n2 else n2
smallest =n1 if n1<n2 else n2

print("max : ",largest)
print("min : ",smallest)