db_pass = "vivek"
db_otp = 8888

password = input("enter your password : ")

if db_pass == password:
    
    otp = int(input("enter otp : "))
    
    if otp == db_otp:
        print("login success")
    
    else:
        print("wrong otp")

else:
    print("incorrect password")