#1.
#zerodivisonerror
#valuerror
#indexerror
#keyerror
#nameerror
#2.
try:
    int(input("Enter a number: "))
except ValueError:
    print("error")
try:
    a =int(input("Enter a number: "))
    print({213 / a})
except ZeroDivisionError:
    print("error")
try:
    with open('a.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("error")
#3.
try:
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    print(b / c) 
except ZeroDivisionError:
    print("no")
eekfeifjefwkeqmdsapmfk = [1, 2, 3, 4, 5]
try:
    print(eekfeifjefwkeqmdsapmfk[10])
except IndexError:
    print("error")
#4.
#else only runs if no exception occurs and finally always runs
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
   
except ZeroDivisionError:
    print("no")
else:
    print(a/b)
finally:
    print("ewjfkkewjjkfejfjejkfje")
#5.
#a normal python error might not work because it might not show a more specific error 
#it makes it easier for other people to read
#the message should be depending on the error
#6.
#zerodivisionerror = dividing by zero, change what number you are dividing by
#valuerror = enter a invalid value, change the input to a valid number
#indexerror = trying to access an index that does not exist, change the index to a valid one
#keyerror = trying to access a key that does not exist in a dictionary, change the key to a valid one
#nameerror = trying to add a string to a number, change the string to a valid number
