def calculator(num1, operator, num2) -> str:
    if operator == "+":
        result = num1 + num2
        return f"The sum of {num1} and {num2} is {result}"

    if operator == "-":
        result = num1 - num2
        return f"The subtraction of {num1} and {num2} is {result}"

    if operator == "/":
        result = num1 / num2
        return f"The division of {num1} and {num2} is {result}"

    if operator == "*":
        result = num1 * num2
        return f"The multiplication of {num1} and {num2} is {result}"

    if operator == "%":
        result = num1 % num2
        return f"The modulo of {num1} and {num2} is {result}"

    return "Done"


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operators = input("Enter operator e.g +, -, /, *, %: ")
print(calculator(number1, operators, number2))
