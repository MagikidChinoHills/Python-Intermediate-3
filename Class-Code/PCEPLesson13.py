# Lesson 13: Solving Problems with Loops and Lists

# bug: computer error
# debugging: fixing bug
# debugger: tools which allows the programmer to run the code in
#       a fully controllable environment
# print debugging: uses the print statement to trace execution
#       parts
# testing: the environment that will allow you to ensure that the
#       code behave correctly

# List: mutable collection, indexing to have access to element,
#       slice a list, we can also iterate the list

# Loops: while loop and for loop
# while loop: loops run as long as condition is true
# for loop: loops iterated over each element in a sequence

# pass by reference: where variable are pointing to the same information
# pass by value: where variable create a copy value

print("pass by reference example: ")
list1 = [10, 20, 30]
list2 = list1 # pass by reference
list3 = list1
print("modifying list2")
list2[1] = 50
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

print("\npass by value example:")
list1 = [10, 20, 30]
list2 = list1[:] # pass by value AKA making a copy from list1
list3 = list1 # pass by reference
print("modifying list2")
list2[0] = 15
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

list4 = [20, 25, 30, 45] # sum total = 20 + 25 + 30 + 45
total = 0
for i in list4:
    total += i
print("total:", total)

# create a function that takes a list and stores the numbers that are
# even into a new list and return that new list at the end

# create a function that takes a list and returns the calculated average
# from the list. Requirement: user for loop
def average(listName):
    count = 0
    total = 0

    for i in list4:
        count += 1

    for i in list4:
        total += i

    return total/count

def average_2(listName):
    count = len(listName)
    total = sum(listName)
    return total / count

monday = ["water", "sandwich", "toast", "watermelon", "rice"]
tuesday = ["sandwich", "water", "toast", "spicy chips", "bananas"]
copies = []

for item in monday:
    if item in tuesday:
        copies.append(item)
print("repeated food:", copies)

def f_to_c(listInfo):
    celsius = []
    for f in listInfo:
        c = (f - 32) * (5 / 9)
        celsius.append(c)
    print("celsius:", celsius)
f_to_c([32, 50, 77, 90])

all_recipes = ["pasta with tomate sauce", "chicken curry", "pesto pasta shrimp", "avocado salad", "berry smoothie", "fried rice"]
ingredients = ["avocado", "berry", "rice"]
dishes = []
for recipe in all_recipes:
    for ing in ingredients:
        if ing in recipe:
            dishes.append(recipe)
print("dishes:", dishes)

all_tasks = []
personal_tasks = ["practice instruments", "practice badminton", "wro competition", "python class"]
work_tasks = ["geometry homework", "python homework", "clean room", "chop wood", "water plants"]
all_tasks = personal_tasks + work_tasks # passing by value
all_tasks.sort()
print("sorted tasks:", all_tasks)

# Filtering Prices Below a Threshold
prices = [10.99, 25.50, 5.75, 15.00, 50.00]
threshold = 20.00
below_threshold = []
for i in prices:
    if i < threshold:
        below_threshold.append(i)
print(below_threshold)

# pass by reference (doesn't propagate)
def fun(paramenter):
    parameter = [2]

the_list = [1]
fun(the_list)
print(the_list)

# passing by value (AKA will propagate)
def fun2(parameter):
    parameter[0] = 2
the_list = [1]
fun2(the_list)
print(the_list)
