#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)
    v = 0
    w = 0
    for tup in my_list:
        v += tup[0] * tup[1]
        w += tup[1]
    return (v / w)
