import sqlite3

def count_students(db_path):
    return sqlite3.connect(db_path).execute("SELECT COUNT(*) FROM students").fetchone()

db_path = 'path_to_your_database.db'
print(f"Number of students: {count_students(db_path)}")
