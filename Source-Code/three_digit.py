n = int(input("enter your 3 digit integer: "))
count = 0
while(count != 3):
    m = int(input("enter your integer: "))

    if(m == n):
        print("true")
        break
    elif(m != n):
        count += 1
        print("input the right integer " + "error", count)
