# recursion : a function calling itself


# def say_hi(limit):

#     if limit==0:

#         return
    
#     print("hai")

#     return say_hi(limit-1)

# say_hi(5)



# def display_hello_world(limit):

#     if limit == 0:

#         return
    
#     print("hello world!")

#     return display_hello_world(limit-1)

# display_hello_world(5)


#sum of n digits
# def sum_of_n(limit):

#     if limit==1:
#         return 1

#     return limit+sum_of_n(limit-1)

# print(sum_of_n(5))


"""
sum_of_n(5)
5+sum_of(4)=>5+10=>15
4+sum_of(3)=>4+6=>10
3+sum_of(2)=>3+3=>6
2+sum_of(1)=>2+1=>3
sum_of(1)=>1

"""

#factorial

# def fact(num):

#     if num==0:
#         return 1
    
#     return num*fact(num-1)

# print(fact(5))



"""
fact(5)
5 * fact(4)
5 * 4 * fact(3)
5 * 4 * 3 * fact(2)
5 * 4 * 3 * 2 * fact(1)
5 * 4 * 3 * 2 * 1 * fact(0)
120
"""


#sum of digits
# def sum_of_dig(num):

#     if num == 0:

#         return 0
    
#     return num%10+sum_of_dig(num//10)

# print(sum_of_dig(21))


#product of digits

# def product(num):

#     if num == 0:

#         return 1
    
#     return num%10*product(num//10)

# print(product(45))


#reverse of a digit

def reverse(num):

    if num == 0:

        return ""
    
    return str(num%10)+str(reverse(num//10))

print(reverse(124))
    






















    