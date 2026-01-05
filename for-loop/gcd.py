num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))

smallest_num = min(num1,num2)

gcd = 0

for i in range(1,smallest_num+1):

    if num1%i==0 and num2%i==0 :
        gcd=i

print(gcd)        

