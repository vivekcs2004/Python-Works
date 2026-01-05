number = int(input("enter the number : ")) #234

while (number!=0): #234!=0
    last_digit = number%10 #last_digit = 234%10 = 4
    sq=last_digit**2 #sq=4**2

    print(sq) #16

    number = number//10 #234//10 = 23