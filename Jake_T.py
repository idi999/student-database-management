def count_students(file_path):
    try:
        # Initialize a counter for students
        count = 0
        
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line in the file
            for line in file:
                # Increment the count for each line (student)
                count += 1

        return count

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return 0
    except Exception as e:
        print(f"An error occurred while counting students: {e}")
        return 0

# Example usage
if __name__ == "__main__":
    file_path = 'students.txt'  # Update this path as needed
    total_students = count_students(file_path)
    print(f"Number of students: {total_students}")
