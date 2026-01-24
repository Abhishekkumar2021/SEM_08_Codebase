import random as rand
import math

# Random float between 0.0 and 1.0
x = rand.random()
print(f"Random float between 0.0 and 1.0: {x}")

# Random between a and b
a = 5
b = 10
x = rand.randint(a, b)
print(f"Random integer between {a} and {b}: {x}")

def rand_between(a, b):
    """Return a random integer N such that a <= N <= b."""
    scale = b - a + 1
    shift = a
    integer_part = math.floor(rand.random() * scale)
    return integer_part + shift

# Using the custom function to get a random integer between a and b
x = rand_between(a, b)
print(f"Random integer between {a} and {b} using custom function: {x}")

# Random float between a and b
x = rand.uniform(a, b)
print(f"Random float between {a} and {b}: {x}")

# random choice from a list
fruits = ['apple', 'banana', 'cherry', 'date']

# Way 01 -> Get random integer between 0 and len(fruits)-1
index = rand.randint(0, len(fruits) - 1)
print(f"Random fruit using index: {fruits[index]}")

# Way 02 -> Using random.choice()
fruit = rand.choice(fruits)
print(f"Random fruit using choice(): {fruit}")