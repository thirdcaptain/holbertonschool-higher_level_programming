#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    zero = (0,)
    if len(tuple_a) == 0:
        tuple_a = tuple_a + zero + zero
    elif len(tuple_a) == 1:
        tuple_a = tuple_a + zero
    if len(tuple_b) == 0:
        tuple_b = tuple_b + zero + zero
    elif len(tuple_b) == 1:
        tuple_b = tuple_b + zero
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c
