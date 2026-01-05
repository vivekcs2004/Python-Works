#checks object is pointing to same memory location or not

resin_fv_food = "biriyani"

abi_fv_food = "biriyani"

print(resin_fv_food == abi_fv_food) #true

print(resin_fv_food is abi_fv_food) #true exception in small strings

person1_fav_movies = ["interstellar","inception"]

person2_fav_movies = ["interstellar","inception"]

print(person1_fav_movies == person2_fav_movies) #true

print(person1_fav_movies is person2_fav_movies) #false




