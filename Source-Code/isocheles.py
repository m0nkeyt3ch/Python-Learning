side = int(input("input sides: "))

for i in range(side):
    print(' ' * (side - i - 1) + '*' * (2 * i + 1))
    # single whitespace present in the print statement string
