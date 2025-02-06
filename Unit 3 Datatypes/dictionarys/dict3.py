dict1={
    "name":"vishal",
     "age":21,
    "college":"GECA"
    
}



for key, value in dict1.items():
    print(key, ": ",value)

for a in range(len(dict1)):
        print(" the data is in the dict is :",a)
    
dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York'}

keys = list(dict1.keys())

for i in range(len(keys)):
    print(f"The key is: {keys[i]}")
    print(f"The data in the dictionary is: {dict1[keys[i]]}")

    