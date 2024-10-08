def delete_student(name):
    global student_database  

    for student in student_database:
        if student["name"].lower() == name.lower():  
            student_database.remove(student) 
            print(f"{name} has been deleted from the database.")
            return
        
print(f"The student you have named {name} not found in the database.")
