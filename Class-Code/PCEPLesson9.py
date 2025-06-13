# Lesson 9: Functions

# Problem: Write a function that takes two numbers and returns their sum.
# Test it out by calling the function and print the result.
# def me():
#     a = int(input("Can I have a number please: "))
#     b = int(input("Can I have another number please: "))
#     return a + b
# print(me())
#
# def sum(a, b):
#     return a + b
# print(sum(10, 22))
#
# # Problem: Write a function that checks whether a number is even or odd.
# def check_even_or_odd():
#     a = int(input("enter a number please: "))
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check_even_or_odd()
#
# def even_odd(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# # Problem: Write a function that returns the largest of three numbers.
# def max_of_three(a, b, c):
#     print("the max is:", max(a, b, c))
# max_of_three(10, 6, 20)
#
# # Problem: Write a function that returns the factorial of a number.
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# Problem: Write a function that counts the number of vowels in a string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print("total of vowels:", count)
count_vowels("hello world lets play roblox")

# Problem: Write a function that reverses a string.
def reverse_string(s):
    print(s[::-1])
reverse_string("word")
