# 8. Print:

# A B C D
# A B C D
# A B C D
# A B C D


for i in range(4):
    for j in range(4):
        print(chr(65 + j), end=" ")
    print()
