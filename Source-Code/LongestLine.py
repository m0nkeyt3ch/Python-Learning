maxi = int(input())
data = []

#loop for get input
for i in range(maxi):
    num = input()
    data.append(num)

print(max(data, key = len))
#in here key is declare for keyword in this case is len of string
