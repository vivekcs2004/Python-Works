def palindrome_words(words):

    palindrome_words = []

    for w in words:

        if w == w[::-1]:
            palindrome_words.append(w)  
    
    return palindrome_words
    
words = ["cat","act","dam","malayalam","madam"]

print(palindrome_words(words))