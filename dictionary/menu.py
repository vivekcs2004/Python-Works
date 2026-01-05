menu = {
        "biriyani":150,"fried rice":130,
        "lime":30,"shawarma":150,
        "tea":10,"cofee":15}

#display all keys
# for k in menu.keys():
#     print(k)

# display all key values
# for k,v in menu.items():
#     print(k,v)

#display all items under 50
# for k,v in menu.items():
#     if v < 50:
#         print(k,v)

#fetch price of shawai / shawarma

item_price = menu.get("shawai",0)
print(item_price)

# item_price = menu.get("shawarma",0)
# print(item_price)

#check item tea exist, if exist update tea current price as +5

# if "tea" in menu:
#      menu["tea"]+=5
# print(menu)




