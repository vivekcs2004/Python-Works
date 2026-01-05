# 7. Print:

# 1 A A A
# 1 1 A A
# 1 1 1 A
# 1 1 1 1

for i in range(4):
    for j in range(4):
        if j <= i:
            print(1, end=" ")
        else:
            print("A", end=" ")
    print()
