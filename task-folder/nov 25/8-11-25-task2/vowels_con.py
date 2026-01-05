#vowel consonant count
def display_vowel_and_consonant_count(word):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    for ch in word.casefold():
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count,c_count

print(display_vowel_and_consonant_count("fcbarcelona"))

