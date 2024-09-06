import sqlite3

# Step 1: Connect to SQLite Database (or create it)
conn = sqlite3.connect('example.db')  # 'example.db' is the database file

# Step 2: Create a cursor object using the connection
cursor = conn.cursor()

# Step 3: Create a table if it doesn't exist
'''
table looks like this ...

---------------------------------------------------------------------------
|id (primary key integer) | name (text) | age (integer) | grade (integer) | 
---------------------------------------------------------------------------
|                                                                         |
|                                                                         |
|_________________________________________________________________________|
'''
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL, 
                   age INTEGER NOT NULL, 
                   grade TEXT)''')

# Step 4: Insert data into the table
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('John Doe', 20, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jane Smith', 22, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Mike Johnson', 21, 'C')")

# Step 5: Commit the changes to the database
conn.commit()

# Step 6: Query the data from the table
cursor.execute("SELECT * FROM students")

# Step 7: Fetch all rows from the query result
rows = cursor.fetchall()

# Step 8: Display the data
print("Student Data:")
for row in rows:
    # alternate method for printing variables - string interpolation like in C ...
    # a little bit easier on the eyes :)
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")

# Step 9: Close the connection
conn.close()
