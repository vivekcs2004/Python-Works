story_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/word_count.py/story.txt"

fr_story = open(story_path,"r")

wc = {}
for line in  fr_story:

    line = line.rstrip("\n")

    words = line.split(" ")

    for w in words:

        w = w.rstrip(",")
        w = w.rstrip(".")

        if w in wc:

            wc[w] += 1
        
        else:

            wc[w] = 1
print(wc)


max_word = {k : v for k,v in wc.items() if v==max(wc.values()) and k.isalpha()}

print(f"max count = {max_word}")