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

Go into `main.hs` and type in the following code, then run it using `runghc src/main.hs`.

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
