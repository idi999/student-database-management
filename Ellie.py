students = [
    {'name' : 'John', 'age' : 18, 'grade' : 80.5}
    {'name' : 'Samantha', 'age' : 20, 'grade' : 64.0}
]

def display_students():
    for i in range(len(students)):
        print(*students[i])

