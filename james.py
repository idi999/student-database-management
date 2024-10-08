# Sample student database for demonstration
student_database = [
    {"name": "Alice", "age": 20, "grade": 85.5},
    {"name": "Bob", "age": 19, "grade": 78.0},
    {"name": "Charlie", "age": 22, "grade": 90.2}
]

def delete_student(name):
    global student_database  # Declare to use the global variable
    
    # Search for the student in the database
    for student in student_database:
        if student["name"].lower() == name.lower():  # Case-insensitive comparison
            student_database.remove(student)  # Remove the student
            print(f"{name} has been deleted.")
            return

    print(f"Student named {name} not found in the database.")

# Example usage
if __name__ == "__main__":
    student_delete = input("What student would you like to delete? ")
    delete_student(student_delete)
    print("Updated student database:", student_database)
