def calculate_bill_details():
    try:
        # Get user input for restaurant bill details
        num_people = int(input("Enter the number of people: "))
        cost_per_meal = float(input("Enter the cost of each meal: $"))
        sales_tax_percentage = float(input("Enter the sales tax percentage: "))
        tip_percentage = float(input("Enter the tip percentage: "))

        # Calculate total cost of food
        total_cost_of_food = num_people * cost_per_meal

        # Calculate total sales tax
        total_sales_tax = (sales_tax_percentage / 100) * total_cost_of_food

        # Calculate total tip amount
        total_tip_amount = (tip_percentage / 100) * total_cost_of_food

        # Calculate total bill amount per person
        total_bill_per_person = (total_cost_of_food + total_sales_tax + total_tip_amount) / num_people

        # Print the calculated values
        print(f"\nTotal Cost of Food: ${total_cost_of_food:.2f}")
        print(f"Total Sales Tax: ${total_sales_tax:.2f}")
        print(f"Total Tip Amount: ${total_tip_amount:.2f}")
        print(f"Total Bill Amount Per Person: ${total_bill_per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

# Run the program
calculate_bill_details()
