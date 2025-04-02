dog = {}

dog = {'name':'Tom',
       'color':'negro',
       'breed':'Chihuahua',
       'legs':4,
       'age':1}

student = {
    'first_name':'Hector',
    'last_name':'Olivo',
    'gender':'Male',
    'age':20,
    'marital_status':'single',
    'skills':['Python','SQL','HTML','CSS','JS'],
    'country':'Mexico',
    'city':'Aguascalientes',
    'addres':{
        'street':'Baker Street',
        'zipcode':'NW1 6XE',
    }
}

print(f'The lenght of the student dictionary is {len(student)}')
print(f'The data type of student skills is {type(student["skills"])}')

student['skills'].append('PHP')
print(student['skills'])

keyList = list(student.keys())
print(keyList)

valList = list(student.values())
print(valList)

studentTuple = student.items()
print(studentTuple)

student.pop('gender')
print(student)

del dog