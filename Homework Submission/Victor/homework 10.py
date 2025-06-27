# Lesson 10: Advanced Error Handling - Combined Code Examples

# --------------------------
# 1. Identifying Exceptions
# --------------------------

print("1. Identifying Common Exceptions")
try:
    print("Divide by zero:")
    result = 5 / 0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError:", e)

try:
    print("\nConvert string to int:")
    number = int("abc")
except ValueError as e:
    print("Caught ValueError:", e)

try:
    print("\nAccess invalid list index:")
    my_list = [1, 2, 3, 4, 5]
    print(my_list[10])
except IndexError as e:
    print("Caught IndexError:", e)

try:
    print("\nAccess missing dictionary key:")
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print("Caught KeyError:", e)

try:
    print("\nUse undefined variable:")
    print(x + 5)
except NameError as e:
    print("Caught NameError:", e)

print("\n" + "-" * 40)

# --------------------------
# 2. Exception Handling in User Input
# --------------------------

print("2. Handling User Input Errors")

# ValueError Example
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

# ZeroDivisionError Example
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# FileNotFoundError Example
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")

print("\n" + "-" * 40)

# --------------------------
# 3. Handling Multiple Exceptions
# --------------------------

print("3. Handling Multiple Exceptions")

my_list = [10, 20, 30, 40]
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    index = int(input("Enter index to access list: "))
    result = num1 / num2
    print("Division result:", result)
    print("List value:", my_list[index])
except ValueError:
    print("Input error: Please enter only numbers.")
except ZeroDivisionError:
    print("Math error: Cannot divide by zero.")
except IndexError:
    print("Index error: That index does not exist in the list.")

print("\n" + "-" * 40)

# --------------------------
# 4. Using else and finally
# --------------------------

print("4. Using else and finally")
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Division by zero error.")
else:
    print("Division successful. Result:", y)
finally:
    print("Execution complete.")

print("\n" + "-" * 40)

# --------------------------
# 5. Creating Custom Exceptions
# --------------------------

print("5. Custom Exception: Insufficient Funds")

class InsufficientFundsError(Exception):
    def __init__(self, message="Withdrawal denied. Insufficient funds."):
        self.message = message
        super().__init__(self.message)

balance = 100

try:
    withdraw = int(input("Enter amount to withdraw: "))
    if withdraw > balance:
        raise InsufficientFundsError()
    else:
        balance -= withdraw
        print("Withdrawal successful. New balance:", balance)
except InsufficientFundsError as e:
    print(e)

print("\n" + "-" * 40)

# --------------------------
# 6. Debugging Common Errors
# --------------------------

print("6. Debugging Error Messages")

# ZeroDivisionError
try:
    a = 1 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")

# ValueError
try:
    b = int("abc")
except ValueError:
    print("ValueError: invalid literal for int() with base 10: 'abc'")

# IndexError
try:
    c = [1, 2, 3]
    print(c[5])
except IndexError:
    print("IndexError: list index out of range")

# KeyError
try:
    d = {"x": 1}
    print(d["y"])
except KeyError:
    print("KeyError: 'missing_key'")

# TypeError
try:
    e = 5 + "hello"
except TypeError:
    print("TypeError: unsupported operand type(s) for +: 'int' and 'str'")

print("\nEnd of Homework Examples")
