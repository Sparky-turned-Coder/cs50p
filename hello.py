# Ask user for their name
name = input("Hello. What is your name?\n")
# Say hello using their name
print("Hello, " + name + ".")

x = 12
y = 3

# If/else statements
if x > y:
    print("boo")
else:
    print("finished with boo")

# We redefined 'x' after the first if statement. Therefore, next if statement should print the opposite.
x = x - 10

if x > y:
    print("boo")
else:
    print("not boo")

# Pseudocode is an important type ofd comment that bcomes a special type of to-do list, especially when you don't understand how to accompolish a coding task.
# For example, in your code you might edit your code to say:

# Ask the user for their name
name = input("What's your name? ")
# Print Hello
print("hello,", name + ".")
# Print the name that was inputted
# print(name)

# To further improve our code, see above!
# Looking at the documentation, you'll learn that the 'print' function automatically includes the arguement "end='\n'". In C, we have to include '\n' ourselves.
# This '\n' indicates that the 'print' function will automatically create a new line break when run.
# The function takes an arguement called 'end', and the default is to create a new line.
# However, we can technically provide an arguement for 'end' ourselves, such that a new line is NOT created! See below on line 41.

# Ask the user for their name
name = input("What's your viking name? ")
print("Hello, ", end="")
print(name + ".")

# By providing 'end=""' we are overwriting the default value of 'end' such that it never creates a new line after this first print statment.
# Providing the name as "Chris", the output in the terminal window will be 'Hello, Chris'.
