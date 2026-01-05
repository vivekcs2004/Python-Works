from mysql import connector


connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwise_db"
)

print("success")


cursor = connection.cursor()

query = """

insert into user(name,email,password) values (%s,%s,%s)

"""

data = (("vivek","vivek1@gmail.com","vivek123"),
       ("ashik","ashik@gmail.com","ashik123"),
       ("abi","abi@gmail.com","abi123"))

cursor.executemany(query,data)

connection.commit()
print("query executed..")

cursor.close()
connection.close()