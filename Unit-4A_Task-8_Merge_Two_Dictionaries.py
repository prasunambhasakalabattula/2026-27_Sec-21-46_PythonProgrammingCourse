# Create two dictionaries
dict1 = {"Python": 90, "Java": 85}
dict2 = {"C": 80, "Computer": 95}

# Create a copy of the first dictionary
merged_dict = dict1.copy()

# Merge the second dictionary into the copy
merged_dict.update(dict2)

# Print the dictionaries
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)