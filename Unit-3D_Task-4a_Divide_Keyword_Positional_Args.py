# Define a function
def divide(a, b):
    return a / b

# Call using keyword arguments
result1 = divide(b=10, a=20)

# Call using positional arguments
result2 = divide(10, 20)

# Print the results
print("Result using keyword arguments:", result1)
print("Result using positional arguments:", result2)