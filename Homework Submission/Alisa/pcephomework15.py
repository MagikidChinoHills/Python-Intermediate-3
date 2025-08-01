numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(numbers[::2]) # 3, 9, 15, 21, 27

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
print(fruits[:6]) # "apple", "banana", "cherry", "date", "elderberry"

names = ["Alice", "Bob", "Charlie", "David", "Emma"]
# Write your slicing operation here
print(names[::-1]) # Emma, David, Charlie, Bob, Alice

word = "madam"
# Write your palindrome check here
if word == word[::-1]:
    print(word, "palindrome") # madam palindrome

list = [1, 2, 3, 4, 5]
def custom_step_slicing(lst, step):
    return lst[::step]

print(custom_step_slicing(list, 2))
print(custom_step_slicing(list, 3))

