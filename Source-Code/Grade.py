grade = [98, 86, 90, 78, 65, 83, 90, 56, 69, 77]
sum = 0
A = [] #100~90
B = [] #89~80
C = [] #79~70
D = [] #69~60
E = [] #59~0
long = len(grade)
grade.sort()

for i in grade:
    sum += i

    if(i<=100 and i>=90):
        A.append(i)
    elif(i<=89 and i>=80):
        B.append(i)
    elif(i<=79 and i>=70):
        C.append(i)
    elif(i<=69 and i>=60):
        D.append(i)
    elif(i<=59 and i>=0):
        E.append(i)

print("100~90 =", len(A))
print("89~80 =", len(B))
print("79~70 =", len(C))
print("69~60 =", len(D))
print("59~0 =", len(E))
print("average score =", float(sum/long))
print(max(grade))
print(grade)
