# ====================
# How __name__ Works
# ====================
#
# The value of the __name__ variable changes based on how the Python file is executed:
#   -   When the script is run directly: The Python interpreter sets the __name__ variable
#       to the string "__main__". This signifies that the current file is the entry point
#       of the program.
#   -   When the script is imported as a module: The __name__ variable is set to the name
#       of the module (which is usually the filename without the .py extension). For example,
#       if you import a file named 'my_module.py', the value of __name__ inside that file
#       will be 'my_module'.

# The Common Use Case: 'if __name__ == '__main__':
#
# This behavior is most often used with the conditional statement if __name__ == '__main__':
# to control the execution flow of a script.
#
# Code inside this 'if' block will only run when the script is executed as a standalone program. This is useful for:
#   -   Including test or demonstration code: You can put unit tests or example usage code within this block,
#       which allows developers to run the file directly to verify functionality, without that code running
#       automatically when the file is imported into another project.
#   -   Separating main logic from reusable functions: It allows a single Python file to serve as both a reusable
#       module (offering functions and classes to other files) and a directly executable script with its own main
#       application logic.
#   -   Preventing unintended side effects: It ensures that certain code, such as functions that prompt for user
#       input, don't run unexpectedly when the module is imported by another script.
#
#       Example:  my_script.py


def greeting(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    # This code only runs when my_script.py is executed directly.
    user_name = input("Enter your name: ")
    print(greeting(user_name))
else:
    # This code runs when my_script.py is imported
    print(f"{__name__} was imported as a module")


# =============================================================================
