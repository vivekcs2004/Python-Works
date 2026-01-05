# 6. Cross Pattern
# 0 0 1 0 0
# 0 0 1 0 0
# 1 1 1 1 1
# 0 0 1 0 0
# 0 0 1 0 0

n = 5
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
