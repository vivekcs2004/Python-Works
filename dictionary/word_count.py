#create a dict of word count 
words = ["hai","hello","hai","hello","python"]

word_count = {}

for w in words:

    if w in word_count:
      word_count[w] += 1

    else:
       word_count[w] = 1 

print(word_count)

      


