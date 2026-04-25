# Simple Calculator Project
# Codsoft Internship - Python Programming

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Taking inputs
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Enter your choice (+, -, *, /): ")

    # Performing calculation
    if choice == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select a valid operation.")

# Run the calculator
calculator()
