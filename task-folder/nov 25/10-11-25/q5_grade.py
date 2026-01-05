# Q5. Define a function grade(marks) that returns A/B/C/F based on score.
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(grade(82))
