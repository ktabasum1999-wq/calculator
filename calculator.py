while True:
    operator = input("Enter an operator (+ - * /) or 'q' to quit: ")
    if operator == 'q':
        print("Calculator exited.")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            continue
        result = num1 / num2
    else:
        print("Invalid operator!")
        continue

    print("Result:", round(result, 4))
