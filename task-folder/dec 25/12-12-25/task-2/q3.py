# 3. X-Pattern with 1s
# For n = 5:

# 1   0   0   0   1
# 0   1   0   1   0
# 0   0   1   0   0
# 0   1   0   1   0
# 1   0   0   0   1

n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
