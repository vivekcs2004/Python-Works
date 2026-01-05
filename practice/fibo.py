class IsFibonacciNumber:

    def solution(self, number):

        is_fibo_number = True  

        p = 0
        c = 1

        while p < number:
            temp = p + c
            p = c
            c = temp

        
        if p != number:
            is_fibo_number = False
        
        return is_fibo_number
    
instance = IsFibonacciNumber()
print(instance.solution(1))