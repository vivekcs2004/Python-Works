class Employee:

    def __init__(self,id,dep,salary):

       self.id = id
       self.dep = dep
       self.salary = salary

    def display(self):

        print(f"id : {self.id} department : {self.dep}  salary : {self.salary}")

class Developer(Employee):

    def __init__(self, id, dep, salary,prg_lan,fw):
        super().__init__(id, dep, salary)

        self.prg_lan = prg_lan
        self.fw = fw

    def display(self):
        super().display()
        print(f"programming language : {self.prg_lan} , framework : {self.fw}")

employee_instance1 = Developer(10,"HR",30000,"python","django")

employee_instance1.display()
