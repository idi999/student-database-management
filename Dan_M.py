import students_file

  # Define the function to load student data from a file
def load_from_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Initialize the global student database
            global student_database
            student_database = []
 
            # Read each line in the file
            for line in file:
                # Split the line by commas to get student details
                name, age, grade = line.strip().split(',')
 
                # Convert age to integer and grade to float
                age = int(age)
                grade = float(grade)
 
                # Append the student data as a tuple to the database
                student_database.append((name, age, grade))
 
        print(f"Data loaded successfully from {filename}")
 
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
 
# Example usage
if __name__ == "__main__":
    load_from_file('students.txt')
    print(student_database)
