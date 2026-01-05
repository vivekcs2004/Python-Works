all_users = {"sachin","dravid","laxman","sreenath","ganguly","zaheer","yuvi","kaif","dhoni"}

sachin_friends = {"dravid","laxman","ganguly"}
dhoni_friends = {"dravid","laxman","yuvi","kaif"}

mutual_friends = sachin_friends.intersection(dhoni_friends)

suggestion = all_users.difference(sachin_friends)
suggestion.remove("sachin")

print(suggestion)
print(mutual_friends)