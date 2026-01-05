# Q1 : Set Operations Basics
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# a) Elements common to both sets
print("Common to both:", (set1.intersection(set2)))
   
# b) Elements present in A but not in B
print("In A but not in B:", (set1.difference(set2)))

# c) The symmetric difference between A and B
print("Symmetric difference:", (set1.symmetric_difference(set2)))
