import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to delete the student with id = 3
delete_student_sql = '''
DELETE FROM students
WHERE id = ?;
'''

# Execute the SQL command to delete the student
cursor.execute(delete_student_sql, (3,))

# Commit the changes
conn.commit()

# SQL command to query the table to verify the deletion
select_all_sql = '''
SELECT * FROM students;
'''

# Execute the SQL command to select all records
cursor.execute(select_all_sql)

# Fetch all results
records = cursor.fetchall()

# Print the results
print("Remaining Records:")
print("ID | Name    | Age | Grade")
print("-" * 30)  # Print a separator line
if records:
    for record in records:
        print(f"{record[0]:<2} | {record[1]:<7} | {record[2]:<3} | {record[3]:<5}")
else:
    print("No records found.")

# Close the connection
conn.close()
