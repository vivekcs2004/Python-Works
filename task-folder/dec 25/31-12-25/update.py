from mysql import connector


connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "task3112"
)

cursor = connection.cursor()

query = "update members set name = %s where id = %s"

data = ("ashin",5)
cursor.execute(query,data)

connection.commit()

print("updated")


cursor.close()
connection.close()


