def calculate_sum_of_squares_if_odd(num1, num2):
    if num1 % 2 == 1 and num2 % 2 == 1:
        sum_of_squares = num1**2 + num2**2
        print(f"The sum of squares of {num1} and {num2} is: {sum_of_squares}")
    else:
        print("Calculation not performed. Please enter two odd integers.")

# Get user input for two integers
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    # Call the function to calculate and print the sum of squares if both are odd
    calculate_sum_of_squares_if_odd(num1, num2)

except ValueError:
    print("Invalid input. Please enter valid integers.")
