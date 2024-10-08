def save_to_file(filename)
  tyr:
      with open{filename, 'W'} as file:
      for student in student_database:
         name, age, grade = student
        file.write(f'{name},{age},{grade}\n')

      print(f'Data saved successfully to {filename}')

except Exception as e:
        print(f"An error occurred while saving data: {e}")
 
if __name__ == "__main__":
   
    student_database = [
        ("Alice", 20, 85.5),
        ("Bob", 19, 78.0),
        ("Charlie", 22, 90.2)
    ]
   
    save_to_file('students.txt')
