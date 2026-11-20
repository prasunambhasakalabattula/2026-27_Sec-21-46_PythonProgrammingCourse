# Define a function
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)

    return area, perimeter

# Call the function
l = 10
b = 5

area, perimeter = rectangle(l, b)

# Print the results
print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)