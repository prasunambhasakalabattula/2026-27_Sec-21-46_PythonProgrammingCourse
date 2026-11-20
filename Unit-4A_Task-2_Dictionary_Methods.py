# Create a sample dictionary
student = {
    "name": "Prasunna",
    "age": 18,
    "course": "Python"
}

# 1. keys() - Display all keys
print("Keys:", student.keys())

# 2. values() - Display all values
print("Values:", student.values())

# 3. items() - Display key-value pairs
print("Items:", student.items())

# 4. get() - Get a particular value
print("Name:", student.get("name"))

# 5. update() - Update dictionary values
student.update({"age": 19})
print("After update:", student)

# 6. pop() - Remove an item
student.pop("course")
print("After pop:", student)