class Parent:
    def show_parent(self):
        print("I am the parent.")

class Child(Parent):
    def show_child(self):
        print("I am the child.")

# Example
child = Child()
child.show_parent()  # Accessing parent class method
child.show_child()   # Accessing child class method
