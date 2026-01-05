word = "fcbbcafcb"
#       012345678

search_word = "fcb"

count = 0

for i in range(0,7):

    sliced_word = word[i:i+3]

    if search_word == sliced_word:
        count += 1
print(count)

    