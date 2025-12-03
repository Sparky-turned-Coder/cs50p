# Define the functions
# First, define the individual functions that the master function will route to.
def add(x, y):
    return f"Result of add: {x + y}"


def subtract(x, y):
    return f"Result of subtract: {x - y}"


def multiply(x, y):
    return f"Result of multiply: {x * y}"


# Create a dispatch table
# Create a dictionary where the keys are the 'route names' (e.g., strings representing operations) and the values are the function objects themselves.
function_routes = {"add": add, "subtract": subtract, "multiply": multiply}


# Create the 'Master Function'
# Finally, create the master function. It takes the 'name of the function to call'(the route name) and any arguements it needs to pass along.
# It uses the dispatch table to look up and execute the correct function dynamically.
def master_router(operation_name, *args, **kwargs):
    """
    Routes the call to the appropriate function based on the operation_name.

    Args:
        operation_name (str): The name of the operation to perform.
        *args: Positional arguments to pass to the target function.
        **kwargs: Keyword arguments to pas to the target function.

    Returns:
        The result of the called function, or an error message if the operation is not found.
    """
    # Check if the requested operation is in our dictionary
    if operation_name in function_routes:
        # Get the function object from the dictionary
        func_to_call = function_routes[operation_name]
        # Call the function with the provided arguments and return its result
        return func_to_call(*args, **kwargs)
    else:
        # Handle cases where the requested operation is invalid
        return f"Error: Unknown operation '{operation_name}'"


result_add = master_router("add", 10, 5)
print(result_add)

result_subtract = master_router("subtract", 20, 10)
print(result_subtract)

result_multiply = master_router("multiply", 9, 9)
print(result_multiply)

result_unknown = master_router("divide", 18, 2)
print(result_unknown)
