def add(a, b):
    """
    Adds two numbers together and returns the result.

    Parameters:
    a (int): The first number to be added.
    b (int): The second number to be added.

    Returns:
    int: The sum of a and b.
    """
    c = a + b
    return c
       
def sqr(a):
    """
    Calculates the square of a given number.

    Args:
        a (int or float): The number for which the square needs to be calculated.

    Returns:
        int or float: The square of the input number.
    """
    c = a**2
    return c
    
def divs(a, b):
    """
    Perform division operation on two input parameters and return the result.

    Args:
        a (numeric): The numerator for the division operation.
        b (numeric): The denominator for the division operation.

    Returns:
        float: The result of the division if successful.
        tuple: A tuple with the string "an error occurred" and the error message if a ZeroDivisionError occurs.

    Example Usage:
        result = divs(10, 2)
        print(result)
        # Output: 5.0

        result = divs(10, 0)
        print(result)
        # Output: ('an error occurred', ZeroDivisionError('division by zero'))
    """
    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        return ("an error occurred", e)
        
