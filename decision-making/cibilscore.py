cs = int(input("enter cibil score :"))

if cs in range(300,550):
    print("poor")
elif cs in range(550,650):
    print("average")
elif cs in range(650,750):
    print("good")
elif cs in range(750,901):
    print("excellent")
else:
    print("invalid")