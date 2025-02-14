# Introduction to Object Oriented Programming (OOP) in Python
'''
1. Object Oriented Programming:
    OOP is a programming paradigm that organize code into obkects.
    Objects have both data(attributes) and behavior(methods)
    associated to them.

2. Class:
    A class is a blueprint for creating objects. It defines
    the structure and behavior that its
    instances(objects) will have.

3. Object:
    An instance of a class, representing a specitic entity
    in the program.
'''

# Exercises 1
# Define a class called Book, with attributes 'title',
# 'author', and 'page'. Include methods such as
# 'display_info', that prints the books information

'''
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title} , Author: {self.author} , Pages: {self.pages}")

# First book
book1 = Book("Leo's diary", "Leo", 642)
book2 = Book("Leo's e-book that he bought by selling his soul", "Leo", 23)
book3 = Book("Alisa's ebook that she bought by selling her soul", "Alisa", 4)
book4 = Book("Cooking book", "Morgan Freeman", 4)
book5 = Book("Python Advanced", "Estevan", 42)

# Challenge 1
# Create 4 new books
# Create a list named Library and append all 5 books to this list.
# Optional: Create a for loop that displays info of each book

Library = [book1, book2, book3, book4, book5]

for book in Library:
    book.display_info()
'''
'''
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")
        else:
            print("Get ur money up")

    def get_balance(self):  # Getter method to access private balance
        return self.__balance

# Create an account
name = input("Enter your name: ")
account = BankAccount(name, 500)

# Menu
while True:
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: $"))
        account.deposit(amount)
        print(f"Your new balance is ${account.get_balance()}")  # Use the getter method
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: $"))
        account.withdraw(amount)
        print(f"Your new balance is ${account.get_balance()}")  # Use the getter method
    elif choice == "3":
        print("Thank you for stealing money from Leo's bank account")
        break
    else:
        print("Invalid choice")
'''

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # List to store grades

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Added grade: {grade}")

    def show_grades(self):
        if not self.grades:
            print(f"{self.name} has no grades yet.")
        else:
            print(f"{self.name}'s grades: {self.grades}")
            print(f"Average: {sum(self.grades) / len(self.grades):.2f}")

# Create a student instance
name = input("Enter student name: ")
student = Student(name)

while True:
    print("\n1. Add Grade")
    print("2. Show Grades")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        grade = float(input("Enter grade: "))
        student.add_grade(grade)

    elif choice == "2":
        student.show_grades()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")

