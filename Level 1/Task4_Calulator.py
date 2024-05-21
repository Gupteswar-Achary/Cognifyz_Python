def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y


def main():
    print("Basic Calculator")

    # Prompt user to enter the first number
    num1 = float(input("Enter the first number: "))

    # Prompt user to enter the operator
    operator = input("Enter an operator (+, -, *, /, %): ")

    # Prompt user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Perform the requested operation
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '%':
        result = modulus(num1, num2)
    else:
        result = "Invalid operator!"

    # Display the result
    print(f"The result of {num1} {operator} {num2} is: {result}")


if __name__ == "__main__":
    main()
