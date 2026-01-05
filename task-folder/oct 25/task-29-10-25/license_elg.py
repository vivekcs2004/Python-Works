# Driving License Eligibility

age = int(input("enter your age : "))

if age>=18:

    test = input("did you pass the test yes or no : ")

    if test=="yes":
        print("license approved")

    else:
        print("Test not cleared")

else:
    print("Not eligible due to age")
 