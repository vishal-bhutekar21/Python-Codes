# taking multiple as user wanted numbers from the user using the loop 

n= int(input("Enter how many list items you wnat to add ."))
 
list1=[]
for i in range(n):
    element=input(f"Enter {i+1} element in the list .")
    list1.append(element)


print("Elements from the list are ..",list1)