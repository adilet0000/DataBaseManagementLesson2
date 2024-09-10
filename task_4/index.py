import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to select all records
select_all_sql = 'SELECT * FROM students;'

# Execute the SQL command
cursor.execute(select_all_sql)

# Fetch all results
records = cursor.fetchall()

# Print the results in a readable format
print("ID | Name    | Age | Grade")
print("-" * 30)  # Print a separator line
for record in records:
    print(f"{record[0]:<2} | {record[1]:<7} | {record[2]:<3} | {record[3]:<5}")

# Close the connection
conn.close()
