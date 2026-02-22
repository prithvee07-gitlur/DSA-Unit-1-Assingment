# Recursive Factorial and Fibonacci

# --- Factorial using recursion ---
# this function calculates factorial of a number using recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Time Complexity: O(n) - we multiply n times
# Space Complexity: O(n) - because of recursive function calls


# --- Factorial using memoization ---
# stores already calculated results so we don't repeat work
memo_fact = {}

def factorial_memo(n):
    if n in memo_fact:
        return memo_fact[n]
    if n <= 1:
        return 1
    else:
        memo_fact[n] = n * factorial_memo(n - 1)
        return memo_fact[n]

# Time Complexity: O(n) - each value is calculated only once
# Space Complexity: O(n) - because of recursive calls and stored results


# --- Fibonacci using recursion ---
# this function returns the nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Time Complexity: O(2^n) - two recursive calls for each term
# Space Complexity: O(n) - because of recursive function calls


# --- Fibonacci using memoization ---
# stores already calculated results so we don't repeat work
memo_fib = {}

def fibonacci_memo(n):
    if n in memo_fib:
        return memo_fib[n]
    if n <= 1:
        return n
    else:
        memo_fib[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        return memo_fib[n]

# Time Complexity: O(n) - each value is calculated only once
# Space Complexity: O(n) - because of recursive calls and stored results


# --- taking input from user ---
n = int(input("Enter a positive number: "))

while n < 0:
    n = int(input("Please enter a positive number: "))

# printing factorial
print("Factorial of", n, "is", factorial(n))
print("Factorial of", n, "(with memoization) is", factorial_memo(n))

# printing fibonacci
print("Fibonacci term at position", n, "is", fibonacci(n))
print("Fibonacci term at position", n, "(with memoization) is", fibonacci_memo(n))