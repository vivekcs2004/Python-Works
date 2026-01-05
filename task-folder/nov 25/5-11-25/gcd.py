# create a function gcd with two parameter num1,num2
# return gcd of two numbers

def gcd(num1, num2):
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd

print(gcd(12, 16))
