num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))

last_digit_num1 = num1%10
last_digit_num2 = num2%10

sum = last_digit_num1+last_digit_num2

print(sum>5)
