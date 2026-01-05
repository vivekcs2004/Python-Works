# **kwargs - dictionary
# *args - tuple

# def display_person(**kwargs):

#     print(kwargs)

# display_person(name="hari",age="21",place="tsr",salary=1234)

def operation(*args,**kwargs):

    op = kwargs.get("key")

    if op =="max":

        return max(args)
    
    else :

        return min(args)

print(operation(10,20,30,40,key= "max"))


print(operation(10,20,30,40,key= "min"))

