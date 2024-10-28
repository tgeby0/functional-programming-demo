# Functional Programming Demo

For this tutorial, you will be converting an imperative Python program into a functional program using Haskell. To submit this assignment, email a link of your forked repository to knguyen07@email.wm.edu.

### Pre-Requisites

Haskell Setup
* Follow the Haskell installation at https://www.haskell.org/ghcup/install/. You will only need the default installation.
* Download the Haskell VSCode extension at https://marketplace.visualstudio.com/items?itemName=haskell.haskell.

Pre-made Files
* `main.py`: A file that shows all the tasks you need to complete using functional programming
* `main.hs`: A blank file where you'll complete all your Haskell tasks
* `test.hs`: An optional, blank file for you to use to experiment with Haskell

## Haskell Tutorial

Here are a few tutorial websites to help you out: 
* https://www.schoolofhaskell.com/school/starting-with-haskell/introduction-to-haskell/1-haskell-basics
* https://www.tutorialspoint.com/haskell/haskell_overview.htm

First, let's try writing some basic Haskell code. Run `ghci` in your terminal, then enter the following code:

```hs
print "Hello, world!"
```

This should print "Hello, world!" in the console.

Now try entering this code:

```hs
a = 5
b = a * 2 + 3
```

If you check the values of a and b, you will find that they are 5 and 13 respectively. 

Now try entering `a = a + 1`, and check the value of a. You will find that the console hangs. This is because variables in Haskell are immutable, so the program cannot determine a value of a.

For comparison, look at the following Python code for adding up every number from 1 to 10.

```py
count = 0

for i in range(1, 11):
    count += i

print(count) # Prints 55
```

This code uses mutable variables, but this is impossible in Haskell, so how would you implement this behavior?

### Recursion

The answer is recursion. Recursive functions are key to Haskell, as they allow you to implement functions that depend on previous variables without having to mutate them.

Go into `test.hs` and type in the following code, then run it using `runghc src/test.hs`.

```hs
addNums :: Int -> Int
addNums 0 = 0
addNums n = n + addNums (n - 1)

main = print (addNums 10)
```

It will print "55" to the terminal.
Recursive functions have a base case and one or more inductive cases. They call the inductive cases until the function reaches the base case. Here, the `addNums` function better resembles how it would be mathematically defined.

The type hints are very important, so that the compiler knows what type and number of parameters the function will use. The actual function uses pattern matching, which chooses code to execute based on the values of the parameters. 

The base case is 0, as the sum of the numbers from 1 to 0 is 0. The inductive case then builds off of that to produce the final answer. The programmer does not need to manage the details of how this is calculated, they can just enter the definition of the function and Haskell will do the rest.

### Lists

Lists are the main data structure used in Haskell. Unlike Python's lists, these lists are actually linked lists. This makes writing some types of functions more convenient, but isn't great for indexing the middle of a list.

You can create a list using square brackets, like in Python. However, all values in the list must have the same type. You can also use the `:` operator to add an item to the beginning of the list. For example: `3 : [4, 5]` produces `[3, 4, 5]`.

You can also use pattern matching to work with lists, here is an example:

```hs
-- Adds together the values taken to the given power of each number in the list.
sumPowers :: Int -> [Int] -> Int
sumPowers _ [] = 0
sumPowers power (x : xs) = (x ^ power) + sumPowers power xs
```

When a Haskell function has multiple parameters, the type is written as such. You can pattern match with both parameters, and use `_` as a wildcard to represent any possible value when you don't need that parameter for the calculation. In this case, the first pattern matches any combination of parameters with an empty list, while the second pattern matches any combination where the list has at least one element.

Interestingly, you don't actually need to provide all parameters to a function. If you just provide a single parameter, such as `sumPowers 2`, it returns a function that you can call with the remaining parameters. This is called partial application. Generally you want to order parameters such that the parameters that change the least go first, as this makes partial application easier.

```hs
sumPowers2 = sumPowers 2
sumPowers3 = sumPowers 3

sum1 = sumPowers2 [1, 2, 3, 4] -- 30
sum2 = sumPowers3 [1, 2, 3, 4] -- 100
```

There are plenty of useful functions for lists, such as `map`, `filter`, `sum`, and `foldr`. Feel free to check out these functions at https://hackage.haskell.org/package/base-4.20.0.1/docs/Data-List.html. 

### Data Types

Haskell contains many different data types, and also allows you to define your own. For example, the `Maybe` type is useful for defining a value which may or may not exist. The definition looks like this:

```hs
data Maybe a = Just a | Nothing
```

You can then create an instance of this `Maybe` type using `Just` with a value, or `Nothing`. You can also pattern match with data types. Here is an example:

```hs
-- Calls a function on a Maybe value if it exists, returning the result, or returns a default value otherwise
callOrDefault :: (a -> b) -> b -> Maybe a -> b
callOrDefault fn _ (Just x) = fn x
callOrDefault _ defaultValue Nothing = defaultValue
```

The code path taken depends on what type `Maybe` is. This is also an example of a higher-order function, as it takes a function as a parameter. Feel free to check out more functions for `Maybe` at https://hackage.haskell.org/package/base-4.20.0.1/docs/Data-Maybe.html.

## Writing your own Haskell

There are several Python functions you will be tasked with converting into Haskell.

### printAMessage

This function just prints a value to the screen.

```py
def printAMessage(x):
    print(x)
```

For Haskell, it will have this type: `printAMessage :: Show a => a -> IO ()`. This means that it takes any value which can be converted to a string, and executes an IO side-effect.

Try writing your own version of the Python function in `main.hs`.

### division

This function divides 2 numbers, returning None if the denominator is 0.

```py
def division(x,y):
    if x == y:
        return None
    else:
        return x/y
```

In Haskell, it is generally preferred to always return something from a function. In this case, you will want your function to return a `Maybe` value. The type of your function will probably look like `division :: Double -> Double -> Maybe Double`.