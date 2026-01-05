product = {"code":345,"title":"shirt","color":"blue","size":"m","price":1500}

if "offer" in product:

    product["offer"] += 50 #update

else:

    product["offer"] = 100 #add

print(product)