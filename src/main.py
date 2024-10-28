# List of imperative functions to transform in Haskell
# Only modify the main function if you want to test these functions with different inputs

def printAMessage(x):
    print(x)

def division(x,y):
    if x == y:
        return None
    else:
        return x/y
    
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        number = 1
        for i in range(2, n+1):
            number *= i
        return number

def factList(n):
    factorial_list = [None] * n
    j = 0
    for i in range(1, n+1):
        factorial_list[j] = factorial(i)
        j += 1
    return factorial_list

def merge(ls1, ls2):
    result = []
    i = 0
    j = 0
    
    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            result.append(ls1[i])
            i += 1
        else:
            result.append(ls2[j])
            j += 1
            
    while i < len(ls1):
        result.append(ls1[i])
        i += 1
        
    while j < len(ls2):
        result.append(ls2[j])
        j += 1
        
    return result


if __name__ == "__main__":

    # Testing all imperative functions
    # You do not need to replicate the print statements exactly in main.hs

    printAMessage("\nHello World!\n\n")

    print("Testing division: \n")
    z = division(1,2)
    w = division(1,1)
    g = division(6,2)
    print(f'z: {z}, w: {w}, g: {g}\n')

    print("\nTesting factorial: \n")
    a = factorial(1)
    b = factorial(7)
    print(f'a: {a}, b: {b}\n')

    print("\nTesting factList: \n")
    testList = factList(5)
    print(f"testList: {testList}\n")
    
    print("\nTesting merge: \n")
    merged = merge([1, 3, 6], [2, 4, 5, 6, 7])
    print(f"merge: {merged}\n")
