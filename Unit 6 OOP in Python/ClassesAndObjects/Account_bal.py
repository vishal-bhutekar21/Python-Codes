class Account:
    def __init__(self,name,bal,accno):
        self.name=name
        self.balance=bal
        self.Account_no=accno
        print("Account Created for :",self.name)
        
    def credit(self,amount):
        self.balance += amount
        print("MOney Credited in your account :",amount)

        print("Your Available Balance is :",self.balance)
    
    def debit(self,amount):
        print("MOney Debited form  your account :",amount)

        self.balance -= amount
        print("Your Available Balance is :",self.balance)
    

A1=Account("Vishal Bhutekar",70000,584892834)
print(f"THe remaining balance in {A1.name} is :",A1.balance)
A1.credit(9000)
print(f"THe remaining balance in {A1.name} is :",A1.balance)
A1.debit(20000)
print(f"THe remaining balance in {A1.name} is :",A1.balance)