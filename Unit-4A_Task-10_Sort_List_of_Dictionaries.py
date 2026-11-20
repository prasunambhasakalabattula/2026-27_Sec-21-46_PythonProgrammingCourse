# Create a list of student dictionaries
students = [
    {"name": "Prasunna", "marks": 90},
    {"name": "Ravi", "marks": 75},
    {"name": "Sita", "marks": 85},
    {"name": "Kiran", "marks": 95}
]

# Sort by marks in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

# Sort by marks in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

# Print results
print("Ascending Order:")
for student in ascending:
    print(student)

print("\nDescending Order:")
for student in descending:
    print(student)