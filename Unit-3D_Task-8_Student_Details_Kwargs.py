# Define a function using **kwargs
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Call the function
student_details(name="Krishna", Python=90, Java=85, C=80)