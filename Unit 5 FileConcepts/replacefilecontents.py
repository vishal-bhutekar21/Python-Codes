with open("demo1.txt", "r") as f:
    data = f.read()  # Read the entire content of the file
    print("This is the old data in the file .............")
    print(data)  # Print the old data

newdata = data.replace("Vishal", "Vishal Bhutekar")  # Replace the text
print("This is the new data after replacement .............")
print(newdata)  # Print the new data

with open("demo1.txt", "w") as f:
    f.write(newdata)  # Write the new data back to the file
