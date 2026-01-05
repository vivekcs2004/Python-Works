# Q2  Find even numbers between 1 and 20 that are also divisible by 3

for x in range(1, 21):
    if x % 2 == 0 and x % 3 == 0:
        print(x, end=' ')

