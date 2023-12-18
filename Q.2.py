def calculate_factorial(num):
    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return None

    factorial_result = 1
    for i in range(1, num + 1):
        factorial_result *= i

    return factorial_result

# Get user input for the number
try:
    number = int(input("Enter a non-negative integer to calculate its factorial: "))
    
    # Call the function to calculate and print the factorial
    result = calculate_factorial(number)
    
    if result is not None:
        print(f"The factorial of {number} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
