class Person:
    def __init__(self,name,age,gender):

        self.gender = gender
        self.name = name
        self.age = age
    
    def display(self):

        print(f"name = {self.name} age = {self.age} gender = {self.gender}")

class Student(Person):

    roll_number = int
    course = str

    def __init__(self,name,age,gender,role,course):

        super().__init__(name,age,gender)

        self.role = role
        self.course = course
    
    def display(self):

        super().display()
        print(f"role_num ={self.role} course = {self.course}")
        

stud_instance1 = Student("vivek",21,"male",10,"django")
stud_instance1.display()