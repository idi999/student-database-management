import os

def load(filename):
    students = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, age, score = line.strip().split(', ')
                students.append({'name': name, 'age': int(age), 'score': float(score)})
    return students

def save(filename, students):
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student['name']}, {student['age']}, {student['score']:.2f}\n")

def display(students):
    print("\n> Current Students:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Score: {student['score']:.2f}")

def add(students):
    name = input("> Enter the student's name\n> ")
    age = int(input("> Enter the student's age\n> "))
    score = float(input("> Enter the student's score\n> "))
    students.append({'name': name, 'age': age, 'score': score})

def remove(students):
    display(students)
    idx = int(input("Enter the associated student number of the student you want to remove\n> ")) - 1
    if 0 <= idx < len(students):
        students.pop(idx)
        print("> Student removed.")
    else:
        print("> Invalid student number.")

def alter(students):
    display(students)
    idx = int(input("Enter the number of the associated student whose score you want to modify\n> ")) - 1
    if 0 <= idx < len(students):
        new_score = float(input("Enter the new score\n> "))
        students[idx]['score'] = new_score
        print("> Score updated.")
    else:
        print("> Invalid student number.")

def main():
    filename = 'student_data.txt'
    students = load(filename)

    while True:
        print("\n> Options")
        print("> 1|List students")
        print("> 2|Add student")
        print("> 3|Remove student")
        print("> 4|Modify student score")
        print("> 5|Save and exit")
        
        choice = input("> ")
        
        if choice == '1':
            display(students)
        elif choice == '2':
            add(students)
        elif choice == '3':
            remove(students)
        elif choice == '4':
            alter(students)
        elif choice == '5':
            save(filename, students)
            print("> Changes saved. Exiting.")
            break
        else:
            print("> Invalid. Try another.")

if __name__ == "__main__":
    main()

# Can add students
# Can remove students
# Can modify student scores
# Can list all students saved
# Can save to and read from student_data.txt
