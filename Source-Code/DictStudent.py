def Find_key(id, dictionary):
    for key in dictionary:
        if id in key['stuID']:
            return print(key)
    if id not in key['stuID']:
        return print("Student ID not exist")

def Update_data(id, age, dictionary):
    for key in dictionary:
        if id in key['stuID']:
            key['age'] = age
            return print(key)
    if id not in key['stuID']:
        return print("Student ID not Exist")

def Delete_data(id, dictionary):
    for i in range(len(dictionary)):
        if(dictionary[i]['stuID'] == id):
            del dictionary[i]
            break
    else:
        print("Student ID not Exist")

#list of student dictionary
StuDict = [
    {'no': 'stu1', 'stuID': '0001', 'name':'Kate', 'gender':'F', 'age':18, 'major': 'Computer'},
    {'no': 'stu2', 'stuID': '0003', 'name':'Jake', 'gender':'M', 'age':19, 'major': 'Art'},
    {'no': 'stu3', 'stuID': '0004', 'name':'Lily', 'gender':'M', 'age':20, 'major': 'Computer'},
    {'no': 'stu4', 'stuID': '0006', 'name':'Fresh', 'gender':'F', 'age':20, 'major': 'Math'}
]

#Find a student with his stuIDand output his info.
stu_id = input("Please enter student id to find: ")

Find_key(stu_id, StuDict)

#Update the student’s age by user input whose stuID by user input
up_id = input("Please enter student id to update: ")
age_up = int(input("Please enter age to update: "))

Update_data(up_id, age_up, StuDict)

#Delete the student whose stuID is by user input
del_id = input("Please enter student id to delete: ")
Delete_data(del_id, StuDict)

#Print all the students’ info one by one
for item in StuDict:
    print(StuDict)
"""
Note: 
The reason that i use user input to determine which ID that user want to delete
is to make the program more dynamic.
"""