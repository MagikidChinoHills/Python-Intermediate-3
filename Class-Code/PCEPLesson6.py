# Lesson 6: Functions in Python
from cert_lesson11 import names


# functions: reusable code
# parameters: any variable inside the parenthese when the function is
#       created
# arguments: variables that are put inside the parenthese
#       when calling a function
# returning function: a function that returns something
# lambda functions: function without name and it's represented
#   by a variable name
# recursive function: when the function calls itself until it solves the problem

#
def greet():
    print("hello")

# call the function by using its function name
greet()

# create a function that has 1 parameter
# and print a message with that parameter information
def hi(name):
    print(f"hello {name}")

# create a function that takes 2 argument
# return the sum of those 2 arguments
def sum(a, b):
    return a + b

# void function: a function that does not return anything

# is it possible for functions to call other functions: yes

# create a function that collects/calls another function
def calculate_area(l, w):
    return l * w

def display_area(l, w):
    area = calculate_area(l, w)
    print(f"The area is {area} square units.")

def hit(hi):
    if hi == 1:
        return 1
    return hi * hit(hi - 1)
a = hit(5)
print(a)

# lambda functions
multiplication = lambda x, y, z: x * y
print(multiplication(2, 3, 6))

# functions with a vairbale number of arguments
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=25)

# Write a function multiply(a, b) that returns the product of
#   two numbers. Assign it to a variable called product and
#   print it.
def multiply(a, b):
    return a * b
product = multiply(3, 4)
print(product)

# Create a function introduce(name, age=18) that prints a
#   default age if not provided .
def introduce(name, age=18):
    print(f"{name} is {age} years old")
introduce("Victor", 50)
introduce("Victor")

# Create a program with get_data(), process_data(),
#   and display_result() functions that interact
#   with each other.
def get_data():
    pass
def process_data():
    pass
def display_info():
    print(get_data(), process_data())
