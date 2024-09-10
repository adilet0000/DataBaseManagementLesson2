import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to insert a duplicate record
insert_duplicate_sql = '''
INSERT INTO students (id, name, age, grade, email)
VALUES (?, ?, ?, ?, ?);
'''

# Data for the duplicate record (id = 1)
duplicate_data = (1, 'Alice', 20, 3.8, 'alice@example.com')

try:
    # Execute the SQL command to insert the duplicate record
    cursor.execute(insert_duplicate_sql, duplicate_data)
    
    # Commit the changes
    conn.commit()
    
    print("Record inserted successfully.")
except sqlite3.IntegrityError as e:
    # Handle the IntegrityError which occurs due to duplicate primary key
    print("Error: Unable to insert record. It may be a duplicate.")
    print(f"Details: {e}")

# Close the connection
conn.close()
