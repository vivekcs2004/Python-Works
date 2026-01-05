# Q11. Write a function square_list(numbers) that returns a list of their squares.
def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n * n)
    return result

print(square_list([1, 2, 3, 4, 5]))
