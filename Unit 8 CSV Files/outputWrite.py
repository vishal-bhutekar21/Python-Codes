import csv

# Data to write to the CSV file
data = [["Name", "Age", "City"], ["Alice", 24, "New York"], ["Bob", 27, "Los Angeles"]]

# Open the CSV file in write mode
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write multiple rows to the file
    csv_writer.writerows(data)
