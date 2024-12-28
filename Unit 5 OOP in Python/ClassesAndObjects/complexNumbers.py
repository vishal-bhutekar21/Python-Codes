class Complex :
    def __init__(self, real, img):
        self.real=real
        self.img=img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    
    def add(self,num2):
        pass
     
num1=Complex(2,3)
num1.showNumber()

num2=Complex(234,5353)
num2.showNumber()        