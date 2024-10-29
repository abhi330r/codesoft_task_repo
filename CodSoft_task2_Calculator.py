def simple_calculator():
    while True:
        # First Number
        num1 = float(input("Enter the first number: "))
        
        # Second Number
        num2 = float(input("Enter the second number: "))
        
        # Choose an operation
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        operation = input("Enter the operation (+, -, *, /) or '5' to exit: ")
        
        # Perform the chosen operation and display the result
        if operation == '+':
            result = num1 + num2
            print("Result:", result)
        elif operation == '-':
            result = num1 - num2
            print("Result:", result)
        elif operation == '*':
            result = num1 * num2
            print("Result:", result)
        elif operation == '/':
            if num2 != 0:  # Check to avoid division by zero
                result = num1 / num2
                print("Result:", result)
            else:
                print("Error: Division by zero is not allowed.")
        elif operation == '5':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop and end the calculator
        else:
            print("Invalid operation. Please choose one of +, -, *, /, or '5' to exit.")
        
        print()  # Blank line for readability

# Call the function to run the calculator
simple_calculator()