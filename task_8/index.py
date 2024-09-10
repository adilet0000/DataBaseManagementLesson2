import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to add a new column 'email' to the 'students' table
add_column_sql = '''
ALTER TABLE students
ADD COLUMN email TEXT;
'''

# Execute the SQL command to add the column
cursor.execute(add_column_sql)

# Commit the changes
conn.commit()

# SQL command to get the table schema
get_schema_sql = '''
PRAGMA table_info(students);
'''

# Execute the SQL command to get the schema
cursor.execute(get_schema_sql)

# Fetch all results
schema_info = cursor.fetchall()

# Print the schema information
print("Table Schema for 'students':")
print("Column ID | Name | Type  | Not Null | Default Value | Primary Key")
print("-" * 70)  # Print a separator line
for column in schema_info:
    print(f"{column[0]:<9} | {column[1]:<4} | {column[2]:<5} | {column[3]:<8} | {column[4]:<13} | {column[5]:<11}")

# Close the connection
conn.close()
