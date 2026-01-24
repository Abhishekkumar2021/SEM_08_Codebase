'''
Docstring for src.examples.functions

Functions Examples
- Defining a function
- Function with parameters
- Function with return value
'''

# Defining a function
def greet():
    print("Hello, World!")
    
greet()  # Calling the function

# Function with parameters
def add(a: int, b: float):
    return a + b

result = add(5, 3.2)
print(f"The sum is: {result}")

# Function with return value
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = 5
fact = factorial(num)
print(f"The factorial of {num} is: {fact}")