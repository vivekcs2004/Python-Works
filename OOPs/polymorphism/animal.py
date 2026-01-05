class Animal:

    def __init__(self,name):
        
        self.name = name
     

    def sounds(self):

        print(self.name,"sound")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sounds(self):

        print(self.name,"bow")

class Cat(Animal):      

    def __init__(self, name):
        super().__init__(name)

    def sounds(self):
        
        print(self.name,"meow")

dog_instance = Dog("dog")
cat_instance = Cat("cat")

dog_instance.sounds()
cat_instance.sounds()