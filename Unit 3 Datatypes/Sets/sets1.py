# set are unorded and all items are immutablea and also set all must must be unique

set1={1,2,3,4}
print(set1)
print("Type of the set1 is :",type(set1))
print("Lenght of the set is :",len(set1))
# len funciton only prints the real not duplicate values from the set
# add method is used to add elements in set
set1.add(3)
print(set1)

set1.remove(2)#The remove method remove the specified elemnt from the set

print(set1)
popped_val=set1.pop()
print("the popped value is :",popped_val)

set1.clear()
print(set1)




#union and intersection method 

# union method combines both the set values and returns  unique value
set12={1,2,3,4,5,6}
set3={1,2,35,67,6}
print(set12.union(set3))
print(set12.intersection(set3))