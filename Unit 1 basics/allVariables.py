# 1. String Variable
name = "Vishal"  # A string variable
print("Name:", name)  # Printing the value of the string variable
print("Type of 'name':", type(name))  # Printing the type of the variable 'name'

# 2. Integer Variable
age = 20  # An integer variable
print("\nAge:", age)  # Printing the value of the integer variable
print("Type of 'age':", type(age))  # Printing the type of the variable 'age'

# 3. Float Variable
height = 5.9  # A float variable
print("\nHeight:", height)  # Printing the value of the float variable
print("Type of 'height':", type(height))  # Printing the type of the variable 'height'

# 4. Boolean Variable
is_student = True  # A boolean variable
print("\nIs Student:", is_student)  # Printing the value of the boolean variable
print("Type of 'is_student':", type(is_student))  # Printing the type of the variable 'is_student'

# 5. List Variable
my_list = [1, 2.5, "Vishal", True]  # A list variable containing multiple types of data
print("\nList:", my_list)  # Printing the value of the list
print("Type of 'my_list':", type(my_list))  # Printing the type of the variable 'my_list'

# 6. Tuple Variable
my_tuple = (1, 2.5, "Vishal")  # A tuple variable
print("\nTuple:", my_tuple)  # Printing the value of the tuple
print("Type of 'my_tuple':", type(my_tuple))  # Printing the type of the variable 'my_tuple'

# 7. Dictionary Variable
my_dict = {"name": "Vishal", "age": 20, "is_student": True}  # A dictionary variable
print("\nDictionary:", my_dict)  # Printing the value of the dictionary
print("Type of 'my_dict':", type(my_dict))  # Printing the type of the variable 'my_dict'

# 8. Set Variable
my_set = {1, 2, 3, 4, 5}  # A set variable
print("\nSet:", my_set)  # Printing the value of the set
print("Type of 'my_set':", type(my_set))  # Printing the type of the variable 'my_set'

# 9. NoneType Variable
nothing = None  # A NoneType variable
print("\nNothing:", nothing)  # Printing the value of the NoneType variable
print("Type of 'nothing':", type(nothing))  # Printing the type of the variable 'nothing'

# 10. Complex Number Variable
complex_number = 2 + 3j  # A complex number variable
print("\nComplex Number:", complex_number)  # Printing the value of the complex number
print("Type of 'complex_number':", type(complex_number))  # Printing the type of the variable 'complex_number'

# 11. Reassigning Variables (Dynamic Typing in Python)
x = 10  # Assigning an integer to variable x
print("\nValue of 'x':", x)
print("Type of 'x':", type(x))

x = "Now I'm a string"  # Reassigning a string to the same variable x
print("New value of 'x':", x)
print("New type of 'x':", type(x))

# 12. Multiple Assignment
a, b, c = 5, "Vishal", 3.14  # Multiple assignment of different types
print("\nMultiple assignment:")
print("a:", a, "Type of 'a':", type(a))
print("b:", b, "Type of 'b':", type(b))
print("c:", c, "Type of 'c':", type(c))

# 13. Using Constants (Convention)
PI = 3.14159  # Constant (Python convention is to use uppercase for constants)
print("\nPI:", PI)  # Printing the constant
print("Type of 'PI':", type(PI))  # Printing the type of the constant

# 14. Global and Local Variables Example
# Global variable
global_var = 100

def my_function():
    # Local variable
    local_var = 50
    print("\nInside function:")
    print("Global variable:", global_var)  # Accessing global variable
    print("Local variable:", local_var)  # Accessing local variable

my_function()  # Calling the function

# 15. Demonstrating Dynamic Typing
y = 42  # Integer type
print("\nValue of 'y':", y, "Type of 'y':", type(y))

y = "Now I am a string"  # Reassigning to a string type
print("New value of 'y':", y, "New type of 'y':", type(y))
