class Employee:
    company_name = "Tech Corp"  # Class variable

    def __init__(self, name, position):
        self.name = name  # Instance variable
        self.position = position  # Instance variable

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Company: {Employee.company_name}")

# Creating objects of the Employee class
emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Developer")

# Accessing the method of the objects
emp1.display_info()
emp2.display_info()
