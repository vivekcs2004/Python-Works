def is_palindrome(word):

    word = word.casefold()

    return word == word[::-1]

print(is_palindrome("malayalam"))