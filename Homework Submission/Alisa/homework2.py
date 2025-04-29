'Arithmetic Operators perform simple mathematical operations on numbers.'
'Comparison Operators compare 2 things and return the result as True or False'
'Logical Operators are used to check conditions and return a boolean'
'Assignment Operators are used to assign values to variables'

# 1. Arithmetic Operators
x =10
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x // y)

# 2. Comparison Operators
a = 8
b = 15
print(a > b)
print(a == b)
print(b >= a)

# 3. Logical Operators
is_raining = True
is_windy = False
print(is_raining and is_windy)
print(is_raining or is_windy)
print(not is_raining)

# 4. Assignment Operators
c = 5
c += 10
print(c)
c -= 3
print(c)
c *= 2
print(c)
c /= 4
print(c)

# 5. Create Your Own Function
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
    
print(fizz_buzz(15))
print(fizz_buzz(9)) 
print(fizz_buzz(29))