# Importing the necessary functions from other files
from Terry import add_student
from Ellie import display_students
from Callum import search_student
from Cia import update_grade
from James import delete_student
from Jake import count_students
from Dan_S import average_grade
from Matty import save_to_file
from Dan_M import load_from_file
 
# Initializing the student database as a list
student_database = []
 
def main():
    # Load existing student data from file if needed
    load_from_file("students.txt")
 
    while True:
        print("\n--- Student Database Management System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search for Student")
        print("4. Update Student Grade")
        print("5. Delete Student")
        print("6. Count Students")
        print("7. Average Grade")
        print("8. Save to File")
        print("9. Load from File")
        print("0. Exit")
        choice = input("Please choose an option (0-9): ")
 
        if choice == '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            add_student(name, age, grade)
            print(f"Student {name} added successfully.")
        elif choice == '2':
            print("Displaying all students:")
            display_students()
        elif choice == '3':
            name = input("Enter the name of the student to search for: ")
            student = search_student(name)
            if student:
                print(f"Student found: {student}")
            else:
                print("Student not found.")
        elif choice == '4':
            name = input("Enter the student's name to update their grade: ")
            new_grade = float(input("Enter the new grade: "))
            update_grade(name, new_grade)
            print(f"Grade updated for student {name}.")
        elif choice == '5':
            name = input("Enter the name of the student to delete: ")
            delete_student(name)
            print(f"Student {name} deleted successfully.")
        elif choice == '6':
            count = count_students()
            print(f"There are {count} students in the database.")
        elif choice == '7':
            avg_grade = average_grade()
            print(f"The average grade is: {avg_grade:.2f}")
        elif choice == '8':
            save_to_file("students.txt")
            print("Student data saved to students.txt.")
        elif choice == '9':
            load_from_file("students.txt")
            print("Student data loaded from students.txt.")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
 
if __name__ == "__main__":
    main()
