class GrangParent:

    def properties(self):

        print("50 cent land , 1 huge vintage home")

class Parent(GrangParent):
    
    def vehicle(self):

        print("swift car")

class Child(Parent):

    def gadgets(self):

        print("s23")

child_instance = Child()

child_instance.gadgets()
child_instance.vehicle()
child_instance.properties()