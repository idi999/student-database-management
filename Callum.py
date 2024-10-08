student_records = [
    {"name": "Alice", "age": 20, "grade": 85.5},
    {"name": "Bob", "age": 19, "grade": 78.0},
    {"name": "Charlie", "age": 22, "grade": 90.2}
]

def search_student_by_name(name):
    # Extract names from student records
    names = [student['name'] for student in student_records]

    # Attempt to find the index of the student
    try:
        index = names.index(name)
        return index  # Return the index if found
    except ValueError:
        return None  # Return None if not found

# Example usage
if __name__ == "__main__":
    user_input = input('Please enter the name of the student: ')
    index = search_student_by_name(user_input)

    if index is None:
        print('No record found.')
    else:
        student_found = student_records[index]  # Get student details
        print(f"Record found: {student_found}")