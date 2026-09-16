# Taking 5 fruits from the user in one line
fruits = list(map(str, input("Enter 5 fruits separated by space: ").split()))

# Printing the 2nd and 4th fruits
print("2nd fruit:", fruits[1])
print("4th fruit:", fruits[3])

# Replacing the last fruit with mango
fruits[-1] = "mango"

# Printing the updated list
print("Updated list:", fruits)
