# creata function common_divisor with one parameter number
# return common divisors of number

def common_divisor(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

common_divisor(16)
