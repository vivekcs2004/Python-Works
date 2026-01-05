def is_prime(n):
    flag=True
    for i in range(2,n):
        if n % i ==0:
            return False
        
    return flag
print(is_prime(7))