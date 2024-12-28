try: 
    l=[3,4,234,646,75,7]
    index=int(input("Enter which indec value you want you access ."))
    print("THe value you want to access is :",l[index])
    
    
except Exception as e:
    print(e)
    
finally:
    print("The Finally block is excecutteed...")