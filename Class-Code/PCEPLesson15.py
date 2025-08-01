# Lesson 15: Iterating with List Slicing in Python
# to extract a cert part of the list
# list slicing to pass by value (AKA making a copy)

# subset information during list slicing:
# list[start:stop:step]
# - start: starting index for slicing, inclusive, 0 index is used if not specified
# - end/stop: stopping index, exclusive, stops at the end of the list is not specified
# - step: step size or the amounts of elements to skip, step of size 1 is used if not specified

# example:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6]) # output: [2, 3, 4, 5]
print(numbers[:5]) # output: [0,1,2,3,4]
print(numbers[3:]) # output: [3, 4, 5, 6, 7, 8, 9]
print(numbers[::2]) # output: [0,2,4,6,8]
print(numbers[::-1]) # output: [9, 8, 7, 6 ,5, 4, 3, 2, 1, 0]
print(numbers[-4:-1:2]) # output: [6, 8]
print(numbers[-4:-8:2]) # output: []

# using loops with list slicing
fruits = ["mango", "lychee", "strawberry", "apple", "banana", "cherry"]
# extract and print elements from index 1 to 3
for fruit in fruits[1:4]:
    print(fruit)

# example of loops with slicing and steps
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print every two elements
for num in numbers[0::2]:
    print(num)

# exercise:
# create a list with 5 names
# use for loop and list slicing to print the list of names in
# reverse order
names = ["Leo", "Alisa", "Ariana", "Alice", "Bob"]
for n in names[::-1]:
    print(n)

# Exercise: Given a list, print every third element using slicing.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# output: [1, 4, 7, 10]
print(numbers[::3])

# Extract the middle three elements from a list and
# iterate over them.
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
for c in colors[2:5]:
    print(c)

# Reverse the list and print every second element.
words = ["dog", "cat", "elephant", "tiger", "lion", "bear"]
# output: ['bear', 'tiger', 'cat']
print(words[::-2])

# modify the slice step so that the sum of the numbers is equals to 100
# also print that the sum of those numbers is indeed equals to 100
nums = [5, 10, 15, 20, 25, 30, 35, 40]
total = 0
for n in nums[1::2]:
    print(n)
    total += n
print(total)
sliced = nums[1::2]
total = sum(sliced)
print(sliced, total)

# create a list of 5 words where at least one of them is a palindrome
# inside a for loop, check if the work is palindrome or not
words = ["racecar", "noodle", "pizza", "level", "cheese"]
for w in words:
    print(w, "->", end=" ")
    if w == w[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
