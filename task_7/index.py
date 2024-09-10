import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to select all students with age greater than 20
select_filtered_sql = '''
SELECT * FROM students
WHERE age > 20;
'''

# Execute the SQL command
cursor.execute(select_filtered_sql)

# Fetch all results
filtered_records = cursor.fetchall()

# Print the results
print("Students with Age Greater than 20:")
print("ID | Name    | Age | Grade")
print("-" * 30)  # Print a separator line
if filtered_records:
    for record in filtered_records:
        print(f"{record[0]:<2} | {record[1]:<7} | {record[2]:<3} | {record[3]:<5}")
else:
    print("No records found.")

# Close the connection
conn.close()
