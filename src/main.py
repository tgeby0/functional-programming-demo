# List of imperative functions to transform in Haskell
# Only modify the main function if you want to test these functions with different inputs

def printAMessage(x):
    print(x)

def division(x,y):
    if x == y:
        return 0
    else:
        return x/y
    
def factorial(n):
    if n == 1 or n == 0:
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



if __name__ == "__main__":

    # Testing all imperative functions
    # You do not need to replicate the print statements exactly in main.hs

    printAMessage("\nHello World!\n")

    print("Testing division: \n")
    z = division(1,2)
    w = division(1,1)
    g = division(6,2)
    print(f'z: {z}, w: {w}, g: {g}\n')

    print("Testing factorial: \n")
    a = factorial(1)
    b = factorial(7)
    print(f'a: {a}, b: {b}\n')

    print("Testing factList: \n")
    testList = factList(5)
    print(f"testList: {testList}\n")
