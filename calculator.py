# Python includes an 'Interactive Mode'. A mode you can enter in your terminal and directly run python commands.

# Here, we have 'nested' our input functions inside an 'integer' function. This is converting user-inputted strings to integers.
# This is a variation of the method we used for our conversion on line 10.
# x = int(input("What is x? "))
# y = int(input("What is y? "))

# Floats support decimal numbers. Here we convert user strings to floats.
# x = float(input("What is x? "))
# y = float(input("What is y? "))

# z = x / y

# Below, we are converting the user's input from a string to an 'Integer', so that we can mathematically add the numbers.
# In Python, and this case in particular, we are applying an integer 'function' to perform this conversion.
# z = int(x) + int(y)

# Below we use a cryptic way to determine the amount of digits after the decimal we want to print.
# print(f"{z:.4f}")

# Now, let's round our numbers to a specific amount of digits.
# round(number[, ndigits])


# Returning Values ****


# Here we define a function that asks the user what x is, and then we print the result of the user's number as squared.
def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))


# Above, we can't perform the print function without telling Python what 'square' means. Thus, we create another function for 'square' and tell it what to do.
def square(n):
    return n * n


# Effectively, 'x' is passed to 'square'. Then, the calculation of 'x * x' is 'RETURNED' back to the main function. Here we use 'n' simply as a placeholder variable
# within this specific function.


main()
