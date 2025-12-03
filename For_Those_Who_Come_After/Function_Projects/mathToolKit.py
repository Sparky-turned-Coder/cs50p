# "Math Tookkit" CLI
#  Write a program full of tiny functions
#  Followed by a 'main menu' that can call all these functions.

# ===============
# max_of_three(a, b, c)
# ===============
#
# ===============
# factorial(n)
# ===============
# The 'factorial(n)' function, often denoted as n!, is the product of all positive integers less than or equal to a non-positive integer n.
#
# For a given non-negative integer n, the factorial is defined as:
#   n! = n * (n - 1) * (n - 2) * ... * 2 * 1
#
# By definition, the factorial of zero is 1:
#   0! = 1
#
# For example, the factorial of 5 is calculated as:
#   5! = 5 * 4 * 3 * 2 * 1 = 120
#
# ==============
# is_prime(n)
# ==============
#
# ==============
# fib(n)
# ==============


def add(x, y):
    return f"Result is: {float(x + y)}"


def subtract(x, y):
    return f"Result is: {float(x - y)}"


def multiply(x, y):
    return f"Result is: {float(x * y)}"


def divide(x, y):
    return f"Result is: {float(x / y)}"


def modulo(x, y):
    return f"Result is: {x % y}"


# def factorial(n):
#    return f"Result is: { }"

function_routes = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "modulo": modulo,
}


def main():
    initial = input(
        "Which would you like to do: add, subtract, multiply, divide, or modulo? "
    ).lower()
    if initial in function_routes:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        func_to_call = function_routes[initial]
        result = func_to_call(x, y)
        print(f"Result is: {result}")
    else:
        # print(f"Error: Unknown formula' {initial}'")
        return main()


main()
