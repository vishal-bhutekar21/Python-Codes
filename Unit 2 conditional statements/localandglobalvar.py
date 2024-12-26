globalvar=1380

def vish():
     
    
    globalvar="7721924292"
    print(globalvar)
    
vish()
print(globalvar)



# above is the simple code to check and print if the varible is global or not


# now to modify the global variable we use global keyboard

globalvar=1380

def vish():
     
     
    globalvar="7721924292"
    print("inside the function ",globalvar)
    
vish()
print("the actual value of the global variable ",globalvar)

