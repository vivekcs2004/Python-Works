from copy import deepcopy

p1_fvt_food = [

    ["dosa","tea"],
    ["meals","lime"],
    ["chapathi","water"]
]

p2_fvt_food = deepcopy(p1_fvt_food)

p2_fvt_food[0][0] = "idly"

print("Person 1 :",p1_fvt_food)
print("Person 2 :",p2_fvt_food)