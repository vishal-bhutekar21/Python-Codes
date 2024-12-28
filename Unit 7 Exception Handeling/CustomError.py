try: 
    num=int(input("Enter any number in the Keyboard."))
    print("Entered Number is : ",num)

except ValueError:
    print("Enter only interger number ")
except ImportError:
    print("index Error")