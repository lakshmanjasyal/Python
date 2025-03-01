student={'name':'John','age':25,'courses':['Math','CompSci']}
# print(student['name'])
# print(student['courses'])
# print(student.get('phone'))
# student['phone']='555-5555'
# print(student.get('phone'))
del student['age']

print(student)
print(student.keys())
print(student.values())
print(student.items())
for key,value in student.items():
    print(key,value)
    print(student)