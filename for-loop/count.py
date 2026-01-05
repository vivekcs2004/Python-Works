number = int(input("enter number : "))

even = 0
odd = 0

for i in range(1,number+1):

    if i%2==0:
        even=even+1
    
    else:
        odd = odd+1

print("even number count",even)
print("odd number count",odd)