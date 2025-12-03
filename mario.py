def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        # Begin a new line
        print()


main()

# Cleaner version of the code above.

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# def print_row(width):
#     print("#" * width)
