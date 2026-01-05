class Course():

    def __init__(self,course_name):

        self.cours_name = course_name
        
    def display(self):

        print("course name :",self.cours_name)

class Module(Course):

    def __init__(self, course_name,module_name):
        super().__init__(course_name)

        self.module_name = module_name

    def display(self):
        super().display()
        print("Module name :",self.module_name)

class Lessson(Module):

    def __init__(self, course_name, module_name,lesson_name):
        super().__init__(course_name, module_name)

        self.lesson_name = lesson_name

    def display(self):
        super().display()
        print("Lesson name :",self.lesson_name)



lesson_instance = Lessson("Python","OOP","Inheritance")

lesson_instance.display()


        