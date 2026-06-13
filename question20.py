#20. Write a program to read a CSV file and display its contents.
import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def read_csv_as_dict(filename):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Create a sample CSV file
sample_data = [['Name', 'Age', 'City'],
               ['Alice', '25', 'New York'],
               ['Bob', '30', 'London'],
               ['Charlie', '35', 'Paris']]

with open('sample.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(sample_data)

# Read and display CSV file
print("Reading CSV file as rows:")
read_csv_file('sample.csv')

print("\nReading CSV file as dictionaries:")
read_csv_as_dict('sample.csv')
