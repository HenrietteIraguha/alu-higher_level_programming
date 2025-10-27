#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad with zeros to ensure at least 2 elements
    a = tuple_a + (0,) * (2 - len(tuple_a))
    b = tuple_b + (0,) * (2 - len(tuple_b))
    # Use only the first two elements and add them
    return (a[0] + b[0], a[1] + b[1])
