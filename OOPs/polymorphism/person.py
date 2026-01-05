class Person:

    def __init__(self,name,age,gender):

        self.name = name
        self.age = age
        self.gendr = gender
        
    @property
    def get_age(self):

        print(self.age)

person_instance1 = Person("v",21,"m")

person_instance1.get_age




