def max_two(n1,n2):

    return n1 if n1>n2 else n2

print(max_two(200,500))

#return true if number is odd else false
def is_odd(n):

    return True if n%2 != 0 else False

print(is_odd(5))

#create a function last_digit_max of two number

def last_digit_max(n1,n2):
    return n1 if n1%10 > n2%10 else n2

print(last_digit_max(192,356))

#largest odd number

def is_leap_year(year):

    return True if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0) else False

print(is_leap_year(2012))
print(is_leap_year(2013))
print(is_leap_year(2014))

