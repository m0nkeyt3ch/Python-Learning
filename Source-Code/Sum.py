x = input("integer number ")
if int(x) < 0:
    print("Error")
total = 0
for i in range(int(x) + 1):
    total += i
if int(x) < 0:
    print("the sum of ", x, "is error")
else:
    print("the sum of ", x, "is", sum)