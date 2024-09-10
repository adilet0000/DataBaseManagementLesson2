import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to update the grade of students with age > 20 to 4.0
update_grade_sql = '''
UPDATE students
SET grade = 4.0
WHERE age > 20;
'''

try:
    # Start a transaction
    cursor.execute('BEGIN TRANSACTION;')
    
    # Execute the SQL command to update the grades
    cursor.execute(update_grade_sql)
    
    # Commit the transaction
    conn.commit()
    
    print("Transaction committed successfully. Grades updated.")
except sqlite3.DatabaseError as e:
    # Rollback the transaction in case of any error
    conn.rollback()
    print("Transaction failed. Rolled back changes.")
    print(f"Error details: {e}")
finally:
    # Close the connection
    conn.close()
