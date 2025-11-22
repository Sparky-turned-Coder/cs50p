# Ask the user for their name
# name = input("What's your name? ")  # .strip().title()

# Remove whitespace from str.  In this case, 'strip' is a function.
# name = name.strip()
# Capatilize the first letter of each word in the str.
# name = name.title()
# Capatilize the first letter of first word in user's input str.
# name = name.upper()

# If we want to strip user's input of whitespace AND capitalize their names, tighten it up with this:
# name = name.strip().title()
# To make the line above EVEN tighter, you can add these functions to the initial input function.


# Split user's name into a first name and a last name.
# first, last = name.split(" ")

# Say hello to user
# This will CONCATENATE the string "Hello, " with the string assigned to "name".
# print(f"Hello, {name}. ")

x = "I feel"
# first, second, third, fourth, fifth, sixth = x.split("...")

first, last = x.join(" ")
print(first, last)
