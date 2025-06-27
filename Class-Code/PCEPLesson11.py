# Lesson 1: Advanced Lops in Python

# for loop and while loop
# for loop: based on a number of times
# while loop: based on a true condition

# for loop example:
# numbers = [10, 20 , 30]
# for num in numbers:
#     print(num)
# else:
#     print("something")
#
# # while loop example:
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print(7)
#
# # create a list with 5 different colors
# # use for loop to print each color from the list
#
# # use while loop and print numbers that are only divisible by 4
# # from 1 to 20
# num = 1
# while num <= 20:
#     if num % 4 == 0:
#         print(num)
#     num += 1

# use a while loop to print numbers from 1 to 20 and skip numbers
# that are divisible by 3 and 7
# hint: use "continue"
num = 1
while num <= 20:
    if num % 3 != 0 and num % 7 != 0:
        print(num)
    num += 1

# enumerate: split the list information into two parts
# first part: index
# second part: element
colors = ["pink", "red", "black", "brown"]
for idx, elem in enumerate(colors):
    print(idx, elem)

# create a list of your top 5 favorite games
# print only the top 3 games along with its ranking by
# using the enumerate function
sports = ["soccer", "basketball", "volleyball", "badminton", "ping pong"]
for idx, s in enumerate(sports):
    if idx > 2:
        break # exit the loop
    print(f"{idx + 1}. {s}")

# zip: allows parallel iteration over multitple iteration
names = ["Henry", "Leo", "Victor", "Alisa"]
ages = [12, 13, 14, 15]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# create a list of 3 names
# create a list with 3 different professions
# create a list of 3 salary wages
# use zip to print all three list information together
# by making a story out of it.

# nested loops: loop inside another loop
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in matrix:
    for elem in row:
        print(elem, end="*")
    print()

print(matrix[1][1])

# using matrix, nested loop, and enumerate to find a number
target = 8
found = False
for i, row  in enumerate(matrix):
    for j, val in enumerate(row):
        if val == target:
            print(f"Found {target} at position ({i}, {j})")
            found = True
            break
    if found:
        break
