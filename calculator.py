    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    # Prevent division by zero error
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print(f"'{operator}' is not a valid oper
ator.")# Simple Python Calculator

# Take operator input from the user
operator = input("Enter an operator (+ - * /): ")

# Take two number inputs
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Perform calculation based on the operator
if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
