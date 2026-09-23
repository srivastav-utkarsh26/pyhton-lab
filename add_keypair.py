# Function to add a new key-value pair
def add_entry(d):
    # Add "age" as a new key with value 20
    d["age"] = 20


# Create a dictionary
my_dict = {"name": "Rahul"}

# Print dictionary before calling the function
print("Before:", my_dict)

# Call the function
add_entry(my_dict)

# Print dictionary after calling the function
print("After:", my_dict)
