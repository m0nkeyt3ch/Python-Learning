from sys import stdout

data = int(input("input number: "))
lst = []
lst.append(data % 10)
lst.append(data % 100 / 10)
lst.append(data % 1000 / 100)
lst.append(data / 1000)

for i in range(4):
    lst[i] += 5
    lst[i] %= 10
    for i in range(2):
        lst[i], lst[3 - i] = lst[3-i], lst[i] #swap
        for i in range(3,-1,-1):
            stdout.write(str(lst[i]))
