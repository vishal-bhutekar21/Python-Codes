class FileNotFoundError(Exception):
    pass

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        print(file.read())
except FileNotFoundError:
    raise FileNotFoundError(f"The file {file_name} was not found.")
