def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if (
        n % 2 == 0
    ):  # Easy way to determine an even number. If it's divisible by 2, it's even.
        return True
    else:
        return False


# Tighter ways to write our 'is_even' function below:
#
# def is_even(n):
#     return n % 2 == 0

# def is_even(n):
#     return True if n % 2 == 0 else False

main()
