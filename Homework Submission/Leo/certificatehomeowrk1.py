#arithmethic operators:operations used for math
#comparitive operators:operations used for comparing items
#logical operators:operations used for editing conditional statements
#assigment operators:used to assign a value to a variable

#ex 1
x = 10
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x // y)
#ex 2
a = 8
b = 15
print(a>b)
print(a==b)
print(b>=a)
#ex 3
is_raining = True
is_windy =  False
print(is_raining and is_windy)
print(is_raining or is_windy)
print(not is_raining)
#ex 4
c = 5
c += 10
print(c)
c -= 3
print(c)
c *= 2
print(c)
c /= 4
print(c)
#ex 5
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print("no")
