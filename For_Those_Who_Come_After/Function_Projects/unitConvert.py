## Unit Converter Factory
## converts one type of unit measurement to another type of unit measurement
## ===========================================================================

# ======================
# ROUTING FUNCTION
# ======================


def master_converter():
    """
    Routes the call input to the appropriate function based on the user's input.

    Unlike the example master function in the other file.py, we don't pass any argurments into this function because we are simply using it
    to route the user's input to the appropriate answer(function).
    """
    # Ask the user to input 1 of 4 options
    from_unit = input("Converting fahrenheit, inches, pounds, or hours? ").lower()
    # Check if the user's input is in our dictionary (function_routes)
    if from_unit in function_routes:
        # Get the function object from the dictionary
        func_to_call = function_routes[from_unit]
        # Call the specified function
        return func_to_call()
    else:
        print(f"Error: Unknown unit of measurment ' {from_unit}'")


# ==============================
#  CONVERTER FUNCTIONS
# ==============================


def inch_converter():  # Converting tool / main function
    inches = inch_to_cm(input("Enter the amount of inches: "))
    print(f"In centimeters that would be: {inches:.2f}")


def temp_converter():
    temp = fahr_to_celsius(int(input("Enter the temperature in fahrenheit: ")))
    print(f"Your temperature in Celsius is: {temp:.2f}")


def weight_converter():
    weight = lbs_to_kg(float(input("Enter your current weight in pounds: ")))
    print(f"Your current weight in kilograms is: {weight:.2f}")


def time_converter():
    hours = hour_to_minutes(int(input("Enter the amount of hours: ")))
    print(f"That equals {hours:.2f} minutes.")


# ===================
# MATH FORMULAS
# ===================


def inch_to_cm(n):  # inches to centimeters  / function that takes input
    return float(n) * 2.54


def fahr_to_celsius(n):  # fahrenheit to celcius  / function that takes input
    return (float(n) - 32) / 1.8


def lbs_to_kg(lbs):  # pounds to kilograms  / function that takes input
    return float(lbs) * 0.453592


def hour_to_minutes(hour):  # hours to minutes / function that takes input
    return float(hour) * 60


# ==========================
# ROUTE TABLE / DICTIONARY
# ==========================

function_routes = {
    "fahrenheit": temp_converter,
    "inches": inch_converter,
    "pounds": weight_converter,
    "hours": time_converter,
}

# Call the main Function / Run the program
master_converter()
