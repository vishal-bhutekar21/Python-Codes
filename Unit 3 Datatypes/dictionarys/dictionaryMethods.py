student={
    "name":"vishal bhuteakr",
    "college ":"Government college of engineering Aurangabad"
    ,"Marks":{
        "Chem":99,
        "phy":83,
        "Bio":88
    }
    
    
    }
print("The keys in the dictionary are : ",student.keys())
print("The values from the dictionary are :",student.values())
print("Items from the dictionary are :",student.items())#returns all the key and values in form of tuples 
#get method is used to print the value of the key specified
print("the key is the :",student.get("name")) #if the key not found then it does not throw the eror
#  if we want to add multiple keys and values at the same time in dictionary we can take help from the update method

dict2={"true":True,"jinda hai kya":True}
student.update(dict2)
print(student)

print(student.clear())

#clear method is used to clear all the data from the dictionary

print(student)

dict3=student.copy()
print(dict3)
if  dict3 is student :
    print("The both dicitonary are same !")
else:
    print("Same nahi hai bhai......~! ")