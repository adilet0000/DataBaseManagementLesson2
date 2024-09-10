import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to update the grade of the student with id = 2
update_grade_sql = '''
UPDATE students
SET grade = ?
WHERE id = ?;
'''

# Execute the SQL command to update the grade
cursor.execute(update_grade_sql, (3.7, 2))

# Commit the changes
conn.commit()

# SQL command to query the updated record
select_updated_sql = '''
SELECT * FROM students
WHERE id = ?;
'''

# Execute the SQL command to select the record with id = 2
cursor.execute(select_updated_sql, (2,))

# Fetch the result
updated_record = cursor.fetchone()

# Print the result
print("Updated Record:")
print("ID | Name | Age | Grade")
print("-" * 25)
if updated_record:
    print(f"{updated_record[0]:<2} | {updated_record[1]:<4} | {updated_record[2]:<3} | {updated_record[3]:<5}")
else:
    print("No record found.")

# Close the connection
conn.close()
