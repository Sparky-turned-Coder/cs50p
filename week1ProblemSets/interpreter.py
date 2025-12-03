# Implement a program that prompts the user for an arithmetic expression and then calculates and
# outputs the result as a floating-point value formatted to one decimal place.


def interpreter(expression):
    expression = expression.split(" ")
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        # print("Unsupported operator.")
        # Instead of the print statement for 'else', just return 'None' to the caller and let it handle the error.
        return None


def main():
    result = interpreter(input("Expression: ").strip())
    if result is None:
        print("Unsupported operator.")
    else:
        print(f"Result: {result:.1f}")


main()
