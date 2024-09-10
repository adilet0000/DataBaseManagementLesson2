import sqlite3

connection = sqlite3.connect('school.db')
cursor = connection.cursor()
print(f"success {connection}")