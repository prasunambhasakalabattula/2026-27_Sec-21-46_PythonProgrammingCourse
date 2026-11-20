# Program to demonstrate ValueError and IndexError

my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter list index: "))
    print("Element:", my_list[index])

except ValueError:
    print("Error: Please enter a valid integer")

except IndexError:
    print("Error: List index is out of range")