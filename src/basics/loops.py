'''
Docstring for src.examples.loops

Loops Examples
- for loop
    - iterating over a list
    - iterating over a dictionary
- while loop
'''

# For loop examples
# Iterating over a list
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
    
# Using index to iterate over a list

n = len(fruits)
for i in range(n): # [0, n)
    print(f"The fruit at index {i} is {fruits[i]}")
    
# Iterating over a dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in person:
    print(f"{key}: {person[key]}")
    
for key, value in person.items():
    print(f"{key}: {value}")
