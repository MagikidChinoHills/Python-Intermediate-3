# Lesson 16: PCEP Review

# 1. Core Python Concepts
# 1.1 Variable and Data Types: float, string, int, bool,
# example:
name = "Alice" # string
age = 25 # integer
height = 5.7 # float
is_student = False # boolean

# source code: any programming code
# language: programming languages, high level programming languages,
#   machine languages, natural language
# compilation: convert a source code into a binary that later the compiler
#   will execute (run)
# compiler: the program in charge of running the compiled file
# interpretation: a source that does not need to be translated into a
#   binary file
# interpreter: the program is able to execute the source code without being
#   compiled

# 1.2 Operators and expressions
# arithmetic operators (7):
#   +, -, *, /, ** (exponentiation), // (floor division), % (modulus)
# comparison operators (6): >, <, >=, <=, ==, !=
# logical operators (3): and (&&), or (||), not (!)
# ^ -> XOR -> exclusive or: only one condition can be true for the final answer to be true
# example:
x = 10
y = 3
print(x + y, x // y, x ** y) # output: 13 3 100

# 1.3 Control Flow (Conditional Statements)
# it allows decision-making in the code
# if, elif, else
# example:
age = 18
if age >= 18:
    print("you can vote")
elif age < 18:
    print("you are not old enough")
if age >= 18:
    print("you are at least 18 years old")
elif age > 18:
    print("you are older than 18")
else:
    print("you are not eligible to vote")

# 2. Loops and iteration
# loops: for loop and while loop
# iteration: repeating over and over

# 2.1 For Loops
# for loops can be used iterates over a sequence like lists, tuples, and ranges
for i in range(5):
    print(i) # output: 0, 1, 2, 3, 4
# range(start, stop, step)
# start: index at 0 is not defined, inclusive
# stop: stop is required, and it's exclusive
# step: how many steps at the time
# example:
for i in range(2, 8, 3):
    print(i, end=" ") # output: 2 5

# 2.2 While loops: runs as long as the condition is true
# example:
count = 2
while count < 5:
    print(count)
    count += 3 # output: 2

# 3. Functions: reusable block of code,
def function_name(paremeter):
    return f"hello {paremeter}"
# example of calling the function and passing the argument
function_name("Bob") # does not print anything because we are not using the print statement

# 4. Data Structure
# 4.1 List: ordered, mutable, indexing, []
# example:
color = ["pink", "darker pink", "very dark pink"]
color.append("super dark pink") # adds to the end of the list
print(color)
print(color[2]) # output: very dark pink
color.insert(1, "darkest pink in the world")
print(color)

# 4.2 Tuples: immutable, ordered, index, ()
# example:
coordinates = (10, 20)
print(coordinates[0]) # output: 10
coordinates = 1, # What is this? a single element tuple
print(coordinates)
x, y = (1, 2)
print(y) # output: 2

# 4.3 Dictionaries: key-value pairs, unordered, mutable, {}
# we use colons (:) to separate the key and value
# example:
person = {"name": "Bob", "age": 100}
print(person)
print(person['age']) # output: 100
print(person.keys()) # output: name, age
print(person.values()) # output: Bob, 100

# 4.4 Sets: mutable, unordered, {}, remove duplicates
numbers = {1, 2, 1, 2, 3}
print(numbers) # output: 1, 2, 3
# print(numbers[2]) -> not possible because it's unordered

# 5. Exception Handling: to handle errors gracefully
# try-except block to prevent program crashes
# What about else and finally? They are not mandatory to be included when
#   creating an exception handler
# example:
try:
    result = 10 / 0
except Exception as e:
    print("error:", e)
else:
    print("else gets printed when not exception is triggered")
finally:
    print("inside finally")

# 6. File Handling: reading and writing the files
# example:
with open("filename.txt", "w") as variable_name:
    variable_name.write("this the content of a file")

# exercise:
x = 5
y = 10
# what is the output for (x + y // 2 * 3): 20

# exercise: identify the error
numbers = [1, 2, 3]
# print(numbers[3]) # IndexError

# exercise: what will be printed
for i in range(3):
    print(i, end="\t*") # output: 0 *1  *2  *
    
