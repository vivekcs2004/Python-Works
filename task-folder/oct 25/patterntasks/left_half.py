for r in range(1,6): #1,2,3,4,5

    for s in range(5-r,0,-1): #5-1,5-2,5-3,5-4,5-5
      print(" ",end=" ")

    for c in range(0,r): # *,**,***,****,*****
      print("*",end=" ")
    print()