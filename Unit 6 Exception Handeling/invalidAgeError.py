class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))
if age < 0 or age > 120:
    raise InvalidAgeError("Age must be between 0 and 120.")
else:
    print("Age is valid.")
