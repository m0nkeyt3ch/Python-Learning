from operator import itemgetter

def sort_byno(dictionary):
    for data in dictionary:
        for item in sorted(data['math']):
            print(item)

StuDict = [
    {'no': 'stu1', 'math': 67, 'english': 76, 'python': 84},
    {'no': 'stu2', 'math': 72, 'english': 84, 'python': 79},
    {'no': 'stu3', 'math': 89, 'english': 80, 'python': 91},
    {'no': 'stu4', 'math': 82, 'english': 66, 'python': 85}
]


#print(StuDict['no'])
print("By No:")
sort_byno(StuDict)

"""
print("\n")
print("By Grade:")
for grade in sorted(StuDict, key=itemgetter('math')):
    print(grade)

for i, j in StuGrade.items():
    avgdict[i] = sum(j)/float(len(j))

print("\n")
print("By avg:")
print(sorted(avgdict.values()))
"""
