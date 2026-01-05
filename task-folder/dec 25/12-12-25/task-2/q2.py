# 2. Print:

# R R R R
# R S S R
# R S S R
# R R R R

for i in range(4):
    for j in range(4):
        if i in (0, 3) or j in (0, 3):
            print("R", end=" ")
        else:
            print("S", end=" ")
    print()
