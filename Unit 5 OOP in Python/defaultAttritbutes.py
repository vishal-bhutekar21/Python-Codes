class Student :
    name=""
    addres=""
    college_name=""
    def __init__(self):
        self.height=133
        print("constructor is called")
        
    def  print_details(self):
        print("The name of the student is :",self.name)
        print("The height of the student is :",self.height)
        print("The address of the student is :",self.addres)
        print("The college_name of the student is :",self.college_name)
        

s1=Student()
print("Height of the student is :",s1.height)
s1.print_details()