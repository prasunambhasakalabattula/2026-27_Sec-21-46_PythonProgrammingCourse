# Global counter
count = 0

# Define a function
def increment():
    global count
    count += 1
    print("Counter:", count)

# Call the function
increment()
increment()
increment()