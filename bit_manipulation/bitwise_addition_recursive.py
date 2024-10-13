"""
Calculates the sum of two non-negative integers using bitwise operators
Wikipedia explanation: https://en.wikipedia.org/wiki/Binary_number
"""

def validate_inputs(number: int, other_number: int):
    """Helper function to validate inputs."""
    if not isinstance(number, int) or not isinstance(other_number, int):
        raise TypeError(f"Both arguments MUST be integers! Got {type(number)} and {type(other_number)}")

    if number < 0 or other_number < 0:
        raise ValueError(f"Both arguments MUST be non-negative! Got {number} and {other_number}")


def bitwise_addition_recursive(number: int, other_number: int) -> int:
    """
    Adds two non-negative integers using bitwise operators (recursive).

    >>> bitwise_addition_recursive(4, 5)
    9
    >>> bitwise_addition_recursive(8, 9)
    17
    >>> bitwise_addition_recursive(0, 4)
    4
    >>> bitwise_addition_recursive(4.5, 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers! Got <class 'float'> and <class 'int'>
    >>> bitwise_addition_recursive('4', 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers! Got <class 'str'> and <class 'int'>
    >>> bitwise_addition_recursive(-1, 9)
    Traceback (most recent call last):
        ...
    ValueError: Both arguments MUST be non-negative! Got -1 and 9
    >>> bitwise_addition_recursive(1, -9)
    Traceback (most recent call last):
        ...
    ValueError: Both arguments MUST be non-negative! Got 1 and -9
    """
    validate_inputs(number, other_number)

    bitwise_sum = number ^ other_number
    carry = number & other_number

    if carry == 0:
        return bitwise_sum

    return bitwise_addition_recursive(bitwise_sum, carry << 1)


def bitwise_addition_iterative(number: int, other_number: int) -> int:
    """
    Adds two non-negative integers using bitwise operators (iterative).

    >>> bitwise_addition_iterative(4, 5)
    9
    >>> bitwise_addition_iterative(8, 9)
    17
    >>> bitwise_addition_iterative(0, 4)
    4
    >>> bitwise_addition_iterative(100, 50)
    150
    >>> bitwise_addition_iterative(0, 0)
    0
    >>> bitwise_addition_iterative(4.5, 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers! Got <class 'float'> and <class 'int'>
    >>> bitwise_addition_iterative('4', 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers! Got <class 'str'> and <class 'int'>
    >>> bitwise_addition_iterative(-1, 9)
    Traceback (most recent call last):
        ...
    ValueError: Both arguments MUST be non-negative! Got -1 and 9
    >>> bitwise_addition_iterative(1, -9)
    Traceback (most recent call last):
        ...
    ValueError: Both arguments MUST be non-negative! Got 1 and -9
    """
    validate_inputs(number, other_number)

    while other_number != 0:
        bitwise_sum = number ^ other_number
        carry = (number & other_number) << 1
        number = bitwise_sum
        other_number = carry

    return number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
