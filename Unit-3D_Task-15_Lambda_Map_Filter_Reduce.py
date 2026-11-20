from functools import reduce

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# 1. map() - Square each number
squares = list(map(lambda x: x*x, numbers))

# 2. filter() - Select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 3. reduce() - Find the sum of all numbers
total = reduce(lambda x, y: x + y, numbers)

# Print results
print("Original Numbers:", numbers)
print("Squares using map():", squares)
print("Even Numbers using filter():", even_numbers)
print("Sum using reduce():", total)