# for loop is for when you have a specific number of times for the code to run, while runs until the condition is False.
# if you want something to run for a specific number of times, a for loop is good
# if you dont have a specific number of times, a while loop is better

# enumerate gives the index, and whats in the index in a tuple
Cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
# enumerate would help because we could give a rank to the cities and know what order they are in
for index, city in enumerate(Cities):
    print(f"{index + 1}, {city}")

matrix = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

# You can use the first loop to go through the rows, then the nested one to go through the elements in each row
# I just would use the index if I had to print out the diagonals

Numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
number = [num for num in Numbers if num % 10 != 0]
print(number)

Numbers = [5, 10, 15, 20, 25, 30]

for num in Numbers:
    if num != 20:
        print(num)
    else: 
        break

for num in Numbers:
    if num != 15:
        print(num)

