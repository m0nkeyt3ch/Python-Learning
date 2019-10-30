price = int(input("Price: "))
disc1 = (10/100)*price
disc2 = (20/100)*price

if(price <= 10):
    print(price - disc1)

elif(price >= 20):
    print(price - disc2)
