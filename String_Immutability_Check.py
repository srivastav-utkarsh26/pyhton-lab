# This function tries to change the first character of the string
def change_string(s):
    s = "X" + s[1:]  # Replace the first character with "X"
    print("String inside the function:", s)


# Taking a string to test the function
my_string = "Hello"

# Showing the original string before calling the function
print("Before calling the function:", my_string)

# Calling the function
change_string(my_string)

# Checking the original string after the function call
print("After calling the function:", my_string)

# The original string does not change because strings are immutable in Python