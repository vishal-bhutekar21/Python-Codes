import csv

# Open the CSV file in read mode
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV
    for row in csv_reader:
        print(row)
