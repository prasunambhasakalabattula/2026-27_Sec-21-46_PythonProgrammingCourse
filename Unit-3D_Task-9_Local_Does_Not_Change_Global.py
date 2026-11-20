# Global variable
x = 10

# Define a function
def my_function():
    x = 20  # Local variable
    print("Local variable:", x)

# Call the function
my_function()

# Print global variable
print("Global variable:", x)