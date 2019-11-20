def Fibo(number):
    if(number <= 1):
        return number
    return Fibo(number-1) + Fibo(number-2)

