students = {
    "Alice": 85.5,
    "Bob": 78.0,
    "Charlie": 90.2
}

def average_grade():
    """
    Calculate and return the average grade of all students.
    """
    if not students:  # Check if the dictionary is empty
        return 0  # Avoid division by zero if no students are present

    total = sum(students.values())  # Sum up all the grades
    average = total / len(students)  # Calculate the average
    return average

def alphabetical():
    """
    Print the student names in alphabetical order.
    """
    print("Students in alphabetical order:", sorted(students))

def student_count():
    """
    Return the total number of students.
    """
    return len(students)

# Example usage
if __name__ == "__main__":
    # Print average grade
    avg = average_grade()
    print(f"Average grade: {avg}")

    # Print students in alphabetical order
    alphabetical()

    # Print student count
    count = student_count()
    print(f"Total number of students: {count}")
