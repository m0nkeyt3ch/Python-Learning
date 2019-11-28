from operator import itemgetter

StuDict = [
    {'no': 'stu1', 'math': 67, 'english': 76, 'python': 84},
    {'no': 'stu2', 'math': 72, 'english': 84, 'python': 79},
    {'no': 'stu3', 'math': 89, 'english': 80, 'python': 91},
    {'no': 'stu4', 'math': 82, 'english': 66, 'python': 85}
]

StuGrade = {
    'stu1':[67, 76, 84],
    'stu2':[72, 84, 79],
    'stu3':[89, 80, 91],
    'stu4':[82, 66, 85]
}

avgdict ={}

#print(StuDict['no'])
print("By No:")
for key in sorted(StuDict, key=itemgetter('no')):
    print(key)

print("\n")
print("By Grade:")
for grade in sorted(StuDict, key=itemgetter('math')):
    print(grade)

for i, j in StuGrade.items():
    avgdict[i] = sum(j)/float(len(j))

print("\n")
print("By avg:")
print(sorted(avgdict.values()))

