def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.removeprefix("$"))
    return d


def percent_to_float(p):
    p = float(p.removesuffix("%")) / 100
    return p


main()

# Let's go over this problem set and how it works...

# def main()
# We define our main function.
# inside it we are calling on 3 variables: dollars, percent, and tip.
# dollars has been assigned the value of: user input
# percent has been assigned the value of: user input
# tip has been assigned the value of:  'dollars' multipilied by 'percent'
# Then, when we call the main function it: prints("Leave a tip in the amount of $ + value of tip + 2 digits past the decimal

# def dollars_to_float(d)
# We define a function that acts on the user input in the main function, thus altering the value of 'dollars'
# first, we convert the user's input (d) into a float for math stuff. then we remove the dollar sign from the user's input.
# after that, the dollars_to_float(d) function returns the altered input from the user back to 'dollars' in the main function.

# def percent_to_float(p)
# we define a function that acts on the user input in the main function, thus altering the value of 'percent'
# first, we convert the user's input (p) into a float for the math stuff. then we remove the percent sign from the user's input.
# after that, we divide the user's input by 100 for percentage, and then we return the value of (p) back to 'percent' in the main function.

# Because we used these last two functions to change re-format the user's inputs, it allowed the main function to properly calculate the rest of its instructions.
# Thus, we can assign a proper value to 'tip' because now we can multiply our two floats (can't multiply strings)

# lastly, the main function prints the result. In the print statement, we are also defining how many places we want to allow past the decimal point.

# REMEMBER:  you figured out all these problem sets by reading the docs and finding the best string methods to apply to each problem. KEEP IT UP!!!
# ALSO:   you did it in Neovim, bonus points!!!
