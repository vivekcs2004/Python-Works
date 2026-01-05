# 5. Hollow Box With 1s
# For n = 5:

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1

n = 5
for i in range(n):
    for j in range(n):
        if i in (0, n-1) or j in (0, n-1):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
