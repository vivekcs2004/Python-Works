def is_anagram(w1,w2):

    sort_w1 = sorted(w1.casefold())

    sort_w2 = sorted(w2.casefold())

    return sort_w1 == sort_w2

print(is_anagram("listen","silent"))
print(is_anagram("listen","silence"))


    