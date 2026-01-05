for r in range(1,5):
    for s in range(5-r,0,-1):
        print(" ",end="")
    for c in range(0,r):
        print("* ",end="")
    print()
for r in range(3,0,-1):
    for s in range(5-r,0,-1):
        print(" ",end="")
    for c in range(0,r):
        print("* ",end="")
    print()
