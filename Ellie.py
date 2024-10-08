# Assuming the database is a 2D array named 'students'

def display_students():
    for i in range(len(students)):
        print(*students[i])