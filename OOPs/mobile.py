class Mobile:
    
    title = str
    price = int
    brand = str
    features = str

    def __init__(self,title,price,brand,features):
         
         self.title = title
         self.price = price
         self.brand = brand
         self.features = features

    def display(self):
         
         print("mobile title    : ",self.title)
         print("mobile price    : ",self.price)
         print("mobile brand    : ",self.brand)
         print("mobile features : ",self.features)

mobile_instance1 = Mobile("s23",10000,"samsung","galaxy AI")
mobile_instance2 = Mobile("Pixel",15000,"google","pixel AI")

mobile_instance1.display()
print()
mobile_instance2.display()
        