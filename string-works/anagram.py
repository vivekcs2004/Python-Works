def anagram(word1,word2):

    if len(word1)==len(word2):
        for i in word1 :
            
            if i not in word2:
                return False
        return True
    return False
print(anagram("cat","act"))
