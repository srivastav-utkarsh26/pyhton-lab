# Function to remove the last item from the list
def remove_last(lst):
    lst.pop()  # pop() removes the last element


# Creating a list to test the function
my_list = [10, 20, 30, 40]

# Showing the list before calling the function
print("Before calling the function:", my_list)

# Calling the function
remove_last(my_list)

# Checking the list after the function call
print("After calling the function:", my_list)

# The original list changes because lists are mutable in Python