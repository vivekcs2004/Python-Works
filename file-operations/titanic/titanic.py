file_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/titanic/titanic-dataset.csv"

fr = open(file_path,"r")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

# print(data)

passenger_name = [dic.get("Name") for dic in data]

# print(passenger_name)

gender = [g.get("Sex") for g in data]

male_count = gender.count("male")
female_count = gender.count("female")

# print("Male count :",male_count )
# print("Female count :",female_count)


survived_unsurvived = [s.get("Survived") for s in data]

# print("surviver_count : ",survived_unsurvived.count("1"))
# print("death_count : ",survived_unsurvived.count("0"))


#4 number of passengers in each of passenger class

passenger_class = [p.get("Pclass") for p in data]

# print("class 1 :",passenger_class.count("1"))
# print("class 2 :",passenger_class.count("2"))
# print("class 3 :",passenger_class.count("3"))

#5 oldest and youngest passenger

ages = [int(p.get("Age")) for p in data if p.get("Age").isdigit()]

oldest = max(ages)
youngest = min(ages)

oldest_pass = [p.get("Name") for p in data if p.get("Age").isdigit() and int(p.get("Age"))==oldest]
# print(oldest_pass)

youngest_pass = [p.get("Name") for p in data if p.get("Age").isdigit() and int(p.get("Age"))==youngest]
# print(youngest_pass)

#6 average age of passengers

#get names of first 10 passengers

first_ten = data[:11]

first_ten_names = [p.get("Name") for p in first_ten]

# print(first_ten_names)



#boarding station count

all_passengers_boarding_station = [p.get("Embarked") for p in data if len(p.get("Embarked"))>0]

boarding_count = {s:all_passengers_boarding_station.count(s) for s in all_passengers_boarding_station}

# print(boarding_count)

#passengers below age 10 ? how many survived ?

below_ten = [p for p in data if p.get("Age").isdigit() and int(p.get("Age"))<10]

suvived_children = [p for p in below_ten if p.get("Survived")=="1"]

# print("children under age of 10 : ",len(below_ten))
# print("survived children : ",len(suvived_children))



#1 calculate the survival rate

total_count = [s.get("Survived") for s in data]
# print(len(total_count))

survival_count = total_count.count("1")
# print(survival_count)

survival_rate = (survival_count/len(total_count))*100

# print("survival rate : ",survival_rate)


#2 survival rate by gender

male_list = [p for p in data if p.get("Sex")=="male"]
female_list = [p for p in data if p.get("Sex")=="female"]

male_survivors = [p for p in male_list if p.get("Survived") == "1"]
female_survivors = [p for p in female_list if p.get("Survived") == "1"]


male_survival_rate = round((len(male_survivors) / len(male_list)) * 100,2)
female_survival_rate = round((len(female_survivors) / len(female_list)) * 100,2)


# print(male_survival_rate)
# print(female_survival_rate)

#3 compare survival rate across passenger class

passenger_class1 = [p.get("Pclass") for p in data if (p.get("Pclass"))=="1"]
passenger_class2 = [p.get("Pclass") for p in data if (p.get("Pclass"))=="2"]
passenger_class3 = [p.get("Pclass") for p in data if (p.get("Pclass"))=="3"]

survived_class1 = [p.get("Pclass") for p in data if (p.get("Survived"))=="1" and (p.get("Pclass"))=="1"]
survived_class2 = [p.get("Pclass") for p in data if (p.get("Survived"))=="1" and (p.get("Pclass"))=="2"]
survived_class3 = [p.get("Pclass") for p in data if (p.get("Survived"))=="1" and (p.get("Pclass"))=="3"]


print("class 1 survival rate : ",(len(survived_class1)/len(passenger_class1))*100)
print("class 2 survival rate : ",(len(survived_class2)/len(passenger_class2))*100)
print("class 3 survival rate : ",(len(survived_class3)/len(passenger_class3))*100)












