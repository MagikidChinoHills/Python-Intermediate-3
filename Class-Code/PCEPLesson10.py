# Lesson 10: Advanced Error Handling
# it crash/stop the entire code when it detects an error
# try-except blocks to handles the error
# we can handle multiple exceptions together and individually
#
#
# try:
#     num = int(input("enter a number: "))
# except ValueError:
#     print("invalid input")
#
# # create a function that asks the user to enter 2 numbers
# # and find the product of those two numbers. Additionally,
# # that function is also going to handle the ValueError exception
# # Finally, test the function by calling and printing out the result.
#
#
# def prod():
#     try:
#         num1 = int(input("enter the first number: "))
#         num2 = int(input("enter the second number: "))
#         return num1 * num2
#     except ValueError:
#         print("invalid inout")
#
# result = prod()
# print(result)

# create a function that handles ZeroDivisionError and test it out to make
#   sure it works properly
# def div(a, b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("you cannot divide by zero")
# div(5,0)


# create a function that will access a list and that also handles both the
#   index error and type error individually
# def save_access(first, index):
#     try:
#         return first[index]
#     except IndexError:
#         return "error"
#     except TypeError:
#         return "type error"
#
# numbers = [10, 20, 30]
# index = 5
# print(save_access(numbers, 2))
#
# # create a function that will access a list and that also handles both the
# #   index error and type error together in a single except
# def list_errors(first, index):
#     try:
#         return first[index]
#     except (IndexError, TypeError):
#         return "error"

# create a custom exception and test it out
class CustomError(Exception):
    pass

try:
    raise CustomError("My customized message goes here")
except CustomError as e:
    print("custom error: ", e)
