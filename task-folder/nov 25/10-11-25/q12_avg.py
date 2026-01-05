# Q12. Create a function average_list(numbers) that returns the average of numbers in the list.
def average_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(average_list([10, 20, 30, 40]))
