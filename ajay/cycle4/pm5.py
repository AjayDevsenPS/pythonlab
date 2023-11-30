

def add_integers(*args):
    """
    Adds variable-length integer arguments.

    Parameters:
    *args (int): Variable number of integer arguments.

    Returns:
    int: Sum of the integer arguments.
    """
    return sum(args)

# Get user input
user_input = input("Enter integers separated by spaces: ")

# Convert input to a list of integers
numbers = [int(num) for num in user_input.split()]

# Call the function with variable-length arguments
result = add_integers(*numbers)

# Display the result
print("Sum:", result)
