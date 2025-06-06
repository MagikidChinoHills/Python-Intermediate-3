# Lesson 8: Exceptions in Python
# Exception: errors that occur during the execution of a program
#   and breaks the flow of the code.

# Python handles the exception by raising it when it cannot be
# handled automatically

# example: is the following code possible?
# x = 10 / 0 # this will cause a ZeroDivisionError

# ZeroDivisionError: occurs when we divide a number by zero
# ValueError: received an invalid value
# TypeError: operation applied to not compatible types
# IndexError: accessing invalid index
# KeyError: accessing nonexistent key
# AttributeError: attribute reference is invalid  ex: "abc".length
# ImportError: importing a nonexistent module
# FileNotFoundError: trying to access a file that doesn't exist
# NameError: trying to access a variable that doesn't exist
# AssertionError: invalid assertion, ex: assert 2 + 2 == 5

# example of ZeroDivisionError:
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("You cannot divide by 0.")
# except ValueError:
#     print("Invalid input.")

# create a block of code that will handle both type error and value error
# try:
#     num = int(input("enter a number"))
#     letter = input("enter a letter")
#     error = num + letter
# except TypeError:
#     print("Invalid math operation")
# except ValueError:
#     print("Invalid input.")

try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print(f"You entered: {value}")
finally:
    print("This will always run.")

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

# Write a program that reads a file and handles a FileNotFoundError.
