words = ["hello", "hai", "hello", "is"]

# Q1: recursive 
recursive = []
for w in words:
    if words.count(w) > 1 and w not in recursive:
        recursive.append(w)

# Q2: non-recursive 
non_recursive = []
for w in words:
    if words.count(w) == 1:
        non_recursive.append(w)

print("Recursive words :", recursive)
print("Non-recursive words :", non_recursive)
