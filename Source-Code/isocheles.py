side = int(input())
c = '*'
for i in range(side):
    print((c*i).rjust(side-1)+c+(c*i).ljust(side-1))