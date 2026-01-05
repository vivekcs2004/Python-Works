for r in range(1,6):
    for s in range(0,r):
        print(" ",end="")
    for c in  range(6-r,0,-1):
        print("* ",end="")
    print()
