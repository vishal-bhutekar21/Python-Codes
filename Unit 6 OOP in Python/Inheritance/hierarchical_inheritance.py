class Parent:
    def show_parent(self):
        print("I am the parent.")

class Child1(Parent):
    def show_child1(self):
        print("I am the first child.")

class Child2(Parent):
    def show_child2(self):
        print("I am the second child.")

# Example
child1 = Child1()
child1.show_parent()  # Accessing parent class method
child1.show_child1()  # Accessing first child class method

child2 = Child2()
child2.show_parent()  # Accessing parent class method
child2.show_child2()  # Accessing second child class method
