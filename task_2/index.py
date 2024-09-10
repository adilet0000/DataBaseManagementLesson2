import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to create the table
create_table_sql = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade REAL NOT NULL
);
'''

# Execute the SQL command
cursor.execute(create_table_sql)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Table 'students' created successfully (if it did not already exist).")
