class VishalError(Exception):
    pass

v = int(input("Enter any number which you want to enter: "))
if v < 0 or v > 10:
    raise VishalError("The number is not valid")
