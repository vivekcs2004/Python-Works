# # 1️⃣ Print numbers from 1 to N
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)

print_1_to_n(5)


# # 2️⃣ Sum of first N natural numbers
# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)

# print(sum_n(5))


# # 3️⃣ Factorial of a number
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))


# # 4️⃣ Nth Fibonacci number
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))


# # 5️⃣ Count number of digits
# def count_digits(num):
#     if num == 0:
#         return 0
#     return 1 + count_digits(num // 10)

# print(count_digits(12345))


# # 6️⃣ Sum of digits
# def sum_of_digits(num):
#     if num == 0:
#         return 0
#     return num % 10 + sum_of_digits(num // 10)

# print(sum_of_digits(123))


# # 7️⃣ Reverse a number (numeric, not string hack)
# def reverse_number(num, rev=0):
#     if num == 0:
#         return rev
#     return reverse_number(num // 10, rev * 10 + num % 10)

# print(reverse_number(124))


# # 8️⃣ Palindrome check (string)
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])

# print(is_palindrome("madam"))


# # 9️⃣ Power of a number
# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)

# print(power(2, 5))


# 🔟 GCD of two numbers  
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(48, 18))
