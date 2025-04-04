import math_operations  # Import the math module
import string_operations  # Import the string module

# Using math functions
num1, num2 = 10, 5
print(f"Addition: {math_operations.add(num1, num2)}")
print(f"Subtraction: {math_operations.subtract(num1, num2)}")
print(f"Multiplication: {math_operations.multiply(num1, num2)}")
print(f"Division: {math_operations.divide(num1, num2)}")
print(f"Exponentiation: {math_operations.exponentiate(num1, num2)}")
print(f"factorial: {math_operations.factorial(num1)}")
print(f"Square Root: {math_operations.square_root(num1)}")


# String functions
text = "Victor's Diary"
print(f"Reversed String: {string_operations.reverse_string(text)}")
print(f"Capitalized String: {string_operations.capitalize_string(text)}")
print(f"Vowel Count: {string_operations.count_vowels(text)}")


# string_operations.py - A module containing string manipulation functions

def reverse_string(s):
    """Returns the reversed version of the input string."""
    return s[::-1]

def capitalize_string(s):
    """Returns the string with the first letter capitalized."""
    return s.capitalize()

def count_vowels(s):
    """Returns the count of vowels in the given string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# math_operations.py - A module containing math-related functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero is not allowed!"

def exponentiate(base, exponent):
    return base ** exponent

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def square_root(n):
    if n >= 0:
        return n**0.5
    else:
        "Error: square root is not allowed!"
