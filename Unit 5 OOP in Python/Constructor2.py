class Student :
    name="vishal"
    def print_name(self):
        print("The class variable name is :",Student.name)
    def __init__(self,name):
        self.name=name
        print("The name of the student is :",self.name)
        

s1=Student("karan")
s1.print_name()
s1.name="vishal Bhutekar"
print("The new value of the name in class is :",s1.name)