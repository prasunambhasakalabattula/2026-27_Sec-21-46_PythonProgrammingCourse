# Define a function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get temperature from the user
c = float(input("Enter temperature in Celsius: "))

# Call the function
result = celsius_to_fahrenheit(c)

# Print the result
print("Temperature in Fahrenheit:", result)