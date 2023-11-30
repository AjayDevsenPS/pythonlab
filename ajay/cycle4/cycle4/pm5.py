def add_integers(*args):
    """
    Adds variable-length integer arguments.

    Parameters:
    *args (int): Variable number of integer arguments.

    Returns:
    int: Sum of the integer arguments.
    """
    return sum(args)

user_input = input("Enter integers separated by spaces: ")

numbers = [int(num) for num in user_input.split()]

result = add_integers(*numbers)

print("Sum:", result)
