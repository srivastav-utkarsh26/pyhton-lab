# Function to calculate factorial
def factorial(n):
    # Start the result with 1
    result = 1

    # Repeat from 1 to n
    for i in range(1, n + 1):
        # Multiply result by i
        result = result * i

    # Return the final factorial value
    return result


# Take an integer input from the user
n = int(input("Enter a number: "))

# Call the function and store the answer
answer = factorial(n)

# Print the factorial
print("Factorial =", answer)
