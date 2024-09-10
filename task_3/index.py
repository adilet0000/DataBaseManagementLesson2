import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to insert records
insert_data_sql = '''
INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?);
'''

# Data to be inserted
data = [
    (1, 'Alice', 20, 3.8),
    (2, 'Bob', 21, 3.5),
    (3, 'Charlie', 22, 3.9)
]

# Execute the SQL command for each record
cursor.executemany(insert_data_sql, data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully.")
