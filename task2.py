try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /, %, **): ")
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            print("Error: Division by zero")
    elif operation == '%':
        if number2 != 0:
            result = number1 % number2
        else:
            print("Error: Division by zero")
    elif operation == '**':
        result = number1 ** number2
    else:
        print("Invalid operation")
    print(f"num1 {operation} num2 = {result}.")

except ValueError:
    print("Invalid input. Please enter numeric values.")
