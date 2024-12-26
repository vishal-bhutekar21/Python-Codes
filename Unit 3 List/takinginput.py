# Get user input for a nested list
user_input = [x.split(",") for x in input("Enter nested list (use commas and semicolons): ").split(";")]

print("Nested List:", user_input)