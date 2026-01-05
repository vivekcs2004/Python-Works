from mysql import connector

class Vehicles:

    def __init__(self):
        try:
            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Password@123",
                database = "gosell_db"
            )

            self.cursor = self.connection.cursor()

            print("DB connected✅")

        except Exception as e:
            print(e)



    def add_vehicles(self, **kwargs):
        try :
            columns = ""

            values = ""

            for k in kwargs.keys():
                columns += k+","
                values += "%s"+","
            
            columns = columns.rstrip(",")
            values = values.rstrip(",")

            query = f"""insert into vehicle ({columns}) values
                    ({values})"""

            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query,data)

            self.connection.commit()

            print("Data inserted✅")

        except Exception as e:
            print(e)

    
    def list_all_data(self,table_name):
        try:
            query = f"""select * from {table_name}"""

            self.cursor.execute(query)
            records = self.cursor.fetchall()

            for row in records:
                print(row)
            
        except Exception as e:
            print(e)

    
    def retrieve_vehicle(self,id=None):

        try:
            query = f"""select * from vehicle where id = {id}"""

            self.cursor.execute(query)

            record = self.cursor.fetchone()

            print(record)

        except Exception as e:
            print(e)

    def delete_vehicle(self, id=None):
        try:
            query = f"delete from vehicle where id = {id}"

            self.cursor.execute(query)

            self.connection.commit()

            print("Deleted✅")
        
        except Exception as e :
            print(e)

    def update_vehicle(self, id=None, **kwargs):
        try:
            placeholder = ""
            for k in kwargs.keys():
                placeholder += k + "=" + "%s" + ","

            placeholder = placeholder.rstrip(",")

            query = f"update vehicle set {placeholder} where id = {id}"
            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query,data)
            self.connection.commit()

            print("Updated✅")
        
        except Exception as e:
            print(e)



vehicles_instance1 = Vehicles()

# vehicles_instance1.add_vehicles(name="passion plus", price= 20000, year= 2010, fuel_type= "petrol", comments= "Showroom condition",
#                                 running_km=50000, owner_type= "third", owner= "Abhijith", location= "Kodakara")

# vehicles_instance1.list_all_data(table_name="vehicle")

vehicles_instance1.update_vehicle(id=1,location="Thrissur",name="Himalayan")
vehicles_instance1.list_all_data(table_name="vehicle")