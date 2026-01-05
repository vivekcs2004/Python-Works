# Positive Number – Even or Odd

num = int(input("enter a  number : "))

if num>0 and num%2==0:
    print("positive even number")

elif num>0 and num%2!=0:
    print("positive odd number")
    
else:
    print("not a positive number")