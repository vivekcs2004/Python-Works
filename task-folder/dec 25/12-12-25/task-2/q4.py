# 4. Triangular 1s Pattern
# 1 0 0 0
# 1 1 0 0
# 1 1 1 0
# 1 1 1 1

for i in range(4):
    for j in range(4):
        if j <= i:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
