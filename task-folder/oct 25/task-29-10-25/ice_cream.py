#  Ice Cream Flavors

print("Ice Cream Flavors")
print("1. Chocolate")
print("2. Vanilla")
print("3.Strawberry")
print("4.Butterscotch" )
ice_cream = int(input("enter your choice 1-4 : "))

match ice_cream:

    case 1:
        print("Chocolate")
    case 2:
        print("Vanilla")
    case 3:
        print("Strawberry")
    case 4:
        print("Butterscotch")
    case _:
        print("invalid")



