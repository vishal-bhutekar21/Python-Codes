a=1
b=0

try:
    print("The result is :",(a/b))
except Exception as a:
    print("Hey you cannot divide by zero :",a)
    
except Exception as ea:
    print("something went wrong ")
finally:
    print("deleting and deallocationg the rasources :")
    