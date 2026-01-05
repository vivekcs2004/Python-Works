num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))

i=1
small = 0

if num1>num2:
    small = num2

else:
    small = num1

while(i<=small):

    if num1%i==0 and num2%i==0 :

        print(i)

    i+=1    

