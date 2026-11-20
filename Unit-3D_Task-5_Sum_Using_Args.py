# Define a function using *args
def find_sum(*args):
    total = sum(args)
    return total

# Call the function
result1 = find_sum(10, 20, 30)
result2 = find_sum(5, 10, 15, 20, 25)

# Print the results
print("Sum of first values:", result1)
print("Sum of second values:", result2)