def print_bytes_repr(n: int | float, precision=8) -> None:
    print(f"{n:0{precision}b}")


def bit_or(a, b):
    print_bytes_repr(a)
    print_bytes_repr(b)
    result = a | b
    print_bytes_repr(result)
    return result


def left_shift(a, b):
    """
    2^b
    """
    print_bytes_repr(a)
    print_bytes_repr(b)
    result = a << b
    print_bytes_repr(result)
    return result


def right_shift(a, b):
    """a/(2^b)"""
    print_bytes_repr(a)
    print_bytes_repr(b)
    result = a >> b
    print_bytes_repr(result)
    return result


# bit_or(1, 2)
# left_shift(1, 2)
right_shift(1, 2)
