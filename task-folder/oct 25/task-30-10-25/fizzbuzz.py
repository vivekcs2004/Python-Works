#fizz if div by 3,buzz if 5,fizzbuzz both
i=1
while i<=20:
    if i%5==0 and i%3==0:
                print("fizzbuzz")
    if i % 3 == 0:
        print("fizz") 
    if i % 5 ==0:
            print("buzz")
    else:
        print(i)  
    i+=1              