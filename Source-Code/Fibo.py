def Fibo(number):
    if(number <= 1):
        return number
    return Fibo(number-1) + Fibo(number-2)


user_input = int(input())

for i in range(user_input):
    print("Fibo", i, Fibo(i))
