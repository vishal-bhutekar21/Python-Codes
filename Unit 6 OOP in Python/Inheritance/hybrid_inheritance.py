class Grandparent:
    def show_grandparent(self):
        print("I am the grandparent.")

class Parent1(Grandparent):
    def show_parent1(self):
        
        print("I am the first parent.")

class Parent2(Grandparent):
    def show_parent2(self):
        print("I am the second parent.")

class Child(Parent1, Parent2):
   
    def show_child(self):
        
        print("I am the child.")

# Example
child = Child()
child.show_grandparent()  # Accessing grandparent class method
child.show_parent1()      # Accessing first parent class method
child.show_parent2()      # Accessing second parent class method
child.show_child()        # Accessing child class method
