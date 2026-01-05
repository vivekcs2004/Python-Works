from mysql import connector


connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "task3112"
)

# print("success")


cursor = connection.cursor()

query = """

insert into members(name,email,password) values (%s,%s,%s)

"""

data = (("vivek1","vive11k@gmail.com","vivek123"),
       ("ashik1","ashik1@gmail.com","ashik123"),
       ("abi1","abi1@gmail.com","abi123"))

cursor.executemany(query,data)

connection.commit()
print("query executed..")

cursor.close()
connection.close()