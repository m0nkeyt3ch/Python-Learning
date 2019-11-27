a = int(input("input basis number: "))
n = int(input("input count: "))

arr = []

num = 0

for i in range(n):
    num += a * (10 ** i)
    arr.append(num)

base = len(arr)
for i in range(base):
    print ("%d"%arr[i], end = ' ')
    if i == base - 1:
        print ('')
    else:
        print ('+', end = ' ')

print (sum(arr))
