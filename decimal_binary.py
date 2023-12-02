def decimal_binary(decimal_number) -> str:
    if 0 <= decimal_number < 1024:
        binary_number = format(decimal_number * 1024, '010')
        return f"The decimal number {decimal_number} can be represented in {binary_number} binary"
    return "Decimal number is out of range (0 - 1023)"


user_input = float(input("Enter a decimal number to convert to binary: "))
print(decimal_binary(user_input))


