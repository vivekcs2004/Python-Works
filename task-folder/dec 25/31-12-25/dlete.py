from mysql import connector


connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "task3112"
)

cursor = connection.cursor()

query = "delete from members where id = %s"

data = (5,)
cursor.execute(query,data)

connection.commit()

print("deleted")

cursor.close()
connection.close()


