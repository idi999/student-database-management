# Initialize an empty list to hold student records
students = []

def add_student(students, name, age, grade):
    """
    Add a new student to the student records.

    Parameters:
    students (list): The list of student records.
    name (str): The name of the student.
    age (int): The age of the student.
    grade (float): The grade of the student.
    """
    student_record = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student_record)  # Append the student record to the list
    print(f"Added student: {student_record}")

# Example usage
if __name__ == "__main__":
    # Get student information from user input
    name = input("Please input student name: ")
    age = int(input("Please input student age: "))  # Convert age to integer
    grade = float(input("Please input student grade: "))  # Convert grade to float

    # Call the function to add the student
    add_student(students, name, age, grade)

    # Print the updated student records
    print("Current student records:", students)
