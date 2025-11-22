# Let's write some code from memory


# tip calculator
def tip_calc_main():
    """A calculator for determining the amount to tip your waiter."""
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage tip would you like to leave them? ")
    )
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.removeprefix("$"))
    return d


def percent_to_float(p):
    p = float(p.removesuffix("%")) / 100
    return p


tip_calc_main()
