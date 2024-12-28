#we use __ to infront of the variabale to make it private so we cannot 
#access in our code

class Account:
    def __init__(self,name,pass1):
        self.name=name
        self.__pass1=pass1

    def print_details(self):
        print("The password is : ",self.__pass1)

a1=Account("Vishal",1234)
a1.print_details()
# print(a1.__pass1) gives error say class does not have this attribute