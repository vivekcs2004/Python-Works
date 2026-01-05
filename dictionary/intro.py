# super_hero = {"name":"batman","universe":"DC","power":"rich"}

# print(super_hero["power"])
# print(super_hero["name"])
# print(super_hero["universe"])

employee = {"id":8,"name":"vivek","department":"hr","location":"thrissur","salary":30000}

# employee["phone"]=1010101010 #adds new key value pair
# employee["department"]="cs" #updates the value of the key departments, keys are unique 

# print(employee)

if "id" in employee: #checks if key exists
    print("exist")
else:
    print("dont exist")