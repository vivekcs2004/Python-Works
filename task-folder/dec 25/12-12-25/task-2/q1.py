# 1. Print Table of Sums
# Using nested loops, print sums of pairs:

# 1+1=2  1+2=3  1+3=4
# 2+1=3  2+2=4  2+3=5
# 3+1=2  3+2=4  3+3=6

for r in range(1,4):
    for c in range(1,4):
        print(r+c,end=" ")
    print()

