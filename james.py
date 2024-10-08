def delete_students(name):
  student_database.pop(student_delete)
  print(student_database)
student_delete = input("What student would you like to delete?")
