class Father:
    def show_father(self):
        print("I am the father.")

class Mother:
    def show_mother(self):
        print("I am the mother.")

class Child(Father, Mother):
    def show_child(self):
        print("I am the child.")

# Example
child = Child()
child.show_father()  # Accessing method from Father
child.show_mother()  # Accessing method from Mother
child.show_child()   # Accessing child class method
