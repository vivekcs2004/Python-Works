def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n % i == 0 :
            sum = sum+i
    result = " perfect number" if n == sum else  "perfect number"      
    return result           
print(perfect_num(6))
    

    

        
        
            