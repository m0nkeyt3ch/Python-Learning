max = int(input())
array = []

#loop for get input
for i in range(max):
    num = int(input())
    array.append(num)

print(array[::-1]) #print reverse list