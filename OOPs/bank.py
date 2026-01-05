class Bank:

    acc_num = int
    name = str
    acc_type = str
    balance = int

    def create_acc(self,acc_num,name,acc_type,balance):

        self.acc_num = acc_num
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"your account{self.acc_num} credited with {amount} your avail bal is {self.balance}")

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance -= amount
            print(f"your account{self.acc_num} debited with {amount} your avail bal is {self.balance}")
        else:
            print("transaction failed insufficient balance")
    
    def balance_enq(self):

        print(f"hai {self.name} your acc bal is {self.balance}")


bank_acc_instance1 = Bank()

bank_acc_instance1.create_acc(8,"vivek","savings",10000)

bank_acc_instance1.deposit(1000)

bank_acc_instance1.withdraw(100)

bank_acc_instance1.balance_enq()






    
    

        