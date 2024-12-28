import csv

# Data to write (single row)
data = ["Alice", 24, "New York"]

# Open the CSV file in write mode
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write a single row to the file
    csv_writer.writerow(data)
