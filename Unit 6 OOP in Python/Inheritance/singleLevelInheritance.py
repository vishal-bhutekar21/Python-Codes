# class Parent:
#     class constructor:
#     class attributes :
#     class methods()
    
#     pass



# class Child (Parent):
#      class constructor:
#     class attributes :
#     class methods()
    
#     pass



class Parent:
    def __init__(self):
        print("Parent Borned......")

class Child(Parent):
    def __init__(self):
        #we can use super method to access the paren calss methods and constructor
        
        super().__init__()  # Call the Parent class's constructor
        print("Child Borned......")

# Create an instance of the Child class
c1 = Child()

