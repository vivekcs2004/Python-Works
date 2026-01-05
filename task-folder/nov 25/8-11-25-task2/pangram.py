#check pangram
def is_pangram(word):
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for ch in alphabets.casefold():
        if ch not in word:
            return False
    return True
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("the quick brown fox jumps over the lazy cat"))

