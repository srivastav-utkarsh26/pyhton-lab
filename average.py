# Taking 5 numbers from the user in one line
numbers = list(map(int, input("Enter 10 numbers separated by space: ").split()))

# Calculating the average
average = sum(numbers) / len(numbers)
 
# Printing the average
print("Average:", average)
