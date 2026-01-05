day = int(input("enter a day 1-7 : "))

if day in range(1,6):

    print("weekday")

elif day in range(6,8):

    print("weekend")

else:
    
    print("INVALID")