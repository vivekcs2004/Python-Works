# Q9. Write a function is_palindrome(word) that returns True if palindrome.
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))
