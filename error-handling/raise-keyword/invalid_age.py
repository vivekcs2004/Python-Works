age = int(input("Enter age: "))

if age<0:
    raise Exception("Invalid age") #custom error throw
else:
    print("ok")