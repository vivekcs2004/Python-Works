class Calculator():

    def add(self,*args):

        print(sum(args))

add_instance = Calculator()

add_instance.add(100,200)
add_instance.add(12,234,2345,567)


        
