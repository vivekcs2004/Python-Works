def is_anagram(word1,word2):

    is_anagram = True

    if len(word1) != len(word2):
        return False

    for ch in word1.casefold():

        ch_count_in_w1 = word1.count(ch)
    
        ch_count_in_w2 = word2.count(ch)

        if ch_count_in_w1 != ch_count_in_w2:
            
            is_anagram=False

            break
    return is_anagram

print(is_anagram("cat","act"))
print(is_anagram("cat","ant"))
print(is_anagram("cat","ants"))
