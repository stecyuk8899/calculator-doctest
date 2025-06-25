def add(a, b):
    return float(a + b)


def subtract(a, b):
    return float(a - b)


def multiply(a, b):
    return float(a * b)


def divide(a, b):
    """Compute and return the result of divide two numbers with each other.
    Usage examples:
    >>> divide(4.0, 2.0)
    2.0
    >>> divide(4.0, 0.0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Cannot divide by zero.
    """
    if b == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return float(a / b)


a = 5
b = 3

print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))
