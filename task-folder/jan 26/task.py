from mysql import connector

class Products:
   
    def __init__(self):
        try:   
            self.connection = connector.connect(
                host ="localhost",
                user = "root",
                password ="Password@123",
                database = "task0201"
            )

            self.cursor = self.connection.cursor()
        
            print("DB CONNECTED")
        except Exception as e:
            print(e)

    # def add_prodcuts(self):
    #     try:

    #     except:
product_instance = Products()