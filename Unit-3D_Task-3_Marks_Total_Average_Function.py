# Define a function
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    return total, average

# Call the function
a = 90
b = 85
c = 95

total, average = calculate_marks(a, b, c)

# Print the results
print("Total Marks:", total)
print("Average Marks:", average)