def printAMessage(x):
    print(x)

def division(x,y):
    if x == y:
        return 0
    else:
        return x/y
    
def factorial(n):
    if n == 1:
        return n
    else:
        number = 1
        for i in range(2, n+1):
            number *= i
        return number

def factList(n):
    factorial_list = []
    iterator = 0
    for i in range(1, n+1):
        factorial_list[iterator] = factorial(i)
        iterator += 1
    return factorial_list