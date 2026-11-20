# Create a nested dictionary
students = {
    1: {"name": "Prasunna", "marks": 90},
    2: {"name": "Ravi", "marks": 85},
    3: {"name": "Sita", "marks": 95}
}

# Print student names and marks
for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print()