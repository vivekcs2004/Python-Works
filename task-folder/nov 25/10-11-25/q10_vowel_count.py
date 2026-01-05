# Q10. Define a function count_vowels(s) that returns the number of vowels.
def count_vowels(s):
    sum = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:  
            sum += 1
    return sum

print(count_vowels("Education"))
