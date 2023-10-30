#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    if len_a < 2:
        if len_a == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    len_b = len(tuple_b)
    if len_b < 2:
        if len_b == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    elet1 = tuple_a[0] + tuple_b[0]
    elet2 = tuple_a[1] + tuple_b[1]
    return (elet1, elet2)
