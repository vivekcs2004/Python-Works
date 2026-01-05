"""
     def keys()            returns all keys
     def values()          returns all values
     def items()           returns key and values
     def get(key,def_val)  return the value for key if key is in the dictionary, else default(none)
     def pop(key)          remove specified key and return the corresponding value
"""

treasure = {"box1":"gold","box2":"silver","box3":"diamond","box4":"platinum"}

# for k in treasure.keys():
#     print("keys   : ",k)

# for v in treasure.values():
#     print("values : ",v)

# for k,v in treasure.items():
#     print(k,v)

# print(treasure.get("box10","key dont exist")) 

treasure.pop("box2")
print(treasure)
