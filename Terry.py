students = []

def add_student(name, age, grade):

    student_record = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student_record)
    print(f"Added student: {student_record}")

if __name__ == "__main__":
    name = input("Please input student name: ")
    age = input("Please input student age: ")
    grade = input("Please input student grade: ")
    add_students(name, age, grade)
