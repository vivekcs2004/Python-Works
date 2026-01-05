db_pin = 1124

db_balance = 5000

pin = int(input("enter PIN : "))

if db_pin == pin:

    amount = int(input("enter amount : "))

    if amount <= db_balance:
        print("transaction success")

    else:
        print("insuffient balance")

else:
    print("wrong pin")