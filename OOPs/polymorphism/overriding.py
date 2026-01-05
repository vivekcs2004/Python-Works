
#child class changes the behaviour of method it gets from parent class

class Vehicles:

    def __init__(self,brand,title):
        
        self.brand = brand
        self.title = title

    def move(self):

        print(self.title ,"is moving")

class Car(Vehicles):

    def __init__(self, brand, title):
        super().__init__(brand, title)

class Ship(Vehicles):

    def __init__(self, brand, title):
        super().__init__(brand, title)
    
    def move(self):

        print(self.title,"is sailing")

car_instance = Car("toyota","fortuner")

ship_instance = Ship("abc","titanic")

car_instance.move()

ship_instance.move()
