# What to store:
# 1. height
# 2. name
# 3. lecture number
# 4. grades
import random

def create_student(n):
    """ TODO: finish creating student dictionary """
    student = {}
    student['height'] = 5.5
    student['name'] = n
    student['lecture'] = random.randint(1,3)
    student['grades'] = [random.randint(0,100)
                         for var in range(3)]
    return student

s1 = {'height':5.5, 'name':'amy', 'lecture':1,
      'grades':[97,80,74]}
s2 = {'Height':6, 'Name':'Bob','Lecture':2,
      'Grades':[40,78,90]}
students = [s1, s2]

for student in students:
    print student['Name'] # KeyError for s1 - 'name' vs 'Name'
    print sum(student['Grades'])/float(len(student['Grades']))
