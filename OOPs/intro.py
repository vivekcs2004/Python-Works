class Car:
    name:str
    brand:str
    price:int

    def set_car(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    
    def display(self):

        print("car name  : ",self.name)
        print("car brand : ",self.brand)
        print("car price : ",self.price)

car_instance1 = Car()

car_instance1.set_car("swift","maruti","5 lakhs")

car_instance1.display()