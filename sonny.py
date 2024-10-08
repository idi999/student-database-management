Students = {

}

def average_grade():
    average = 0
    for value in Students:
        average = average+value
    average = average/len(Students)

def alphabetical():
    print (sorted(Students))

def student_count():
    count = 0
    for value in range (Students):
        count = count+1
