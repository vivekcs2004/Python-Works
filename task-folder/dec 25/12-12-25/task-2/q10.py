# 10. Print:

# A B C D
# B C D A
# C D A B
# D A B C

letters = ["A", "B", "C", "D"]

for i in range(4):
    for j in range(4):
        print(letters[(i + j) % 4], end=" ")
    print()
