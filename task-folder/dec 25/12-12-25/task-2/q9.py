# 9. Print:

# A A A A
# B B B B
# C C C C
# D D D D

letters = ["A", "B", "C", "D"]

for i in range(4):
    for j in range(4):
        print(letters[i], end=" ")
    print()
