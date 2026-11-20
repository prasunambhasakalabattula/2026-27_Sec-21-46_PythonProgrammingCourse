# Define a function with default rate
def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Call function using default rate
result1 = simple_interest(10000, 2)

# Call function using explicit rate
result2 = simple_interest(10000, 2, 10)

# Print the results
print("Simple Interest with default rate:", result1)
print("Simple Interest with explicit rate:", result2)