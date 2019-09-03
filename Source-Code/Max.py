import sys

def Max(list):
    mini = int(list[0])
    maxi = int(list[0])
    for j in list:
        if j < mini:
            mini = j
        elif j > maxi:
            maxi = j
    return mini, maxi
#main
List = []
n = int(input("max input number: "))
for i in range(n):
    List.append(int(input()))

print(Max(List))