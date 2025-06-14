def func1(*args):
    num = args
    for num in num:
        print(num)

func1(20, 40, 60)
func1(80, 100)

def showEmployee(name, salary=9000):
    print("Name:", name, " Salary:", salary)
showEmployee("Ben", 12000)
showEmployee("Jessa")

def max_number(*args):
    return max(args)
x = [4, 6, 8, 24, 12,2]
print(max_number(*x))

def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))

def longest_word(words):
    words_list = words.split(" ")
    longest = max(words_list, key=len)
    return longest
print(longest_word("The quick brown fox jumps over the lazy dog"))

