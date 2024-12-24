my_list = [1987, 224, 3]
my_list.append(4)
print("after adding the 4 on the list",my_list)  

#append is used to  add the data at the end of the list

#extend is used to add multiple items to the list or extend the list

my_list.extend([12,23,525,25])
print(my_list)

# sort method is used to sort in ascending order 
my_list.sort()
print(my_list)

# insert method is used to insert the element at the 
# specified position at the Index

my_list.insert(3,3033)
print("after inserting 303 at index 3",my_list)

# remove the first found occourence from the list

my_list.remove(3033)
print(my_list)

# pop is usesd to to return the last and remove the last element from the list
removed_item=my_list.pop()
print("after using the pop method", removed_item)
removed_item3=my_list.pop(3)
print("after removing the 3 element from the list ",removed_item3)
# index method is used to return the first occourance of the element from the list
print("location of the element 535 is",my_list.index(525))
# count method is used to counnt the elememt from in the list
print(my_list.count(525))


my_list.sort()
print(my_list)
my_list.reverse()
new_list=my_list.copy()
print(my_list)
#clear method is used to clear all the elements from the list
my_list.clear()
print(my_list)

#copy method is used to copy the list from one to another


print(new_list)


# we can convert the string into an list using the list function 
str = "vidhal bhutekar"

namelist=list(str)

print(namelist)

# join is used to join two list using the seperator 


result="-----".join(namelist)
print(result)