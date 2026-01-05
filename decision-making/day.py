day = int(input("enter a day btwn 1-7 :  "))

if day<=5 and day>0 :
    print("weekday")

elif day>5 and day<=7 :
    print("weekend")

else :
    print("invalid")
