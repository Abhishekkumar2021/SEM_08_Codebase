'''
Docstring for src.examples.conditionals

Conditionals Example
- if statement
- if-else statement
- if-elif-else statement
- matching with match-case (Python 3.10+)

This module demonstrates the use of conditional statements in Python.
'''

age = 20

if age > 18:
    print("You are an adult.")
    
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
    
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
    
status = "student"

match status:
    case "student":
        print("You are a student.")
    case "employed":
        print("You are employed.")
    case "unemployed":
        print("You are unemployed.")
    case _:
        print("Status unknown.")