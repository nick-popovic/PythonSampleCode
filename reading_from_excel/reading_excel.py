# pip install pandas openpyxl
import pandas as pd

# Step 1: Specify the file path
file_path = 'example.xlsx'  # Replace with the path to your Excel file

# Step 2: Read the Excel file using pandas
try:
    data = pd.read_excel(file_path)  # Read the first sheet by default
    print("Excel file read successfully!")
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
    exit()

# Step 3: Display the data (first few rows)
print("Data from Excel file:")
print(data.head())  # Display the first 5 rows of the data

# Step 4 (Optional): Display specific columns
# If you want to display specific columns, you can do so like this:
# print(data[['Column1', 'Column2']])  # Replace with your column names
