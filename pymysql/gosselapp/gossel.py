from mysql import connector

class Vehicles:

    def __init__(self):
        
        try:

            self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Password@123",
            database ="gosell_db"

            )

            self.cursor = self.connection.cursor()

            print("db connection succesful......")

        except Exception as e:

            print(e)


    def add_vehicles(self,**kwargs):
            
        try:

            columns=""
            values=""

            for k,v in kwargs.items():
                columns+=k+","
                values +="%s"+","

            columns = columns.rstrip(",")
            values = values.rstrip(",")
            query = f"""
            insert into vehicle({columns}) values
            ({values})
            """   

            data = [v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record inserted")

        except Exception as e:

            print(e)


    def list_vehicles(self):

        try:
            query = "select *from vehicle"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
        
                print(row)

        except Exception as e:
            print(e)

    def retrieve_vehicle(self,id):

        try:
            query = "select *from vehicle where id=%s"

            data =(id,)

            self.cursor.execute(query,data)

            record =self.cursor.fetchone()
            
            print(record)
        except Exception as e:
            print(e)

    def delete_vehicle(self,id=None):

        try:
            query = "delete from vehicle where id=%s"

            data =(id,)

            self.cursor.execute(query,data)

            self.connection.commit()
            
           
        except Exception as e:
            print(e)
    
    def update_vehicle(self,id,**kwargs):

        place_holder =""

        for k,v in kwargs.items():

            place_holder+=k+"%s"+","

            place_holder= place_holder.rstrip(",")

            query = f"update vehicles set {place_holder} where id = {id}"

            data= [v for k,v in kwargs.items()]

            self.cursor.execute(query,data)
            self.connection.commit()



vehicle_instance = Vehicles()

vehicle_instance.update_vehicle(id=4,location="amballur",name="glamour")

# vehicle_instance.delete_vehicle(id=5)

# vehicle_instance.retrieve_vehicle(id=1)

# vehicle_instance.list_vehicles()

# vehicle_instance.add_vehicles(name="passion pro",price="25000",year="2012",fuel_type="petrol",
#                             comments="well maintained",running_km="55000",owner_type="second",
#                             owner="vaishak",location="thrissur")



    