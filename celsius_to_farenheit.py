# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    # Apply the formula
    f = (c * 9 / 5) + 32

    # Return the Fahrenheit value
    return f


# Take temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Call the function
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the temperature in Fahrenheit
print("Temperature in Fahrenheit =", fahrenheit)
