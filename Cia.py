
student_records = {
    "Alice": 85.5,
    "Bob": 78.0,
    "Charlie": 90.2
}

def update_grade(name, new_grade):
    
    if name in student_records:
        student_records[name] = new_grade  
        print(f"{name}'s grade has been updated to {new_grade}.")
    else:
        print(f"No record found for student named {name}.")


if __name__ == "__main__":
    name = input("Enter the name of the student: ")
    new_grade = float(input("Enter the new grade: "))  
    update_grade(name, new_grade)
    print("Updated student records:", student_records)