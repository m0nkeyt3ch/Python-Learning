StuDict = {
    'stu4': [82, 66, 85],
    'stu1': [67, 76, 84],
    'stu2': [72, 84, 79],
    'stu3': [98, 80, 91]

}

for key in sorted(StuDict, reverse=True):
    print(key, StuDict[key])
