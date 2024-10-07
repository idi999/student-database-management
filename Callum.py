User_input = input('Would you kindly, enter the name of the name of the student. ')
search_student = [d ['name'] for d in student_records]
try:
    index = search_student.index(User_input)
except ValueError:
    index = 'No record found'
if index == 'No record found':
    print('No record found')
else:
    print(index)
