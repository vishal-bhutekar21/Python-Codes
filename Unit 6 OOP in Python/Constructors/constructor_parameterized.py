class Student :
 
 #parameterized constructor
    def __init__(self,name,age,marks,address):
        print("The constructor is Created ...")
        self.name=name
        self.address=address
        self.age=age
        self.marks=marks
        
                
    def print_name(self):
        print("The name  is :",self.name)
        print("The age of the student is :",self.age)
        print("The address of the student is :",self.address)
        print("The marks of the student is :",self.marks)

s1=Student("Vishal Bhutekar",12,100,"At Jalna,Maharashtra,431213")
s1.print_name()
