from mysql import connector


connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "task3112"
)

# print("success")


cursor = connection.cursor()

query = "select *from members"

cursor.execute(query)

records = cursor.fetchall()

for row in records:
    print(row)

cursor.close()
connection.close()