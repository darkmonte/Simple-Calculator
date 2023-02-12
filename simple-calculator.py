# Simple Calculator

def calculate():
    # Get the first number
    num1 = float(input("Enter first number: "))
    # Get the second number
    num2 = float(input("Enter second number: "))
    # Get the operator
    operator = input("Enter operator (+, -, *, /): ")

    # Perform the calculation based on the operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    # Display the result
    print("Result:", result)

# Run the calculator
calculate()
