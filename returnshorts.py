# Here we have modified the shorts video for return values to actually ask the user for some input.
def main():
    house = houseArea()
    yard = yardArea()
    total = house + yard
    print(str(total) + " total square feet")


def houseArea():
    length = int(input("What is the footage length of your house? "))
    width = int(input("What is the footage width of your house? "))
    return length * width


def yardArea():
    length = int(input("What is the footage length of your yard? "))
    width = int(input("What is the footage width of your yard? "))
    return length * width


main()
