# Create a subject-marks dictionary
subjects = {
    "Python": 90,
    "Java": 85,
    "C": 80,
    "Computer": 95
}

# Print keys using loop
print("Subject Names:")
for key in subjects.keys():
    print(key)

# Print values using loop
print("\nSubject Marks:")
for value in subjects.values():
    print(value)

# Print items using loop
print("\nSubject and Marks:")
for key, value in subjects.items():
    print(key, ":", value)