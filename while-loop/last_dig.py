number = int(input("enter number : ")) #1899

while (number!=0): #1899!=0 189!=0 18!=0 1!=0 0==0
    
    last_digit = number % 10 #last_digit = 1899%10=9 189%10=9 18%10=8 1%10=1

    print(last_digit) #9 9 8 1

    number = number // 10 #number = 1899//10=1890 1890//10=189 189//18 18//10=1